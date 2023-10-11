.. _beaglev-fire-design:

Design & specifications
#######################

If you want to know how BeagleV-Fire board is designed and what are it's 
high-level specifications then this chapter is for you. We are going to discuss 
each hardware design element in detail and provide high-level device 
specifications in  a short and crisp form as well.

.. tip:: 

    For hardware design files and schematic diagram you can checkout BeagleV-Fire 
    GitLab repository: https://git.beagleboard.org/beaglev-fire/beaglev-fire

Block diagram
**************

.. figure:: media/hardware-design/system-block-diagram.*
    :width: 720
    :align: center
    :alt: System block diagram

    System block diagram

.. figure:: media/hardware-design/power-tree-diagram.*
    :width: 720
    :align: center
    :alt: Power tree diagram

    Power tree diagram

.. figure:: media/hardware-design/iic-tree-diagram.*
    :width: 720
    :align: center
    :alt: I2C tree diagram

    I2C tree diagram
 
System on Chip (SoC)
*********************

.. figure:: media/hardware-design/soc-bank0.*
    :width: 720
    :align: center
    :alt: SoC bank0

    SoC bank0

.. figure:: media/hardware-design/soc-bank1.*
    :width: 720
    :align: center
    :alt: SoC bank1

    SoC bank1

.. figure:: media/hardware-design/soc-bank2.*
    :width: 720
    :align: center
    :alt: SoC bank2

    SoC bank2

.. figure:: media/hardware-design/soc-bank3.*
    :width: 720
    :align: center
    :alt: SoC bank3

    SoC bank3

.. figure:: media/hardware-design/soc-bank4.*
    :width: 720
    :align: center
    :alt: SoC bank4

    SoC bank4

.. figure:: media/hardware-design/soc-power.*
    :width: 1240
    :align: center
    :alt: SoC power

    SoC power


Power management
*****************

.. figure:: media/hardware-design/dc-5v-input.*
    :width: 720
    :align: center
    :alt: DC 5V input

    DC 5V input

.. figure:: media/hardware-design/ideal-diode.*
    :width: 720
    :align: center
    :alt: Ideal diode

    Ideal diode

.. figure:: media/hardware-design/vcc-1v0.*
    :width: 720
    :align: center
    :alt: VCC 1V0

    VCC 1V0

.. figure:: media/hardware-design/vcc-1v1.*
    :width: 720
    :align: center
    :alt: VCC 1V1

    VCC 1V1

.. figure:: media/hardware-design/vcc-1v8.*
    :width: 720
    :align: center
    :alt: VCC 1V8

    VCC 1V8

.. figure:: media/hardware-design/vcc-2v5.*
    :width: 720
    :align: center
    :alt: VCC 2V5

    VCC 2V5

.. figure:: media/hardware-design/vcc-3v3.*
    :width: 720
    :align: center
    :alt: VCC 3V3

    VCC 3V3

.. figure:: media/hardware-design/vcca-1v0.*
    :width: 720
    :align: center
    :alt: VCCA 1V0

    VCCA 1V0

.. figure:: media/hardware-design/vio-enable.*
    :width: 720
    :align: center
    :alt: VIO enable

    VIO enable

General Connectivity and Expansion
**********************************

USB-C port
============

P8 & P9 cape header pins
=========================

Buttons and LEDs
******************

Boot select buttons
====================

User LEDs and Power LED
========================

Power and reset button
=======================

Wired and wireless connectivity
********************************

Ethernet
========


Memory, Media and Data storage
********************************

DDR memory
==========


eMMC
=====


microSD
=======


EEPROM
======


Multimedia I/O
***************

CSI
====

Debug
******

UART debug port 
===============

JTAG debug port
===============


Mechanical Specifications 
**************************

.. table:: Dimensions & weight

    +--------------------+----------------------------------------------------+
    | Parameter          | Values                                             |
    +====================+====================================================+
    | Size               |                                                    |
    +--------------------+----------------------------------------------------+
    | Max heigh          |                                                    |
    +--------------------+----------------------------------------------------+
    | PCB Size           |                                                    |
    +--------------------+----------------------------------------------------+
    | PCB Layers         |                                                    |
    +--------------------+----------------------------------------------------+
    | PCB Thickness      |                                                    |
    +--------------------+----------------------------------------------------+
    | RoHS compliant     |                                                    |
    +--------------------+----------------------------------------------------+
    | Gross Weight       |                                                    |
    +--------------------+----------------------------------------------------+
    |  Net weight        |                                                    |
    +--------------------+----------------------------------------------------+