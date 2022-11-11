.. _beagleplay-zephyr-development:

BeaglePlay & Zephyr Development
###############################

BeaglePlay includes a `Texas Instruments CC1352P7 wireless microcontroller <https://www.ti.com/product/CC1352P7>`_
that can be programmed using the `Linux Foundation Zephyr RTOS <https://www.zephyrproject.org/>`_.

Developing directly in Zephyr will not be ultimately required for end-users 
who won't touch the firmware running on the CC1352 on BeaglePlay™ and will instead
use the provided wireless functionality. However, it is important for early 
adopters as well as people looking to extend the functionality of the open 
source design. If you are one of those people, this is a good place to get 
started.

Install the latest software image for BeaglePlay
*************************************************

Download and install the Debian Linux operating system image for BeaglePlay.

#. Download the BeagleBoard.org Debian image from 
   `here <https://`_. These instructions were validated with **TBD.img.xz**.

#. Load this image to a microSD card using a tool like Etcher.

#. Insert the microSD card into BeaglePlay.

#. Power BeaglePlay via the USB-C connector.

.. note::

   #TODO: describe how to know it is working

Log into BeaglePlay
*********************************

Please either plug in a keyboard, monitor and mouse or :code:`ssh` into the board. We can point
somewhere else for instructions on this.

Install Zephyr development tools on BeaglePlay
************************************************************

#. Download and setup Zephyr for BeagleConnect™
    .. code-block:: bash
        
        cd
        west init -m https://git.beagleboard.org/beagleplay/zephyr-beagle-cc1352 --mr sdk zephyr-beagle-cc1352-sdk
        cd $HOME/zephyr-beagle-cc1352-sdk
        west update
        west zephyr-export
        pip3 install -r zephyr/scripts/requirements-base.txt
        echo "export CROSS_COMPILE=/usr/bin/arm-none-eabi-" >> $HOME/.bashrc
        echo "export ZEPHYR_BASE=$HOME/zephyr-beagle-cc1352-sdk/zephyr" >> $HOME/.bashrc
        echo "export PATH=$HOME/zephyr-beagle-cc1352-sdk/zephyr/scripts:$PATH" >> $HOME/.bashrc
        echo "export BOARD=beagleplay_cc1352" >> $HOME/.bashrc
        source $HOME/.bashrc
    
Build applications for BeaglePlay CC1352
*********************************************

Now you can build various Zephyr applications

#. Change directory to BeagleConnect Freedom zephyr repository.

    .. code-block:: bash

        cd $HOME/bcf-zephyr
        
#. Build blinky example

    .. code-block:: bash

        west build -d build/blinky zephyr/samples/basic/blinky

#. TODO

    .. code-block:: bash

        west build -d build/sensortest zephyr/samples/boards/beagle_bcf/sensortest -- -DOVERLAY_CONFIG=overlay-subghz.conf

#. TODO

    .. code-block:: bash

        west build -d build/wpanusb modules/lib/wpanusb_bc -- -DOVERLAY_CONFIG=overlay-subghz.conf

#. TODO

    .. code-block:: bash

        west build -d build/bcfserial modules/lib/wpanusb_bc -- -DOVERLAY_CONFIG=overlay-bcfserial.conf -DDTC_OVERLAY_FILE=bcfserial.overlay

#. TODO

    .. code-block:: bash

        west build -d build/greybus modules/lib/greybus/samples/subsys/greybus/net -- -DOVERLAY_CONFIG=overlay-802154-subg.conf


Flash applications to BeagleConnect Freedom from BeagleBone Green Gateway
=========================================================================

And then you can flash the BeagleConnect Freedom boards over USB

#. Make sure you are in Zephyr directory
    .. code-block:: bash

        cd $HOME/bcf-zephyr

#. Flash Blinky
    .. code-block:: bash

        cc2538-bsl.py build/blinky

Debug applications over the serial terminal
===========================================

#TODO#
