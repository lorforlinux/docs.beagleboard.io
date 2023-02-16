.. _accessories-power-supplies:

Power supplies
###############

All BeagleBone boards require different power supplies like BeagleBone Balack and other AM335X 
based boards will be fine with a 5VDC @ 1A  but, BeagleBone AI-64 requires aleast 5VDC @ 3A. You 
have to either supply the power via USB jack or a 2.1mm/2.5mm inner diameter and 5.5mm outer 
diameter (center positive) barrel jack.

.. note::
    The power supply is not supplied with the board.

.. table:: BeagleBone power supplies
    
    +----------------------------+-------------------+-------------+-------------------------------------------------------------+
    | Board                      | Connector         | Power       |  Tested accessories                                         |
    +============================+===================+=============+=============================================================+
    | BeagleBone Black           | 2.1mm Barrel Jack | 5V @ 2A     | - `Adafruit <http://www.adafruit.com/products/276>`_        |
    +----------------------------+                   |             | - `Sparkfun <https://www.sparkfun.com/products/8269?>`_     |
    | BeagleBone Black Wireless  |                   |             | - `Logic Supply <http://www.logicsupply.com/pw-5v2a/>`_     |
    +----------------------------+                   |             |                                                             |
    | Beaglebone xM              |                   |             |                                                             |
    +----------------------------+-------------------+-------------+-------------------------------------------------------------+
    | PocketBeagle               | microUSB          | 5V @ 2A     | - `AA10A-050A(M)-R <https://mou.sr/3XUPOL0>`_               |
    |                            |                   |             | - `AA10E-050A(M)-R <https://mou.sr/3jrA4zZ>`_               |
    +----------------------------+-------------------+-------------+-------------------------------------------------------------+
    | BeagleBone AI-64           | Type-C            | 5V @ 3A     | - `AA65M-59FKA-R <https://mou.sr/3Dz9P1E>`_                 |
    +----------------------------+                   |             |                                                             |
    | Beaglebone AI              |                   |             |                                                             |      
    +----------------------------+-------------------+-------------+-------------------------------------------------------------+
    | BeagleBone Green Gateway   | 2.1mm Barrel Jack | 12V @ 5A    | - `PSAC60M-120-R <https://mou.sr/3Rs657U>`_                 |
    +----------------------------+                   |             |                                                             |
    | Beaglebone Blue            |                   |             |                                                             |
    +----------------------------+-------------------+-------------+-------------------------------------------------------------+
    | BeagleBone X15             | 2.5mm Barrel Jack | 12V @ 5A    | - `TRG70A120-12E01-Level-V <https://mou.sr/3RvRBnl>`_       +
    +----------------------------+-------------------+-------------+-------------------------------------------------------------+

.. tip::
    Most modern day mobile phone chargers are capable of delivering enough current to power any BeagleBone. 
    You may try using that with suitable cable before buying any standalone power srource for your board.

If you plan to use capes or add your own circuitry, higher amperage may be required.
Make sure that you have a grounded connection. This can be the USB cable or the HDMI cable.
