.. _imx219-csi-cameras:

.. note:: This page is a work in progress. Further drive testing and images will be added soon


Using IMX219 CSI Cameras
############################

To enable an IMX219 CSI camera, modify the following file: /boot/firmware/extlinux/extlinux.conf

Using CSI Port 0
**************************************

Then, add the following line to load the IMX219 CSI0 DTBO: 

.. code:: bash

   fdtoverlays /overlays/k3-am625-beagleplay-lt-lcd185.dtbo

Your /boot/firmware/extlinux/extlinux.conf file should look something like this:

.. code:: bash

   label Linux eMMC
      kernel /Image
      append root=/dev/mmcblk0p2 ro rootfstype=ext4 rootwait net.ifnames=0 systemd.unified_cgroup_hierarchy=false quiet
      fdtdir /
      fdtoverlays /overlays/k3-am625-beagleplay-lt-lcd185.dtbo
      initrd /initrd.img

Using CSI Port 1
*******************


Troubleshooting
*******************