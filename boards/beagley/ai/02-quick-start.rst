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

.. todo:: Attaching antennas instructions for BeagleY-AI

.. todo:: BeagleY-AI unboxing video

Getting started
***************

To get started your BeagleY-AI you need the following:

1. :ref:`5V @ 3A power supply <accessories-power-supplies>`
2. MicroSD Card (32GB)
3. Boot media (Software image)

You may need additional accessories based on the mode of operation, you can use your BeagleY-AI in different ways.

1. :ref:`USB Tethering by directly connecting via USB type-c port <beagley-ai-usb-tethering>`
2. :ref:`Headless connection via UART debug port <beagley-ai-headless>`
3. :ref:`Standalone connection with Monitor and other peripherals attached <standalone-connection>`

Easiest option is to connect the board directly to your PC or Laptop using a USB type-C to type-c cable. There is only one USB type-C port on board, if you 
choose to use a dedicated power supply for first time setup, you may choose to access the board via any other methods listed above.

Power Supply
=============

To power the board you can either connect it to a dedicated power supply like a mobile charger or a wall adapter that 
can provide 5V ≥ 3A. Checkout the :ref:`docs power supply page <accessories-power-supplies>` for power supply recommendations.

.. note:: 
    Instead of using a :ref:`power supply or power adapter <accessories-power-supplies>` if you are using a :ref:`USB type-A to 
    type-C cable or type-C to type-C cable <accessories-cables-usb>` to connect the board to your laptop/PC then make sure it can supply at least 1000mA.

Boot Media (Software image)
============================

.. todo:: Update this section to use latest boot media (software image) for BeagleY-AI.

Download the boot media from
`https://www.beagleboard.org/distros/beagley-ai-debian-xfce-12-5-2024-03-25 <https://www.beagleboard.org/distros/beagley-ai-debian-xfce-12-5-2024-03-25>`_ 
and flash it on a micro SD Card using using `Balena Etcher <https://etcher.balena.io/>`_ following these steps:

1. Select downloaded boot media
2. Select SD Card 
3. Flash!

.. tip:: For more detailed steps checkout the :ref:`beagleboard-getting-started` under support section of the documentation.

.. image:: images/balena-etcher.*

Once flashed, you can insert the SD card into your BeagleY-AI as shown in the image below:

.. image:: images/beagley-ai-micro-sd-card.*

.. _beagley-ai-usb-tethering:

USB Tethering
==============

.. note:: 
    If you are using the board with a fan or running a heavy task you should always power 
    the board with a dedicated power supply that can supply 5V ≥ 3A. 

    As per USB standards these are the current that each cable can supply:

    - Type-A to Type-C - 900mA
    - Type-C to Type-C - 1500mA

    Thus it's recommended to use type-C to type-C cable.

To initially test your board, you can connect the board directly to your computer using a ``type-A to type-C`` or ``type-C to type-C`` cable shown in the image below.

.. figure:: images/beagley-ai-tethered-connection.*
    :align: center
    :alt: BeagleY-AI tethered connection

    BeagleY-AI tethered connection

After connecting, you should see the power LED glow, and soon just like with other Beagles, BeagleY-AI will create a virtual wired connection on your computer. To access the board you can use the SSH command as shown below.

.. code:: shell
    
    ssh debian@192.168.7.2

.. note::
    Here you must update the default password to something safer.

.. figure:: images/ssh-connection.*
    :align: center 
    :alt: BeagleY-AI SSH connection

    BeagleY-AI SSH connection

With this you have the access to BeagleY-AI terminal. Now, you can connect your board to WiFi, 
try out all the cool demos and explore all the other ways to access your BeagleY-AI.

- :ref:`beagley-ai-connecting-wifi`
- :ref:`beagley-ai-demos`

.. _beagley-ai-headless:

Headless connection
===================

If you want to run your BeagleY-AI in headless mode, you need `Raspberry Pi Debug Probe <https://www.raspberrypi.com/documentation/microcontrollers/debug-probe.html>`_ or similar serial adapter.

.. _standalone-connection:

Standalone connection
=====================

To setup your BeagleY-AI for standalone usage, you need the following additional accessories,

1. HDMI monitor
2. micro HDMI to full-size HDMI cable
3. Wireless keyboard & mice combo
4. Ethernet cable (Optional)

Make sure you have the sd Card with boot media (software image) inserted in to the BeagleY-AI. Now connect,

1. microHDMI to BeagleY-AI and full size HDMI to monitor
2. keyboard and mice combo to one of the four USB port of BeagleY-AI
3. Power supply to USB type-c connector of BeagleY-AI

The connection diagram below provides a clear representation of all the connections,

.. image:: images/standalone.*

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

.. _beagley-ai-connecting-wifi:

Connecting to WiFi
===================

Once board is fully booted and you have access to the shell, follow the commands below to connect to any WiFi access point,

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

Attach fan
==========

.. todo:: add instructions to attach raspberrypi official fan.

Demos and Tutorials
*******************

* :ref:`beagley-ai-expansion-nvme`
