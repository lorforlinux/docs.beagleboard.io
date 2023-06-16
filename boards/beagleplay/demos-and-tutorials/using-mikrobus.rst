.. _beagleplay-mikrobus:

Using mikroBUS
##############

Using boards with ClickID
*************************

What is mikroBUS?
=================

mikroBUS is an open standard for add-on boards for sensors, connectivity, displays, storage and more with over 1,400 available from just a single source, `MikroE <https://www.mikroe.com/click>`_. With the flexibility of all of the most common embedded serial busses, UART, I2C and SPI, along with ADC, PWM and GPIO functions, it is a great solution for connecting all sorts of electronics.

.. note::

   Learn more at https://www.mikroe.com/mikrobus

What is ClickID?
================

ClickID enables mikroBUS add-on boards to be identified along with the configuration required to use it with the mikroBUS Linux driver. The configuration portion is called a ``manifest``.

.. note::

   Learn more at https://github.com/MikroElektronika/click_id

BeaglePlay's Linux kernel is patched with a mikrobus driver that automatically reads the ClickID and loads a driver, greatly simplifying usage.


Does my add-on have ClickID?
============================

Look for the "ID" logo on the board. It should be on the side with the pins sticking out, near the AN pin.

.. todo::

   Need an image of the logo

If your add-on has ClickID, simply connect it while BeaglePlay is powered off and then apply power.

To use the add-on, see TBD below.

What if my add-on doesn't have ClickID?
=======================================

It is still possible a ``manifest`` has been created for your add-on as we have created over 100 of them. You can install the existing manifest files onto your BeaglePlay.


.. code::

   sudo apt update
   sudo apt install bb-clickid-manifests
   cat /lib/firmware/mikrobus/amibient-light-click.mnfb > /sys/bus/mikrobus/devices/mikrobus-0/new_device

It'll forget on reboot... need to have a boot service.

To make it stick, ...


Steps:

1. Identify if mikroBUS add-on includes an ID. If not, ID must be supplied.
2. Identify if mikroBUS add-on is supported by the kernel. If not, kernel module must be added.
3. Identify how driver exposes the data: IIO, net, etc.
4. Connect and power
5. Verify and utilize

.. note::

   We will be adding a link to the ``mikrobus-0`` device at ``/dev/play/mikrobus`` in the near
   future, but you can find it for now at ``/sys/bus/mikrobus/devices/mikrobus-0``. If you
   need to supply an ID (manifest), this is the directory where you will do it.

   Manifesto: https://git.beagleboard.org/beagleconnect/manifesto

   Patched Linux with out-of-tree Mikrobus driver: https://git.beagleboard.org/beagleboard/linux


How does ClickID work?
**********************


Disabling the mikroBUS driver
*****************************

If you'd like to use other means to control the mikroBUS connector, you might want to disable the mikroBUS driver. This is most easily done by enabling a deivce tree overlay at boot.

.. todo::

    Document kernel version that integrates this overlay and where to get update instructions.

.. note::

    To utilize the overlay with these instructions, make sure to have TBD version of kernel, modules and firmware installed. Use `uname -a` to determine the currently running kernel version. See TBD for information on how to update.

Apply overlay to disable mikrobus0 instance.

.. code-block:: bash

    echo "    fdtoverlays /overlays/k3-am625-beagleplay-release-mikrobus.dtbo" | sudo tee -a /boot/firmware/extlinux/extlinux.conf
    sudo shutdown -r now

Log back in after reboot and verify the device driver did not capture the busses.

.. code-block:: shell-session

    debian@BeaglePlay:~$ ls /dev/play
    grove  mikrobus  qwiic
    debian@BeaglePlay:~$ ls /dev/play/mikrobus/
    i2c
    debian@BeaglePlay:~$ ls /sys/bus/mikrobus/devices/
    debian@BeaglePlay:~$ ls /proc/device-tree/chosen/overlays/
    k3-am625-beagleplay-release-mikrobus  name
    debian@BeaglePlay:~$

To re-enable.

.. code-block:: bash

    sudo sed -e '/release-mikrobus/ s/^#*/#/' -i /boot/firmware/extlinux/extlinux.conf
    sudo shutdown -r now

Verify driver is enabled again.

.. code-block:: shell-session

    debian@BeaglePlay:~$ ls /sys/bus/mikrobus/devices/
    mikrobus-0
    debian@BeaglePlay:~$ ls /proc/device-tree/chosen/overlays/
    ls: cannot access '/proc/device-tree/chosen/overlays/': No such file or directory
    debian@BeaglePlay:~$

.. todo::

   * How do turn off the driver?
   * How do turn on spidev?
   * How do I enable GPIO?
   * How do a provide a manifest?


.. todo::

   * Needs udev
   * Needs live description
