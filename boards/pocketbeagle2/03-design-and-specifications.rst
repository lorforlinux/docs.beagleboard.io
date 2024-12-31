.. _pocketbeagle2-design:

Design and Specifications
##########################

If you want to know how PocketBeagle2 is designed and the detailed specifications, then
this chapter is for you. We are going to attempt to provide you a short and crisp overview
followed by discussing each hardware design element in detail.

Block Diagram and Overview
**************************

The below figure provides a high-level overview of the PocketBeagle2 hardware architecture, illustrating 
the main components and their interconnections. This includes the System on Chip (SoC), power management, 
memory, connectivity interfaces, and other peripheral components.

.. figure:: images/hardware-design/block-diagram.png
   :width: 1200px
   :align: center
   :alt: PocketBeagle2 Block Diagram

   PocketBeagle2 Block Diagram

The following figure illustrates the I2C tree of the PocketBeagle2, showing the connections between the I2C 
master and various I2C slave devices on the board.

.. figure:: images/hardware-design/i2c-tree.png
   :width: 1200px
   :align: center
   :alt: I2C tree

   I2C tree

The following figure shows the power tree of the PocketBeagle2, detailing the power distribution from the 
main power sources to various components on the board.

.. figure:: images/hardware-design/power-tree.png
   :width: 1200px
   :align: center
   :alt: Power tree

   Power tree

.. _pocketbeagle2-processor:

System on Chip (SoC)
*********************

The PocketBeagle2 is powered by the AM6232 SoC, which is a high-performance, low-power processor 
designed for embedded applications. The AM6232 integrates dual ARM Cortex-A53 cores, a 
Cortex-M4F core, and various peripherals to support a wide range of functionalities. It is 
optimized for power efficiency and performance, making it suitable for applications requiring 
robust processing capabilities while maintaining low power consumption. The AM6232 SoC functional 
block diagram below provides a detailed view of the internal architecture of the System on Chip. It 
highlights the various functional blocks such as the CPU cores, memory controllers, peripheral 
interfaces, and other integrated components. This diagram is essential for understanding how 
the SoC manages data flow and interacts with other hardware components on the PocketBeagle2 board.

.. figure:: images/hardware-design/soc-functional-block-diagram.png
   :align: center
   :alt: SoC functional block diagram

   SoC functional block diagram

Decoupling capacitors are used to filter out noise and provide a stable power supply to the SoC. They 
help in maintaining the integrity of the power signals by smoothing out voltage fluctuations and transient 
spikes, ensuring reliable operation of the SoC and preventing potential malfunctions due to power instability.

.. figure:: images/hardware-design/soc-dcaps.png
   :align: center
   :alt: SoC decoupling capacitors
   
   SoC decoupling capacitors

The following figure shows the DDR controller of the SoC, which manages the communication between the 
processor and the DDR memory. It ensures efficient data transfer and memory access, playing a crucial 
role in the overall performance of the system.

.. figure:: images/hardware-design/soc-ddr-controller.png
   :align: center
   :alt: SoC DDR controller
   
   SoC DDR controller

The following figure shows the power capacitors used for the SoC. These capacitors are crucial for 
maintaining stable power delivery to the SoC, filtering out noise, and ensuring reliable operation 
by smoothing out voltage fluctuations.

.. figure:: images/hardware-design/soc-power-caps.png
   :align: center
   :alt: SoC power capacitors
   
   SoC power capacitors

The following figure shows the power distribution for the SoC, detailing how power is supplied to 
various components within the SoC to ensure stable and efficient operation.

.. figure:: images/hardware-design/soc-power.png
   :align: center
   :alt: SoC power
   
   SoC power

The following figure shows the VSS (Ground) connection for the SoC. This connection is crucial 
for providing a common reference point for all the electrical signals and ensuring the proper 
operation of the SoC by stabilizing the voltage levels.

.. figure:: images/hardware-design/soc-vss.png
   :align: center
   :alt: SoC VSS (Ground) connection
   
   SoC VSS (Ground) connection

.. _pocketbeagle2-boot-modes:

Boot Modes
===========

.. figure:: images/hardware-design/boot-config.png
   :align: center
   :alt: Boot configuration

   Boot configuration

.. figure:: images/hardware-design/bootstrap.png
   :align: center
   :alt: Bootstrap pins connection

   Bootstrap pins connection

SoC GPIOs
==========

.. figure:: images/hardware-design/gpio-gpmc.png
   :align: center
   :alt: GPIO GPMC

   GPIO GPMC

.. figure:: images/hardware-design/gpio-mcasp0.png
   :align: center
   :alt: GPIO MCASP0

   GPIO MCASP0

.. figure:: images/hardware-design/gpio-osc0.png
   :align: center
   :alt: GPIO OSC0

   GPIO OSC0

.. figure:: images/hardware-design/gpio-ospi.png
   :align: center
   :alt: GPIO OSPI

   GPIO OSPI

.. figure:: images/hardware-design/gpio-rgmii1.png
   :align: center
   :alt: GPIO RGMII1

   GPIO RGMII1

.. figure:: images/hardware-design/gpio-rgmii2.png
   :align: center
   :alt: GPIO RGMII2

   GPIO RGMII2

.. figure:: images/hardware-design/gpio-vout0.png
   :align: center
   :alt: GPIO VOUT0

   GPIO VOUT0

.. figure:: images/hardware-design/mcu-domain.png
   :align: center
   :alt: MCU domain

   MCU domain

.. figure:: images/hardware-design/mcu-system.png
   :align: center
   :alt: MCU system

   MCU system

.. figure:: images/hardware-design/wkup-domain.png
   :align: center
   :alt: Wakeup domain

   Wakeup domain


.. _pocketbeagle2-power-management:

Power Management
*****************

PMIC
====

.. figure:: images/hardware-design/pmic.png
   :align: center
   :alt: PMIC

   PMIC

3V3 power
=========

.. figure:: images/hardware-design/dc-3v3.png
   :align: center
   :alt: 3V3 power

   3V3 power

Power path
===========

.. figure:: images/hardware-design/power-path.png
   :align: center
   :alt: Power path

   Power path

Battery charging
================

.. figure:: images/hardware-design/battery-charging.png
   :align: center
   :alt: Battery charging

   Battery charging

Decoupling capacitors
======================

.. figure:: images/hardware-design/vdd-1v2-caps.png
   :align: center
   :alt: VDD 1.2V capacitors

   VDD 1.2V capacitors

.. figure:: images/hardware-design/vdd-1v8-caps.png
   :align: center
   :alt: VDD 1.8V capacitors

   VDD 1.8V capacitors

.. figure:: images/hardware-design/vdd-3v3-caps.png
   :align: center
   :alt: VDD 3.3V capacitors

   VDD 3.3V capacitors

.. figure:: images/hardware-design/vdda-0v85-caps.png
   :align: center
   :alt: VDDA 0.85V capacitors

   VDDA 0.85V capacitors

.. figure:: images/hardware-design/vdd-core-caps.png
   :align: center
   :alt: VDD core capacitors

   VDD core capacitors

.. _pocketbeagle2-connectivity-and-expansion:

General connectivity and expansion
************************************

USB connections
===============

.. figure:: images/hardware-design/usb.png
   :align: center
   :alt: USB connections

   USB connections

Cape headers
=============

P1 cape header
---------------

.. figure:: images/hardware-design/cape-header-p1.png
   :align: center
   :alt: P1 cape headers

   P1 cape headers

P2 cape header
---------------

.. figure:: images/hardware-design/cape-header-p2.png
   :align: center
   :alt: P2 cape headers

   P2 cape headers

MicroSD card slot
=================

.. figure:: images/hardware-design/microsd.png
   :align: center
   :alt: MicroSD card slot

   MicroSD card slot

.. figure:: images/hardware-design/microsd-3v3.png
   :align: center
   :alt: MicroSD card power

   MicroSD card power

.. todo:: Add MicroSD card slot information

Buttons & LEDs
***************

User & Power Button
=====================

.. figure:: images/hardware-design/buttons.png
   :align: center
   :alt: Buttons

   Buttons

.. todo:: Add button details

LED Indicators
===============

.. todo:: Add information about LED indicators

.. figure:: images/hardware-design/leds.png
   :align: center
   :alt: LED indicators

   LED indicators

.. _pocketbeagle2-memory-media-storage:

Memory, Media, and storage 
***************************

Described in the following sections are the memory devices found on the board.

.. _pocketbeagle2-gb-embedded-mmc:

4GB embedded MMC (optional)
===========================

.. figure:: images/hardware-design/emmc.png
   :align: center
   :alt: 4GB eMMC storage (optional)

   4GB eMMC storage (optional)

.. _pocketbeagle2-4gb-ddr4:

512MB LPDDR4
==============

.. figure:: images/hardware-design/ddr.png
   :align: center
   :alt: 512MB LPDDR4 RAM

   512MB LPDDR4 RAM

.. figure:: images/hardware-design/ddr-power.png
   :align: center
   :alt: DDR power

   DDR power


.. _pocketbeagle2-mspm0-adc-eeprom:

MSPM0 ADC & EEPROM
==================

.. figure:: images/hardware-design/mspm0.png
   :align: center
   :alt: MSPM0L1105 as 8ch 12bit ADC & 4KB EEPROM

   MSPM0L1105 as 8ch 12bit ADC & 4KB EEPROM

.. _pocketbeagle2-debug-ports:

Debug Ports
************

Serial debug port
=================

.. figure:: images/hardware-design/uart-debug.png
   :align: center
   :alt: Serial debug port

   Serial debug port

TagConnect (JTAG)
=================

.. figure:: images/hardware-design/jtag.png
   :align: center
   :alt: JTAG

   JTAG

.. figure:: images/hardware-design/tag-connect.png
   :align: center
   :alt: TagConnect (JTAG)

   TagConnect (JTAG)

Mechanical specifications
**************************

Dimensions & Weight
====================

.. table:: Dimensions & weight

   +--------------------+----------------------------------------------------+
   | Parameter          | Value                                              |
   +====================+====================================================+
   | Size               | 56 x 35mm                                          |
   +--------------------+----------------------------------------------------+
   | Max heigh          | 13.6                                               |
   +--------------------+----------------------------------------------------+
   | PCB Size           | 55 x 35mm                                          |
   +--------------------+----------------------------------------------------+
   | PCB Layers         | 10--layers                                         |
   +--------------------+----------------------------------------------------+
   | PCB Thickness      | 1.6mm                                              |
   +--------------------+----------------------------------------------------+
   | RoHS compliant     | Yes                                                |
   +--------------------+----------------------------------------------------+
   | Net Weight         | 12.7g                                              |
   +--------------------+----------------------------------------------------+
   | Gross Weight       | 19g                                                |
   +--------------------+----------------------------------------------------+


Board Dimensions
=================

.. figure:: images/pocketbeagle2-revA-dimensions.jpg
   :align: center
   :alt: PocketBeagle2 RevA Dimensions

   PocketBeagle2 RevA Dimensions
