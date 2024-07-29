.. _beaglev-fire-apb-axi-demo

Accessing APB and AXI Peripherals Through Linux
###############################################

AXI
***

.. line-block::
    AXI is part of the ARM AMBA (Advanced Microcontroller Bus Architecture) protocol family. 
    It is designed for high-performance, high-frequency system-on-chip (SoC) designs. 
    AXI provides high-speed data transfer with minimal latency and is widely used in various applications, 
    including high-end embedded systems and complex digital circuits.

APB
***

.. line-block::
    APB is also part of the ARM AMBA protocol family, designed for low-power and low-latency communication with peripheral devices. 
    It is simpler and lower performance compared to AXI, making it suitable for slower peripheral devices.

Accessing AXI and APB Peripherals from Linux
********************************************

.. line-block::
    To access AXI and APB peripherals from Linux, memory-mapped I/O (MMIO) is commonly used. 
    This involves mapping the physical addresses of the peripherals into the virtual address space of a user-space application. 
    The following sections demonstrate how to access APB peripherals using the Linux /dev/mem interface and AXI peripherals using the UIO (Userspace I/O) framework.

APB Interfaces
==============

.. line-block::
    The MSS includes fabric interfaces for interfacing FPGA fabric with the CPU Core Complex. 
    It provides one APB 32-bit FIC3 to provide APB interface to the FPGA fabric. 
    FIC3 provides a master interface to the MSS, FIC3 must be connected to a slave in the fabric.

Design Details
--------------
For this example, you can try to write to the APB slave present in the Verilog Tutorial Cape gateware. 
Select the gateware by changing `custom-fpga-design/my_custom_fpga_design.yaml` to include `VERILOG_TUTORIAL` as the cape option.

The APB Slave has two registers, one read-only register at 0x00, one read-write register at 0x10 and a status register containing the last read value at 0x20.

.. line-block::
    Having a look at the design, we can see that the APB slave is connected with a CoreAPB3 arbitrer, which assigns it the 0xXX10_0000 address, the top two bits being ignored. 
    Tracing to the master connected with the CoreAPB3 device, we can see that there is another arbitrer present, which gives our slave the 0xX100_0000 address. 
    From the polarfire technical manual, we know that FIC3 peripherals can start from the 0x4000_0000 address. 
    Therefore, the final address of our APB slave becomes 0x4110_0000.

Now, we shall access this address through a memory-mapped interface in Linux.

Accessing the Interface
------------------------
There are two ways to access such registers. One can use the `devmem2` utility or write a C program for accessing the memory region. 
The first method is quite simple.

1. To read from a register:

   .. code-block:: shell

      sudo devmem2 0x41100000 w

2. To write to a register:

   .. code-block:: shell

      sudo devmem2 0x41100010 w 0x1

In the second method, we can use the `/dev/mem` interface to access the registers inside the APB Slave. 
Here is an example C program which demonstrates this.

.. code-block:: c

   #include <stdio.h>
   #include <stdint.h>
   #include <unistd.h>
   #include <fcntl.h>
   #include <sys/mman.h>

   #define MAP_SIZE 4096   // 4096 bytes as per DTSO file
   #define BASE_ADDRESS 0x41100000
   #define OFFSET_REG1 0x00   // Read only register which contains 0xDEADBEEF
   #define OFFSET_REG2 0x10   // Read/write register
   #define OFFSET_STATUS 0x20 // Read only register which contains the status of the last read operation

   int main() {
       int mem_fd = open("/dev/mem", O_RDWR | O_SYNC);
       if (mem_fd == -1) {
           printf("Error: cannot open /dev/mem\n");
           return -1;
       }

       // Calculate the offset within the mapped region
       off_t offset = BASE_ADDRESS;
       size_t length = MAP_SIZE;

       void *mapped_base = mmap(NULL, length, PROT_READ | PROT_WRITE, MAP_SHARED, mem_fd, offset);
       if (mapped_base == MAP_FAILED) {
           perror("Failed to map memory");
           close(mem_fd);
           return -1;
       }

       // Read REG1 and verify if it contains 0xDEADBEEF
       uint32_t value = *((volatile uint32_t *)(mapped_base + OFFSET_REG1));
       if (value == 0xdeadbeef) {
           printf("REG1 contains 0xDEADBEEF\n");
       } else {
           printf("REG1 does not contain 0xDEADBEEF\n");
       }

       // Write 0x12345678 to REG2
       *((volatile uint32_t *)(mapped_base + OFFSET_REG2)) = 0x12345678;

       // Read REG2 and verify if it contains 0x12345678
       value = *((volatile uint32_t *)(mapped_base + OFFSET_REG2));
       if (value == 0x12345678) {
           printf("REG2 contains 0x12345678\n");
       } else {
           printf("REG2 does not contain 0x12345678\n");
       }

       // Read STATUS and print the value
       value = *((volatile uint32_t *)(mapped_base + OFFSET_STATUS));
       printf("STATUS: 0x%x\n", value);

       munmap(mapped_base, length);
       close(mem_fd);

       return 0;
   }

AXI Interfaces
==============
The MSS includes three 64-bit AXI FICs out of which FIC0 is used for data transfers to/from the fabric. 
FIC0 is connected as both master and slave.

Design Details
--------------

.. line-block::
    A simple design can be created by first connecting the FIC0 Initiator from the MSS to a CoreAXI4Interconnect. 
    Now, you can connect an AXI slave to this interconnect. We will be using the Polarfire AXI LSRAM.

    Both the CoreAXI4Interconnect and the PF AXI LSRAM will have to be configured. 
    The AXI ID Width of both the modules will have to be matched, as well as the address space of the only slave will have to be configured. 
    In this example, LSRAM gets an address of `0x6000_0000` to `0x6000_ffff`, and the AWID is kept to 9 bits.

.. figure:: images/axi-slave-demo.png
    :width: 1040
    :alt: AXI LSRAM slave

    Example design

Finally, an entry will be added to the device tree to make a UIO device point to our LSRAM's memory region.

.. code-block::

   &{/} {
       fabric-bus@40000000 {
           fpgalsram: uio@60000000 {
               compatible = "generic-uio";
               linux,uio-name = "fpga_lsram"; // mandatory for program. If changed, please update program as well.
               reg = <0x0 0x60000000 0x0 0x1000>;
               status = "enabled";
           };
       };
   };

Once the gateware is compiled, we can access the memory-mapped interface by the same methods, and by the UIO device as well.

1. Using devmem2

   .. code-block:: shell

      sudo devmem2 0x60000000 w # for read
      sudo devmem2 0x60000000 w 0x1 # for write

2. Using the UIO device

   .. code-block:: c

      #include <sys/stat.h>
      #include <sys/mman.h>
      #include <fcntl.h>
      #include <errno.h>
      #include <string.h>
      #include <stdint.h>
      #include <unistd.h>
      #include <stdio.h>
      #include <stdlib.h>

      #define SYSFS_PATH_LEN        (128)
      #define ID_STR_LEN            (32)
      #define UIO_DEVICE_PATH_LEN   (32)
      #define NUM_UIO_DEVICES       (32)

      char uio_id_str[] = "fpga_lsram";
      char sysfs_template[] = "/sys/class/uio/uio%d/%s";

      /* Function to get UIO device number */
      int get_uio_device(char *id) {
          FILE *fp;
          int i;
          char file_id[ID_STR_LEN], sysfs_path[SYSFS_PATH_LEN];

          for (i = 0; i < NUM_UIO_DEVICES; i++) {
              snprintf(sysfs_path, SYSFS_PATH_LEN, sysfs_template, i, "/name");
              if (!(fp = fopen(sysfs_path, "r"))) break;

              fscanf(fp, "%32s", file_id);
              if (strncmp(file_id, id, strlen(id)) == 0) {
                  fclose(fp);
                  return i;
              }
              fclose(fp);
          }
          return -1;
      }

      /* Function to get UIO device memory size */
      uint32_t get_memory_size(char *sysfs_path, char *uio_device) {
          FILE *fp;
          uint32_t sz;

          if (!(fp = fopen(sysfs_path, "r"))) {
              fprintf(stderr, "unable to determine size for %s\n", uio_device);
              exit(0);
          }

          fscanf(fp, "0x%016X", &sz);
          fclose(fp);
          return sz;
      }

      int main() {
          int uioFd_0, index;
          char uio_device[UIO_DEVICE_PATH_LEN], sysfs_path[SYSFS_PATH_LEN], d1;
          volatile uint32_t *mem_ptr0;
          uint32_t mmap_size, i;

          printf("locating device for %s\n", uio_id_str);
          if ((index = get_uio_device(uio_id_str)) < 0) {
              fprintf(stderr, "can't locate uio device for %s\n", uio_id_str);
              return -1;
          }

          snprintf(uio_device, UIO_DEVICE_PATH_LEN, "/dev/uio%d", index);
          if ((uioFd_0 = open(uio_device, O_RDWR)) < 0) {
              fprintf(stderr, "cannot open %s: %s\n", uio_device, strerror(errno));
              return -1;
          }

          snprintf(sysfs_path, SYSFS_PATH_LEN, sysfs_template, index, "maps/map0/size");
          if (!(mmap_size = get_memory_size(sysfs_path, uio_device))) {
              fprintf(stderr, "bad memory size for %s\n", uio_device);
              return -1;
          }

          if ((mem_ptr0 = mmap(NULL, mmap_size, PROT_READ | PROT_WRITE, MAP_SHARED, uioFd_0, 0)) == MAP_FAILED) {
              fprintf(stderr, "Cannot mmap: %s\n", strerror(errno));
              close(uioFd_0);
              return -1;
          }

          while (1) {
              printf("\n\t# Options:\n");
              printf("\t1. Show memory\n\t2. Write pattern\n\t3. Write zeroes\n");
              printf("\t4. Print size\n\t5. Fill & verify\n\t6. Exit\n");
              printf("Enter choice: ");
              scanf("%c%*c", &d1);

              if (d1 == '6') break;

              switch (d1) {
                  case '1':
                      for (i = 0; i < (mmap_size / 4); i++) {
                          if (i % 4 == 0) printf("\n0x%08X: ", i * 4);
                          printf("0x%08X ", *(mem_ptr0 + i));
                      }
                      printf("\n");
                      break;
                  case '2':
                      for (i = 0; i < (mmap_size / 4); i++) *(mem_ptr0 + i) = i;
                      printf("Pattern written.\n");
                      break;
                  case '3':
                      for (i = 0; i < (mmap_size / 4); i++) *(mem_ptr0 + i) = 0;
                      printf("Zeroes written.\n");
                      break;
                  case '4':
                      printf("Memory size: 0x%x bytes (%u bytes)\n", mmap_size, mmap_size);
                      break;
                  case '5':
                      for (i = 0; i < (mmap_size / 4); i++) *(mem_ptr0 + i) = 0xFFFFFFFF;
                      printf("Verifying...\n");
                      for (i = 0; i < (mmap_size / 4); i++) {
                          if (*(mem_ptr0 + i) != 0xFFFFFFFF) {
                              printf("\nVerification failed at 0x%08X\n", i * 4);
                              break;
                          }
                      }
                      printf("Verification passed.\n");
                      break;
                  default:
                      printf("Invalid option.\n");
              }
          }

          munmap((void *)mem_ptr0, mmap_size);
          close(uioFd_0);
          return 0;
      }

Issues that can be faced when using an improperly configured AXI/APB interface
===============================================================================
A CPU stall can be faced when accessing the FIC interfaces without any slaves connected to the memory region being accessed. 
Your BVF will stop responding if connected to SSH, and on serial you will see the following kernel messages:

.. code-block:: shell

   [   24.110099] rcu: INFO: rcu_sched detected stalls on CPUs/tasks:
   [   24.116041] rcu:     0-...0: (1 GPs behind) idle=e00c/0/0x1 softirq=40/41 fqs=2626
   [   24.123377]     (detected by 3, t=5255 jiffies, g=-1131, q=9 ncpus=4)
   [   24.129573] Task dump for CPU 0:
   [   24.132810] task:swapper/0       state:R  running task     stack:0     pid:0     ppid:0      flags:0x00000008
   [   24.142757] Call Trace:
   [   24.145213] [<ffffffff80a67ba0>] __schedule+0x27c/0x834

If this happens, please double check your design. Specifically, check the address configured for the slaves, the AXI ID wire width and other AXI parameters.
