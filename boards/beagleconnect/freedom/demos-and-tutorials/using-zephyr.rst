.. _beagleconnect-freedom-using-zephyr:

Using Zephyr
############

Developing directly in Zephyr will not be ultimately required for end-users 
who won't touch the firmware running on BeagleConnect™ Freedom and will instead
use the BeagleConnect™ Greybus functionality, but is important for early 
adopters as well as people looking to extend the functionality of the open 
source design. If you are one of those people, this is a good place to get 
started.

Equipment to begin development
******************************

There are many options, but using BeaglePlay gives a reasonable common
environment. Please adjust as you see fit.

Required
========

* BeaglePlay

* BeagleConnect Freedom

* 2x 5V/3A USB power adapters

Recommended
===============

* Ethernet cable and Internet connection

Install the SDK on BeaglePlay
*****************************

See :ref:`beagleplay-zephyr-development-setup`_.

.. important::

   #TODO: note the tested version of software for BeaglePlay
   
   #TODO: describe how to know it is working

Change default board
====================

The instructions linked above setup the environment for targeting BeaglePlay's on CC1352. We need to change
it to target BeagleConnec Freedom.

    .. code-block:: bash

        echo "export BOARD=beagleconnect_freedom" >> $HOME/zephyr-beagle-cc1352-sdk/zephyr-beagle-cc1352-env/bin/activate
        source $HOME/zephyr-beagle-cc1352-sdk/zephyr-beagle-cc1352-env/bin/activate


Try demo applications
*********************

Now you can build various Zephyr applications

Build and flash Blinky
======================

Make sure your BeagleConnect Freedom is connected to your BeaglePlay via the USB cable provided.

    .. code-block:: bash

        cd $ZEPHYR_BASE
        west build zephyr/samples/basic/blinky
        west flash

Debug applications over the serial terminal
===========================================

.. note::

   #TODO#
