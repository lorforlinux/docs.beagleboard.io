.. _accessories-cables:

Cables
#######

USB Cables
***********

A microUSB cable will normally be supplied with the BeagleBone Black. For other beaglebone boards like PocketBeagle, BeagleBone AI, 
BeagleBone AI-64 you'll have to procure your own USB cable.

.. table:: USB ports on BeagleBone hardware

    +----------------------------+--------------+
    | Board                      | USB type     |
    +============================+==============+
    | BeagleBone Play            | USB-C        |
    +----------------------------+--------------+
    | BeagleBone Black           | miniUSB      |
    +----------------------------+--------------+
    | PocketBeagle               | microUSB     |
    +----------------------------+--------------+
    | BeagleBone AI              | USB-C        |
    +----------------------------+--------------+
    | BeagleBone AI-64           | USB-C        |
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

The default serial port settings for the board are:

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

TagConnect (JTAG)
==================

Boards like :ref:`beagleconnect_freedom_home` and :ref:`beagleplay-home` use the TagConnect 
interface which allows you to perform firmware updates and JTAG hardware debugging. To use the 
interface, the the parts below from `tag-connect <https://www.tag-connect.com>`_  are required.

1. `10pin TagConnect (no legs) ribbon cable. <https://www.tag-connect.com/product/tc2050-idc-nl-10-pin-no-legs-cable-with-ribbon-connector>`_
2. `TagConnect retaining clip. <https://www.tag-connect.com/product/tc2050-clip-3pack-retaining-clip>`_

Standard FTDI Cable
====================

The debug cable is a standard FTDI to TTL cable. Make sure you get the 3.3V version. 
It can purchased from several different sources including but not limited to:

- `DigiKey <http://www.digikey.com/product-detail/en/TTL-232R-3V3/768-1015-ND/1836393>`_
- `Newark <http://www.newark.com/jsp/search/productdetail.jsp?SKU=34M8872&CMP=KNC-GPLA&mckv=%7Cpcrid%7C19038771501%7Cplid%7C>`_
- `Sparkfun <https://www.sparkfun.com/products/9717>`_
- `FTDI <http://www.ftdichip.com/Products/Cables/USBTTLSerial.htm>`_
- `Adafruit <https://www.adafruit.com/products/70>`_

.. image:: images/FTDI_Cable.jpg
    :align: center
    :alt: FTDI Cable

Pin 1 on the cable is the black wire and connects to pin 1 on the board. (the pin with the white dot next to it)

Adafruit 4 Pin Cable (PL2303)
==============================

This is a Prolific chipset based cable sold by `Adafruit <http://www.adafruit.com/products/954>`_.
Some people have reported issues with the cable causing some issues with data corruption. Your experience 
may vary. You will need to install the Prolific drivers, downloadable from Adafruit.

.. image:: images/RPI_Serial.png
    :align: center
    :alt: 4 pin serial cable
    
.. table:: Adafruit 4 pin serial cable connection to BeagleBone Black

    +--------------+--------------+--------------+
    | Board        | Wire         | Function     |
    +==============+==============+==============+
    | Pin 1        | Black        | Ground       |
    +--------------+--------------+--------------+
    | Pin 4        | Green        | Receive      |
    +--------------+--------------+--------------+
    | Pin 5        | White        | Transmit     |
    +--------------+--------------+--------------+


.. note:: 
    The naming of the signals reflect those of the cable. 
    The swapping of TX and RX takes place on the board.

You will also find an extra RED wire on this cable, this can be left unconnected.


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

Working miniDP to HDMI
=======================

.. note::
    BeagleBone-AI64 requires an **ACTIVE** Mini DisplayPort to HDMI cable or adaptor to work, 
    a passive miniDP to HDMI setup will not work at all.

- `IVANKY 4K Active Mini DisplayPort to HDMI Adapter <https://www.amazon.com/dp/B089GF8M87/>`_
- `CableCreation Mini DP (Thunderbolt 2 Compatible) to HDMI <https://www.amazon.in/CD0257-Mini-DP-to-HDMI/dp/B01FM51O0W/>`_

Examples of "Bad" MiniDP to HDMI
===================

- `UGREEN Mini DP Male to HDMI <https://www.amazon.in/Mini-Male-Female-Converter-Cable/dp/B01CL1P6TA/>`_
- `AGARO Mini Displayport (Mini Dp) To Hdmi <https://www.amazon.in/AGARO-Meters-Laptop-Computers-Mobile/dp/B09GW1NMNZ/>`_
- `AmazonBasics Mini Display Port to HDMI <https://www.amazon.in/AmazonBasics-Mini-DisplayPort-HDMI-Adapter/dp/B0134V3KIA/>`_