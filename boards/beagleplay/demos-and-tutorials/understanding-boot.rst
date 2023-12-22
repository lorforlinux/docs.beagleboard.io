.. _play-understanding-boot:

Understanding Boot
##################

There are several phases to BeaglePlay boot. The simplest place to take control of
the system is using :ref:`play-distro-boot`. It is simplest because it is very generic,
not at all specific to BeaglePlay or AM62, and was included in the earliest BeagleBoard.org Debian
images shipping pre-installed in the on-board flash.

Over time, BeaglePlay images will include `SystemReady
support <https://www.arm.com/architecture/system-architectures/systemready-certification-program>`_ to
provide for the most generic boot support allowing execution of 

.. _play-distro-boot:

Distro Boot
***********

For some background on distro boot, see `the u-boot documentation on
distro boot <https://docs.u-boot.org/en/latest/develop/distro.html>`_.

In :ref:`play-typical-extlinux-conf`, you can see line 1 provides a label
and subsequent indented lines provide parameters for that boot option.

.. _play-typical-extlinux-conf:

.. code-block::
    :caption: Typical /boot/firmware/extlinux/extlinux.conf file
    :linenos:

    label Linux eMMC
        kernel /Image
        append root=/dev/mmcblk0p2 ro rootfstype=ext4 rootwait net.ifnames=0 quiet
        fdtdir /
        #fdtoverlays /overlays/<file>.dtbo
        initrd /initrd.img

It is important to note that this file is not on the root file system of BeaglePlay. It
is sitting on a separate FAT32 partition that is mounted at ``/boot/firmware``. You can
see the mounted file systems and their formats in :ref:`play-boot-mounted-fs`.

The FAT32 partition in this setup is often referred to as the boot file system.

.. _play-boot-mounted-fs:

.. code-block:: shell-session
    :caption: List of mounted file systems

    debian@BeaglePlay:~$ df
    Filesystem     1K-blocks     Used Available Use% Mounted on
    udev              903276        0    903276   0% /dev
    tmpfs             197324     1524    195800   1% /run
    /dev/mmcblk0p2  14833640 12144024   1914296  87% /
    tmpfs             986608        0    986608   0% /dev/shm
    tmpfs               5120        4      5116   1% /run/lock
    /dev/mmcblk0p1    130798    53214     77584  41% /boot/firmware
    tmpfs             197320       32    197288   1% /run/user/1000
    debian@BeaglePlay:~$ lsblk
    NAME         MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
    mmcblk0      179:0    0 14.6G  0 disk 
    ├─mmcblk0p1  179:1    0  128M  0 part /boot/firmware
    └─mmcblk0p2  179:2    0 14.5G  0 part /
    mmcblk0boot0 179:256  0    4M  1 disk 
    mmcblk0boot1 179:512  0    4M  1 disk 
    debian@BeaglePlay:~$ sudo sfdisk -l /dev/mmcblk0
    Disk /dev/mmcblk0: 14.6 GiB, 15678308352 bytes, 30621696 sectors
    Units: sectors of 1 * 512 = 512 bytes
    Sector size (logical/physical): 512 bytes / 512 bytes
    I/O size (minimum/optimal): 512 bytes / 512 bytes
    Disklabel type: dos
    Disk identifier: 0xba67172a

    Device         Boot  Start      End  Sectors  Size Id Type
    /dev/mmcblk0p1 *      2048   264191   262144  128M  c W95 FAT32 (LBA)
    /dev/mmcblk0p2      264192 30621695 30357504 14.5G 83 Linux


To better understand BeaglePlay's U-Boot Distro Boot, let's install the kernel image
we made in :ref:`play-kernel-development`. To do this, we need to have an uncompressed
version of the kernel in the FAT32 file system and a ramdisk image we plan to use. The
ramdisk image is utilized to make sure any kernel modules needed are available and to
provide a bit of a recovery opportunity in case the root file system is corrupted. You
can learn more about initrd on `the Debian Initrd Wiki page <https://wiki.debian.org/Initrd>`
and `the Linux kernel documentation admin guide initrd
entry <https://docs.kernel.org/admin-guide/initrd.html>`.

In :ref:`play-copy-kernel`, we perform a copy of the kernel that was installed via
:ref:`play-dpkg-install-kernel` and then reverted with ...

.. todo::

   Put the step into play-kernel-development.rst to revert back to the Beagle kernel.

The contents of the initrd can be read using ``lsinitramfs /boot/firmware/initrd.img-6.6.0``.

.. _play-copy-kernel:

.. code-block:: shell-session
    :caption: Copy kernel to FAT32 filesystem

    debian@BeaglePlay:~$ sudo cp /boot/vmlinuz-6.6.0 /boot/firmware/Image-6.6.gz
    [sudo] password for debian: 
    debian@BeaglePlay:~$ sudo gunzip /boot/firmware/Image-6.6.gz 
    debian@BeaglePlay:~$ sudo cp /boot/initrd.img-6.6.0 /boot/firmware/

.. _play-modified-extlinux-conf:

.. code-block::
    :caption: Modified /boot/firmware/extlinux/extlinux.conf file
    :linenos:

    menu title Select image to boot
    timeout 30
    default Linux 6.6

    label Linux default
        kernel /Image
        append root=/dev/mmcblk0p2 ro rootfstype=ext4 rootwait net.ifnames=0 quiet
        fdtdir /
        #fdtoverlays /overlays/<file>.dtbo
        initrd /initrd.img

    label Linux 6.6
        kernel /Image-6.6
        append root=/dev/mmcblk0p2 ro rootfstype=ext4 rootwait net.ifnames=0 quiet
        fdtdir /
        initrd /initrd.img-6.6.0

.. _play-boot-modified-kernel:

.. code-block:: shell-session
    :caption: Reboot into modified kernel

    debian@BeaglePlay:~$ sudo shutdown -r now
    Connection to 192.168.0.117 closed by remote host.
    Connection to 192.168.0.117 closed.
    jkridner@slotcar:~$ ssh -Y debian@192.168.0.117
    Debian GNU/Linux 11

    BeagleBoard.org Debian Bullseye Xfce Image 2023-05-18
    Support: https://bbb.io/debian
    default username:password is [debian:temppwd]

    debian@192.168.0.117's password: 

    The programs included with the Debian GNU/Linux system are free software;
    the exact distribution terms for each program are described in the
    individual files in /usr/share/doc/\*/copyright.

    Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
    permitted by applicable law.
    Last login: Tue Dec 12 15:33:21 2023 from 192.168.0.171
    debian@BeaglePlay:~$ uname -a
    Linux BeaglePlay 6.6.0 #4 SMP Tue Dec  5 13:50:59 UTC 2023 aarch64 GNU/Linux


Booting U-Boot
**************

.. _play-boot-install-emmc:

.. literalinclude:: boot/install-emmc.sh
    :caption: Install bootloader to eMMC
    :language: bash

:download:`install-emmc.sh <boot/install-emmc.sh>`

