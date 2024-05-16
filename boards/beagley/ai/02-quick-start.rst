.. _beagley-ai-quick-start:

BeagleY-AI Quick Start
######################

What's included in the box?
****************************

.. todo:: Update BeagleY-AI what's included in the box section as per production release.

When you purchase a BeagleY-AI, you'll get the following in the box:

1. `BeagleY-AI <https://www.beagleboard.org/boards/beagley-ai>`_
2. 2.4GHz antenna
3. Quick-start card

.. tip:: For board files, 3D model, and more, you can checkout the `BeagleY-AI repository on OpenBeagle <https://openbeagle.org/beagley-ai/beagley-ai>`_.

.. todo:: Attaching antennas instructions for BeagleY-AI

.. todo:: BeagleY-AI unboxing video

Getting started
***************

To get started you need the following:

1. :ref:`USB type-A to type-C cable or type-C to type-C cable <accessories-cables-usb>`
2. :ref:`5V - 3A power supply <accessories-power-supplies>`
3. MicroSD Card 
4. Boot media

Boot Media
===========

Download the boot media from
`https://www.beagleboard.org/distros/beagley-ai-debian-xfce-12-5-2024-03-25 <https://www.beagleboard.org/distros/beagley-ai-debian-xfce-12-5-2024-03-25>`_ 
and flash it on a micro SD Card using using `Balena Etcher <https://etcher.balena.io/>`_ following these steps:

1. Select downloaded boot media
2. Select SD Card 
3. Flash!

.. image:: images/balena-etcher.*

Once flashed, you can insert the SD card into your BeagleY-AI as shown in the image below:

.. image:: images/beagley-ai-micro-sd-card.*

Power Supply
=============

To power the board you can either connect it to a dedicated power supply like a mobile charger or a wall adapter that 
can provide 5V ≥ 3A. Checkout the `docs power supply page <https://docs.beagleboard.org/latest/accessories/power-supplies.html#accessories-power-supplies>`_ 
for power supply recommendations.

Board connection
=================

There is only one USB type-C port on board, if you choose to use a dedicated power supply for first time setup, you may access the board via one of the following methods:

1. Connection to HDMI display, Keyboard and Mouse
2. UART using RPi debug probe or similar
3. Ethernet network connection

Another direct and easy option is to connect the board directly to your PC or Laptop using a USB type-C cable. 

.. note:: 
    If you are using the board with a fan or running a heavy task you should always power 
    the board with a dedicated power supply that can supply 5V ≥ 3A. 

USB Tethering
==============

To initially test your board, you can connect the board directly to your computer using a type-A to type-C cable shown in the image below. 

.. image:: images/beagley-ai-tethered-connection.*

After connecting, you should see the power LED glow, and soon just like with other Beagles, you’ll see a virtual wired connection on your computer. To access the board you can use SSH as shown below.

.. note::
    Here you must update the default password to something safer.

.. image:: images/ssh-connection.*

Using BeagleY-AI 
=================

To setup your BeagleY-AI for normal usage, connect the following:

 1. 5V ≥ 3A power supply
 2. HDMI monitor using micro HDMI to full-size HDMI cable
 3. Ethernet cable from the board to your router
 4. Wireless or wired keyboard & mice

.. image:: images/beagley-ai-tethered-connection.*

If everything is connected properly you should see four penguins on your monitor.

.. image:: images/boot-penguins.*

When prompted, log in using the updated login credentials you updated during the USB tethering step.

.. note:: You can not update login credentials at this step, you must update them during USB tethering step!

.. image:: images/login.*

Once logged in you should see the splash screen shown in the image below:

.. image:: images/screen-saver.*

Test network connection by running ping 8.8.8.8

.. image:: images/ping-test.*

Explore and build with your new BeagleY-AI board!

.. image:: images/htop.*

Connecting to WiFi
===================

Connect 2x antennas to your BeagleY-AI board if not pre-attached.

After successfully attaching the antenna, power up the board. Once booted you can follow the commands below to connect to any WiFi access point,

- To list the wireless devices attached, (you should see wlan0 listed)

.. code:: shell

    iwctl device list

- Scan WiFi using,

.. code:: shell

    iwctl station wlan0 scan

- Get networks using, 

.. code:: shell

    iwctl station wlan0 get-networks

- Connect to your wifi network using, 

.. code::

    iwctl --passphrase "<wifi-pass>" station wlan0 connect "<wifi-name>"

- Check wlan0 status with, 

.. code::

    iwctl station wlan0 show

- To list the networks with connected WiFi marked you can again use, 

.. code::

    iwctl station wlan0 get-networks

- Test connection with ping command,

.. code::
    
    ping 8.8.8.8

Demos and Tutorials
*******************

* :ref:`beagley-ai-expansion-nvme`
