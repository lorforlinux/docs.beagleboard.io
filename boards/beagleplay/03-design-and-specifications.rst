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

