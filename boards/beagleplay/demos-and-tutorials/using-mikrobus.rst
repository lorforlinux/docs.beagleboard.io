.. _beagleplay-mikrobus:

Using mikroBUS
##############

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
