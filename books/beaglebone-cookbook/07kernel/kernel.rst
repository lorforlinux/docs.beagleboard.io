.. _beaglebone-cookbook-kernel:

The Kernel
###########

The kernel is the heart of the Linux operating system. It's the software that takes the 
low-level requests, such as reading or writing files, or reading and writing general-purpose 
input/output (GPIO) pins, and maps them to the hardware. When you install a new version of the 
OS (:ref:`basics_latest_os`), you get a certain version of the kernel. 

You usually won't need to mess with the kernel, but sometimes you might want to try something new 
that requires a different kernel. This chapter shows how to switch kernels. The nice thing is you 
can have multiple kernels on your system at the same time and select from among them which to boot up.

Updating the Kernel
====================

Problem
--------

You have an out-of-date kernel and want to make it current.

Solution
---------

Use the following command to determine which kernel you are running:

.. code-block:: bash

    bone$ uname -a
    Linux beaglebone 5.10.168-ti-r62 #1bullseye SMP PREEMPT Tue May 23 20:15:00 UTC 2023 armv7l GNU/Linux
    GNU/Linux


The *5.10.168-ti-r62* string is the kernel version.

To update to the current kernel, ensure that your Bone is on the Internet 
(:ref:`networking_usb` or :ref:`networking_wired`) and then run the following commands:

.. code-block:: bash

    bone$ apt-cache pkgnames | grep linux-image | sort | less
    ...
    linux-image-5.10.162-ti-r59
    linux-image-5.10.162-ti-rt-r56
    linux-image-5.10.162-ti-rt-r57
    linux-image-5.10.162-ti-rt-r58
    linux-image-5.10.162-ti-rt-r59
    linux-image-5.10.168-armv7-lpae-x71
    linux-image-5.10.168-armv7-rt-x71
    linux-image-5.10.168-armv7-x71
    linux-image-5.10.168-bone71
    linux-image-5.10.168-bone-rt-r71
    linux-image-5.10.168-ti-r60
    linux-image-5.10.168-ti-r61
    linux-image-5.10.168-ti-r62
    linux-image-5.10.168-ti-rt-r60
    linux-image-5.10.168-ti-rt-r61
    linux-image-5.10.168-ti-rt-r62
    ...

    bone$ sudo apt install linux-image-5.10.162-ti-rt-r59
    bone$ sudo reboot

    bone$ uname -a
    Linux beaglebone 5.10.162-ti-rt-r59 #1 SMP PREEMPT Wed Nov 19 21:11:08 UTC 2014 armv7l
    GNU/Linux


The first command lists the versions of the kernel that are available. The second command installs one. 
After you have rebooted, the new kernel will be running.

If the current kernel is doing its job adequately, you probably don't need to update, but sometimes a new 
software package requires a more up-to-date kernel. 
Fortunately, precompiled kernels are available and ready to download.  

Seeing which kernels are installed
^^^

You can have multiple kernels install at the same time. T
hey are saved in **/boot**

.. code-block:: bash

    bone$ cd /boot
    bone$ ls 
    config-5.10.168-ti-r62      initrd.img-5.10.168-ti-r63  uboot                    vmlinuz-5.10.168-ti-r63
    config-5.10.168-ti-r63      SOC.sh                      uEnv.txt
    dtbs                        System.map-5.10.168-ti-r62  uEnv.txt.orig
    initrd.img-5.10.168-ti-r62  System.map-5.10.168-ti-r63  vmlinuz-5.10.168-ti-r62

Here I have two kernel versions installed. 

.. tabs::

    .. group-tab:: Bone

        On the Bone (Not the Play) the file **uEnv.txt** tells which 
        kernel to use on the next reboot. Here are the first few lines:

        .. code-block:: bash

            Line
            1 #Docs: http://elinux.org/Beagleboard:U-boot_partitioning_layout_2.0
            2 
            3 # uname_r=4.14.108-ti-r137
            4 uname_r=4.19.94-ti-r50
            5 # uname_r=5.4.52-ti-r17
            6 #uuid=

        Lines 3-5 list the various kernels, and the uncommented one on line 4 is the one that will be used next time. You will have to add your own uname's. Get the names from the files in /boot. Be careful, if you mistype the name your Bone won't boot.

    .. group-tab:: Play

        On the Play you can see which version of the kernel will boot
        next by:

        .. code-block:: bash

            play$ cat /boot/firmware/kversion
            5.10.168-ti-arm64-r106

If you want to change the version run:

.. code-block:: bash

    bone$ sudo apt install linux-image-5.10.168-ti-arm64-r105 --reinstall 


.. _kernel_building_modules:

Building and Installing Kernel Modules
=======================================

Problem
--------

You need to use a peripheral for which there currently is no driver, or you need to improve the 
performance of an interface previously handled in user space.

Solution
---------

The solution is to run in kernel space by building a kernel module. There are entire 
`books on writing Linux Device Drivers <https://bootlin.com/doc/books/ldd3.pdf>`_. This recipe assumes that 
the driver has already been written and shows how to compile and install it. After you've 
followed the steps for this simple module, you will be able to apply them to any other module.

For our example module, add the code in :ref:`kernel_simple_module` to a file called ``hello.c``.

.. _kernel_simple_module:

.. literalinclude:: ../code/07kernel/hello.c
   :caption: Simple Kernel Module (hello.c)
   :linenos:

:download:`hello.c <../code/07kernel/hello.c>`

When compiling on the Bone, all you need to do is load the Kernel 
Headers for the version of the kernel you're running:

.. code-block:: bash

    bone$ sudo apt install linux-headers-`uname -r`

.. note:: 

    The quotes around ``uname -r`` are backtick characters. On a United States keyboard, 
    the backtick key is to the left of the 1 key.


This took a little more than three minutes on my Bone. The ``uname -r`` part of the command 
looks up what version of the kernel you are running and loads the headers for it. 

Next, add the code in :ref:`kernel_Makefle` to a file called ``Makefile``.

.. _kernel_Makefle:

.. literalinclude:: ../code/07kernel/Makefile.display
   :caption: Simple Kernel Module (``Makefile``)
   :linenos:

:download:`Makefile.display <../code/07kernel/Makefile.display>`

.. note:: 
    Replace the two instances of *<TAB>* with a tab character (the key left of the Q key on a United States keyboard). 
    The tab characters are very important to makefiles and must appear as shown.


Now, compile the kernel module by using the *make* command:

.. code-block:: bash

    bone$ make
    make -C /lib/modules/5.10.168-ti-r62/build M=$PWD
    make[1]: Entering directory '/usr/src/linux-headers-5.10.168-ti-r62'
    CC [M]  /home/debian/docs.beagleboard.io/books/beaglebone-cookbook/code/07kernel/hello.o
    MODPOST /home/debian/docs.beagleboard.io/books/beaglebone-cookbook/code/07kernel/Module.symvers
    CC [M]  /home/debian/docs.beagleboard.io/books/beaglebone-cookbook/code/07kernel/hello.mod.o
    LD [M]  /home/debian/host/BeagleBoard/docs.beagleboard.io/books/beaglebone-cookbook/code/07kernel/hello.ko
    make[1]: Leaving directory '/usr/src/linux-headers-5.10.168-ti-r62'
    
    bone$ ls
    Makefile        hello.c   hello.mod.c  hello.o
    Module.symvers  hello.ko  hello.mod.o  modules.order

Notice that several files have been created. 
``hello.ko`` is the one you want. Try a couple of commands with it:

.. code-block:: bash

    bone$ modinfo hello.ko
    filename:       /home/debian/host/BeagleBoard/docs.beagleboard.io/books/beaglebone-cookbook/code/07kernel/hello.ko
    license:        GPL
    description:    Hello World Example
    author:         Boris Houndleroy
    depends:        
    name:           hello
    vermagic:       5.10.168-ti-r62 SMP preempt mod_unload modversions ARMv7 p2v8 
    
    bone$ sudo insmod hello.ko
    bone$ dmesg | tail -4
    [  377.944777] lm75 1-004a: hwmon1: sensor 'tmp101'
    [  377.944976] i2c i2c-1: new_device: Instantiated device tmp101 at 0x4a
    [85819.772666] Loading hello module...
    [85819.772687] Hello, World!

The first command displays information about the module. The *insmod* command inserts the module into the running kernel. 
If all goes well, nothing is displayed, but the module does print something in the kernel log. The *dmesg* command displays 
the messages in the log, and the *tail -4* command shows the last four messages. The last two messages are from the module. It worked!

.. _kernel_LEDs:

Controlling LEDs by Using SYSFS Entries
========================================

Problem
---------

You want to control the onboard LEDs from the command line.

Solution
---------

On Linux, `everything is a file <http://bit.ly/1AjhWUW>`_ that is, you can access all the inputs and outputs, the LEDs, 
and so on by opening the right ``file`` and reading or writing to it. For example, try the following:

.. code-block:: bash

    bone$ cd /sys/class/leds/
    bone$ ls
    beaglebone:green:usr0  beaglebone:green:usr2
    beaglebone:green:usr1  beaglebone:green:usr3


What you are seeing are four directories, one for each onboard LED. Now try this:

.. code-block:: bash

    bone$ cd beaglebone\:green\:usr0
    bone$ ls
    brightness  device  max_brightness  power  subsystem  trigger  uevent
    bone$ cat trigger
    none nand-disk mmc0 mmc1 timer oneshot [heartbeat] 
        backlight gpio cpu0 default-on transient 


The first command changes into the directory for LED *usr0*, which is the LED closest to the edge of the board. 
The *[heartbeat]* indicates that the default trigger (behavior) for the LED is to blink in the heartbeat pattern. 
Look at your LED.  Is it blinking in a heartbeat pattern?

Then try the following:

.. code-block:: bash

    bone$ echo none > trigger
    bone$ cat trigger 
    [none] nand-disk mmc0 mmc1 timer oneshot heartbeat
        backlight gpio cpu0 default-on transient 


This instructs the LED to use *none* for a trigger. Look again. It should be no longer blinking.

Now, try turning it on and off:

.. code-block:: bash

    bone$ echo 1 > brightness
    bone$ echo 0 > brightness


The LED should be turning on and off with the commands.

.. _kernel_gpio_sysfs:

Controlling GPIOs by Using SYSFS Entries
=========================================

Problem
--------

You want to control a GPIO pin from the command line.

Solution
---------

:ref:`kernel_LEDs` introduces the *sysfs*. This recipe shows how to read and write a GPIO pin. 

Reading a GPIO Pin via sysfs
=============================

Suppose that you want to read the state of the *P9_42* GPIO pin. (:ref:`sensors_pushbutton` shows how to wire a switch to *P9_42*.)  
First, you need to map the *P9* header location to GPIO number using :ref:`kernel_gpio_map_fig`, which shows that *P9_42* maps to GPIO 7.

.. _kernel_gpio_map_fig:

.. figure:: figures/cape-headers-digitalGPIO7.png
    :align: center
    :alt: Mapping Header Position to GPIO Numbers

    Mapping P9_42 header position to GPIO 7

Next, change to the GPIO *sysfs* directory:

.. code-block:: bash

    bone$ cd /sys/class/gpio/
    bone$ ls
    export  gpiochip0  gpiochip32  gpiochip64  gpiochip96  unexport


The *ls* command shows all the GPIO pins that have be exported. In this case, none have, 
so you see only the four GPIO controllers. Export using the *export* command:

.. code-block:: bash

    bone$ echo 7 > export
    bone$ ls
    export  gpio7  gpiochip0  gpiochip32  gpiochip64  gpiochip96  unexport


Now you can see the ``gpio7`` directory. Change into the ``gpio7`` directory and look around:

.. code-block:: bash

    bone$ cd gpio7
    bone$ ls
    active_low  direction  edge  power  subsystem  uevent  value
    bone$ cat direction
    in
    bone$ cat value
    0


Notice that the pin is already configured to be an input pin. (If it wasn't already configured that way, 
use *echo in > direction* to configure it.) You can also see that its current value is *0*—that is, it 
isn't pressed. Try pressing and holding it and running again:

.. code-block:: bash

    bone$ cat value
    1


The *1* informs you that the switch is pressed. When you are done with GPIO 7, you can always *unexport* it:

.. code-block:: bash

    bone$ cd ..
    bone$ echo 7 > unexport
    bone$ ls
    export  gpiochip0  gpiochip32  gpiochip64  gpiochip96  unexport


Writing a GPIO Pin via sysfs
=============================

Now, suppose that you want to control an external LED. :ref:`displays_externalLED` shows 
how to wire an LED to *P9_14*. :ref:`kernel_gpio_map_fig` shows *P9_14* is GPIO 50. Following 
the approach in :ref:`kernel_gpio_sysfs`, enable GPIO 50 and make it an output:

.. code-block:: bash

    bone$ cd /sys/class/gpio/
    bone$ echo 50 > export
    bone$ ls
    gpio50  gpiochip0  gpiochip32  gpiochip64  gpiochip96
    bone$ cd gpio50
    bone$ ls
    active_low  direction  edge  power  subsystem  uevent  value
    bone$ cat direction
    in


By default, *P9_14* is set as an input. Switch it to an output and turn it on:

.. code-block:: bash

    bone$ echo out > direction
    bone$ echo 1 > value
    bone$ echo 0 > value


The LED turns on when a *1* is written to *value* and turns off when a *0* is written.

.. _kernel_compiling:

Compiling the Kernel
=====================

Problem
--------

You need to download, patch, and compile the kernel from its source code.

Solution
---------

This is easier than it sounds, thanks to some very powerful scripts.

.. warning:: 
    Be sure to run this recipe on your host computer. The Bone has enough computational 
    power to compile a module or two, but compiling the entire kernel takes lots of time and resources.


Downloading and Compiling the Kernel
=====================================

To download and compile the kernel, follow these steps:

.. code-block:: bash

    host$ git clone https://git.beagleboard.org/RobertCNelson/ti-linux-kernel-dev # <1>
    host$ cd ti-linux-kernel-dev
    host$ git checkout ti-linux-5.10.y # <2>
    host$ ./build_deb.sh # <3>

.. note:: 
    If you are using a 64 bit Bone, **git checkout ti-linux-arm64-5.10.y**

1. The first command clones a repository with the tools to build the kernel for the Bone.
2. When you know which kernel to try, use *git checkout* to check it out. 
   This command checks out branch *ti-linux-5.10.y*.
3. *build_deb.sh* is the master builder. If needed, it will download the cross compilers 
   needed to compile the kernel (`gcc <https://gcc.gnu.org/>`_ is the current cross compiler). 
   If there is a kernel at ``~/linux-dev``, it will use it; otherwise, 
   it will download a copy to ``ti-linux-kernel-dev/ignore/linux-src``. 
   It will then patch the kernel so that it will run on the Bone. 

.. note:: 
    *build_deb.sh* may ask you to install additional files. Just run **sudo apt install *files*** to
    install them.

After the kernel is patched, you'll see a screen similar to :ref:`kernel_config_fig`, on which you can configure the kernel.

.. _kernel_config_fig:

.. figure:: figures/KernelConfig5.10.png
    :align: center
    :alt: Kernel configuration menu

    Kernel configuration menu

You can use the arrow keys to navigate. No changes need to be made, so you can just press the right 
arrow and Enter to start the kernel compiling. The entire process took about 25 minutes on my 8-core host. 

The ``ti-linux-kernel-dev/KERNEL`` directory contains the source code for the kernel. The ``ti-linux-kernel-dev/deploy``
directory contains the compiled kernel and the files needed to run it.

.. _kernel_install:

Installing the Kernel on the Bone
===================================

The **./build_deb.sh** script creates a single .deb file that contains all the files needed for the new kernel. 
You find it here:

.. code-block:: bash

    host$ cd ti-linux-kernel-dev/deploy
    host$ ls -sh
    total 40M
    7.7M linux-headers-5.10.168-ti-r62_1xross_armhf.deb  8.0K linux-upstream_1xross_armhf.buildinfo
     33M linux-image-5.10.168-ti-r62_1xross_armhf.deb    4.0K linux-upstream_1xross_armhf.changes
    1.1M linux-libc-dev_1xross_armhf.deb

The **linux-image-** file is the one we want. It contains over 3000 files.

.. code-block:: bash

    host$ dpkg -c linux-image-5.10.168-ti-r62_1xross_armhf.deb | wc
       3251   19506  379250

The **dpkg** command lists all the files in the .deb file and the wc counts all the lines in the output. 
You can see those files with:

.. code-block:: bash
 
    host$ dpkg -c linux-image-5.10.168-ti-r62_1xross_armhf.deb | less
    drwxr-xr-x root/root         0 2023-06-12 12:57 ./
    drwxr-xr-x root/root         0 2023-06-12 12:57 ./boot/
    -rw-r--r-- root/root   4763113 2023-06-12 12:57 ./boot/System.map-5.10.168-ti-r62
    -rw-r--r-- root/root    191331 2023-06-12 12:57 ./boot/config-5.10.168-ti-r62
    drwxr-xr-x root/root         0 2023-06-12 12:57 ./boot/dtbs/
    drwxr-xr-x root/root         0 2023-06-12 12:57 ./boot/dtbs/5.10.168-ti-r62/
    -rwxr-xr-x root/root     90644 2023-06-12 12:57 ./boot/dtbs/5.10.168-ti-r62/am335x-baltos-ir2110.dtb
    -rwxr-xr-x root/root     91362 2023-06-12 12:57 ./boot/dtbs/5.10.168-ti-r62/am335x-baltos-ir3220.dtb
    -rwxr-xr-x root/root     91633 2023-06-12 12:57 ./boot/dtbs/5.10.168-ti-r62/am335x-baltos-ir5221.dtb
    -rwxr-xr-x root/root     88684 2023-06-12 12:57 ./boot/dtbs/5.10.168-ti-r62/am335x-base0033.dtb

You can see it's putting things in the **/boot** directory.

Note: You can also look into the other two .deb files and see what they install.

Move the **linux-image-** file to your Bone.

.. code-block:: bash

    host$ scp linux-image-5.10.168-ti-r62_1xross_armhf.deb bone:.

You might have to use debian@192.168.7.2 for bone if you haven't set everything up.

Now ssh to the bone.

.. code-block:: bash

    host$ ssh bone
    bone$ ls -sh
    bin  exercises linux-image-5.10.168-ti-r62_1xross_armhf.deb

Now install it.

.. code-block:: bash

    bone$ sudo dpkg --install linux-image-5.10.168-ti-r62_1xross_armhf.deb

Wait a while. (Mine took almore 2 minutes.) Once done check /boot.

.. code-block:: bash
        
    bone$ ls -sh /boot
    total 40M
    160K config-4.19.94-ti-r50        4.0K SOC.sh                     4.0K uEnv.txt.orig
    180K config-5.10.168-ti-r62       3.5M System.map-4.19.94-ti-r50  9.7M vmlinuz-4.19.94-ti-r50
    4.0K dtbs                         4.1M System.map-5.10.168-ti-r62 8.6M vmlinuz-5.10.168-ti-r62
    6.4M initrd.img-4.19.94-ti-r50    4.0K uboot
    6.8M initrd.img-5.10.168-ti-r62   4.0K uEnv.txt

You see the new kernel files along with the old files. Check uEnv.txt.

.. code-block:: bash

    bone$ head /boot/uEnv.txt
    #Docs: http://elinux.org/Beagleboard:U-boot_partitioning_layout_2.0
    # uname_r=4.19.94-ti-r50
    uname_r=5.10.168-ti-r62

I added the commented out uname_r line to make it easy to switch between versions of the kernel.

Reboot and test out the new kernel.

.. code-block:: bash

    bone$ sudo reboot

.. _kernel_using_cross_compiler:

Using the Installed Cross Compiler
===================================

.. todo
    This should be removed 

Problem
--------

You have followed the instructions in :ref:`kernel_compiling` 
and want to use the cross compiler it has downloaded.

.. tip::
    You can cross-compile without installing the 
    entire kernel source by running the following:

    .. code-block:: bash

        host$ sudo apt install gcc-arm-linux-gnueabihf


Then skip down to :ref:`kernel_skip_to_here`. 


Solution
---------

:ref:`kernel_compiling` installs a cross compiler, but you need to set up a 
couple of things so that it can be found. :ref:`kernel_compiling` installed the 
kernel and other tools in a directory called ``ti-linux-kernel-dev``. Run the 
following commands to find the path to the cross compiler:

.. code-block:: bash

    host$ cd ti-linux-kernel-dev/dl
    host$ ls
    gcc-linaro-arm-linux-gnueabihf-4.7-2013.04-20130415_linux
    gcc-linaro-arm-linux-gnueabihf-4.7-2013.04-20130415_linux.tar.xz


Here, the path to the cross compiler contains the version number 
of the compiler. Yours might be different from mine. *cd* into it:

.. code-block:: bash

    host$ cd gcc-linaro-arm-linux-gnueabihf-4.7-2013.04-20130415_linux
    host$ ls
    20130415-gcc-linaro-arm-linux-gnueabihf  bin  libexec
    arm-linux-gnueabihf                      lib  share


At this point, we are interested in what's in ``bin``:

.. code-block:: bash

    host$ cd bin
    host$ ls
    arm-linux-gnueabihf-addr2line     arm-linux-gnueabihf-gfortran
    arm-linux-gnueabihf-ar            arm-linux-gnueabihf-gprof
    arm-linux-gnueabihf-as            arm-linux-gnueabihf-ld
    arm-linux-gnueabihf-c+*           arm-linux-gnueabihf-ld.bfd
    arm-linux-gnueabihf-c++filt       arm-linux-gnueabihf-ldd
    arm-linux-gnueabihf-cpp           arm-linux-gnueabihf-ld.gold
    arm-linux-gnueabihf-ct-ng.config  arm-linux-gnueabihf-nm
    arm-linux-gnueabihf-elfedit       arm-linux-gnueabihf-objcopy
    arm-linux-gnueabihf-g+*           arm-linux-gnueabihf-objdump
    arm-linux-gnueabihf-gcc           arm-linux-gnueabihf-pkg-config
    arm-linux-gnueabihf-gcc-4.7.3     arm-linux-gnueabihf-pkg-config-real
    arm-linux-gnueabihf-gcc-ar        arm-linux-gnueabihf-ranlib
    arm-linux-gnueabihf-gcc-nm        arm-linux-gnueabihf-readelf
    arm-linux-gnueabihf-gcc-ranlib    arm-linux-gnueabihf-size
    arm-linux-gnueabihf-gcov          arm-linux-gnueabihf-strings
    arm-linux-gnueabihf-gdb           arm-linux-gnueabihf-strip


What you see are all the cross-development tools. You need to add this directory 
to the *$PATH* the shell uses to find the commands it runs:

.. code-block:: bash

    host$ pwd
    /home/yoder/BeagleBoard/ti-linux-kernel-dev/dl/\
        gcc-linaro-arm-linux-gnueabihf-4.7-2013.04-20130415_linux/bin
        
    host$ echo $PATH
        /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:\
        /usr/games:/usr/local/games


The first command displays the path to the directory where the cross-development 
tools are located. The second shows which directories are searched to find commands 
to be run. Currently, the cross-development tools are not in the *$PATH*. Let's add it:

.. code-block:: bash

    host$ export PATH=`pwd`:$PATH
    host$ echo $PATH
    /home/yoder/BeagleBoard/ti-linux-kernel-dev/dl/\
        gcc-linaro-arm-linux-gnueabihf-4.7-2013.04-20130415_linux/bin:\
        /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:\
        /usr/games:/usr/local/games


.. note:: 
    Those are backtick characters (left of the "1" key on your keyboard) around *pwd*.


The second line shows the *$PATH* now contains the directory with the cross-development tools.

.. _kernel_skip_to_here:

Setting Up Variables
=====================

Now, set up a couple of variables to know which compiler you are using:

.. code-block:: bash

    host$ export ARCH=arm
    host$ export CROSS_COMPILE=arm-linux-gnueabihf-


These lines set up the standard environmental variables so that you can determine which cross-development 
tools to use. Test the cross compiler by adding :ref:`kernel_helloWorld` to a file named _helloWorld.c_.

.. _kernel_helloWorld:

.. literalinclude:: ../code/07kernel/helloWorld.c
   :caption: Simple helloWorld.c to test cross compiling (helloWorld.c)
   :linenos:

:download:`helloWorld.c <../code/07kernel/helloWorld.c>`

You can then cross-compile by using the following commands:

.. code-block:: bash

    host$ ${CROSS_COMPILE}gcc helloWorld.c
    host$ file a.out
    a.out: ELF 32-bit LSB executable, ARM, version 1 (SYSV), 
    dynamically linked (uses shared libs), for GNU/Linux 2.6.31, 
    BuildID[sha1]=0x10182364352b9f3cb15d1aa61395aeede11a52ad, not stripped


The *file* command shows that *a.out* was compiled for an ARM processor.

.. _kernel_patches:

Applying Patches
=================

.. todo
    Remove patches?
    
Problem
--------

You have a patch file that you need to apply to the kernel.

Solution
---------

:ref:`kernel_hello_patch` shows a patch file that you can use on the kernel. 

.. _kernel_hello_patch:

.. literalinclude:: ../code/07kernel/hello.patch
   :caption: Simple kernel patch file (hello.patch)
   :linenos:

:download:`hello.patch <../code/07kernel/hello.patch>`

Here's how to use it:

- Install the kernel sources (:ref:`kernel_compiling`).
- Change to the kernel directory (+cd ti-linux-kernel-dev/KERNEL+).
- Add :ref:`kernel_hello_patch` to a file named ``hello.patch`` in the ``ti-linux-kernel-dev/KERNEL`` directory.
- Run the following commands:

.. code-block:: bash

    host$ cd ti-linux-kernel-dev/KERNEL
    host$ patch -p1 &lt; hello.patch
    patching file hello/Makefile
    patching file hello/hello.c


The output of the *patch* command apprises you of what it's doing. 
Look in the ``hello`` directory to see what was created:

.. code-block:: bash

    host$ cd hello
    host$ ls
    hello.c  Makefile

:ref:`kernel_building_modules` shows how to build and install a module, and :ref:`kernel_create_patch` 
shows how to create your own patch file.

.. _kernel_create_patch:

Creating Your Own Patch File
=============================

Problem
--------

You made a few changes to the kernel, and you want to share them with your friends.

Solution
---------

Create a patch file that contains just the changes you have made. 
Before making your changes, check out a new branch:

.. code-block:: bash

    host$ cd ti-linux-kernel-dev/KERNEL
    host$ git status
    # On branch master
    nothing to commit (working directory clean)


Good, so far no changes have been made. Now, create a new branch:

.. code-block:: bash

    host$ git checkout -b hello1
    host$ git status
    # On branch hello1
    nothing to commit (working directory clean)


You've created a new branch called ``hello1`` and checked it out. Now, make whatever changes 
to the kernel you want. I did some work with a simple character driver that we can use as an example:

.. code-block:: bash

    host$ cd ti-linux-kernel-dev/KERNEL/drivers/char/
    host$ git status
    # On branch hello1
    # Changes not staged for commit:
    #   (use "git add file..." to update what will be committed)
    #   (use "git checkout -- file..." to discard changes in working directory)
    #
    #	modified:   Kconfig
    #	modified:   Makefile
    #
    # Untracked files:
    #   (use "git add file..." to include in what will be committed)
    #
    #	examples/
    no changes added to commit (use "git add" and/or "git commit -a")


Add the files that were created and commit them:

.. code-block:: bash

    host$ git add Kconfig Makefile examples
    host$ git status
    # On branch hello1
    # Changes to be committed:
    #   (use "git reset HEAD file..." to unstage)
    #
    #	modified:   Kconfig
    #	modified:   Makefile
    #	new file:   examples/Makefile
    #	new file:   examples/hello1.c
    #
    host$ git commit -m "Files for hello1 kernel module"
    [hello1 99346d5] Files for hello1 kernel module
    4 files changed, 33 insertions(+)
    create mode 100644 drivers/char/examples/Makefile
    create mode 100644 drivers/char/examples/hello1.c
 

Finally, create the patch file:

.. code-block:: bash

    host$ git format-patch master --stdout &gt; hello1.patch

