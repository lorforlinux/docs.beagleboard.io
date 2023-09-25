.. _beaglev-fire-introduction:

Introduction
#############

BeagleV®-Fire is a revolutionary SBC powered by the Microchip's PolarFire® MPFS025T FCVG484E 5x core RISC-V System on Chip 
(SoC) with FPGA fabric. BeagleV®-Fire opens up new horizons for developers, tinkerers, and the open-source community to explore the vast potential 
of RISC-V architecture and FPGA technology. It has the same P8 & P9 cape header pins as BeagleBone Black allowing you to stack your favourite BeagleBone 
cape on top to expand it's capability. Built around the powerful and energy-efficient RISC-V instruction set architecture (ISA) along with its versatile FPGA fabric, 
BeagleV®-Fire SBC offers unparalleled opportunities for developers, hobbyists, and researchers to explore and experiment with RISC-V technology.

.. table::
   :align: center
   :widths: auto

   +----------------------------------------------------+---------------------------------------------------------+
   | .. image:: media/product-pictures/front.*          | .. image:: media/product-pictures/back.*                |
   |    :width: 700                                     |       :width: 700                                       |
   |    :align: center                                  |       :align: center                                    |
   |    :alt: BeagleV Fire front                        |       :alt: BeagleV Fire back                           |
   +----------------------------------------------------+---------------------------------------------------------+

Pinout Diagrams
***************

Choose the cape header to see respective pinout diagram.

.. tabs::

   .. group-tab:: P8 cape header

        .. figure:: media/pinout/BeagleV-Fire-P8.*
            :align: center
            :alt: BeagleV Fire P8 cape header pinout

            BeagleV Fire P8 cape header pinout


   .. group-tab:: P9 cape header

        .. figure:: media/pinout/BeagleV-Fire-P9.*
            :align: center
            :alt: BeagleV Fire P9 cape header pinout

            BeagleV Fire P9 cape header pinout

.. _beaglev-fire-detaild-overview:

Detailed overview
******************

.. table:: BeagleV Fire features
        
    +----------------------------+---------------------------------------------------------------------------+
    | Feature                    | Description                                                               |
    +============================+===========================================================================+
    | Processor                  | MPFS025T-FCVG484E                                                         |
    +----------------------------+---------------------------------------------------------------------------+
    | Memory                     | 2GB (1Gb x 16)- 1866MHz 3733Mbps, LPDDR4                                  |
    +----------------------------+---------------------------------------------------------------------------+
    | Storage                    | Kingston 16GB eMMC                                                        |
    +----------------------------+---------------------------------------------------------------------------+
    | Wireless                   | 1x M.2 Key E, support 2.4GHz/5GHz WiFi module                             |
    +----------------------------+---------------------------------------------------------------------------+
    | Ethernet                   | - PHY: Realtek RTL8211F-VD-CG Gigabit Ethernet phy                        |
    |                            | - Connector: integrated magnetics RJ-45                                   |
    +----------------------------+---------------------------------------------------------------------------+
    | USB C                      | - Connectivity: Flash/programming support                                 |
    |                            | - Power: Input: 5V @ <To-Do>                                              |
    +----------------------------+---------------------------------------------------------------------------+
    | Other connectors           | - 1x SYZYGY High speed connector                                          |
    |                            | - microSD card slot                                                       |
    |                            | - CSI connector compatible with BeagleBone AI-64, BeagleV-Ahead Raspberry |
    |                            |   Pi Zero / CM4 (22-pin)                                                  |
    +----------------------------+---------------------------------------------------------------------------+

Board components location
==========================

This section describes the key components on the board, their location and function.

Front components location
-------------------------

.. figure:: media/BeagleV-Fire-Front-Annotated.*
    :width: 1400
    :align: center
    :alt: BeagleV Fire board front components location
    
    BeagleV Fire board front components location


.. todo:: add front components table.


Back components location
-------------------------

.. figure:: media/BeagleV-Fire-Back-Annotated.*
    :width: 1400
    :align: center
    :alt: BeagleV Fire board back components location

    BeagleV Fire board back components location


.. todo:: add back components table.