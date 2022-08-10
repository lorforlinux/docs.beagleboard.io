.. _bone-cape-basics:

Basics
#######

BeagleBone has sold a module called Cape, which connects to the BeagleBoard and the PocketBeagle. 

Using Cape, you can easily add sensors, communication peripherals, etc. with ease.

Please see below for Cape available to date.

`BeagleBoard.org - Cape <https://beagleboard.org/capes>`_

Features
=============

For example, BeagleBoard has various variants such as Black, Green, and AI.
The device tree overlay feature allows BeagleBone capes 
to be identical across these different pieces of hardware.

Each hardware has different internal pin assignments 
and the number of peripherals in the SoC, but the device tree overlay absorbs these differences.

The user of Cape are essentially able to use it 
across the corresponding Boards without changing any code at all.