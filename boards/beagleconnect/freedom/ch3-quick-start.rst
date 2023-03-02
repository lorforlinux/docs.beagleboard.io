.. _beagleconnect-freedom-quick-start:

Quick Start Guide
####################

This section describes the usage model we are developing. To use the current
code in development, please refer to the [development] section.


BeagleConnect wireless user experience
***************************************

Enable a Linux host with BeagleConnect
=======================================
.. image:: media/ProvStep1.jpg
   :width: 600
   :align: center
   :height: 400
   :alt: ProvStep1

Log into a host system running Linux that is BeagleConnect™ enabled. Enable a
Linux host with BeagleConnect™ by plugging a **BeagleConnect™ gateway device**
into its USB port. You’ll also want to have a **BeagleConnect™ node device**
with a sensor, actuator or indicator device connected.

.. note::
  BeagleConnect™ Freedom can act as either a BeagleConnect™ gateway device
  or a BeagleConnect™ node device.

.. important::
  The Linux host will need to run the BeagleConnect™ management
  software, most of which is incorporated into the Linux kernel. Support will be
  provided for BeagleBoard and BeagleBone boards, x86 hosts, and Raspberry Pi.

#TODO#: Clean up images

Connect host and device
=======================

.. image:: media/ProvStep2.jpg
   :width: 600
   :align: center
   :height: 400
   :alt: ProvStep2

Initiate a connection between the host and devices by pressing the discovery
button(s).

Device data shows up as files
=============================

.. image:: media/ProvStep3.jpg
   :width: 600
   :align: center
   :height: 400
   :alt: ProvStep3

New streams of self-describing data show up on the host system using native
device drivers.

High-level applications, like Node-RED, can directly read/write these
high-level data streams (including data-type information) to Internet-based
`MQTT <https://mqtt.org/>`_ brokers, live dashboards, or other logical
operations without requiring any sensor-specific coding. Business logic can be
applied using simple if-this-then-that style operations or be made as complex
as desired using virtually any programming language or environment.

Components
**********

BeagleConnect™ enabled host Linux computer, possibly single-board computer
(SBC), with BeagleConnect™ management software and BeagleConnect™ gateway
function. BeagleConnect™ gateway function can be provided by a BeagleConnect™
compatible interface or by connecting a BeagleConnect™ **gateway** device over USB.

.. note::
  If the Linux host has BLE, the BeagleConnect™ **gateway** is optional for short
  distances

BeagleConnect™ Freedom Board, case, and wireless MCU with Zephyr based firmware
for acting as either a BeagleConnect™ gateway device or BeagleConnect™ node
device.

* In BeagleConnect™ **gateway** device mode: Provides long-range, low-power
  wireless communications, Connects with the host via USB and an associated
  Linux kernel driver, and is powered by the USB connector.
* In BeagleConnect™ **node** device mode: Powered by a battery or USB connector
  Provides 2 mikroBUS connectors for connecting any of hundreds of `Click Board <https://bbb.io/click>`_
  mikroBUS add-on devices Provides new Linux host controllers for SPI, I2C,
  UART, PWM, ADC, and GPIO with interrupts via Greybus

BeagleConnect **gateway** device
==================================

Provides a BeagleConnect™ compatible interface to a host. This could be a
built-in interface device or one connected over USB. BeagleConnect™ Freedom can
provide this function.

BeagleConnect **node** device
==============================

Utilizes a BeagleConnect™ compatible interface and TODO

BeagleConnect compatible interface
==================================

Immediate plans are to support Bluetooth Low Energy (BLE), 2.4GHz IEEE 802.15.4
, and Sub-GHz IEEE 802.15.4 wireless interfaces. A built-in BLE interface is
suitable for this at short range, whereas IEEE 802.15.4 is typically
significantly better at long ranges. Other wired interfaces, such as CAN and
RS-485, are being considered for future BeagleConnect™ gateway device and
BeagleConnect™ node device designs.

Greybus
-------

TODO

#TODO: Find a place for the following notes:

* The device interfaces get exposed to the host via Greybus BRIDGED_PHY
  protocol
* The I2C bus is probed for a an identifier EEPROM and appropriate device
  drivers are loaded on the host
* Unsupported Click Boards connected are exposed via userspace drivers on the
  host for development

What’s different?
*****************

So, in summary, what is so different with this approach?

* No microcontroller code development is required by users
* Userspace drivers make rapid prototyping really easy
* Kernel drivers makes the support code collaborative parts of the Linux kernel
  , rather than cut-and-paste

.. _beagleconnect-zephyr:

BeagleConnect Freedom & Zephyr
******************************

Develop for BeagleConnect Freedom with Zephyr
**********************************************

Developing directly in Zephyr will not be ultimately required for end-users 
who won't touch the firmware running on BeagleConnect™ Freedom and will instead
use the BeagleConnect™ Greybus functionality, but is important for early 
adopters as well as people looking to extend the functionality of the open 
source design. If you are one of those people, this is a good place to get 
started.

Equipment to begin development
==============================

There are many options, but let's get started with one recommended set for the beta users.

Required
--------

* beta-kit
    * Seeed Studio BeagleBone® Green Gateway

    * 3x BeagleConnect™ Freedom board, antenna, U.FL to SMA cable, SMA antenna and USB Type-A to Type-C cable

    * 1x MikroE ID Click

* microSD card (6GB or larger)

* microSD card programmer

Recommended
-----------

* `12V power brick <https://smile.amazon.com/TMEZON-Power-Adapter-Supply-2-1mm/dp/B00Q2E5IXW>`_

* `USB to TTL 3.3V UART adapter <https://smile.amazon.com/Converter-Terminated-Galileo-BeagleBone-Minnowboard/dp/B06ZYPLFNB>`_

* Ethernet cable and Internet connection

* 2x USB power adapters

* `BME280-based Weather Click <https://www.mikroe.com/weather-click>`_

* `iAQ-Core-based Air Quality 2 Click <https://www.mikroe.com/air-quality-2-click>`_

Optional
--------

* x86_64 computer running Ubuntu 20.04.3 LTS


Install the latest software image for BeagleBone Green Gateway
==============================================================

Download and install the Debian Linux operating system image for the Seeed 
BeagleBone® Green Gateway host.

#. Download the special mikroBUS/Greybus BeagleBoard.org Debian image from 
   `here <https://rcn-ee.net/rootfs/debian-mikrobus-armhf/>`_. Pick the most 
   recent directory and select the file beginning with **bone-** and ending with 
   **.img.xz**. Today that file is 
   **bone-debian-11.2-iot-mikrobus-armhf-2022-03-04-4gb.img.xz**.

#. Load this image to a microSD card using a tool like Etcher.

#. Insert the microSD card into the Green Gateway.

#. Power BeagleBone Green Gateway via the 12V barrel jack.

#TODO: describe how to know it is working

Other systems
-------------

.. important::

    If you are using the image above, none of the instructions in this section are required.

#. Update the system.
    .. code-block:: bash
        
        sudo apt update

#. Install all BeagleConnect™ management software.
    .. code-block:: bash

        sudo apt install -y \
        beagleconnect beagleconnect-msp430 \
        git vim \
        build-essential \
        cmake ninja-build gperf \
        ccache dfu-util device-tree-compiler \
        make gcc libsdl2-dev \
        libxml2-dev libxslt-dev libssl-dev libjpeg62-turbo-dev \
        gcc-arm-none-eabi libnewlib-arm-none-eabi \
        libtool-bin pkg-config autoconf automake libusb-1.0-0-dev \
        python3-dev python3-pip python3-setuptools python3-tk python3-wheel

    .. code-block:: bash

        echo "export PATH=$PATH:$HOME/.local/bin" >> $HOME/.bashrc

    .. code-block:: bash

        source $HOME/.bashrc

#. Reboot
    .. code-block:: bash

        sudo reboot

#. Install BeagleConnect™ flashing software
    .. code-block:: bash

        pip3 install -U west

#. Reboot
    .. code-block:: bash

        sudo reboot


Log into BeagleBone Green Gateway
=================================

These instructions assume an x86_64 computer running Ubuntu 20.04.3 LTS, but any
computer can be used to connect to your BeagleBone Green Gateway.

#. Log onto the Seeed BeagleBone® Green Gateway using :code:`ssh`.
    * We need IP address, Username, and Password to connect to the device.
    * The default IP for the BeagleBone hardware is :code:`192.168.7.2`
    * The default Username is :code:`debian` & Password is :code:`temppwd`
    * To connect you can simply type :code:`$ ssh debian@192.168.7.2` and when 
      asked for password just type :code:`temppwd`
    * Congratulations, You are now connected to the device!
#. Connect to the `WiFi <https://forum.beagleboard.org/t/debian-11-x-bullseye-monthly-snapshots/31280>`_
    * Execute :code:`sudo nano /etc/wpa_supplicant/wpa_supplicant-wlan0.conf` 
      and provide the password :code:`temppwd` to edit the configuration file 
      for the WiFi connection.
    * Now edit the file (shown below) under the :code:`network={...}`
      section you can set you :code:`ssid` (WiFi name) and :code:`psk` (Wifi 
      Password).

      .. code-block::

        ctrl_interface=DIR=/run/wpa_supplicant GROUP=netdev
        update_config=1
        #country=IN
        network={
                ssid="WiFi Name"
                psk="WiFi Password"
        }

    * Now save the file with :code:`CTRL+O` and exit with :code:`CTRL+X`.
    * Check if the connection is established by executing :code:`$ ping 8.8.8.8`
      you should see something like shown below.

      .. code-block:: bash

        debian@BeagleBone:~$ ping 8.8.8.8
        PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
        64 bytes from 8.8.8.8: icmp_seq=1 ttl=118 time=10.5 ms
        64 bytes from 8.8.8.8: icmp_seq=2 ttl=118 time=5.72 ms
        64 bytes from 8.8.8.8: icmp_seq=3 ttl=118 time=6.13 ms
        64 bytes from 8.8.8.8: icmp_seq=4 ttl=118 time=6.11 ms
        ...

    * If everything goes well, you are ready to update your system and install 
      new applications for beagleconnect.

.. note:

    If you are facing some issue during boot then you can try debugging the 
    boot session with a USB to serial interface cable such as those made by FTDI 
    plugged into J10 with the black wire of the FTDI cable toward the Ethernet 
    connector. Application like tio/minicom/putty can be used to make the connection 
    establishment procedure easy. 

.. note:

   #TODO#: Simplify and elaborate on this section, add boot session debugging walkthrough

Install Zephyr development tools on BeagleBone Green Gateway
============================================================

#. Download and setup Zephyr for BeagleConnect™
    .. code-block:: bash
        
        cd
        west init -m https://github.com/jadonk/zephyr --mr bcf-sdk-3.1.0-rebase bcf-zephyr
        cd $HOME/bcf-zephyr
        west update
        west zephyr-export
        pip3 install -r zephyr/scripts/requirements-base.txt
        echo "export CROSS_COMPILE=/usr/bin/arm-none-eabi-" >> $HOME/.bashrc
        echo "export ZEPHYR_BASE=$HOME/bcf-zephyr/zephyr" >> $HOME/.bashrc
        echo "export PATH=$HOME/bcf-zephyr/zephyr/scripts:$PATH" >> $HOME/.bashrc
        echo "export BOARD=beagleconnect_freedom" >> $HOME/.bashrc
        source $HOME/.bashrc
    
Build applications for BeagleConnect Freedom on BeagleBone Green Gateway
========================================================================

Now you can build various Zephyr applications

#. Change directory to BeagleConnect Freedom zephyr repository.

    .. code-block:: bash

        cd $HOME/bcf-zephyr
        
#. Build blinky example

    .. code-block:: bash

        west build -d build/blinky zephyr/samples/basic/blinky

#. TODO

    .. code-block:: bash

        west build -d build/sensortest zephyr/samples/boards/beagle_bcf/sensortest -- -DOVERLAY_CONFIG=overlay-subghz.conf

#. TODO

    .. code-block:: bash

        west build -d build/wpanusb modules/lib/wpanusb_bc -- -DOVERLAY_CONFIG=overlay-subghz.conf

#. TODO

    .. code-block:: bash

        west build -d build/bcfserial modules/lib/wpanusb_bc -- -DOVERLAY_CONFIG=overlay-bcfserial.conf -DDTC_OVERLAY_FILE=bcfserial.overlay

#. TODO

    .. code-block:: bash

        west build -d build/greybus modules/lib/greybus/samples/subsys/greybus/net -- -DOVERLAY_CONFIG=overlay-802154-subg.conf


Flash applications to BeagleConnect Freedom from BeagleBone Green Gateway
=========================================================================

And then you can flash the BeagleConnect Freedom boards over USB

#. Make sure you are in Zephyr directory
    .. code-block:: bash

        cd $HOME/bcf-zephyr

#. Flash Blinky
    .. code-block:: bash

        cc2538-bsl.py build/blinky

Debug applications over the serial terminal
===========================================

#TODO#
