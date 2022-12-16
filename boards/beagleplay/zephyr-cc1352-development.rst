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

Further, BeaglePlay is a reasonable development platform for creating Zephyr-based
applications for :ref:`beagleconnect_freedom_home`. The same Zephyr development
environment setup here is also described for targeting applications on that board.

Install the latest software image for BeaglePlay
*************************************************

.. note::

    These instructions should be generic for BeaglePlay and other boards and only the
    specifics of which image was used to test these instructions need be included
    here moving forward and the detailed instructions can be referenced elsewhere.

Download and install the Debian Linux operating system image for BeaglePlay.

#. These instructions were validated with the BeagleBoard.org Debian image `am625x-emmc-flasher-debian-11.5-xfce-arm64-2022-12-14-10gb.img.xz** <https://rcn-ee.net/rootfs/debian-arm64-xfce/2022-12-14/am625x-emmc-flasher-debian-11.5-xfce-arm64-2022-12-14-10gb.img.xz>`_.

#. Load this image to a microSD card using a tool like Etcher.

#. Insert the microSD card into BeaglePlay.

#. Power BeaglePlay via the USB-C connector.

.. note::

   #TODO: describe how to know it is working

Log into BeaglePlay
*********************************

Please either plug in a keyboard, monitor and mouse or :code:`ssh` into the board. We can point
somewhere else for instructions on this. You can also point your web browser to the board to log
into the Visual Studio Code IDE environment.

.. note::

    *TODO* A big part of what is missing here is to put your BeaglePlay on the Internet such
    that we can download things in later steps. That has been initially brushed over.

Flash existing IEEE 802.15.4 radio bridge (WPANUSB) firmware
************************************************************

If you've recieved a board fresh from the factory, this is already done and not necessary, unless
you want to restore the contents back to the factory condition.

Background
==========

This `WPANUSB` application was originally developed for radio devices with a USB interface. The CC1352P7
does not have a USB device, so the application was modified to communicate over a UART serial interface.

For the :ref:`beagleconnect_freedom_home`, a USB-to-UART bridge device was used and the USB endpoints
were made compatible with the `WPANUSB linux driver <https://github.com/finikorg/wpanusb>`_ which we
`augmented <https://git.beagleboard.org/beagleconnect/linux/wpanusb/>`_ to support this board. To utilize
the existing `WPANUSB` Zephyr application and this Linxu driver, we chose to encode our UART traffic with
`HDLC <https://en.wikipedia.org/wiki/High-Level_Data_Link_Control>`_. This has the advantage of enabing a
serial console interface to the Zephyr shell while WPANUSB-specific traffic is directed to other
`USB endpoints <https://simple.wikipedia.org/wiki/USB#How_USB_works>`_.

For BeaglePlay, the USB-to-UART bridge is not used, but we largely kept the same `WPANUSB` application,
including the HDLC encoding.

.. note::
    Now you know why this WPAN bridge application is called `WPANUSB`, even though USB isn't used!

Steps
=====

#. Ensure the `bcfserial` driver isn't blocking the serial port.

#. Download and flash the `WPANUSB` Zephyr application firmware onto the CC1352P7 on BeaglePlay from
the `releases on git.beagleboard.org <https://git.beagleboard.org/beagleplay/cc1352/wpanusb/-/releases>`_.

.. code-block: shell-session
    debian@BeaglePlay:~$

Setup Zephyr development on BeaglePlay
*********************************************

#. Download and setup Zephyr for BeaglePlay

    .. note::

        Currently, https://git.beagleboard.org/beagleplay/zephyr-beagle-cc1352 isn't public, so you'll need
        to replace that with git@git.beagleboard.org:beagleplay/zephyr-beagle-cc1352

    .. note::

        Currently, the active branch is `patches-for-cc1352p7`, not `sdk`. I plan to make `sdk` a slightly
        cleaner version.

    .. code-block:: bash
        
        cd
        sudo apt update
        sudo apt install --no-install-recommends -y \
            beagleconnect beagleconnect-msp430 \
            git vim \
            xz-utils file wget \
            build-essential \
            cmake ninja-build gperf \
            ccache dfu-util device-tree-compiler \
            make libsdl2-dev \
            libxml2-dev libxslt-dev libssl-dev libjpeg62-turbo-dev libmagic1 \
            libtool-bin pkg-config autoconf automake libusb-1.0-0-dev \
            python3-dev python3-pip python3-setuptools python3-tk python3-wheel python3-serial
        wget https://github.com/zephyrproject-rtos/sdk-ng/releases/download/v0.15.1/zephyr-sdk-0.15.1_linux-aarch64_minimal.tar.gz
        tar xf zephyr-sdk-0.15.1_linux-aarch64_minimal.tar.gz
        ./zephyr-sdk-0.15.1/setup.sh -t arm-zephyr-eabi -c
        west init -m https://git.beagleboard.org/beagleplay/zephyr-beagle-cc1352 --mr sdk zephyr-beagle-cc1352-sdk
        cd $HOME/zephyr-beagle-cc1352-sdk
        python3 -m virtualenv zephyr-beagle-cc1352-env
        echo "export ZEPHYR_TOOLCHAIN_VARIANT=zephyr" >> $HOME/zephyr-beagle-cc1352-sdk/zephyr-beagle-cc1352-env/bin/activate
        echo "export ZEPHYR_SDK_INSTALL_DIR=$HOME/zephyr-sdk-0.15.1" >> $HOME/zephyr-beagle-cc1352-sdk/zephyr-beagle-cc1352-env/bin/activate
        echo "export ZEPHYR_BASE=$HOME/zephyr-beagle-cc1352-sdk/zephyr" >> $HOME/zephyr-beagle-cc1352-sdk/zephyr-beagle-cc1352-env/bin/activate
        echo "export PATH=$HOME/zephyr-beagle-cc1352-sdk/zephyr/scripts:$PATH" >> $HOME/zephyr-beagle-cc1352-sdk/zephyr-beagle-cc1352-env/bin/activate
        echo "export BOARD=beagleplay" >> $HOME/zephyr-beagle-cc1352-sdk/zephyr-beagle-cc1352-env/bin/activate
        source $HOME/zephyr-beagle-cc1352-sdk/zephyr-beagle-cc1352-env/bin/activate
        west update
        west zephyr-export
        pip3 install -r zephyr/scripts/requirements-base.txt

#. Verify Zephyr setup for BeaglePlay

.. code-block:: shell-session

    (zephyr-beagle-cc1352-env) debian@BeaglePlay:~$ cmake --version
    cmake version 3.22.1

    CMake suite maintained and supported by Kitware (kitware.com/cmake).
    (zephyr-beagle-cc1352-env) debian@BeaglePlay:~$ python3 --version
    Python 3.9.2
    (zephyr-beagle-cc1352-env) debian@BeaglePlay:~$ dtc --version
    Version: DTC 1.6.0
    (zephyr-beagle-cc1352-env) debian@BeaglePlay:~$ west --version
    West version: v0.14.0
    (zephyr-beagle-cc1352-env) debian@BeaglePlay:~$ ./zephyr-sdk-0.15.1/arm-zephyr-eabi/bin/arm-zephyr-eabi-gcc --version
    arm-zephyr-eabi-gcc (Zephyr SDK 0.15.1) 12.1.0
    Copyright (C) 2022 Free Software Foundation, Inc.
    This is free software; see the source for copying conditions.  There is NO
    warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

    
Build applications for BeaglePlay CC1352
*********************************************

Now you can build various Zephyr applications

.. note::

    Currently, https://git.beagleboard.org/beagleplay/micropython isn't public, so you'll need
    to replace that with git@git.beagleboard.org:beagleplay/micropython



#. Build and flash Blinky example

    .. code-block:: bash

        cd $HOME/zephyr-beagle-cc1352-sdk/zephyr
        west build -d build/play_blinky samples/basic/blinky
        west flash -d build/play_blinky

#. Try out Micropython

    .. code-block:: bash

        cd
        git clone -b beagleplay-cc1352 https://git.beagleboard.org/beagleplay/micropython
        cd micropython
        west build -d play ports/zephyr
        west flash -d play
        tio /dev/ttyS4

Build applications for BeagleConnect Freedom
*********************************************

#. Build and flash Blinky example

    .. code-block:: bash

        cd $HOME/zephyr-beagle-cc1352-sdk/zephyr
        west build -d build/freedom_blinky -b beagleconnect_freedom samples/basic/blinky
        west flash -d build/freedom_blinky

#. Try out Micropython

    .. code-block:: bash

        cd
        git clone -b beagleplay-cc1352 https://git.beagleboard.org/beagleplay/micropython
        cd micropython
        west build -d freedom -b beagleconnect_freedom ports/zephyr
        west flash -d freedom
        tio /dev/ttyACM0


.. important::

    Nothing below here is tested

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
