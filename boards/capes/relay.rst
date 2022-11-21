.. _bone-cape-relay:

BeagleBoard.org BeagleBone Relay Cape
#####################################

Relay Cape, as the name suggests, is a simple Cape with relays on it.
It contains four relays, each of which can be operated independently from the BeagleBone.

.. image:: images/BeagleBoneRelayCapeA2-400x274.png
   :align: center

* `Order page <https://beagleboard.org/capes#relay>`_
* `Schematic <https://git.beagleboard.org/beagleboard/capes/-/tree/master/beaglebone/Relay>`_

.. note:: 
    The following describes how to use the device tree overlay under development.
    The description may not be suitable for those using older firmware.

Installation
************

No special configuration is required. When you plug Cape into your BeagleBoard, 
it is automatically recognized by the Cape Universal function.

You can check to see if Relay Cape is recognized with the following command.

.. code-block::

    ls /proc/device-tree/chosen/overlay

A list of currently loaded device tree overlays is displayed here. 
If you see `BBORG_RELAY-00A2.kernel` in this list, it has been loaded correctly.

If it is not loaded correctly, you can also load it directly 
by adding the following to the U-Boot options 
(which can be reflected by changing /boot/uEnv.txt).

.. code-block::

    uboot_overlay_addr0=BBORG_RELAY-00A2.dtbo


Usage
******

.. code-block::

    ls /sys/class/leds

The directory "relay*" exists in the following directory.
The LEDs can be controlled by modifying the files in this directory.

.. code-block::

    echo 1 > relay1/brightness

This allows you to adjust the brightness; 
entering 1 for brightness turns it ON, and entering 0 for OFF.

The four relays can be changed individually 
by changing the number after "relay".

Currently, using sysfs in .c files, libgpiod/gpiod in .c files, and 
python3 files with the RelayCape work well!

* For instance, my current kernel: 5.10.100-ti-r37

* Another idea, my current image: BeagleBoard.org Debian Bullseye Minimal Image 2022-03-02

There are newer images and kernels if you want to update and there are older ones in case you
would like to go back in time to use older kernels and images for the RelayCape.

My current /boot/uEnv.txt file shows the below info:

.. code-block::

    #Docs: http://elinux.org/Beagleboard:U-boot_partitioning_layout_2.0

    uname_r=5.10.100-ti-r37
    #uuid=
    #dtb=

    ###U-Boot Overlays###
    ###Documentation: http://elinux.org/Beagleboard:BeagleBoneBlack_Debian#U-Boot_Overlays
    ###Master Enable
    enable_uboot_overlays=1
    ###
    ###Overide capes with eeprom
    #uboot_overlay_addr0=<file0>.dtbo
    #uboot_overlay_addr1=<file1>.dtbo
    #uboot_overlay_addr2=<file2>.dtbo
    #uboot_overlay_addr3=<file3>.dtbo
    ###
    ###Additional custom capes
    #uboot_overlay_addr4=<file4>.dtbo
    #uboot_overlay_addr5=<file5>.dtbo
    #uboot_overlay_addr6=<file6>.dtbo
    #uboot_overlay_addr7=<file7>.dtbo
    ###
    ###Custom Cape
    #dtb_overlay=<file8>.dtbo
    ###
    ###Disable auto loading of virtual capes (emmc/video/wireless/adc)
    #disable_uboot_overlay_emmc=1
    #disable_uboot_overlay_video=1
    #disable_uboot_overlay_audio=1
    #disable_uboot_overlay_wireless=1
    #disable_uboot_overlay_adc=1
    ###
    ###Cape Universal Enable
    enable_uboot_cape_universal=1
    ###
    ###Debug: disable uboot autoload of Cape
    #disable_uboot_overlay_addr0=1
    #disable_uboot_overlay_addr1=1
    #disable_uboot_overlay_addr2=1
    #disable_uboot_overlay_addr3=1
    ###
    ###U-Boot fdt tweaks... (60000 = 384KB)
    #uboot_fdt_buffer=0x60000
    ###U-Boot Overlays###

    console=ttyS0,115200n8
    cmdline=coherent_pool=1M net.ifnames=0 lpj=1990656 rng_core.default_quality=100 quiet

    #In the event of edid real failures, uncomment this next line:
    #cmdline=coherent_pool=1M net.ifnames=0 lpj=1990656 rng_core.default_quality=100 quiet video=HDMI-A-1:1024x768@60e

    #Use an overlayfs on top of a read-only root filesystem:
    #cmdline=coherent_pool=1M net.ifnames=0 lpj=1990656 rng_core.default_quality=100 quiet overlayroot=tmpfs

    ##enable Generic eMMC Flasher:
    #cmdline=init=/usr/sbin/init-beagle-flasher

And...my current udev rules that handle this specific RelayCape and 
GPIOs are listed below:

.. code-block::
    # The udev rule can be found here...
    # https://github.com/mvduin/overlay-utils/blob/master/BBORG_RELAY-00A2.dtsi

    SUBSYSTEM=="subsystem", KERNEL=="gpio", ACTION=="add", \
        RUN+="/bin/mkdir -p /dev/gpio"

    SUBSYSTEM=="gpio", ACTION=="add", TEST=="value", ATTR{label}!="sysfs", \
        RUN+="/bin/ln -sT '/sys/class/gpio/%k' /dev/gpio/%s{label}"

Now...even though my `enable_uboot_cape_universal=1` in /boot/uEnv.txt shows
that it is `NOT` commented out with a `#` symbol, I have a `/etc/udev/rules.d/84-dev-gpio.rules` file
that handles making the `/dev/gpio/relay-jp1` among other `/relay-jp*`

The official beagleboard.org .dts file for the RelayCape is listed below which is used by way of
`enable_uboot_cape_universal=1` without the `#` symbol in front meaning commented out. 

.. code-block::
    https://git.beagleboard.org/beagleboard/BeagleBoard-DeviceTrees/-/blob/v5.10.x-ti-unified/src/arm/overlays/BBORG_RELAY-00A2.dts

    // SPDX-License-Identifier: GPL-2.0-only
    /*
    * Copyright (C) 2015 Robert Nelson <robertcnelson@gmail.com>
    * Copyright (C) 2019 Amilcar Lucas <amilcar.lucas@iav.de>
    */

    /dts-v1/;
    /plugin/;

    &{/chosen} {
        overlays {
	        BBORG_RELAY-00A2.kernel = __TIMESTAMP__;
	    };
    };

    &ocp {
	    P9_41_pinmux { pinctrl-0 = <&P9_41_gpio_pin>;};
	    P9_42_pinmux { pinctrl-0 = <&P9_42_gpio_pin>;};
	    P9_30_pinmux { pinctrl-0 = <&P9_30_gpio_pin>;};
	    P9_27_pinmux { pinctrl-0 = <&P9_27_gpio_pin>;};
    };

    // relay1
    &bone_led_P9_41 {
        status = "okay";
        label = "relay1";
        default-state = "keep";
    };

    // relay2
    &bone_led_P9_42 {
	    status = "okay";
	    label = "relay2";
	    default-state = "keep";
    };

    // realy3
    &bone_led_P9_30 {
	    status = "okay";
	    label = "relay3";
	    default-state = "keep";
    };

    // realy4
    &bone_led_P9_27 {
	    status = "okay";
	    label = "relay4";
	    default-state = "keep";
    };

So...we have a .dts file, a couple of .dtsi files, and a couple of udev rules to use.

Because of my udev rule, `/etc/udev/rules.d/84-dev-gpio.rules`, I will have `/dev/gpio/*`
available for use and thus a way to handle file descriptors in source like in a C/C++ file.

For instance, here is a .C file for handling GPIO in `/dev/gpio/relay-jp3` on the RelayCape.

.. code-block::
    /*

    This is an example of programming GPIOs from C using the sysfs interface on
    a BeagleBone Black/BeagleBone Black Wireless or other am335x board with the RelayCape.

    We will toggle physical pin 3.16 or P9.30 or gpio108 (which is gpio3_16 and it is 32 * 3 + 12 = 108) on the
    RelayCape attached to the BBBW for a change in seconds and then exits on CTRL-C.

    The original source can be found here by Mr. Tranter: https://github.com/tranter/blogs/blob/master/gpio/part5/demo1.c

    Jeff Tranter <jtranter@ics.com>

    and...Seth. I changed the source a bit to fit the BBBW and RelayCape while using sysfs.

    */

    #include <errno.h>
    #include <fcntl.h>
    #include <stdio.h>
    #include <stdlib.h>
    #include <sys/stat.h>
    #include <sys/types.h>
    #include <unistd.h>

    int main()
    {

    // Export the desired pin by writing to /sys/class/gpio/export or in this case
    // `/dev/gpio/relay-jp3`

        int fd = open("/dev/gpio/relay-jp3/active_low", O_WRONLY);
        if (fd == -1) {
            perror("Unable to open /dev/gpio/relay-jp3/active_low");
            exit(1);
        }

    // Set the pin to be an output by writing "out" to /sys/class/gpio/gpio108/direction
    // In this case, it is /dev/gpio/relay-jp3/direction b/c of the .dtsi file and us
    // not utilizing the specific .kernel .dtbo files available from beagleboard.org.

        fd = open("/dev/gpio/relay-jp3/direction", O_WRONLY);
        if (fd == -1) {
            perror("Unable to open /dev/gpio/relay-jp3/direction");
            exit(1);
        }

        if (write(fd, "out", 3) != 3) {
            perror("Error writing to /dev/gpio/relay-jp3/direction");
            exit(1);
        }

        close(fd);

        fd = open("/dev/gpio/relay-jp3/value", O_WRONLY);
        if (fd == -1) {
            perror("Unable to open /dev/gpio/relay-jp3/value");
            exit(1);
        }

    // Toggle LED 50 ms on, 50ms off, 100 times (10 seconds)

        for (int i = 0; i < 100; i++) {
            if (write(fd, "1", 1) != 1) {
                perror("Error writing to /dev/gpio/relay-jp3/value");
                exit(1);
            }
            usleep(50000);

            if (write(fd, "0", 1) != 1) {
                perror("Error writing to /dev/gpio/relay-jp3/value");
                exit(1);
            }
            usleep(50000);
        }

        close(fd);

    // And exit
        return 0;
    }


    // This is from https://github.com/mvduin/overlay-utils/blob/master/BBORG_RELAY-00A2.dtsi
    // Run w/ make and then sudo make install if necessary?
    // That will build the preprocessor directives for use w/ this script for enabling the .dtsi...


    /*

    #include "bone/black.h"
    #include "gpio.h"

    // IMPORTANT: if you have cape-universal enabled (which is the default),
    // make sure your kernel version is one of the ones listed here or newer:
    //      https://pastebin.com/2w2XtJBP

    // disable conflicting cape-universal nodes.
    // note that P9.41 and P9.42 connect to two cpu pins each, which cape-universal
    // calls P9_41/P9_91 and P9_42/P9_92 respectively.
    USES_PIN( P9_41 );  // gpio 0.20 / relay jp1 (unused)
    USES_PIN( P9_91 );  // gpio 3.20 / relay jp1
    USES_PIN( P9_42 );  // gpio 0.07 / relay jp2 (unused)
    USES_PIN( P9_92 );  // gpio 3.18 / relay jp2
    USES_PIN( P9_30 );  // gpio 3.16 / relay jp3
    USES_PIN( P9_27 );  // gpio 3.19 / relay jp4


    // A udev rule along these lines is recommended, to create symlinks in /dev/gpio:
    //
    //      SUBSYSTEM=="subsystem", KERNEL=="gpio", ACTION=="add", \
    //              RUN+="/bin/mkdir -p /dev/gpio"
    //
    //      SUBSYSTEM=="gpio", ACTION=="add", TEST=="value", ATTR{label}!="sysfs", \
    //              RUN+="/bin/ln -sT '/sys/class/gpio/%k' /dev/gpio/%s{label}"

    / {
        relay-cape {
            compatible = "gpio-of-helper";

            pinctrl-names = "default";
            pinctrl-0 = <&relay_cape_pins>;

            relay-jp1 {
                gpio = <&gpio3 20 ACTIVE_HIGH>;  // P9_41b
                init-low;
            };

            relay-jp2 {
                gpio = <&gpio3 18 ACTIVE_HIGH>;  // P9_42b
                init-low;
            };

            relay-jp3 {
                gpio = <&gpio3 16 ACTIVE_HIGH>;  // P9_30
                init-low;
            };

            relay-jp4 {
                gpio = <&gpio3 19 ACTIVE_HIGH>;  // P9_27
                init-low;
            };
        };
    };

    &am33xx_pinmux {
        relay_cape_pins: relay-cape {
            pinctrl-single,pins = <
                PIN_NOPULL( P9_41a, 7 )  // gpio 0.20 / relay jp1 (unused)
                PIN_PULLDN( P9_41b, 7 )  // gpio 3.20 / relay jp1
                PIN_NOPULL( P9_42a, 7 )  // gpio 0.07 / relay jp2 (unused)
                PIN_PULLDN( P9_42b, 7 )  // gpio 3.18 / relay jp2
                PIN_PULLDN( P9_30,  7 )  // gpio 3.16 / relay jp3
                PIN_PULLDN( P9_27,  7 )  // gpio 3.19 / relay jp4
            >;
        };
    };

    */

Also...if you are looking to dive into the new interface, libgpiod-dev/gpiod, here is another form of
source that can toggle the same GPIO listed from the file descriptor.

.. code-block::

    /*
    Simple gpiod example of toggling a LED connected to a gpio line from
    the BeagleBone Black Wireless and RelayCape.
    Exits when CTRL-C is typed.
    */

    // Also, I want to mention help from #beagle on IRC w/ the repo. that is used.

    // This source can be found here: https://github.com/tranter/blogs/blob/master/gpio/part9/example.c
    // It has been changed by me, Seth, to handle the RelayCape and BBBW Linux based SiP...

    // kernel: 5.10.100-ti-r37
    // image : BeagleBoard.org Debian Bullseye Minimal Image 2022-03-02

    // #include <linux/gpio.h>
    #include <gpiod.h>
    #include <stdio.h>
    #include <unistd.h>

    int main(int argc, char **argv)
    {
        const char *chipname = "gpiochip3";
        struct gpiod_chip *chip;
        struct gpiod_line *lineLED;    
                                 // a LED or any load from relay-jp3
                                 // located at /dev/gpio/relay-jp3
                                 // This is one way to grant access

    int i, ret;

    // Open GPIO chip
    chip = gpiod_chip_open_by_name(chipname);
    if (!chip) {
        perror("Open chip failed\n");
        return 1;
    }

    // Open GPIO lines
    lineLED = gpiod_chip_get_line(chip, 16);
    if (!lineLED) {
        perror("Get line failed\n");
        return 1;
    }

    // Open LED lines for output
    ret = gpiod_line_request_output(lineLED, "relay-jp3", 0);
    if (ret < 0) {
        perror("Request line as output failed\n");
        return 1;
    }

    // Blink a LED
    i = 0;
    while (true) {
        ret = gpiod_line_set_value(lineLED, (i & 1) != 0);
        if (ret < 0) {
            perror("Set line output failed\n");
            return 1;
        }
        usleep(1000000);
        i++;
    }

    // Release lines and chip
    gpiod_line_release(lineLED);
    gpiod_chip_close(chip);
    return 0;
    }

There are a few examples on how to use the RelayCape and am335x supported BBBW/BBB SBC.