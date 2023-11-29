.. _beaglebone-ai-64-design:

BeagleBone AI-64 Design and Specifications
##############################################

If you want to know how BeagleBone AI-64 is designed and the detailed specifications, then
this chapter is for you. We are going to attept to provide you a short and crisp overview
followed by discussing each hardware design element in detail.

Block Diagram and Overview
**************************

:ref:`BeagleBone_AI-64-block-diagram` below shows the high level block 
diagram of BeagleBone AI-64 board surrounding TDA4VM SoC.

.. _BeagleBone_AI-64-block-diagram:

.. figure:: media/ch05/board-block-diagram.*
   :width: 400px
   :align: center 
   
   BeagleBone AI-64 Key Components

.. _processor:

Processor
==========

BeagleBone AI-64 uses TI J721E-family `TDA4VM <https://www.ti.com/product/TDA4VM>`_ 
system-on-chip (SoC) which is part of the K3 Multicore SoC architecture platform 
and it is targeted for the reliability and low-latency needs of the automotive 
market provide for a great general purpose platform suitable for industrial 
automation, mobile robotics, building automation and numerous hobby projects.

The SoC designed as a low power, high performance and highly integrated device 
architecture, adding significant enhancement on processing power, graphics capability, 
video and imaging processing, virtualization and coherent memory support. In addition, 
these SoCs support state of the art security and functional safety features. For the 
remaining of this section device, SoC, and processor will be used interchangeably. 

**Some of the main distinguished characteristics of the device are:**

* 64-bit architecture with virtualization and coherent memory support, which leverages full processing capability of 64-bit Arm® Cortex®-A72
* Fully programmable industrial communication subsystems to enable future-proof designs for customers that need to adopt the new Gigabit Time-sensitive Networks (TSN) standards, but still need full support on legacy protocols and continuous system optimization over the product deployment
* Integration of vision hardware processing accelerators to facilitate extensive processing requirements in low power budget for automotive ADAS and machine vision applications
* Integration of a general-purpose microcontroller unit (MCU) with a dual Arm® Cortex®-R5F MCU subsystem, available for general purpose use as two cores or in lockstep, intended to help customers achieve functional safety goals for their end products
* Integration of a next-generation fixed and floating-point C71x Digital Signal Processor (DSP) that significantly boosts power over a broad range of general signal processing tasks for both general applications and automotive functions which also incorporates advanced techniques to improve control code efficiency and ease of programming such as branch prediction, protected pipeline, precise exception and virtual memory management
* Tightly coupled Matrix Multiplication Accelerator (MMA) that extends the C71x DSP architecture's scalar and vector facilities enabling deep learning and enhance vision, analytics and wide range of general applications. The achieved total TOPS (Tera Operations Per Second) performance significantly differentiates the device for single board computer in machine vision and deep learning applications
* Key display features including flexibility to interface with different panel types (eDP, DSI, DPI) with multi-layer hardware composition
* Integration of hardware features that help applications to achieve functional safety mechanisms
* Robust security architecture with sandboxed DMSC controller managing all secure configurations with high performance client-server messaging scheme between secure DMSC and all cores
* Simplified solution for power supply management, enabling lower cost system solution (on-die bias LDOs and power good comparators for minimal power sequencing requirements consistent with low cost supply design)

**The device is composed of the following main subsystems, across different domains of the SoC, among others:**

* One dual-core 64-bit Arm Cortex-A72 microprocessor subsystem at up to 2.0 GHz and up to 24K DMIPS (Dhrystone Million Instructions per Second)
* Up to three Microcontroller Units (MCU), based on dual-core Arm Cortex-R5F processor running at up to 1.0 GHz, up to 12K DMIPS
* Up to two TMS320C66x DSP CorePac modules running at up to 1.35 GHz, up to 40 GFLOPS
* One C71x floating point, vector DSP running at up to 1.0 GHz, up to 80 GFLOPS
* One deep-learning MMA, up to 8 TOPS (8b) at 1.0 GHz
* Up to two gigabit dual-core Programmable Real-Time Unit and Industrial Communication Subsystems (PRU_ICSSG)
* Two Navigator Subsystems (NAVSS) for data movement and control
* One multi-pipeline Display Subsystem (DSS) with one MIPI® Display Serial Interface Controller (DSI) and shared MIPI D-PHY Transmitter (DPHY_TX), one Embedded DisplayPort Transmitter (EDP) with shared Serializer/Deserializer (SERDES), and two MIPI Display Pixel Interface (DPI) ports
* Two Camera Streaming Interface Receivers (CSI_RX_IF) with dedicated MIPI D-PHYs (DPHY_RX)
* One Camera Streaming Interface Transmitter (CSI_TX_IF) with MIPI D-PHY Transmitter (DPHY_TX) shared with DSI
* One Vision Processing Accelerator (VPAC) with image signal processor
* One Depth and Motion Processing Accelerator (DMPAC)
* One dual-core multi-standard HD Video Decoder (DECODER)
* One dual-core multi-standard HD Video Encoder (ENCODER)
* One Graphics Processing Unit (GPU)
* One Device Management and Security Controller (DMSC)

**The device provides a rich set of peripherals such as:**

* General connectivity peripherals, including:

  * ``Two 12-bit general purpose Analog-to-Digital Converters (ADC)``
  * ``Ten Inter-Integrated Circuit (I2C) interfaces``
  * ``Three Improved Inter-Integrated Circuit (I3C) controllers``
  * ``Eleven master/slave Multichannel Serial Peripheral Interfaces (MCSPI)``
  * ``Twelve configurable Universal Asynchronous Receiver/Transmitter (UART) interfaces``
  * ``Ten General-Purpose Input/Output (GPIO) modules``

* High-speed interfaces, including:

  * ``Two Gigabit Ethernet Switch (CPSW) modules``
  * ``Two Dual-Role-Device (DRD) Universal Serial Bus Subsystems (USBSS) with integrated PHY``
  * ``Four Peripheral Component Interconnect express (PCIe) Gen3 subsystems``

* Flash memory interfaces, including:

  * ``One Octal SPI (OSPI) interface and one Quad SPI (QSPI) or one QSPI and one HyperBus^TM^``
  * ``One General Purpose Memory Controller (GPMC) with Error Location Module (ELM) and 8- or 16-bit-wide data bus width (supports parallel NOR or NAND FLASH devices)``
  * ``Three Multimedia Card/Secure Digital (MMCSD) controllers``
  * ``One Universal Flash Storage (UFS) interface``

* Industrial and control interfaces, including:
  
  * ``Sixteen Controller Area Network (MCAN) interfaces with flexible data rate support``
  * ``Three Enhanced Capture (ECAP) modules``
  * ``Six Enhanced Pulse-Width Modulation (EPWM) subsystems``
  * ``Three Enhanced Quadrature Encoder Pulse (EQEP) modules``

* Audio peripherals, including:
  
  * ``One Audio Tracking Logic (ATL)``
  * ``Twelve Multichannel Audio Serial Port (MCASP) modules supporting up to 16 channels with independent TX/RX clock/sync domain``

* One Video Processing Front End (VPFE) interface module

**The device also integrates:**

* Power distribution, reset controls and clock management components

* Power-management techniques for device power consumption minimization:
  
  * ``Adaptive Voltage Scaling (AVS)``
  * ``Dynamic Frequency Scaling (DFS)``
  * ``Gated clocks``
  * ``Multiple voltage domains``
  * ``Independently controlled power domains for major modules``
  * ``Voltage and Temperature Management (VTM) module``
  * ``Power-on Reset Generators (PRG)``
  * ``Power Sleep Controllers (PSC)``

* Optimized interconnect (CBASS) architecture to enable latency-critical real time network and IO applications

* Control modules (CTRL_MMRs) mainly associated with device top-level configurations such as:
  
  * ``IO Pad and pin multiplexing configuration``
  * ``PLL control and associated High-Speed Dividers (HSDIV)``
  * ``Clock selection``
  * ``Analog function controls``

* Multicore Shared Memory Controller (MSMC)
* DDR Subsystem (DDRSS) with Error Correcting Code (ECC), supporting LPDDR4
* 1KB RAM with ECC support for C71x boot vectors
* 2KB RAM with ECC support for A72 and R5F boot vectors
* 512KB On-Chip SRAM protected by ECC
* One Global Time Counter (GTC) module
* Thirty 32-bit counter timers with compare and capture modes
* Debug and trace capabilities

**The device includes different modules for functional safety requirements support:**

* MCU island with dual lock step Arm Cortex-R5F
* Safety enabled interconnect with implemented features to help with Freedom From Interference (FFI)
* Twelve Real Time Interrupt (RTI) modules with Windowed Watchdog Timer (WWDT) functionality to monitor processor cores
* Sixteen Dual-Clock Comparators (DCC) to monitor clocking sources during run-time
* Three Error Signaling Modules (ESM) to enable error monitoring
* Temperature monitoring sensors
* ECC on all critical memories
* Dedicated hardware Memory Cyclic Redundancy Check (MCRC) blocks

**The device supports the following main security functionalities among others:**

* Secure Boot Management
* Public Key Accelerator (PKA) for large vector math operation
* Cryptographic acceleration (AES, 3DES, MD5, SHA1, SHA2-224, 256, 512 operation)
* Trusted Execution Environment (TEE)
* Secure storage support
* On-the-fly encryption and authentication support for OSPI interface

The device is partitioned into three functional domains as shown in :ref:`soc-block-diagram`, each containing specific processing cores and peripherals:

* Wake-up (WKUP) domain
* Microcontroller (MCU) domain with one of the dual Cortex-R5 cluster
* MAIN domain

.. _soc-block-diagram:

.. figure:: media/ch05/soc-block-diagram.*
   :width: 400px
   :align: center 
   
   Device Top-level Block Diagram

.. _memory:

Memory
=======

Described in the following sections are the three memory devices found on the board.

.. _mb-ddr4l:

4GB LPDDR4
------------

A single (1024M x 16bits x 2channels) LPDDR4 4Gb memory device is used. The memory used is:

* Kingston Q3222PM1WDGTK-U

.. _kb-eeprom:

4Kb EEPROM
-------------

A single 4Kb EEPROM (24FC04HT-I/OT) is provided on I2C0 that holds the board information. This information includes board name, serial number, and revision information.

.. _gb-embedded-mmc:

16GB Embedded MMC
-------------------

A single 16GB embedded MMC (eMMC) device is on the board. The device
connects to the MMC1 port of the processor, allowing for 8bit wide
access. Default boot mode for the board will be MMC1 with an option to
change it to MMC0, the SD card slot, for booting from the SD card as a
result of removing and reapplying the power to the board. Simply
pressing the reset button will not change the boot mode. MMC0 cannot be
used in 8Bit mode because the lower data pins are located on the pins
used by the Ethernet port. This does not interfere with SD card
operation but it does make it unsuitable for use as an eMMC port if the
8 bit feature is needed.

.. _microsd-connector:

MicroSD Connector
-------------------

The board is equipped with a single microSD connector to act as the
secondary boot source for the board and, if selected as such, can be the
primary boot source. The connector will support larger capacity microSD
cards. The microSD card is not provided with the board. Booting from
MMC0 will be used to flash the eMMC in the production environment or can
be used by the user to update the SW as needed.

.. _boot-modes:

Boot Modes
===========

As mentioned earlier, there are two boot modes:

* **eMMC Boot:** This is the default boot mode and will allow for the fastest boot time and will enable the board to boot out of the box using the pre-flashed OS image without having to purchase an microSD card or an microSD card writer.
* **SD Boot:** This mode will boot from the microSD slot. This mode can be used to override what is on the eMMC device and can be used to program the eMMC when used in the manufacturing process or for field updates.

.. todo::

   This section needs more work and references to greater detail. Other boot modes are possible.
   Software to support USB and serial boot modes is not provided by beagleboard.org._Please contact TI for support of this feature.


A switch is provided to allow switching between the modes.

* Holding the boot switch down during a removal and reapplication of power without a microSD card inserted will force the boot source to be the USB port and if nothing is detected on the USB client port, it will go to the serial port for download.
* Without holding the switch, the board will boot try to boot from the eMMC. If it is empty, then it will try booting from the microSD slot, followed by the serial port, and then the USB port.
* If you hold the boot switch down during the removal and reapplication of power to the board, and you have a microSD card inserted with a bootable image, the board will boot from the microSD card.

.. note ::
    
   Pressing the RESET button on the board will NOT result in a change of the boot mode. You MUST remove power and reapply power to change the boot mode. The boot pins are sampled during power on reset from the PMIC to the processor.The reset button on the board is a warm reset only and will not force a boot mode change.

.. _power-management:

Power Management
===================

The *TPS65941213 and TPS65941111* power management device is used along with a separate LDO to provide power to the system.

.. _pc-usb-interface:

PC USB Interface
=====================

The board has a USB type-C connector that connects to USB0 port of the processor.

.. _serial-debug-ports:

Serial Debug Ports
====================================

Two serial debug ports are provided on board via 3pin micro headers,

1. WKUP_UART0: Wake-up domain serial port
2. UART0: Main domain serial port


In order to use the interfaces a `3pin micro to 6pin dupont adaptor header <https://uk.farnell.com/element14/1103004000156/beaglebone-ai-serials-cable/dp/3291081>`_ is required with a 6 pin USB to TTL adapter. The header is compatible with the one provided by FTDI and can be purchased for about $$12 to $$20 from various sources. Signals supported are TX and RX. None of the handshake signals are supported.

.. _bbai64-usb-host-ports:

USB Host Ports
==================

On the board is a stacked dual USB 3.0 Type A female connector with full LS/FS/HS/SS
host support. The ports can
provide power on/off control and up to 1.5A of current at 5V. Under USB
power, the board will not be able to supply the full 1.5A.

.. _power-sources:

Power Sources
====================================

The board can be powered from three different sources:

* 5V > 3A power supply plugged into the barrel jack
* 5V > 3A capable device plugged into the USB Type-C connector
* The cape header pins

The power supply is not provided with the board but can be easily
obtained from numerous sources. A 5V > 3A supply is mandatory to have with
the board, but if there is a cape plugged into the board or you have a power
hungry device or hub plugged into the host port, then more current may
needed from the DC supply.

.. _reset-button:

Reset Button
====================

When pressed and released, causes a reset of the board.

.. _power-button:

Power Button
==============

This button takes advantage of the input to the PMIC for
power down features.

.. _indicators:

Indicators
==============

There are a total of six green LEDs on the board.

* One green power LED indicates that power is applied and the power management IC is up.
* Five blue LEDs that can be controlled via the SW by setting GPIO pins.

.. _bbai64-detailed-hardware-design:

Detailed Hardware Design
*************************

.. important::

   This section is highly inaccurate. Do not read. Please refer to the schematics.

This section provides a detailed description of the hardware design.
This can be useful for interfacing, writing drivers, or using it to help
modify specifics of your own design.

.. todo::

   An extensive amount of the documentation below was taken from BeagleBone Black and presented here as BeagleBone AI-64. It must be gone over in detail
   to determine what is valid and replaced with accurate information.

:ref:`bbai-64-block-diagram-ch06` below is the high level block diagram of the board. For those who may be concerned, It is the same figure as shown in :ref:`beaglebone-ai-64-high-level-specification`. It is placed here again for convenience so it is closer to the topics to follow.

.. _bbai-64-block-diagram-ch06:

.. figure:: media/ch05/board-block-diagram.*
   :width: 400px
   :align: center 
   :alt: BeagleBone AI-64 Key Components

   BeagleBone AI-64 Key Components

.. _power-section:

Power Section
================

:ref:`power-flow-diagram` shows the high level block diagram of the power section of the board.

.. _power-flow-diagram,High level power block diagram:

.. figure:: media/ch06/power.*
   :width: 400px
   :align: center 
   :alt: High level power block diagram

   High level power block diagram

This section describes the power section of the design and all the
functions performed by the *TPS65941213 and TPS65941111*.

.. todo::

   The above image does not represent this board. It has a Pi Header.

.. _TPS65941213-and-TPS65941111-pmic:

TPS65941213 and TPS65941111 PMIC
---------------------------------

The main Power Management IC (PMIC) in the system is the *TPS65941213 and TPS65941111*
which is a single chip power management IC consisting of a linear
dual-input power path, three step-down converters, and four LDOs. LDO
stands for Low Drop Out. If you want to know more about an LDO, you can
go to `http://en.wikipedia.org/wiki/Low-dropout_regulator <http://en.wikipedia.org/wiki/Low-dropout_regulator>`_ .

If you want to learn more about step-down converters, you can go to `_http://en.wikipedia.org/wiki/DC-to-DC_converter <http://en.wikipedia.org/wiki/DC-to-DC_converter>`_ .

The system is supplied by a USB port or DC adapter. Three
high-efficiency 2.25MHz step-down converters are targeted at providing
the core voltage, MPU, and memory voltage for the board.

The step-down converters enter a low power mode at light load for
maximum efficiency across the widest possible range of load currents.
For low-noise applications the devices can be forced into fixed
frequency PWM using the I2C interface. The step-down converters allow
the use of small inductors and capacitors to achieve a small footprint
solution size.

LDO1 and LDO2 are intended to support system standby mode. In normal
operation, they can support up to 100mA each. LDO3 and LDO4 can support
up to 285mA each.

By default only LDO1 is always ON but any rail can be configured to
remain up in SLEEP state. In particular the DCDC converters can remain
up in a low-power PFM mode to support processor suspend mode. The
*TPS65941213 and TPS65941111* offers flexible power-up and power-down sequencing and
several house-keeping functions such as power-good output, pushbutton
monitor, hardware reset function and temperature sensor to protect the
battery.

See the :ref:`TPS6594-Q1-block-diagram` shown below for high level details
for *TPS65941213 and TPS65941111*, for more information on the, refer to https://www.ti.com/product/TPS6594-Q1 Texas instruments product page.

.. _TPS6594-Q1-block-diagram:

.. figure:: media/ch06/TPS6594-Q1.*
   :width: 400px
   :align: center 
   :alt: TPS6594-Q1 block diagram

   TPS6594-Q1 block diagram

.. _pmic-a-diagram,PMIC-A TPS65941213 circuit:

.. figure:: media/ch06/pmic-a.*
   :width: 400px
   :align: center 
   :alt: PMIC-B TPS65941213 circuit

   PMIC-B TPS65941213 circuit

.. _pmic-b-diagram,PMIC-B TPS65941111 circuit:

.. figure:: media/ch06/pmic-b.*
   :width: 400px
   :align: center 
   :alt: PMIC-B TPS65941111 circuit

   PMIC-B TPS65941111 circuit

.. _dc-input:

DC Input
---------------------------------

:ref:`figure-23` below shows how the DC input is connected to the **TPS65941213 and TPS65941111**.

.. _figure-23,Figure 23:

.. figure:: media/image38.*
   :width: 400px
   :align: center 
   :alt: Fig: TPS65217 DC Connection

   Fig: TPS65217 DC Connection

A 5VDC supply can be used to provide power to the board. The power
supply current depends on how many and what type of add-on boards are
connected to the board. For typical use, a 5VDC supply rated at 1A
should be sufficient. If heavier use of the expansion headers or USB
host port is expected, then a higher current supply will be required.

The connector used is a 2.1MM center positive x 5.5mm outer barrel. The
5VDC rail is connected to the expansion header. It is possible to power
the board via the expansion headers from an add-on card. The 5VDC is
also available for use by the add-on cards when the power is supplied by
the 5VDC jack on the board.

.. _usb-power:

USB Power
---------------------------------

The board can also be powered from the USB port. A typical USB 3.0 port is
limited to 900mA. When powering from the USB port, the VDD_5V rail
is not provided to the expansion headers, so capes that require the 5V
rail to supply the cape direct, bypassing the *TPS65941213 and TPS65941111*, will not have
that rail available for use. The 5VDC supply from the USB port is
provided on the SYS_5V, the one that comes from the **TPS65941213 and TPS65941111**, rail
of the expansion header for use by a cape. :ref:`bbai64-usb-power-connections` is the connection
of the USB power input on the PMIC.

.. _bbai64-usb-power-connections:

.. figure:: media/USB-Connection.*
   :width: 400px
   :align: center 
   :alt: USB Power Connection

   USB Power Connection

.. _power-selection:

Power Selection
---------------------------------

The selection of either the 5VDC or the USB as the power source is
handled internally to the *TPS65941213 and TPS65941111* and automatically switches to 5VDC
power if both are connected. SW can change the power configuration via
the I2C interface from the processor. In addition, the SW can read
the *TPS65941213 and TPS65941111* and determine if the board is running on the 5VDC input
or the USB input. This can be beneficial to know the capability of the
board to supply current for things like operating frequency and
expansion cards.

It is possible to power the board from the USB input and then connect
the DC power supply. The board will switch over automatically to the DC
input.

.. _power-button-1:

Power Button
---------------------------------

A power button is connected to the input of the *TPS65941213 and TPS65941111*. This is a
momentary switch, the same type of switch used for reset and boot
selection on the board.

If you push the button the *TPS65941213 and TPS65941111* will send an interrupt to the
processor. It is up to the processor to then pull the **PMIC_POWER_EN**
pin low at the correct time to power down the board. At this point, the
PMIC is still active, assuming that the power input was not removed.
Pressing the power button will cause the board to power up again if the
processor puts the board in the power off mode.

In power off mode, the RTC rail is still active, keeping the RTC powered
and running off the main power input. If you remove that power, then the
RTC will not be powered. You also have the option of using the battery
holes on the board to connect a battery if desired as discussed in the
next section.

If you push and hold the button for greater than 8 seconds, the PMIC
will power down. But you must release the button when the power LED
turns off. Holding the button past that point will cause the board to
power cycle.

.. _section-6-1-7,Section 6.1.7 Power Consumption:

Power Consumption
---------------------------------

The power consumption of the board varies based on power scenarios and
the board boot processes. Measurements were taken with the board in the
following configuration:

* DC powered and USB powered
* monitor connected
* USB HUB
* 4GB USB flash drive
* Ethernet connected @ 100M
* Serial debug cable connected

:ref:`table-4` is an analysis of the power consumption of the board in these various scenarios.

.. _table-4,Table 4:

.. list-table:: BeagleBone AI-64 Features and Specification
   :header-rows: 1

   * - MODE 
     - USB 
     - DC 
     - C+USB
   * - Reset 
     - TBD 
     - TBD 
     - TBD
   * - Idling @ UBoot 
     - 210 
     - 210 
     - 210
   * - Kernel Booting (Peak) 
     - 460 
     - 460 
     - 460
   * - Kernel Idling 
     - 350 
     - 350 
     - 350
   * - Kernel Idling Display Blank 
     - 280 
     - 280 
     - 280
   * - Loading a Webpage 
     - 430 
     - 430 
     - 430

The current will fluctuate as various activates occur, such as the LEDs
on and microSD/eMMC accesses.

.. _processor-interfaces:

Processor Interfaces
----------------------

The processor interacts with the *TPS65941213 and TPS65941111* via several different
signals. Each of these signals is described below.

.. _bbai64-i2c0:

I2C0
~~~~~~~~~~~~~~~

I2C0 is the control interface between the processor and the *TPS65941213 and TPS65941111*.
It allows the processor to control the registers inside the *TPS65941213 and TPS65941111*
for such things as voltage scaling and switching of the input rails.

.. _pmc_powr_en:

PMIC_POWR_EN
~~~~~~~~~~~~~~~

On power up the *VDD_RTC* rail activates first. After the RTC circuitry
in the processor has activated it instructs the *TPS65941213 and TPS65941111* to initiate
a full power up cycle by activating the *PMIC_POWR_EN* signal by taking
it HI. When powering down, the processor can take this pin low to start
the power down process.

.. _ldo_good:

LDO_GOOD
~~~~~~~~~~~~~~~

This signal connects to the *RTC_PORZn* signal, RTC power on reset. The
small “*n*” indicates that the signal is an active low signal. Word
processors seem to be unable to put a bar over a word so the**n** is
commonly used in electronics. As the RTC circuitry comes up first, this
signal indicates that the LDOs, the 1.8V VRTC rail, is up and stable.
This starts the power up process.

.. _pmic_pgood:

PMIC_PGOOD
~~~~~~~~~~~~~~~

Once all the rails are up, the *PMIC_PGOOD* signal goes high. This
releases the**PORZn** signal on the processor which was holding the
processor reset.

.. _wakeup:

WAKEUP
~~~~~~~~~~~~~~~

The WAKEUP signal from the *TPS65941213 and TPS65941111* is connected to the **EXT_WAKEUP**
signal on the processor. This is used to wake up the processor when it
is in a sleep mode. When an event is detected by the *TPS65941213 and TPS65941111*, such
as the power button being pressed, it generates this signal.

.. _pmic_int:

PMIC_INT
~~~~~~~~~~~~~~~

The *PMIC_INT* signal is an interrupt signal to the processor. Pressing
the power button will send an interrupt to the processor allowing it to
implement a power down mode in an orderly fashion, go into sleep mode,
or cause it to wake up from a sleep mode. All of these require SW
support.

.. _power-rails:

Power Rails
-------------

:ref:`figure-25` shows the connections of each of the rails from the **TPS65941213 and TPS65941111**.

.. _figure-25,Figure 25:

.. figure:: media/image39.*
   :width: 400px
   :align: center 
   :alt: Power Rails

   Power Rails

VRTC Rail
~~~~~~~~~~

The *VRTC* rail is a 1.8V rail that is the first rail to come up in the
power sequencing. It provides power to the RTC domain on the processor
and the I/O rail of the **TPS65941213 and TPS65941111**. It can deliver up to 250mA
maximum.

VDD_3V3A Rail
~~~~~~~~~~~~~

The *VDD_3V3A* rail is supplied by the **TPS65941213 and TPS65941111** and provides the
3.3V for the processor rails and can provide up to 400mA.

VDD_3V3B Rail
~~~~~~~~~~~~~

The current supplied by the *VDD_3V3A* rail is not sufficient to power
all of the 3.3V rails on the board. So a second LDO is supplied, U4,
a **TL5209A**, which sources the *VDD_3V3B* rail. It is powered up just
after the *VDD_3V3A* rail.

VDD_1V8 Rail
~~~~~~~~~~~~~

The *VDD_1V8* rail can deliver up to 400mA and provides the power
required for the 1.8V rails on the processor and the display framer. This
rail is not accessible for use anywhere else on the board.

VDD_CORE Rail
~~~~~~~~~~~~~~

The *VDD_CORE* rail can deliver up to 1.2A at 1.1V. This rail is not
accessible for use anywhere else on the board and connects only to the
processor. This rail is fixed at 1.1V and should not be adjusted by SW
using the PMIC. If you do, then the processor will no longer work.

VDD_MPU Rail
~~~~~~~~~~~~

The *VDD_MPU* rail can deliver up to 1.2A. This rail is not accessible
for use anywhere else on the board and connects only to the processor.
This rail defaults to 1.1V and can be scaled up to allow for higher
frequency operation. Changing of the voltage is set via the I2C
interface from the processor.

VDDS_DDR Rail
~~~~~~~~~~~~~~

The *VDDS_DDR* rail defaults to**1.5V** to support the LPDDR4 rails and
can deliver up to 1.2A. It is possible to adjust this voltage rail down
to *1.35V* for lower power operation of the LPDDR4 device. Only LPDDR4
devices can support this voltage setting of 1.35V.

Power Sequencing
-----------------

The power up process is consists of several stages and events. :ref:`figure-26`
describes the events that make up the power up process for the
processer from the PMIC. This diagram is used elsewhere to convey
additional information. I saw no need to bust it up into smaller
diagrams. It is from the processor datasheet supplied by Texas
Instruments.

.. _figure-26,Figure 26:

.. figure:: media/image40.*
   :width: 400px
   :align: center 
   :alt: Power Rail Power Up Sequencing

   Power Rail Power Up Sequencing

:ref:`figure-27` the voltage rail sequencing for the**TPS65941213 and TPS65941111** as it
powers up and the voltages on each rail. The power sequencing starts at
15 and then goes to one. That is the way the *TPS65941213 and TPS65941111* is configured.
You can refer to the TPS65941213 and TPS65941111 datasheet for more information.

.. _figure-27,Figure 27:

.. figure:: media/image41.*
   :width: 400px
   :align: center 
   :alt: TPS65941213 and TPS65941111 Power Sequencing Timing

   TPS65941213 and TPS65941111 Power Sequencing Timing

.. _power-led:

Power LED
----------

The power LED is a blue LED that will turn on once the *TPS65941213 and TPS65941111* has
finished the power up procedure. If you ever see the LED flash once,
that means that the *TPS65941213 and TPS65941111* started the process and encountered an
issue that caused it to shut down. The connection of the LED is shown in
:ref:`figure-25`.

.. _TPS65941213-and-TPS65941111-power-up-process:

TPS65941213 and TPS65941111 Power Up Process
---------------------------------------------

:ref:`figure-28` shows the interface between the **TPS65941213 and TPS65941111** and the
processor. It is a cut from the PDF form of the schematic and reflects
what is on the schematic.

.. _figure-28,Figure 28:

.. figure:: media/image42.*
   :width: 400px
   :align: center 
   :alt: Power Processor Interfaces

   Power Processor Interfaces

When voltage is applied, DC or USB, the *TPS65941213 and TPS65941111* connects the power
to the SYS output pin which drives the switchers and LDOs in
the *TPS65941213 and TPS65941111*.

At power up all switchers and LDOs are off except for the *VRTC LDO*
(1.8V), which provides power to the VRTC rail and controls
the **RTC_PORZn** input pin to the processor, which starts the power up
process of the processor. Once the RTC rail powers up, the *RTC_PORZn*
pin, driven by the *LDO_PGOOD* signal from the *TPS65941213 and TPS65941111*, of the
processor is released.

Once the *RTC_PORZn* reset is released, the processor starts the
initialization process. After the RTC stabilizes, the processor launches
the rest of the power up process by activating the**PMIC_POWER_EN**
signal that is connected to the *TPS65941213 and TPS65941111* which starts the *TPS65941213 and TPS65941111*
power up process.

The *LDO_PGOOD* signal is provided by the**TPS65941213 and TPS65941111** to the processor.
As this signal is 1.8V from the *TPS65941213 and TPS65941111* by virtue of the *TPS65941213 and TPS65941111*
VIO rail being set to 1.8V, and the *RTC_PORZ* signal on the processor
is 3.3V, a voltage level shifter, *U4*, is used. Once the LDOs and
switchers are up on the *TPS65941213 and TPS65941111*, this signal goes active releasing
the processor. The LDOs on the *TPS65941213 and TPS65941111* are used to power the VRTC
rail on the processor.

.. _processor-control-interface:

Processor Control Interface
----------------------------

:ref:`figure-28` above shows two interfaces between the processor and
the **TPS65941213 and TPS65941111** used for control after the power up sequence has
completed.

The first is the *I2C0* bus. This allows the processor to turn on and
off rails and to set the voltage levels of each regulator to supports
such things as voltage scaling.

The second is the interrupt signal. This allows the *TPS65941213 and TPS65941111* to alert
the processor when there is an event, such as when the power button is
pressed. The interrupt is an open drain output which makes it easy to
interface to 3.3V of the processor.

.. _low-power-mode-support:

Low Power Mode Support
-----------------------

This section covers three general power down modes that are available.
These modes are only described from a Hardware perspective as it relates
to the HW design.

RTC Only
~~~~~~~~~

In this mode all rails are turned off except the *VDD_RTC*. The
processor will need to turn off all the rails to enter this mode.
The **VDD_RTC** staying on will keep the RTC active and provide for the
wakeup interfaces to be active to respond to a wake up event.

RTC Plus DDR
~~~~~~~~~~~~

In this mode all rails are turned off except the *VDD_RTC* and
the **VDDS_DDR**, which powers the LPDDR4 memory. The processor will need
to turn off all the rails to enter this mode. The *VDD_RTC* staying on
will keep the RTC active and provide for the wakeup interfaces to be
active to respond to a wake up event.

The *VDDS_DDR* rail to the LPDDR4 is provided by the 1.5V rail of
the **TPS65941213 and TPS65941111** and with *VDDS_DDR* active, the LPDDR4 can be placed in
a self refresh mode by the processor prior to power down which allows
the memory data to be saved.

Currently, this feature is not included in the standard software
release. The plan is to include it in future releases.

Voltage Scaling
~~~~~~~~~~~~~~~~

For a mode where the lowest power is possible without going to sleep,
this mode allows the voltage on the ARM processor to be lowered along
with slowing the processor frequency down. The I2C0 bus is used to
control the voltage scaling function in the *TPS65941213 and TPS65941111*.

.. _sitara-am3358bzcz100-processor:

TI J721E DRA829/TDA4VM/AM752x Processor
=========================================

The board is designed to use the TI J721E DRA829/TDA4VM/AM752x processor in the
15 x 15 package. 

.. _description:

Description
-------------

:ref:`figure-29` is a high level block diagram of the processor. For more information on the processor, go to `https://www.ti.com/product/TDA4VM <https://www.ti.com/product/TDA4VM>`_

.. _figure-29,Figure 29:

.. figure:: media/image43.*
   :width: 400px
   :align: center 
   :alt: Jacinto TDA4VMBZCZ Block Diagram

   Jacinto TDA4VMBZCZ Block Diagram


.. _high-level-features:

High Level Features
-------------------

:ref:`table-5` below shows a few of the high level features of the Jacinto
processor.

.. _table-5,Table 5:


.. list-table:: Table 5: Processor Features
   :header-rows: 1

   * - Operating Systems 
     - Linux, Android, Windows Embedded CE,QNX,ThreadX 
     - MMC/SD 
     - 3
   * - Standby Power 
     - 7 mW 
     - CAN 
     - 2
   * - ARM CPU 
     - 1 ARM Cortex-A8 
     - UART (SCI) 
     - 6
   * - ARM MHz (Max.) 
     - 275,500,600,800,1000 
     - ADC 
     - 8-ch 12-bit
   * - ARM MIPS (Max.) 
     - 1000,1200,2000 
     - PWM (Ch) 
     - 3
   * - Graphics Acceleration 
     - 1 3D 
     - eCAP 
     - 3
   * - Other Hardware Acceleration 
     - 2 PRU-ICSS,Crypto Accelerator 
     - eQEP 
     - 3
   * - On-Chip L1 Cache 
     - 64 KB (ARM Cortex-A8) 
     - RTC 
     - 1
   * - On-Chip L2 Cache 
     - 256 KB (ARM Cortex-A8) 
     - I2C 
     - 3
   * - Other On-Chip Memory 
     - 128 KB 
     - McASP 
     - 2
   * - Display Options 
     - LCD 
     - SPI 
     - 2
   * - General Purpose Memory 
     - 1 16-bit (GPMC, NAND flash, NOR Flash, SRAM)
     - DMA (Ch) 
     - 64-Ch EDMA
   * - DRAM 
     - 1 16-bit (LPDDR-400,DDR2-532, DDR3-400) 
     - IO Supply (V) 
     - 1.8V(ADC),3.3V
   * - USB Ports 
     - 2 
     - Operating Temperature Range (C) 
     - -40 to 90

.. _documentation:

Documentation
--------------

Full documentation for the processor can be found on the TI website at `https://www.ti.com/product/TDA4VM <https://www.ti.com/product/TDA4VM>`_ for the current processor used on the board. Make sure that you always use the latest datasheets and Technical Reference Manuals (TRM).

.. _crystal-circuitry:

Crystal Circuitry
------------------

:ref:`figure-30` is the crystal circuitry for the TDA4VM processor.

.. _figure-30,Figure 30:

.. figure:: media/image44.*
   :width: 400px
   :align: center 
   :caption: Processor Crystals

.. _reset-circuitry:

Reset Circuitry
----------------

:ref:`figure-31` is the board reset circuitry. The initial power on reset is
generated by the **TPS65941213 and TPS65941111** power management IC. It also handles the
reset for the Real Time Clock.

The board reset is the SYS_RESETn signal. This is connected to the
NRESET_INOUT pin of the processor. This pin can act as an input or an
output. When the reset button is pressed, it sends a warm reset to the
processor and to the system.

On the revision A5D board, a change was made. On power up, the
NRESET_INOUT signal can act as an output. In this instance it can cause
the SYS_RESETn line to go high prematurely. In order to prevent this,
the PORZn signal from the TPS65941213 and TPS65941111 is connected to the SYS_RESETn line
using an open drain buffer. These ensure that the line does not
momentarily go high on power up.

.. _figure-31,Figure 31:

.. figure:: media/image45.*
   :width: 400px
   :align: center 
   :alt: Board Reset Circuitry

   Board Reset Circuitry

This change is also in all revisions after A5D.

LPDDR4 Memory
=============

BeagleBone AI-64 uses a single MT41K256M16HA-125 512MB LPDDR4 device
from Micron that interfaces to the processor over 16 data lines, 16
address lines, and 14 control lines. On rev C we added the Kingston
*KE4CN2H5A-A58* device as a source for the LPDDR4 device.

The following sections provide more details on the design.

.. _memory-device:

Memory Device
---------------

The design supports the standard DDR3 and LPDDR4 x16 devices and is built
using the LPDDR4. A single x16 device is used on the board and there is
no support for two x8 devices. The DDR3 devices work at 1.5V and the
LPDDR4 devices can work down to 1.35V to achieve lower power. The LPDDR4 comes in a 96-BALL FBGA package
with 0.8 mil pitch. Other standard DDR3 devices can also be supported,
but the LPDDR4 is the lower power device and was chosen for its ability
to work at 1.5V or 1.35V. The standard frequency that the LPDDR4 is run
at on the board is 400MHZ.

.. _ddr3l-memory-design:

LPDDR4 Memory Design
---------------------

:ref:`figure-32` is the schematic for the LPDDR4 memory device. Each of the
groups of signals is described in the following lines.

*Address Lines:*  Provide the row address for ACTIVATE commands, and the
column address and auto pre-charge bit (A10) for READ/WRITE commands, to
select one location out of the memory array in the respective bank. A10
sampled during a PRECHARGE command determines whether the PRECHARGE applies to one bank (A10 LOW, bank selected by BA[2:0]) or all banks (A10 HIGH). The address
inputs also provide the op-code during a LOAD MODE command. Address
inputs are referenced to VREFCA. A12/BC#: When enabled in the mode
register (MR), A12 is sampled during READ and WRITE commands to
determine whether burst chop (on-the-fly) will be performed (HIGH  BL8
or no burst chop, LOW  BC4 burst chop).

*Bank Address Lines:*  BA[2:0] define the bank to which an ACTIVATE, READ, WRITE, or PRECHARGE command is being applied. BA[2:0] define which mode register (MR0, MR1, MR2, or MR3) is loaded during the LOAD MODE command. BA[2:0] are referenced to VREFCA.

*CK and CK# Lines:* are differential clock inputs. All address and
control input signals are sampled on the crossing of the positive edge
of CK and the negative edge of CK#. Output data strobe (DQS, DQS#) is
referenced to the crossings of CK and CK#.

*Clock Enable Line:* CKE enables (registered HIGH) and disables
(registered LOW) internal circuitry and clocks on the DRAM. The specific
circuitry that is enabled/disabled is dependent upon the DDR3 SDRAM
configuration and operating mode. Taking CKE LOW provides PRECHARGE
power-down and SELF REFRESH operations (all banks idle) or active
power-down (row active in any bank). CKE is synchronous for powerdown
entry and exit and for self refresh entry. CKE is asynchronous for self
refresh exit. Input buffers (excluding CK, CK#, CKE, RESET#, and ODT)
are disabled during powerdown. Input buffers (excluding CKE and RESET#)
are disabled during SELF REFRESH. CKE is referenced to VREFCA.

.. _figure-32,Figure 32:

.. figure:: media/image46.*
   :width: 400px
   :align: center 
   :alt: LPDDR4 Memory Design

   LPDDR4 Memory Design

*Chip Select Line:* CS# enables (registered LOW) and disables
(registered HIGH) the command decoder. All commands are masked when CS#
is registered HIGH. CS# provides for external rank selection on systems
with multiple ranks. CS# is considered part of the command code. CS# is
referenced to VREFCA.

*Input Data Mask Line:* DM is an input mask signal for write data. Input
data is masked when DM is sampled HIGH along with the input data during
a write access. Although the DM ball is input-only, the DM loading is
designed to match that of the DQ and DQS balls. DM is referenced to
VREFDQ.

*On-die Termination Line:* ODT enables (registered HIGH) and disables
(registered LOW) termination resistance internal to the LPDDR4 SDRAM.
When enabled in normal operation, ODT is only applied to each of the
following balls: DQ[7:0], DQS, DQS#, and DM for the x8; DQ[3:0], DQS,
DQS#, and DM for the x4. The ODT input is ignored if disabled via the
LOAD MODE command. ODT is referenced to VREFCA.

.. _power-rails-1:

Power Rails
-----------

The *LPDDR4* memory device and the DDR3 rails on the processor are
supplied by the**TPS65941213 and TPS65941111**. Default voltage is 1.5V but can be scaled
down to 1.35V if desired.

.. _vref:

VREF
~~~~~

The *VREF* signal is generated from a voltage divider on the **VDDS_DDR**
rail that powers the processor DDR rail and the LPDDR4 device itself.
*Figure 33* below shows the configuration of this signal and the
connection to the LPDDR4 memory device and the processor.

.. _figure-33,Figure 33:

.. figure:: media/image47.*
   :width: 400px
   :align: center 
   :alt: LPDDR4 VREF Design

   LPDDR4 VREF Design


.. _gb-emmc-memory:

4GB eMMC Memory
===============

The eMMC is a communication and mass data storage device that includes a
Multi-MediaCard (MMC) interface, a NAND Flash component, and a
controller on an advanced 11-signal bus, which is compliant with the MMC
system specification. The nonvolatile eMMC draws no power to maintain
stored data, delivers high performance across a wide range of operating
temperatures, and resists shock and vibration disruption.

One of the issues faced with SD cards is that across the different
brands and even within the same brand, performance can vary. Cards use
different controllers and different memories, all of which can have bad
locations that the controller handles. But the controllers may be
optimized for reads or writes. You never know what you will be getting.
This can lead to varying rates of performance. The eMMC card is a known
controller and when coupled with the 8bit mode, 8 bits of data instead
of 4, you get double the performance which should result in quicker boot
times.

The following sections describe the design and device that is used on
the board to implement this interface.

.. _emmc-device:

eMMC Device
------------

The device used is one of two different devices:

* Micron *MTFC4GLDEA 0M WT*
* Kingston *KE4CN2H5A-A58*

The package is a 153 ball WFBGA device on both devices.

.. _emmc-circuit-design:

eMMC Circuit Design
-------------------

:ref:`figure-34` is the design of the eMMC circuitry. The eMMC device is
connected to the MMC1 port on the processor. MMC0 is still used for the
microSD card as is currently done on the BeagleBone Black. The size
of the eMMC supplied is now 4GB.

The device runs at 3.3V both internally and the external I/O rails. The
VCCI is an internal voltage rail to the device. The manufacturer
recommends that a 1uF capacitor be attached to this rail, but a 2.2uF
was chosen to provide a little margin.

Pullup resistors are used to increase the rise time on the signals to
compensate for any capacitance on the board.

.. _figure-34,Figure 34:

.. figure:: media/image48.*
   :width: 400px
   :align: center 
   :alt: eMMC Memory Design

   eMMC Memory Design


The pins used by the eMMC1 in the boot mode are listed below in *Table 6*.

.. _table-6,Table 6:

.. figure:: media/image49.*
   :width: 400px
   :align: center 
   :alt: eMMC Boot Pins

   eMMC Boot Pins

For eMMC devices the ROM will only support raw mode. The ROM Code reads
out raw sectors from image or the booting file within the file system
and boots from it. In raw mode the booting image can be located at one
of the four consecutive locations in the main area: offset 0x0 / 0x20000
(128 KB) / 0x40000 (256 KB) / 0x60000 (384 KB). For this reason, a
booting image shall not exceed 128KB in size. However it is possible to
flash a device with an image greater than 128KB starting at one of the
aforementioned locations. Therefore the ROM Code does not check the
image size. The only drawback is that the image will cross the
subsequent image boundary. The raw mode is detected by reading sectors
#0, #256, #512, #768. The content of these sectors is then verified for
presence of a TOC structure. In the case of a *GP Device*, a
Configuration Header (CH) *must* be located in the first sector followed
by a *GP header*. The CH might be void (only containing a CHSETTINGS
item for which the Valid field is zero).

The ROM only supports the 4-bit mode. After the initial boot, the switch
can be made to 8-bit mode for increasing the overall performance of the
eMMC interface.

.. _bbai64-board-id-eeprom:

Board ID EEPROM
================

BeagleBone AI-64 is equipped with a single 32Kbit(4KB) 24LC32AT-I/OT
EEPROM to allow the SW to identify the board. :ref:`table-7` below defined
the contents of the EEPROM.

.. _table-7,Table 7:

.. list-table:: EEPROM Contents
   :header-rows: 1

   * - Name    
     - Size (bytes)    
     - Contents   
   * - Header    
     - 4    
     - 0xAA, 0x55, 0x33, EE   
   * - Board Name    
     - 8    
     - Name for board in ASCII: A335BNLT   
   * - Version    
     - 4    
     - Hardware version code for board in ASCII: 00A3 for Rev A3, 00A4 for Rev A4, 00A5 for Rev A5,00A6 for Rev A6,00B0 for Rev B, and 00C0 for Rev C.   
   * - Serial Number    
     - 12    
     - Serial number of the board. This is a 12 character string which is: WWYY4P16nnnn where: WW  2 digit week of the year of production YY  2 digit year of production BBBK  BeagleBone AI-64 nnnn  incrementing board number   
   * - Configuration Option    
     - 32    
     - Codes to show the configuration setup on this board.All FF   
   * - RSVD    
     - 6    
     - FF FF FF FF FF FF   
   * - RSVD    
     - 6    
     - FF FF FF FF FF FF   
   * - RSVD    
     - 6    
     - FF FF FF FF FF FF   
   * - Available    
     - 4018    
     - Available space for other non-volatile codes/data   

:ref:`figure-35` shows the new design on the EEPROM interface.

.. _figure-35,Figure 35:

.. figure:: media/image50.*
   :width: 400px
   :align: center 
   :alt: EEPROM Design

   EEPROM Design

The EEPROM is accessed by the processor using the I2C 0 bus. The *WP*
pin is enabled by default. By grounding the test point, the write
protection is removed.

The first 48 locations should not be written to if you choose to use the
extras storage space in the EEPROM for other purposes. If you do, it
could prevent the board from booting properly as the SW uses this
information to determine how to set up the board.

.. _micro-secure-digital:

Micro Secure Digital
=====================

The microSD connector on the board will support a microSD card that can
be used for booting or file storage on BeagleBone AI-64.

.. _microsd-design:

microSD Design
-----------------

:ref:`figure-36` below is the design of the microSD interface on the board.

.. _figure-36,Figure 36:

.. figure:: media/image51.*
   :width: 400px
   :align: center 
   :alt: microSD Design

   microSD Design

The signals *MMC0-3* are the data lines for the transfer of data between
the processor and the microSD connector.

The *MMC0_CLK* signal clocks the data in and out of the microSD card.

The *MMCO_CMD* signal indicates that a command versus data is being sent.

There is no separate card detect pin in the microSD specification. It
uses *MMCO_DAT3* for that function. However, most microSD connectors
still supply a CD function on the connectors. In BeagleBone AI-64
design, this pin is connected to the**MMC0_SDCD** pin for use by the
processor. You can also change the pin to *GPIO0_6*, which is able to
wake up the processor from a sleep mode when an microSD card is inserted
into the connector.

Pullup resistors are provided on the signals to increase the rise times
of the signals to overcome PCB capacitance.

Power is provided from the *VDD_3V3B* rail and a 10uF capacitor is
provided for filtering.

.. _user-leds:

User LEDs
==========

There are five user LEDs on BeagleBone AI-64. These are connected to
GPIO pins on the processor. *Figure 37* shows the interfaces for the
user LEDs.

.. _figure-37,Figure 37:

.. figure:: media/image52.*
   :width: 400px
   :align: center 
   :alt: User LEDs

   User LEDs

Resistors R71-R74 were changed to 4.75K on the revision A5B and later
boards.

:ref:`table-8` shows the signals used to control the four LEDs from the
processor.

.. _table-8,Table 8:

.. list-table:: Table 8: User LED Control Signals/Pins
   :header-rows: 1

   * - LED 
     - GPIO SIGNAL 
     - PROC PIN
   * - USR0 
     - GPIO1_21 
     - V15
   * - USR1 
     - GPIO1_22 
     - U15
   * - USR2 
     - GPIO1_23 
     - T15
   * - USR3 
     - GPIO1_24 
     - V16

   

A logic level of “1” will cause the LEDs to turn on.

.. _boot-configuration:

Boot Configuration
===================

The design supports two groups of boot options on the board. The user
can switch between these modes via the Boot button. The primary boot
source is the onboard eMMC device. By holding the Boot button, the user
can force the board to boot from the microSD slot. This enables the eMMC
to be overwritten when needed or to just boot an alternate image. The
following sections describe how the boot configuration works.

In most applications, including those that use the provided demo
distributions available from `beagleboard.org <http://beagleboard.org/>`_ the processor-external boot code is composed of two stages. After the
primary boot code in the processor ROM passes control, a secondary stage
(secondary program loader -- "SPL" or "MLO") takes over. The SPL stage
initializes only the required devices to continue the boot process, and
then control is transferred to the third stage "U-boot". Based on the
settings of the boot pins, the ROM knows where to go and get the SPL and
UBoot code. In the case of BeagleBone AI-64, that is either eMMC or
microSD based on the position of the boot switch.

.. _boot-configuration-design:

Boot Configuration Design
---------------------------

:ref:`figure-38` shows the circuitry that is involved in the boot
configuration process. On power up, these pins are read by the processor
to determine the boot order. S2 is used to change the level of one bit
from HI to LO which changes the boot order.

.. _figure-38,Figure 38:

.. figure:: media/image53.*
   :width: 400px
   :align: center 
   :alt: Processor Boot Configuration Design

   Processor Boot Configuration Design

It is possible to override these setting via the expansion headers. But
be careful not to add too much load such that it could interfere with
the operation of the display interface or LCD panels. If you choose to
override these settings, it is strongly recommended that you gate these
signals with the *SYS_RESETn* signal. This ensures that after coming out
of reset these signals are removed from the expansion pins.

.. _default-boot-options:

Default Boot Options
---------------------

Based on the selected option found in :ref:`figure-39` below, each of the
boot sequences for each of the two settings is shown.

.. _figure-39,Figure 39:

.. figure:: media/image54.*
   :width: 400px
   :align: center 
   :alt: Processor Boot Configuration

   Processor Boot Configuration

The first row in :ref:`figure-39` is the default setting. On boot, the
processor will look for the eMMC on the MMC1 port first, followed by the
microSD slot on MMC0, USB0 and UART0. In the event there is no microSD
card and the eMMC is empty, UART0 or USB0 could be used as the board
source.

If you have a microSD card from which you need to boot from, hold the
boot button down. On boot, the processor will look for the SPIO0 port
first, then microSD on the MMC0 port, followed by USB0 and UART0. In the
event there is no microSD card and the eMMC is empty, USB0 or UART0
could be used as the board source.

.. _ethernet:

10/100/1000 Ethernet
====================

BeagleBone AI-64 is equipped with a 10/100/1000 Ethernet interface.
The design is
described in the following sections.

.. _ethernet-processor-interface:

Ethernet Processor Interface
-----------------------------

:ref:`figure-40` shows the connections between the processor and the PHY. The
interface is in the MII mode of operation.

.. _figure-40,Figure 40:

.. figure:: media/image55.*
   :width: 400px
   :align: center 
   :alt: Ethernet Processor Interface

   Ethernet Processor Interface


This is the same interface as is used on BeagleBone. No changes were
made in this design for the board.

.. _ethernet-connector-interface:

Ethernet Connector Interface
------------------------------

The off board side of the PHY connections are shown in *Figure 41*
below.

.. _figure-41,Figure 41:

.. figure:: media/image56.*
   :width: 400px
   :align: center 
   :alt: Ethernet Connector Interface

   Ethernet Connector Interface

This is the same interface as is used on BeagleBone. No changes were
made in this design for the board.

.. _ethernet-phy-power-reset-and-clocks:

Ethernet PHY Power, Reset, and Clocks
---------------------------------------

:ref:`figure-42` shows the power, reset, and lock connections to
the **LAN8710A** PHY. Each of these areas is discussed in more detail in
the following sections.

.. _figure-42,Figure 42:

.. figure:: media/image57.*
   :width: 400px
   :align: center 
   :alt: Ethernet PHY, Power, Reset, and Clocks

   Ethernet PHY, Power, Reset, and Clocks


VDD_3V3B Rail
~~~~~~~~~~~~~~~~~~~~~

The VDD_3V3B rail is the main power rail for the *LAN8710A*. It
originates at the VD_3V3B regulator and is the primary rail that
supports all of the peripherals on the board. This rail also supplies
the VDDIO rails which set the voltage levels for all of the I/O signals
between the processor and the **LAN8710A**.

VDD_PHYA Rail
~~~~~~~~~~~~~~~~~~~~~

A filtered version of VDD_3V3B rail is connected to the VDD rails of the
LAN8710 and the termination resistors on the Ethernet signals. It is
labeled as *VDD_PHYA*. The filtering inductor helps block transients
that may be seen on the VDD_3V3B rail.

PHY_VDDCR Rail
~~~~~~~~~~~~~~~~~~~~~

The *PHY_VDDCR* rail originates inside the LAN8710A. Filter and bypass
capacitors are used to filter the rail. Only circuitry inside the
LAN8710A uses this rail.

SYS_RESET
~~~~~~~~~~~~~~~~~~~~~

The reset of the LAN8710A is controlled via the *SYS_RESETn* signal, the
main board reset line.

Clock Signals
~~~~~~~~~~~~~~~~~~~~~

A crystal is used to create the clock for the LAN8710A. The processor
uses the *RMII_RXCLK* signal to provide the clocking for the data
between the processor and the LAN8710A.

.. _lan8710a-mode-pins:

LAN8710A Mode Pins
---------------------

There are mode pins on the LAN8710A that sets the operational mode for
the PHY when coming out of reset. These signals are also used to
communicate between the processor and the LAN8710A. As a result, these
signals can be driven by the processor which can cause the PHY not to be
initialized correctly. To ensure that this does not happen, three low
value pull up resistors are used. *Figure 43* below shows the three mode
pin resistors.

.. _figure-43,Figure 43:

.. figure:: media/image97.*
   :width: 400px
   :align: center 
   :alt: Ethernet PHY Mode Pins

   Ethernet PHY Mode Pins

This will set the mode to be 111, which enables all modes and enables
auto-negotiation.

.. _bbai64-displayport-interface:

Display Port Interface
========================

BeagleBone AI-64 has an onboard Display Port framer that converts the LCD
signals and audio signals to drive a Display Port monitor. The design uses the on chip
internal Display Port Framer.

The following sections provide more detail into the design of this
interface.

.. _supported-resolutions:

Supported Resolutions
------------------------------

The maximum resolution supported by BeagleBone AI-64 is 1280x1024 @
60Hz. *Table 9* below shows the supported resolutions. Not all
resolutions may work on all monitors, but these have been tested and
shown to work on at least one monitor. EDID is supported on the
BeagleBone AI-64. Based on the EDID reading from the connected monitor,
the highest compatible resolution is selected.

.Table 9. HDMI Supported Monitor Adapter  Resolutions
[cols"4,1",options"header",]

.. list-table:: Table 9. HDMI Supported Monitor Adapter  Resolutions
   :header-rows: 1

   * - RESOLUTION    
     - AUDIO
   * - 800 x 600 @60Hz    
     - 
   * - 800 x 600 @56Hz    
     - 
   * - 640 x 480 @75Hz    
     - 
   * - 640 x 480 @60Hz    
     - YES 
   * - 720 x 400 @70Hz    
     - 
   * - 1280 x 1024 @75Hz    
     - 
   * - 1024 x 768 @75Hz    
     - 
   * - 1024 x 768 @70Hz    
     - 
   * - 1024 x 768 @60Hz    
     - 
   * - 800 x 600 @75Hz    
     - 
   * - 800 x 600 @72Hz    
     - 
   * - 720 x 480 @60Hz    
     - YES 
   * - 1280 x 720 @60Hz    
     - YES 
   * - 1920x1080 @24Hz    
     - YES 


.. note ::
    
   The updated software image used on the Rev A5B and later boards added support for 1920x1080@24HZ.


Audio is limited to CEA supported resolutions. LCD panels only activate
the audio in CEA modes. This is a function of the specification and is
not something that can be fixed on the board via a hardware change or a
software change.

Connectors and buttons
======================

.. _power-connections:

Power Connections
------------------

.. _hdmi-connector-interface:

miniDP Connector Interface
----------------------------------

.. _usb-host:

USB Host
-----------------------------------

The board is equipped with a dual USB host interface accessible from a
dual stacked USB Type A female connector. :ref:`figure-48` is the design of the USB
Host circuitry.

.. _figure-48,Figure 48:

.. figure:: media/image66.*
   :width: 400px
   :align: center 
   :alt: USB Host circuit

   USB Host circuit

.. _power-switch:

Power Switch
-------------------------

*U8* is a switch that allows the power to the connector to be turned on
or off by the processor. It also has an over current detection that can
alert the processor if the current gets too high via the**USB1_OC**
signal. The power is controlled by the *USB1_DRVBUS* signal from the
processor.

