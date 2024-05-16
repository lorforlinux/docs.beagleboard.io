.. _beagley-ai-design:

Design and specifications
#########################

If you want to know how BeagleY-AI is designed and the detailed specifications, then
this chapter is for you. We are going to attept to provide you a short and crisp overview
followed by discussing each hardware design element in detail.

Block diagram and overview
***************************

.. figure:: images/hardware-design/beagley-ai-block-diagram.*
    :width: 1040
    :align: center
    :alt: BeagleY-AI block diagram

    BeagleY-AI block diagram

.. figure:: images/hardware-design/beagley-ai-pdn.*
    :width: 1040
    :align: center
    :alt: BeagleY-AI power distribution network

    BeagleY-AI power distribution network

.. figure:: images/hardware-design/beagley-ai-iic-tree.*
    :width: 1040
    :align: center
    :alt: BeagleY-AI I2C tree

    BeagleY-AI I2C tree

SoC
****

.. figure:: images/hardware-design/beagley-ai-soc-csi-0123.*
    :width: 1040
    :align: center
    :alt: BeagleY-AI SoC CSI1, CSI2, and CSI3

    BeagleY-AI SoC CSI1, CSI2, and CSI3

.. figure:: images/hardware-design/beagley-ai-soc-ddr0.*
    :width: 1040
    :align: center
    :alt: BeagleY-AI SoC DDR0 connections

    BeagleY-AI SoC DDR0 connections

.. figure:: images/hardware-design/beagley-ai-soc-dsi.*
    :width: 1040
    :align: center
    :alt: BeagleY-AI SoC DSI connections

    BeagleY-AI SoC DSI0 TX connections

.. figure:: images/hardware-design/beagley-ai-soc-efuse-vmon-jtag-rsvd.*
    :width: 1040
    :align: center
    :alt: BeagleY-AI SoC eFUSE, VMON, Debug, and RSVD

    BeagleY-AI SoC eFUSE, VMON, Debug, and RSVD

.. figure:: images/hardware-design/beagley-ai-soc-gpmc.*
    :width: 1040
    :align: center
    :alt: BeagleY-AI SoC GPMC0

    BeagleY-AI SoC GPMC0

.. figure:: images/hardware-design/beagley-ai-soc-ground.*
    :width: 1040
    :align: center
    :alt: BeagleY-AI SoC ground connections

    BeagleY-AI SoC ground connections

.. figure:: images/hardware-design/beagley-ai-soc-mmc-012.*
    :width: 1040
    :align: center
    :alt: BeagleY-AI SoC MMC0, MMC1, and MMC2

    BeagleY-AI SoC MMC0, MMC1, and MMC2

.. figure:: images/hardware-design/beagley-ai-soc-oldi.*
    :width: 1040
    :align: center
    :alt: BeagleY-AI SoC OLDI

    BeagleY-AI SoC OLDI

.. figure:: images/hardware-design/beagley-ai-soc-ospi.*
    :width: 1040
    :align: center
    :alt: BeagleY-AI SoC OSPI0

    BeagleY-AI SoC OSPI0

.. figure:: images/hardware-design/beagley-ai-soc-rgmii.*
    :width: 1040
    :align: center
    :alt: BeagleY-AI SoC RGMII

    BeagleY-AI SoC RGMII

.. figure:: images/hardware-design/beagley-ai-soc-serdes0.*
    :width: 1040
    :align: center
    :alt: BeagleY-AI SoC SERDES0

    BeagleY-AI SoC SERDES0

.. figure:: images/hardware-design/beagley-ai-soc-serdes1.*
    :width: 1040
    :align: center
    :alt: BeagleY-AI SoC SERDES1

    BeagleY-AI SoC SERDES1

.. figure:: images/hardware-design/beagley-ai-soc-supply-noise-kelvin-sensing.*
    :width: 1040
    :align: center
    :alt: BeagleY-AI SoC supply noise kelvin sensing

    BeagleY-AI SoC supply noise kelvin sensing

.. figure:: images/hardware-design/beagley-ai-soc-usb0-and-usb1.*
    :width: 1040
    :align: center
    :alt: BeagleY-AI SoC USB0 and USB1

    BeagleY-AI SoC USB0 and USB1

.. figure:: images/hardware-design/beagley-ai-soc-vout.*
    :width: 1040
    :align: center
    :alt: BeagleY-AI SoC VOUT

    BeagleY-AI SoC VOUT

.. figure:: images/hardware-design/beagley-ai-soc-analog-power1.*
    :width: 1040
    :align: center
    :alt: BeagleY-AI SoC analog power1

    BeagleY-AI SoC analog power1

.. figure:: images/hardware-design/beagley-ai-soc-io-ddr-power2.*
    :width: 1040
    :align: center
    :alt: BeagleY-AI AI SoC IO and DDR power2

    BeagleY-AI AI SoC IO and DDR power2

.. figure:: images/hardware-design/beagley-ai-soc-digital-power3.*
    :width: 1040
    :align: center
    :alt: BeagleY-AI SoC digital power3

    BeagleY-AI SoC digital power3


.. figure:: images/hardware-design/beagley-ai-reset-cntrls-mcu-osc.*
    :width: 1040
    :align: center
    :alt: BeagleY-AI SoC Reset, Cntrls, and Clk

    BeagleY-AI SoC Reset, Cntrls, and Clk

.. figure:: images/hardware-design/beagley-ai-rgmii-rst.*
    :width: 1040
    :align: center
    :alt: BeagleY-AI SoC RGMII1 RST

    BeagleY-AI SoC RGMII1 RST

.. figure:: images/hardware-design/beagley-ai-vdd-core-hcps.*
    :width: 1040
    :align: center
    :alt: BeagleY-AI VDD core hcps

    BeagleY-AI VDD core hcps

.. figure:: images/hardware-design/beagley-ai-wkup-reset-cntrls-osc.*
    :width: 1040
    :align: center
    :alt: BeagleY-AI wkup reset cntrls osc

    BeagleY-AI wkup reset cntrls osc


Boot modes
***********

.. figure:: images/hardware-design/beagley-ai-boot-modes.*
    :width: 1040
    :align: center
    :alt: BeagleY-AI boot modes

    BeagleY-AI boot modes


Power sources
***************

.. figure:: images/hardware-design/beagley-ai-vsys-3v3.*
    :width: 1040
    :align: center
    :alt: BeagleY-AI VSYS 3V3

    BeagleY-AI VSYS 3V3

.. figure:: images/hardware-design/beagley-ai-3v3-2v5-to-1v1-ldo.*
    :width: 1040
    :align: center
    :alt: BeagleY-AI 3V3/V5 to 1V1 LDO

    BeagleY-AI 3V3/V5 to 1V1 LDO

PMIC
*****

.. figure:: images/hardware-design/beagley-ai-pmic.*
    :width: 1040
    :align: center
    :alt: BeagleY-AI PMIC

    BeagleY-AI PMIC

.. figure:: images/hardware-design/beagley-ai-pmic-nvm-programming.*
    :width: 1040
    :align: center
    :alt: BeagleY-AI PMIC NVM programming interface

    BeagleY-AI PMIC NVM programming interface

General connectivity and expansion
************************************

.. figure:: images/hardware-design/beagley-ai-user-expansion-connector.*
    :width: 1040
    :align: center
    :alt: BeagleY-AI user expansion connector

    BeagleY-AI user expansion connector

.. figure:: images/hardware-design/beagley-ai-rpi-csi.*
    :width: 1040
    :align: center
    :alt: BeagleY-AI RPI CSI

    BeagleY-AI RPI CSI

.. figure:: images/hardware-design/beagley-ai-rpi-dsi-csi.*
    :width: 1040
    :align: center
    :alt: BeagleY-AI RPI DSI/CSI

    BeagleY-AI RPI DSI/CSI


.. figure:: images/hardware-design/beagley-ai-dual-usb-1.*
    :width: 1040
    :align: center
    :alt: BeagleY-AI dual USB1

    BeagleY-AI dual USB1

.. figure:: images/hardware-design/beagley-ai-dual-usb-2.*
    :width: 1040
    :align: center
    :alt: BeagleY-AI dual USB2

    BeagleY-AI dual USB2

.. figure:: images/hardware-design/beagley-ai-dual-usb-current-limiter.*
    :width: 1040
    :align: center
    :alt: BeagleY-AI dual USB current limiter

    BeagleY-AI dual USB current limiter


.. figure:: images/hardware-design/beagley-ai-fan-connector.*
    :width: 1040
    :align: center
    :alt: BeagleY-AI fan connector

    BeagleY-AI fan connector

.. figure:: images/hardware-design/beagley-ai-general-io.*
    :width: 1040
    :align: center
    :alt: BeagleY-AI general IO

    BeagleY-AI general IO

.. figure:: images/hardware-design/beagley-ai-mcu-general-io.*
    :width: 1040
    :align: center
    :alt: BeagleY-AI MCU general IO

    BeagleY-AI MCU general IO


.. figure:: images/hardware-design/beagley-ai-usb3-hub.*
    :width: 1040
    :align: center
    :alt: BeagleY-AI USB3 hub

    BeagleY-AI USB3 hub

.. figure:: images/hardware-design/beagley-ai-usb-c.*
    :width: 1040
    :align: center
    :alt: BeagleY-AI USB-C

    BeagleY-AI USB-C

.. figure:: images/hardware-design/beagley-ai-usb-hub-config.*
    :width: 1040
    :align: center
    :alt: BeagleY-AI USB hub config

    BeagleY-AI USB hub config

.. figure:: images/hardware-design/beagley-ai-usb-vbus-resistor-divider-circuit.*
    :width: 1040
    :align: center
    :alt: BeagleY-AI USB VBUS resistor divider circuit

    BeagleY-AI USB VBUS resistor divider circuit


.. figure:: images/hardware-design/beagley-ai-i2c2-pu.*
    :width: 1040
    :align: center
    :alt: BeagleY-AI I2C2 pull-up resistors

    BeagleY-AI I2C2 pull-up resistors

.. figure:: images/hardware-design/beagley-ai-iic-ext-rtc.*
    :width: 1040
    :align: center
    :alt: BeagleY-AI I2C ext RTC

    BeagleY-AI I2C ext RTC

.. figure:: images/hardware-design/beagley-ai-iic-voltage-level-translator.*
    :width: 1040
    :align: center
    :alt: BeagleY-AI voltage level translator

    BeagleY-AI voltage level translator


Buttons and LEDs
*****************

.. figure:: images/hardware-design/beagley-ai-leds.*
    :width: 1040
    :align: center
    :alt: BeagleY-AI LEDs

    BeagleY-AI LEDs

Networking
************

.. figure:: images/hardware-design/beagley-ai-wifi-module.*
    :width: 1040
    :align: center
    :alt: BeagleY-AI WiFi module

    BeagleY-AI WiFi module


Ethernet
*********

.. figure:: images/hardware-design/beagley-ai-ethernet-connector.*
    :width: 1040
    :align: center
    :alt: BeagleY-AI ethernet connector

    BeagleY-AI ethernet connector

.. figure:: images/hardware-design/beagley-ai-ethernet-dp83867.*
    :width: 1040
    :align: center
    :alt: BeagleY-AI ethernet DP83867

    BeagleY-AI ethernet DP83867

.. figure:: images/hardware-design/beagley-ai-ethernet-phy-caps.*
    :width: 1040
    :align: center
    :alt: BeagleY-AI ethernet phy caps

    BeagleY-AI ethernet phy caps

.. figure:: images/hardware-design/beagley-ai-ethernet-phy-misc.*
    :width: 1040
    :align: center
    :alt: BeagleY-AI ethernet phy misc

    BeagleY-AI ethernet phy misc

.. figure:: images/hardware-design/beagley-ai-ethernet-phy-protection.*
    :width: 1040
    :align: center
    :alt: BeagleY-AI ethernet phy protection

    BeagleY-AI ethernet phy protection

.. figure:: images/hardware-design/beagley-ai-ethernet-power-3v3-to-2v5.*
    :width: 1040
    :align: center
    :alt: BeagleY-AI ethernet power 3V3 to 2V5

    BeagleY-AI ethernet power 3V3 to 2V5

.. figure:: images/hardware-design/beagley-ai-poe-header.*
    :width: 1040
    :align: center
    :alt: BeagleY-AI PoE header

    BeagleY-AI PoE header

Memory, media, and storage
****************************

.. figure:: images/hardware-design/beagley-ai-board-id-eeprom.*
    :width: 1040
    :align: center
    :alt: BeagleY-AI board id eeprom

    BeagleY-AI board id eeprom

.. figure:: images/hardware-design/beagley-ai-ddr-caps.*
    :width: 1040
    :align: center
    :alt: BeagleY-AI DDR caps

    BeagleY-AI DDR caps

.. figure:: images/hardware-design/beagley-ai-ddr.*
    :width: 1040
    :align: center
    :alt: BeagleY-AI DDR

    BeagleY-AI DDR

.. figure:: images/hardware-design/beagley-ai-ddr-power.*
    :width: 1040
    :align: center
    :alt: BeagleY-AI DDR power

    BeagleY-AI DDR power

.. figure:: images/hardware-design/beagley-ai-micro-sd-card-interface.*
    :width: 1040
    :align: center
    :alt: BeagleY-AI microSD card interface

    BeagleY-AI microSD card interface

.. figure:: images/hardware-design/beagley-ai-pcie-connector.*
    :width: 1040
    :align: center
    :alt: BeagleY-AI PCIE connector

    BeagleY-AI PCIE connector

Multimedia I/O
***************

.. figure:: images/hardware-design/beagley-ai-hdmi-addr-protection.*
    :width: 1040
    :align: center
    :alt: BeagleY-AI HDMI addr protection

    BeagleY-AI HDMI addr protection

.. figure:: images/hardware-design/beagley-ai-hdmi-power.*
    :width: 1040
    :align: center
    :alt: BeagleY-AI HDMI power

    BeagleY-AI HDMI power

.. figure:: images/hardware-design/beagley-ai-hdmi-reset.*
    :width: 1040
    :align: center
    :alt: BeagleY-AI HDMI reset

    BeagleY-AI HDMI reset

.. figure:: images/hardware-design/beagley-ai-rgb888-to-hdmi.*
    :width: 1040
    :align: center
    :alt: BeagleY-AI RGB888 to HDMI

    BeagleY-AI RGB888 to HDMI

Debug ports
************

.. figure:: images/hardware-design/beagley-ai-tag-connect.*
    :width: 1040
    :align: center
    :alt: BeagleY-AI Tag-Connect

    BeagleY-AI Tag-Connect

.. figure:: images/hardware-design/beagley-ai-debug-uart-port.*
    :width: 1040
    :align: center
    :alt: BeagleY-AI debug UART port

    BeagleY-AI debug UART port

Mechanical Specifications 
**************************

Dimensions & Weight
===================

.. table:: Dimensions & weight

    +--------------------+----------------------------------------------------+
    | Parameter          | Value                                              |
    +====================+====================================================+
    | Size               | 85 x 56 x 20 mm                                    |
    +--------------------+----------------------------------------------------+
    | Max heigh          | 20mm                                               |
    +--------------------+----------------------------------------------------+
    | PCB Size           | 85 x 56 mm                                         |
    +--------------------+----------------------------------------------------+
    | PCB Layers         | 14 layers                                          |
    +--------------------+----------------------------------------------------+
    | PCB Thickness      | 1.6mm                                              |
    +--------------------+----------------------------------------------------+
    | RoHS compliant     | Yes                                                |
    +--------------------+----------------------------------------------------+
    | Gross Weight       | 110 g                                              |
    +--------------------+----------------------------------------------------+
    | Net Weight         | 50 g                                               |
    +--------------------+----------------------------------------------------+