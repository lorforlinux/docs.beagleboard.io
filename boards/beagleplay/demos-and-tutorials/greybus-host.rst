.. _greybus-host:

BeagleConnect™ Greybus demo using BeagleConnect™ Freedom and BeaglePlay
#######################################################################

BeaglePlay CC1352 Firmware
**************************

Build
=====
#. Download and setup Zephyr for BeaglePlay

    .. code-block:: bash
        
        cd
        sudo apt update
        sudo apt install --no-install-recommends -y \
            gperf \
            ccache dfu-util \
            libsdl2-dev \
            libxml2-dev libxslt1-dev libssl-dev libjpeg62-turbo-dev libmagic1 \
            libtool-bin autoconf automake libusb-1.0-0-dev \
            python3-tk python3-virtualenv
        wget https://github.com/zephyrproject-rtos/sdk-ng/releases/download/v0.16.3/zephyr-sdk-0.16.3_linux-aarch64_minimal.tar.xz
        tar xf zephyr-sdk-0.16.3_linux-aarch64_minimal.tar.xz
        rm zephyr-sdk-0.16.3_linux-aarch64_minimal.tar.xz
        ./zephyr-sdk-0.16.3/setup.sh -t arm-zephyr-eabi -c
        west init -m https://git.beagleboard.org/beagleconnect/zephyr/zephyr --mr sdk-next zephyr-beagle-cc1352-sdk
        cd $HOME/zephyr-beagle-cc1352-sdk
        python3 -m virtualenv zephyr-beagle-cc1352-env
        echo "export ZEPHYR_TOOLCHAIN_VARIANT=zephyr" >> $HOME/zephyr-beagle-cc1352-sdk/zephyr-beagle-cc1352-env/bin/activate
        echo "export ZEPHYR_SDK_INSTALL_DIR=$HOME/zephyr-sdk-0.16.3" >> $HOME/zephyr-beagle-cc1352-sdk/zephyr-beagle-cc1352-env/bin/activate
        echo "export ZEPHYR_BASE=$HOME/zephyr-beagle-cc1352-sdk/zephyr" >> $HOME/zephyr-beagle-cc1352-sdk/zephyr-beagle-cc1352-env/bin/activate
        echo 'export PATH=$HOME/zephyr-beagle-cc1352-sdk/zephyr/scripts:$PATH' >> $HOME/zephyr-beagle-cc1352-sdk/zephyr-beagle-cc1352-env/bin/activate
        echo "export BOARD=beagleplay_cc1352" >> $HOME/zephyr-beagle-cc1352-sdk/zephyr-beagle-cc1352-env/bin/activate
        source $HOME/zephyr-beagle-cc1352-sdk/zephyr-beagle-cc1352-env/bin/activate
        west update
        west zephyr-export
        pip3 install -r zephyr/scripts/requirements-base.txt

#. Activate the Zephyr build environment

    If you exit and come back, you'll need to reactivate your Zephyr build environment.

    .. code-block:: bash
        
        source $HOME/zephyr-beagle-cc1352-sdk/zephyr-beagle-cc1352-env/bin/activate

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
        (zephyr-beagle-cc1352-env) debian@BeaglePlay:~$ ./zephyr-sdk-0.16.3/arm-zephyr-eabi/bin/arm-zephyr-eabi-gcc --version
        arm-zephyr-eabi-gcc (Zephyr SDK 0.16.3) 12.1.0
        Copyright (C) 2022 Free Software Foundation, Inc.
        This is free software; see the source for copying conditions.  There is NO
        warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

#. Clone CC1352 Firmware at top level: https://git.beagleboard.org/gsoc/greybus/cc1352-firmware

    .. code-block:: bash

        git clone https://git.beagleboard.org/gsoc/greybus/cc1352-firmware

#. Build the Firmware

    .. code-block:: bash

        west build -b beagleplay_cc1352 -p always cc1352-firmware

#. You can now find the built firmware at `build/zephyr/zephyr.bin`

Flash
=====
#. Ensure the `gb-beagleplay` driver isn't blocking the serial port.

    .. code-block:: bash

        debian@BeaglePlay:~$ echo "    fdtoverlays /overlays/k3-am625-beagleplay-bcfserial-no-firmware.dtbo" | sudo tee -a /boot/firmware/extlinux/extlinux.conf
        debian@BeaglePlay:~$ sudo shutdown -r now

    .. note::

        The default password is `temppwd`.

#. Flash Firmware

    .. code-block:: bash

        west flash -b beagleplay_cc1352

#. Ensure the `gb-beagleplay` driver is set to load.

    .. code-block:: bash

        sudo sed -e '/bcfserial-no-firmware/ s/^#*/#/' -i /boot/firmware/extlinux/extlinux.conf
        sudo shutdown -r now

Installing Kernel
*****************
.. note::
    Check if it possible to use bbb.io-kernel-6.6-k3.

Flashing BeagleConnect Freedom Greybus Firmware
***********************************************
#. Connect beagleconnect freedom to beagleplay
#. Build beagleconnect freedom firmware

.. code-block:: bash

    west build -b beagleconnect_freedom modules/greybus/samples/subsys/greybus/net/ -p -- -DOVERLAY_CONFIG=overlay-802154-subg.conf

#. Flash bcf

.. code-block:: bash

    west flash

Run Demo
*********
#. Connect beagleconnect.
#. See shell output using `tio`

    .. code-block:: bash
    
        tio /dev/ACM0

#. Press reset button on beagleconnect freedom.

#. Verify that greybus is working by checking the `tio` output. It should look as follows:

    .. code-block:: bash

        [00:00:00.000,976] <dbg> greybus_platform_bus: greybus_init: probed greybus: 0 major: 0 minor: 1
        [00:00:00.001,068] <dbg> greybus_platform_string: greybus_string_init: probed greybus string 4: hdc2010
        [00:00:00.001,129] <dbg> greybus_platform_string: greybus_string_init: probed greybus string 3: opt3001
        [00:00:00.001,190] <dbg> greybus_platform_string: greybus_string_init: probed greybus string 2: Greybus Service Sample Application
        [00:00:00.001,251] <dbg> greybus_platform_string: greybus_string_init: probed greybus string 1: Zephyr Project RTOS
        [00:00:00.001,251] <dbg> greybus_platform_interface: greybus_interface_init: probed greybus interface 0
        [00:00:00.001,281] <dbg> greybus_platform_bundle: greybus_bundle_init: probed greybus bundle 1: class: 10
        [00:00:00.001,312] <dbg> greybus_platform_bundle: greybus_bundle_init: probed greybus bundle 0: class: 0
        [00:00:00.001,342] <dbg> greybus_platform_control: greybus_control_init: probed cport 0: bundle: 0 protocol: 0
        [00:00:00.001,434] <dbg> greybus_platform: gb_add_cport_device_mapping: added mapping between cport 1 and device gpio@40022000
        [00:00:00.001,464] <dbg> greybus_platform_gpio_control: greybus_gpio_control_init: probed cport 1: bundle: 1 protocol: 2
        [00:00:00.001,556] <dbg> greybus_platform: gb_add_cport_device_mapping: added mapping between cport 2 and device sensor-switch
        [00:00:00.001,556] <dbg> greybus_platform_i2c_control: greybus_i2c_control_init: probed cport 2: bundle: 1 protocol: 3
        *** Booting Zephyr OS build bcf-sdk-0.2.1-3384-ge76584f824c8 ***
        [00:00:00.009,704] <dbg> greybus_service: greybus_service_init: Greybus initializing..
        [00:00:00.009,765] <dbg> greybus_manifest: identify_descriptor: cport_id = 0
        [00:00:00.009,796] <dbg> greybus_manifest: identify_descriptor: cport_id = 1
        [00:00:00.009,826] <dbg> greybus_manifest: identify_descriptor: cport_id = 2
        [00:00:00.009,857] <dbg> greybus_transport_tcpip: gb_transport_backend_init: Greybus TCP/IP Transport initializing..
        [00:00:00.010,101] <inf> greybus_transport_tcpip: CPort 0 mapped to TCP/IP port 4242
        [00:00:00.014,709] <inf> greybus_transport_tcpip: CPort 1 mapped to TCP/IP port 4243
        [00:00:00.014,953] <inf> greybus_transport_tcpip: CPort 2 mapped to TCP/IP port 4244
        [00:00:00.015,075] <inf> greybus_transport_tcpip: Greybus TCP/IP Transport initialized
        [00:00:00.015,136] <inf> greybus_manifest: Registering CONTROL greybus driver.
        [00:00:00.015,167] <dbg> greybus: _gb_register_driver: Registering Greybus driver on CP0
        [00:00:00.015,411] <inf> greybus_manifest: Registering GPIO greybus driver.
        [00:00:00.015,411] <dbg> greybus: _gb_register_driver: Registering Greybus driver on CP1
        [00:00:00.015,625] <inf> greybus_manifest: Registering I2C greybus driver.
        [00:00:00.015,625] <dbg> greybus: _gb_register_driver: Registering Greybus driver on CP2
        [00:00:00.015,777] <inf> greybus_service: Greybus is active
        uart:~$

#. Check if `gb-beagleplay` is loaded:

    .. code-block:: bash

        debian@BeaglePlay:~$ lsmod | grep gb-beagleplay

#. Check `iio_device` to verify that greybus node has been detected:

    .. code-block:: bash

        debian@BeaglePlay:~$ iio_device

