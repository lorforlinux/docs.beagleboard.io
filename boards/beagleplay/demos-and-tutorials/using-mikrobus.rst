.. _beagleplay-mikrobus:

Using mikroBUS
##############

Using boards with ClickID
*************************

What is mikroBUS?
=================

What is ClickID?
================

ClickID enables mikroBUS add-on boards to be identified along with the configuration required to use it with the mikroBUS Linux driver. The configuration portion is called a ``manifest``.

.. note::

   Learn more at https://github.com/MikroElektronika/click_id


Does my add-on have ClickID?
============================

Look for the "ID" logo on the board. It is likely on the back.

.. todo::

   Need an image of the logo

If your add-on has ClickID, simply connect it while BeaglePlay is powered off and then apply power.

To use the add-on, see TBD below.

What if my add-on doesn't have ClickID?
=======================================

It is still possible a ``manifest`` has been created for your add-on as we have created over 100 of them. You can install the existing manifest files onto your BeaglePlay.


sudo apt update
sudo apt install bb-clickid-manifests
cat /opt/manifests/amibient-light-click.mnfb > /sys/bus/mikrobus/devices/mikrobus-0/new_device

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


.. todo::

   * Needs udev
   * Needs live description
