.. _accessories-cables:

Cables
#######

USB Cables
***********

A microUSB cable will normally be supplied with the BeagleBone Black. For other boards like PocketBeagle, BeagleBone AI & BeagleBone AI-64 you'll have to procure your own USB cable.

.. table:: USB ports on BeagleBone hardware

    +----------------------------+--------------+
    | Board                      | USB type     |
    +============================+==============+
    | BeaglePlay                 | USB-C        |
    +----------------------------+--------------+
    | BeagleV-Fire               | USB-C        |
    +----------------------------+--------------+
    | BeagleBone AI              | USB-C        |
    +----------------------------+--------------+
    | BeagleBone AI-64           | USB-C        |
    +----------------------------+--------------+
    | BeagleV-Ahead              | microUSB 3.0 |
    +----------------------------+--------------+
    | BeagleBone Black           | miniUSB      |
    +----------------------------+--------------+
    | PocketBeagle               | microUSB     |
    +----------------------------+--------------+
    | BeagleBone Blue            | microUSB     |
    +----------------------------+--------------+
    | BeagleBone Black Wireless  | microUSB     |
    +----------------------------+--------------+
    | BeagleBone xM              | miniUSB      |
    +----------------------------+--------------+
    | BeagleBone X15             | microUSB     |
    +----------------------------+--------------+

.. _serial-debug-cables:

Serial Debug Cables
********************

The default serial port settings for BeagleBoards are:

.. table:: UART settings

    +--------------+--------------+
    | Setting      | Value        |
    +==============+==============+
    | Baud         | 115,200      |
    +--------------+--------------+
    | Bits         | 8            |
    +--------------+--------------+
    | Parity       | N            |
    +--------------+--------------+
    | Stop Bits    | 1            |
    +--------------+--------------+
    | Handshake    | None         |
    +--------------+--------------+

JST-SH serial cables
====================

These cables are not active (only wries and connector) and provide an interface 
between USB to Serial converter cables such as the ones listed below and serial debug ports on BeagleBoards such as the BeagleBone AI 
and AI-64. You can purchase these cables from different sources including:

1. `Farnell <https://www.newark.com/element14/1103004000156/serial-cable-ai-board/dp/50AH3702>`_
2. `DigiKey <https://www.digikey.com/en/products/detail/digi-key-electronics/BBCAI/10187731>`_

Standard FTDI Cable
====================

The debug cable is a standard FTDI to TTL cable. **Make sure you get the 3.3V version**! 
It can purchased from several different sources including but not limited to:

- `FTDI serial cable direct <https://www.ftdichip.com/Products/Cables/USBTTLSerial.htm>`_
- `FTDI serial cable at DigiKey <https://www.digikey.com/product-detail/en/TTL-232R-3V3/768-1015-ND/1836393>`_
- `FTDI serial cable at Newark <https://www.newark.com/ftdi/ttl-232r-3v3/usb-to-serial-converter-cable/dp/34M8872?st=TTL-232R-3V3>`_
- `FTDI serial cable at Sparkfun <https://www.sparkfun.com/products/9717>`_
- `FTDI serial cable at Adafruit <https://www.adafruit.com/products/70>`_

Other options with different USB to Serial ICs exist and will work as well, such as CP2102, CH340G etc but may require additional drivers depending on your operating system.

.. image:: images/FTDI_Cable.jpg
    :align: center
    :alt: FTDI Cable

Pin 1 on the cable is the black wire and connects to pin 1 on the board. (the pin with the white dot next to it)

Adafruit 4 Pin Cable (CP2102)
==============================

`Adafruit 4-pin serial cable <http://www.adafruit.com/products/954>`_ (Originally 
this was a Prolific chipset based cable, as of Dec. 21, 2016 Adafruit will be 
shipping cables with SiLabs CP2012 chipset instead of Prolific.)

.. image:: images/RPI_Serial.png
    :align: center
    :alt: 4 pin serial cable
    
.. table:: Adafruit 4 pin serial cable connection to BeagleBone Black

    +--------------+--------------+
    | Board        | Wire         |
    +==============+==============+
    | Pin 1 (GND)  | Black (GND)  |
    +--------------+--------------+
    | Pin 4 (RX)   | Green (TX)   |
    +--------------+--------------+
    | Pin 5 (TX)   | White (RX)   |
    +--------------+--------------+

.. note:: 
    The naming of the signals reflect those of the cable. 
    The swapping of TX and RX takes place on the board.

    You will also find an extra RED wire on this cable 
    that supplies 5V @ 500mA which could power the 
    board if connected to one of the VDD_5V pins. 
    It's recommended that you leave it unconnected.


JTAG debug Cables
*****************

TagConnect (JTAG)
==================

Boards like :ref:`beagleconnect_freedom_home` and :ref:`beagleplay-home` use the TagConnect 
interface which allows you to perform firmware updates and JTAG hardware debugging. To use the 
interface, the the parts below from `tag-connect <https://www.tag-connect.com>`_  are required.

1. `10pin TagConnect (no legs) ribbon cable. <https://www.tag-connect.com/product/tc2050-idc-nl-10-pin-no-legs-cable-with-ribbon-connector>`_
2. `TagConnect retaining clip. <https://www.tag-connect.com/product/tc2050-clip-3pack-retaining-clip>`_


HDMI Cables
************

Working HDMI Cables
====================

The BeagleBone Black uses a microHDMI cable. 

.. image:: images/MicroHDMI.jpg
    :align: center
    :alt: MicroHDMI to HDMI cable

microHDMI to VGA
=================

`Cable Matters Micro HDMI to VGA Adapter <https://www.amazon.com/Cable-Matters-Active-Female-Adapter/dp/B00879EZJI/ref=sr_1_2?ie=UTF8&qid=1381610066&sr=8-2&keywords=micro-hdmi+to+vga>`_

miniDP to HDMI 
****************

Working miniDP to HDMI Adapters
=======================

.. note::
    BeagleBone-AI64 requires an **ACTIVE** Mini DisplayPort to HDMI cable or adaptor to work, 
    a passive miniDP to HDMI setup will not work at all.

- `IVANKY 4K Active Mini DisplayPort to HDMI Adapter <https://www.amazon.com/dp/B089GF8M87/>`_
- `CableCreation Mini DP (Thunderbolt 2 Compatible) to HDMI <https://www.amazon.in/CD0257-Mini-DP-to-HDMI/dp/B01FM51O0W/>`_

Examples of "Bad" MiniDP to HDMI Adapters
=================================

- `UGREEN Mini DP Male to HDMI <https://www.amazon.in/Mini-Male-Female-Converter-Cable/dp/B01CL1P6TA/>`_
- `AGARO Mini Displayport (Mini Dp) To Hdmi <https://www.amazon.in/AGARO-Meters-Laptop-Computers-Mobile/dp/B09GW1NMNZ/>`_
- `AmazonBasics Mini Display Port to HDMI <https://www.amazon.in/AmazonBasics-Mini-DisplayPort-HDMI-Adapter/dp/B0134V3KIA/>`_
