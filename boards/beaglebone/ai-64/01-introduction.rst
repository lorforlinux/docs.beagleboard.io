.. _bbai64-introduction:

Introduction
###############

BeagleBone AI-64 like its predecessors (BeagleBone AI), is designed to address the 
open-source Community, early adopters, and anyone interested in a low cost 64-bit 
Dual Arm® Cortex®-A72 processor based Single Board Computer (SBC). It also offers 
access to many of the interfaces and allows for the use of add-on boards called 
capes, to add many different combinations of features. A user may also develop 
their own board or add their own circuitry.

.. note:: 
    AI-64 has been equipped with a minimum set of features to allow the user to experience the power 
    of the processor and is not intended as a full development platform as many of the features and 
    interfaces supplied by the processor are not accessible from BeagleBone AI-64 via onboard support 
    of some interfaces. It is not a complete product designed to do any particular function. It is a 
    foundation for experimentation and learning how to program the processor and to access the 
    peripherals by the creation of your own software and hardware.



.. _beaglebone-compatibility:

BeagleBone Compatibility
-------------------------

The board is intended to provide functionality well beyond BeagleBone Black or BeagleBone AI, 
while still providing compatibility with BeagleBone Black's expansion headers as 
much as possible. There are several significant differences between the three designs. 

.. _beaglebone-comparison-table, BeagleBone Comparison:

.. table:: Table: BeagleBone Compatibility

    +-------------------+---------------------+----------------------------+--------------------+
    | Feature           | AI-64               | AI                         | Black              |
    +===================+=====================+============================+====================+
    | SoC               | TDA4VM              | AM5729                     | AM3358             |
    +-------------------+---------------------+----------------------------+--------------------+
    | Arm CPU           | Cortex-A72 (64-bit) | Cortex-A15 (32-bit)        | Cortex-A8 (32-bit) |
    +-------------------+---------------------+----------------------------+--------------------+
    | Arm cores/MHz     | 2x 2GHz             | 2x 1.5GHz                  | 1x 1GHz            |
    +-------------------+---------------------+----------------------------+--------------------+
    | RAM               | 4GB                 | 1GB                        | 512MB              |
    +-------------------+---------------------+----------------------------+--------------------+
    | eMMC flash        | 16GB                | 16GB                       | 4GB                |
    +-------------------+---------------------+----------------------------+--------------------+
    | Size              | 4" x 3.1"           | 3.4" x 2.1"                | .4" x 2.1"         |
    +-------------------+---------------------+----------------------------+--------------------+
    | Display           | miniDP + DSI        | microHDMI                  | microHDMI          |
    +-------------------+---------------------+----------------------------+--------------------+
    | USB host (Type-A) | 2x 5Gbps            | 1x 480Mbps                 | 1x 480Mbps         |
    +-------------------+---------------------+----------------------------+--------------------+
    | USB dual-role     | Type-C 5Gbps        | Type-C 5Gbps               | mini-AB 480Mbps    |
    +-------------------+---------------------+----------------------------+--------------------+
    | Ethernet          | 10/100/1000M        | 10/100/1000M               | 10/100M            |
    +-------------------+---------------------+----------------------------+--------------------+
    | M.2               | E-key               | `-`                        | `-`                |
    +-------------------+---------------------+----------------------------+--------------------+
    | WiFi/ Bluetooth   | `-`                 | AzureWave AW&#8209;CM256SM | `-`                |
    +-------------------+---------------------+----------------------------+--------------------+


.. todo::

   add cape compatibility details


.. _beaglebone-ai-64-features-and-specificationd:

BeagleBone AI-64 Features and Specification
---------------------------------------------

This section covers the specifications and features of the board and provides a high level 
description of the major components and interfaces that make up the board.

.. _ai64-features,BeagleBone AI-64 features tabled:

.. table:: Table: BeagleBone AI-64 Features and Specification

    +-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    |                         | Feature                                                                                                                                 |
    +=========================+=========================================================================================================================================+
    | **Processor**           | Texas Instruments TDA4VM                                                                                                                |
    +-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | **Graphics Engine**     | PowerVR® Series8XE GE8430                                                                                                               |
    +-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | **SDRAM Memory**        | LPDDR4 3.2GHz (4GB) Kingston Q3222PM1WDGTK-U                                                                                            |
    +-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | **Onboard Flash**       | eMMC (16GB) Kingston EMMC16G-TB29-PZ90                                                                                                  |
    +-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | **PMIC**                | TPS65941213 and TPS65941111 PMICs regulator and one additional LDO.                                                                     |
    +-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | **Debug Support**       | 2x 3 pin 3.3V TTL header                                                                                                                |
    |                         |     1. WKUP_UART0: Wake-up domain serial port                                                                                           |
    |                         |     2. UART0: Main domain serial port                                                                                                   |
    |                         | 10-pin JTAG TAG-CONNECT footprint                                                                                                       |
    +-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | **Power Source**        | USB C or DC Jack (5V @ >3A)                                                                                                             |
    +-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | **PCB**                 | 4” x 3.1”                                                                                                                               |
    +-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | **Indicators**          | 1x Power & 5x User Controllable LEDs                                                                                                    |
    +-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | **USB-3.0 Client Port** | Access to USB0 SuperSpeed dual-role mode via USB-C (no power output)                                                                    |
    +-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | **USB-3.0 Host Port**   | TUSB8041 4-port SuperSpeed hub 1x on USB1, 2x Type A Socket up-to 2.8A total depending on power input                                   |
    +-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | **Ethernet**            | Gigabit RJ45 link indicator speed indicator                                                                                             |
    +-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | **SD/MMC Connector**    | microSD (1.8/3.3V)                                                                                                                      |
    +-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | **User Input**          | 1. Reset Button                                                                                                                         |
    |                         | 2. Boot Button                                                                                                                          |
    |                         | 3. Power Button                                                                                                                         |
    +-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | **Video Out**           | miniDP                                                                                                                                  |
    +-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | **Audio**               | via miniDP (stereo)                                                                                                                     |
    +-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | **Weight**              | 192gm (with heatsink)                                                                                                                   |
    +-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | **Power**               | Refer to :ref:`main-board-power` section                                                                                                |
    +-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+


.. _board-component-locations:

Board Component Locations
----------------------------

This section describes the key components on the board. It provides information on their location 
and function. Familiarize yourself with the various components on the board.

.. _board-components:

Board components
-----------------

:ref:`board-components-figure` below shows the locations of the connectors, LEDs, and switches on the PCB layout of the board.

.. _board-components-figure:

.. figure:: media/ch04/components.*
   :width: 400px
   :align: center 
   
   BeagleBone AI-64 board components

* **DC Power** is the main DC input that accepts 5V power.
* **Power Button** alerts the processor to initiate the power down sequence and is used to power down the board.
* **GigaBit Ethernet** is the connection to the LAN.
* **Serial Debug ports** WKUP_UART0 for early boot from the management MCU and UART0 is for the main processor.
* **USB Client** is a USB-C connection to a PC that can also power the board.
* **BOOT switch** can be used to force a boot from the microSD card if the power is cycled on the board, removing power and reapplying the power to the board.
* There are five green **LEDs** that can be used by the user.
* **Reset Button** allows the user to reset the processor.
* **microSD** slot is where a microSD card can be installed.
* **miniDP** connector is where the display is connected to.
* **USB Host** can be connected different USB interfaces such as Wi-Fi, Bluetooth, Keyboard, etc.

On bottom side we have,

* **TI TDA4VM** processor.
* **4GB LPDDR4** Dual Data Rate RAM memory.
* **Ethernet PHY** physical interface to the network.
* **eMMC** onboard MMC chip that holds up to 16GB of data.
