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

Setup Zephyr development on BeaglePlay
*********************************************

#. Download and setup Zephyr for BeaglePlay

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
          python3-dev python3-pip python3-setuptools python3-tk python3-wheel
        wget https://github.com/zephyrproject-rtos/sdk-ng/releases/download/v0.15.1/zephyr-sdk-0.15.1_linux-aarch64_minimal.tar.gz
        tar xf zephyr-sdk-0.15.1_linux-aarch64_minimal.tar.gz
        ./zephyr-sdk-0.15.1/setup.sh -t arm-zephyr-eabi -c
        west init -m https://git.beagleboard.org/beagleplay/zephyr-beagle-cc1352 --mr sdk zephyr-beagle-cc1352-sdk
        cd $HOME/zephyr-beagle-cc1352-sdk
        west update
        west zephyr-export
        pip3 install -r zephyr/scripts/requirements-base.txt
        echo "export ZEPHYR_TOOLCHAIN_VARIANT=zephyr" >> $HOME/.bashrc
        echo "export ZEPHYR_SDK_INSTALL_DIR=$HOME/zephyr-sdk-0.15.1" >> $HOME/.bashrc
        echo "export ZEPHYR_BASE=$HOME/zephyr-beagle-cc1352-sdk/zephyr" >> $HOME/.bashrc
        echo "export PATH=$HOME/zephyr-beagle-cc1352-sdk/zephyr/scripts:$PATH" >> $HOME/.bashrc
        echo "export BOARD=beagleplay_cc1352" >> $HOME/.bashrc
        source $HOME/.bashrc

#. Verify Zephyr setup for BeaglePlay

   .. code-block:: shell-session

      debian@BeaglePlay:~$ cmake --version
      cmake version 3.22.1

      CMake suite maintained and supported by Kitware (kitware.com/cmake).
      debian@BeaglePlay:~$ python3 --version
      Python 3.9.2
      debian@BeaglePlay:~$ dtc --version
      Version: DTC 1.6.0
      debian@BeaglePlay:~$ west --version
      West version: v0.14.0
      debian@BeaglePlay:~$ ./zephyr-sdk-0.15.1/arm-zephyr-eabi/bin/arm-zephyr-eabi-gcc --version
      arm-zephyr-eabi-gcc (Zephyr SDK 0.15.1) 12.1.0
      Copyright (C) 2022 Free Software Foundation, Inc.
      This is free software; see the source for copying conditions.  There is NO
      warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.



    
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
