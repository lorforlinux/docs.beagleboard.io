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

.. figure:: images/hardware-design/beagley-ai-pdn.*
    :width: 1040
    :align: center
    :alt:

.. figure:: images/hardware-design/beagley-ai-iic-tree.*
    :width: 1040
    :align: center
    :alt:


SoC
****

.. figure:: images/hardware-design/beagley-ai-soc-csi-0123.*
    :width: 1040
    :align: center
    :alt:

.. figure:: images/hardware-design/beagley-ai-soc-ddr0.*
    :width: 1040
    :align: center
    :alt:

.. figure:: images/hardware-design/beagley-ai-soc-dsi.*
    :width: 1040
    :align: center
    :alt:

.. figure:: images/hardware-design/beagley-ai-soc-efuse-vmon-jtag-rsvd.*
    :width: 1040
    :align: center
    :alt:

.. figure:: images/hardware-design/beagley-ai-soc-gpmc.*
    :width: 1040
    :align: center
    :alt:

.. figure:: images/hardware-design/beagley-ai-soc-ground.*
    :width: 1040
    :align: center
    :alt:

.. figure:: images/hardware-design/beagley-ai-soc-mmc-012.*
    :width: 1040
    :align: center
    :alt:

.. figure:: images/hardware-design/beagley-ai-soc-oldi.*
    :width: 1040
    :align: center
    :alt:

.. figure:: images/hardware-design/beagley-ai-soc-ospi.*
    :width: 1040
    :align: center
    :alt:

.. figure:: images/hardware-design/beagley-ai-soc-rgmii.*
    :width: 1040
    :align: center
    :alt:

.. figure:: images/hardware-design/beagley-ai-soc-serdes0.*
    :width: 1040
    :align: center
    :alt:

.. figure:: images/hardware-design/beagley-ai-soc-serdes1.*
    :width: 1040
    :align: center
    :alt:

.. figure:: images/hardware-design/beagley-ai-soc-supply-noise-kelvin-sensing.*
    :width: 1040
    :align: center
    :alt:

.. figure:: images/hardware-design/beagley-ai-soc-usb0-and-usb1.*
    :width: 1040
    :align: center
    :alt:

.. figure:: images/hardware-design/beagley-ai-soc-vout.*
    :width: 1040
    :align: center
    :alt:

.. figure:: images/hardware-design/beagley-ai-soc-analog-power1.*
    :width: 1040
    :align: center
    :alt:

.. figure:: images/hardware-design/beagley-ai-soc-io-ddr-power2.*
    :width: 1040
    :align: center
    :alt:

.. figure:: images/hardware-design/beagley-ai-soc-digital-power3.*
    :width: 1040
    :align: center
    :alt:


.. figure:: images/hardware-design/beagley-ai-reset-cntrls-mcu-osc.*
    :width: 1040
    :align: center
    :alt:

.. figure:: images/hardware-design/beagley-ai-rgmii-rst.*
    :width: 1040
    :align: center
    :alt:

.. figure:: images/hardware-design/beagley-ai-vdd-core-hcps.*
    :width: 1040
    :align: center
    :alt:

.. figure:: images/hardware-design/beagley-ai-wkup-reset-cntrls-osc.*
    :width: 1040
    :align: center
    :alt:


Boot modes
***********

.. figure:: images/hardware-design/beagley-ai-boot-modes.*
    :width: 1040
    :align: center
    :alt:


Power sources
***************

.. figure:: images/hardware-design/beagley-ai-vsys-3v3.*
    :width: 1040
    :align: center
    :alt:

.. figure:: images/hardware-design/beagley-ai-3v3-2v5-to-1v1-ldo.*
    :width: 1040
    :align: center
    :alt:

PMIC
*****

.. figure:: images/hardware-design/beagley-ai-pmic-nvm-programming.*
    :width: 1040
    :align: center
    :alt:

.. figure:: images/hardware-design/beagley-ai-pmic.*
    :width: 1040
    :align: center
    :alt:


General connectivity and expansion
************************************

.. figure:: images/hardware-design/beagley-ai-user-expansion-connector.*
    :width: 1040
    :align: center
    :alt:

.. figure:: images/hardware-design/beagley-ai-rpi-csi.*
    :width: 1040
    :align: center
    :alt:

.. figure:: images/hardware-design/beagley-ai-rpi-dsi-csi.*
    :width: 1040
    :align: center
    :alt:


.. figure:: images/hardware-design/beagley-ai-dual-usb-1.*
    :width: 1040
    :align: center
    :alt:

.. figure:: images/hardware-design/beagley-ai-dual-usb-2.*
    :width: 1040
    :align: center
    :alt:

.. figure:: images/hardware-design/beagley-ai-dual-usb-current-limiter.*
    :width: 1040
    :align: center
    :alt:


.. figure:: images/hardware-design/beagley-ai-fan-connector.*
    :width: 1040
    :align: center
    :alt:

.. figure:: images/hardware-design/beagley-ai-general-io.*
    :width: 1040
    :align: center
    :alt:

.. figure:: images/hardware-design/beagley-ai-mcu-general-io.*
    :width: 1040
    :align: center
    :alt:


.. figure:: images/hardware-design/beagley-ai-usb3-hub.*
    :width: 1040
    :align: center
    :alt:

.. figure:: images/hardware-design/beagley-ai-usb-c.*
    :width: 1040
    :align: center
    :alt:

.. figure:: images/hardware-design/beagley-ai-usb-hub-config.*
    :width: 1040
    :align: center
    :alt:

.. figure:: images/hardware-design/beagley-ai-usb-vbus-resistor-divider-circuit.*
    :width: 1040
    :align: center
    :alt:


.. figure:: images/hardware-design/beagley-ai-i2c2-pu.*
    :width: 1040
    :align: center
    :alt:

.. figure:: images/hardware-design/beagley-ai-iic-ext-rtc.*
    :width: 1040
    :align: center
    :alt:

.. figure:: images/hardware-design/beagley-ai-iic-voltage-level-translator.*
    :width: 1040
    :align: center
    :alt:


Buttons and LEDs
*****************

.. figure:: images/hardware-design/beagley-ai-leds.*
    :width: 1040
    :align: center
    :alt:

Networking
************

.. figure:: images/hardware-design/beagley-ai-wifi-module.*
    :width: 1040
    :align: center
    :alt:


Ethernet
*********

.. figure:: images/hardware-design/beagley-ai-ethernet-connector.*
    :width: 1040
    :align: center
    :alt:

.. figure:: images/hardware-design/beagley-ai-ethernet-dp83867.*
    :width: 1040
    :align: center
    :alt:

.. figure:: images/hardware-design/beagley-ai-ethernet-phy-caps.*
    :width: 1040
    :align: center
    :alt:

.. figure:: images/hardware-design/beagley-ai-ethernet-phy-misc.*
    :width: 1040
    :align: center
    :alt:

.. figure:: images/hardware-design/beagley-ai-ethernet-phy-protection.*
    :width: 1040
    :align: center
    :alt:

.. figure:: images/hardware-design/beagley-ai-ethernet-power-3v3-to-2v5.*
    :width: 1040
    :align: center
    :alt:

.. figure:: images/hardware-design/beagley-ai-poe-header.*
    :width: 1040
    :align: center
    :alt:



Memory, media, and storage
****************************

.. figure:: images/hardware-design/beagley-ai-board-id-eeprom.*
    :width: 1040
    :align: center
    :alt:

.. figure:: images/hardware-design/beagley-ai-ddr-caps.*
    :width: 1040
    :align: center
    :alt:

.. figure:: images/hardware-design/beagley-ai-ddr.*
    :width: 1040
    :align: center
    :alt:

.. figure:: images/hardware-design/beagley-ai-ddr-power.*
    :width: 1040
    :align: center
    :alt:

.. figure:: images/hardware-design/beagley-ai-micro-sd-card-interface.*
    :width: 1040
    :align: center
    :alt:

.. figure:: images/hardware-design/beagley-ai-pcie-connector.*
    :width: 1040
    :align: center
    :alt:

Multimedia I/O
***************

.. figure:: images/hardware-design/beagley-ai-hdmi-addr-protection.*
    :width: 1040
    :align: center
    :alt:

.. figure:: images/hardware-design/beagley-ai-hdmi-power.*
    :width: 1040
    :align: center
    :alt:

.. figure:: images/hardware-design/beagley-ai-hdmi-reset.*
    :width: 1040
    :align: center
    :alt:

.. figure:: images/hardware-design/beagley-ai-rgb888-to-hdmi.*
    :width: 1040
    :align: center
    :alt:


Debug ports
************

.. figure:: images/hardware-design/beagley-ai-tag-connect.*
    :width: 1040
    :align: center
    :alt:

.. figure:: images/hardware-design/beagley-ai-debug-uart-port.*
    :width: 1040
    :align: center
    :alt: 

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