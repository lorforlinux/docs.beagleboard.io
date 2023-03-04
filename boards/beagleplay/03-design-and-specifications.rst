.. _beagleplay-design-and-specifications:

Design and specifications
#########################

If you want to know how the BeaglePlay hardware is designed and what are it's 
high-level specifications then this chapter is for you. We are going to discuss 
each hardware design element in detail and provide high-level device 
specifications in  a short and crisp form as well.

.. tip:: 
    You can download BeaglePlay schematic to have clear view of 
    all the elements that makes up the BeaglePlay hardware.

    :download:`BeaglePlay schematic diagram PDF <https://git.beagleboard.org/beagleplay/beagleplay/-/blob/main/BeaglePlay_SCH_PDF.pdf>`

BeaglePlay block diagram
*************************

.. figure:: images/block-diagrams/System-Block-Diagram.svg
    :width: 1400
    :align: center
    :alt: BeaglePlay block diagram

System on Chip (SoC)
*********************

.. figure:: images/am625.png
    :width: 1400
    :align: center
    :alt: AM6254 SoC block diagram 

    AM6254 SoC block diagram

Connectivity
*************

Expansion Headers
==================

microSD Connector
==================

Type-C connector
================

Type-A connector
=================

Boot modes
***********

- SD Boot 
- eMMC Boot 

Power
******

The board can be powered via USB-C connector.

JTAG pads
**********

Serial debug port
******************

.. _beagleplay-detailed-hardware-design:

Detailed hardware design
*************************



Power supply
**************

.. figure:: images/hardware-design/dcdc-pmic.jpg
    :alt: DCDC & PMIC

    DCDC & PMIC

.. figure:: images/hardware-design/soc-power.jpg
    :alt: SoC Power

    SoC Power

.. figure:: images/hardware-design/soc-dcaps.jpg
    :alt: SoC DCAPs

    SoC DCAPs

eMMC & microSD
**************

.. figure:: images/hardware-design/emmc-microsd.jpg
    :alt: eMMC & microSD

    eMMC & microSD

Ethernet
*********

.. figure:: images/hardware-design/gigabit-ethernet.jpg
    :alt: Gigabit Ethernet

    Gigabit Ethernet

.. figure:: images/hardware-design/single-pair-ethernet.jpg
    :alt: Single-pair Ethernet

    Single-pair Ethernet

HDMI
*****

.. figure:: images/hardware-design/hdmi.jpg
    :alt: HDMI

    HDMI

USB-A & USB-C
**************

.. figure:: images/hardware-design/uab-a-and-usb-c.jpg
    :alt: USB-A & USB-C

OLDI & CSI
***********

.. figure:: images/hardware-design/oldi-and-csi.jpg
    :alt: OLDI & CSI

    OLDI & CSI

RTC, ID, and Debug 
******************

.. figure:: images/hardware-design/rtc-id-debug.jpg
    :alt: RTC, ID, and Debug 

DDR4 & SoC DDR controller
**************************

.. figure:: images/hardware-design/ddr4-soc-ddr.jpg
    :alt: DDR4 & SoC DDR controller

    DDR4 & SoC DDR controller

CC1352P7
*********

.. figure:: images/hardware-design/cc1352p7.jpg
    :alt: CC1352P7 wireless MCU

    CC1352P7 wireless MCU

WiFi 2.4G/5G
*************

.. figure:: images/hardware-design/wifi.jpg
    :alt: WiFi 2.4G/5G

    WiFi 2.4G/5G

Buttons & LEDs
***************

.. figure:: images/hardware-design/buttons-and-leds.jpg
    :alt: Buttons & LEDs

    Buttons & LEDs

Expansion connector & ADC
**************************

.. figure:: images/hardware-design/expansion-and-adc.jpg
    :alt: Expansion connectors & ADC

    Expansion connectors & ADC


.. _beagleplay-mechanical-specifications:

Mechanical Specifications 
##########################

Dimensions & weight
*******************

.. table:: Dimensions & weight

    +--------------------+----------------------------------------------------+
    | Parameter          | Value                                              |
    +====================+====================================================+
    | Size               | 82.5x80x20mm                                       |
    +--------------------+----------------------------------------------------+
    | Max heigh          | 20mm                                               |
    +--------------------+----------------------------------------------------+
    | PCB Size           | 80x80mm                                            |
    +--------------------+----------------------------------------------------+
    | PCB Layers         | 8 layers                                           |
    +--------------------+----------------------------------------------------+
    | PCB Thickness      | 1.6mm                                              |
    +--------------------+----------------------------------------------------+
    | RoHS compliant     | Yes                                                |
    +--------------------+----------------------------------------------------+
    | Weight             | 55.3g                                              |
    +--------------------+----------------------------------------------------+

