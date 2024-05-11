.. _beagleplay-demo-lpm-video:

Smart energy efficient video doorbell
#####################################

1. Intelligent camera streaming and recording at 640x480 resolution and 30 FPS with power saving.
2. Detect user activity using an external button/sensor and configure it as a wake-up source
3. Camera should start streaming on wakeup event and pause on suspend thus saving power.

Give options to enable below functionalities:

- Live Camera feed to show visitor activity
- On-the-fly recording of live camera feed with a timeout to record visitor activity
- On-the-fly streaming of live camera feed to remote server for post processing/storage or display.

About deep sleep
******************

Deep Sleep AKA Suspend-to-RAM is a low-power mode that allows an embedded
device to retain its state in RAM while the processor is turned off.
This can save a significant amount of power, especially in devices that are battery-powered.

The benefits of using deep sleep in embedded devices are faster wake-up time and
better efficiency.

.. tip:: Checkout `kernel docs on power states <https://www.kernel.org/doc/Documentation/power/states.txt>`_

.. youtube:: 4jbOXl_o4uo
	:width: 100%
	:align: center

Hardware requirements
**********************

1. `BeaglePlay board <https://www.beagleboard.org/boards/beagleplay>`_
2. A CSI MIPI camera like `TEVI-OV5640 <https://www.technexion.com/products/embedded-vision/image-sensors/tevi-ov5640/>`_ or a USB web-cam
3. HDMI monitor & HDMI cable
4. Ethernet cable and a laptop/desktop with an Ethernet port
5. `A Grove PIR sensor <https://wiki.seeedstudio.com/Grove-PIR_Motion_Sensor/>`_ or a Grove button

Software requirements
*********************

First, make sure that you have the latest U-Boot which packages the right firmwares
to make deep sleep work on beagleplay. You will also need to use ti-linux-kernel for
basic suspend-to-RAM because the patches are yet to make it into upstream.

You can always use Robert Nelson's latest default debian images which should come with the
right uboot and kernel required.

On debian, you may also need to make sure you have gstreamer installed, refer to
https://gstreamer.freedesktop.org/documentation/installing/on-linux.html?gi-language=c
for further details on how to install gstreamer.

Devicetree changes
*******************

You will need to tell Linux what your wakeup source is going to be, it can be a simple button
or even a  PIR sensor. To do this you'll need to make the following changes to the
k3-am625-beagleplay.dts:

.. code:: diff

	diff --git a/arch/arm64/boot/dts/ti/k3-am625-beagleplay.dts b/arch/arm64/boot/dts/ti/k3-am625-beagleplay.dts
	index b3328ae24b5f..9a83102e3604 100644
	--- a/arch/arm64/boot/dts/ti/k3-am625-beagleplay.dts
	+++ b/arch/arm64/boot/dts/ti/k3-am625-beagleplay.dts
	@@ -166,6 +166,20 @@ vdd_sd_dv: regulator-5 {
				 <3300000 0x1>;
		};

	+	motion_gpio_key {
	+		compatible = "gpio-keys";
	+		autorepeat;
	+		pinctrl-names = "default";
	+		pinctrl-0 = <&grove_pins_default>;
	+		switch {
	+			label = "senseGPIO";
	+			linux,code = <KEY_WAKEUP>;
	+			interrupts-extended = <&main_gpio1 28 IRQ_TYPE_EDGE_RISING>,
	+				<&main_pmx0 0x1e8>;
	+			interrupt-names = "irq", "wakeup";
	+		};
	+	};
	+
		leds {
			compatible = "gpio-leds";

The above will help us configure the grove connector's GPIO to act as a
wakeup source from Deep Sleep.

If using the CSI MIPI camera like tevi-ov5640 then, be sure to also apply the respective overlay, 
for tevi-ov5640 apply ``k3-am625-beagleplay-csi2-tevi-ov5640.dtbo`` overlay.

The Technexion TEVI-OV5640 module supports Suspend-to-RAM but may fail to set the sensor registers
in time when built as a module. You can fix this by making it a part of the kernel image:
Find further details in the `TI-SDK Documentation <https://software-dl.ti.com/processor-sdk-linux/esd/AM62X/09_01_00_08/exports/docs/linux/Foundational_Components/Kernel/Kernel_Drivers/Camera/CSI2RX.html#suspend-to-ram>`_

.. todo:: Add the below changes to the beagle defconfig

.. code:: diff

	diff --git a/arch/arm64/configs/defconfig b/arch/arm64/configs/defconfig
	index 1f402994efed..0f081e5f96c1 100644
	--- a/arch/arm64/configs/defconfig
	+++ b/arch/arm64/configs/defconfig
	@@ -739,14 +739,14 @@ CONFIG_RC_DECODERS=y
	 CONFIG_RC_DEVICES=y
	 CONFIG_IR_MESON=m
	 CONFIG_IR_SUNXI=m
	-CONFIG_MEDIA_SUPPORT=m
	+CONFIG_MEDIA_SUPPORT=y
	 # CONFIG_DVB_NET is not set
	 CONFIG_MEDIA_USB_SUPPORT=y
	 CONFIG_USB_VIDEO_CLASS=m
	 CONFIG_V4L_PLATFORM_DRIVERS=y
	 CONFIG_SDR_PLATFORM_DRIVERS=y
	 CONFIG_V4L_MEM2MEM_DRIVERS=y
	-CONFIG_VIDEO_CADENCE_CSI2RX=m
	+CONFIG_VIDEO_CADENCE_CSI2RX=y
	 CONFIG_VIDEO_WAVE_VPU=m
	 CONFIG_VIDEO_IMG_VXD_DEC=m
	 CONFIG_VIDEO_IMG_VXE_ENC=m
	@@ -764,12 +764,12 @@ CONFIG_VIDEO_SAMSUNG_EXYNOS_GSC=m
	 CONFIG_VIDEO_SAMSUNG_S5P_JPEG=m
	 CONFIG_VIDEO_SAMSUNG_S5P_MFC=m
	 CONFIG_VIDEO_SUN6I_CSI=m
	-CONFIG_VIDEO_TI_J721E_CSI2RX=m
	+CONFIG_VIDEO_TI_J721E_CSI2RX=y
	 CONFIG_VIDEO_HANTRO=m
	 CONFIG_VIDEO_IMX219=m
	 CONFIG_VIDEO_IMX390=m
	 CONFIG_VIDEO_OV2312=m
	-CONFIG_VIDEO_OV5640=m
	+CONFIG_VIDEO_OV5640=y
	 CONFIG_VIDEO_OV5645=m
	 CONFIG_VIDEO_DS90UB953=m
	 CONFIG_VIDEO_DS90UB960=m
	@@ -1309,8 +1309,8 @@ CONFIG_PHY_XGENE=y
	 CONFIG_PHY_CAN_TRANSCEIVER=m
	 CONFIG_PHY_SUN4I_USB=y
	 CONFIG_PHY_CADENCE_TORRENT=y
	-CONFIG_PHY_CADENCE_DPHY=m
	-CONFIG_PHY_CADENCE_DPHY_RX=m
	+CONFIG_PHY_CADENCE_DPHY=y
	+CONFIG_PHY_CADENCE_DPHY_RX=y
	 CONFIG_PHY_CADENCE_SIERRA=y
	 CONFIG_PHY_MIXEL_MIPI_DPHY=m
	 CONFIG_PHY_FSL_IMX8M_PCIE=y

Linux commands
***************

Once your hardware, software and devicetree changes are all set, and
you boot till linux prompt we can finally start with the final bit!

.. todo:: Add more information on how each gst command is working.

1. Run the following gst pipeline:

.. code:: console

	gst-launch-1.0 -v v4l2src io-mode=dmabuf device="/dev/video0" ! video/x-raw, width=640, height=480, format=YUY2 ! queue ! tee name=t t. ! queue ! kmssink driver-name=tidss force-modesetting=true sync=false async=false t. ! queue ! ticolorconvert ! queue ! x264enc speed-preset=superfast  key-int-max=30 tune=zerolatency bitrate=25000 ! queue ! rtph264pay config-interval=30 ! udpsink sync=false port=5000 host=192.168.0.2 async=false &

If you also want to record the video:

.. code:: console

	gst-launch-1.0 -v v4l2src io-mode=dmabuf device="/dev/video0" ! video/x-raw, width=640, height=480, format=YUY2 ! queue ! tee name=t t. ! queue ! kmssink driver-name=tidss force-modesetting=true sync=false async=false t. ! queue ! ticolorconvert ! x264enc speed-preset=superfast key-int-max=60 bitrate=5000 ! queue ! tee name=t1 t1. ! queue ! rtph264pay config-interval=60 ! udpsink port=5000 host=192.168.0.2 sync=false async=false t1. ! queue ! filesink location="op.h264"


2. Let that process run in the background and then to suspend the device:

.. code:: console

	echo mem > /sys/power/state

3. Then, if you press the button/ trigger PIR sensor with some movement it should
   bring the device back up and you will see the video resume almost instantly!

4. Additionally, you can enable auto suspend for the device by using a simple systemd service. Follow the `guide here <https://tecadmin.net/run-shell-script-as-systemd-service/>`_
   to see how to create and enable a script as a systemd service. The script that I used was as follows:

.. code:: console

        #!/bin/bash

        while true
        do
         sleep 15       # Adjust this time to whatever delay you prefer the device stays on after resume
         echo "Entering Suspend to RAM..."
         echo mem > /sys/power/state
        done

Resources
**********

1. https://software-dl.ti.com/processor-sdk-linux/esd/AM62X/09_02_01_09/exports/docs/linux/Foundational_Components/Kernel/Kernel_Drivers/Power_Management/pm_low_power_modes.html#deep-sleep
2. https://software-dl.ti.com/processor-sdk-linux/esd/AM62X/09_02_01_09/exports/docs/linux/Foundational_Components/Kernel/Kernel_Drivers/Camera/CSI2RX.html

