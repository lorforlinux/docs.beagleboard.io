.. _beagleplay-lpm-video:

Smart Energy efficient video doorbell
####################################

1. Intelligent Camera streaming and recording at  640x480 resolution and 30 FPS with power saving.
2. Detect user activity using an external button/sensor and configure it as a wake-up source
3. Camera should start streaming on wakeup event and pause on suspend thus saving power.

Give options to enable below functionalities:

- Live Camera feed to show visitor activity
- On-the-fly recording of live camera feed with a timeout to record visitor activity
- On-the-fly streaming of live camera feed to remote server for post processing/storage or display.

About Deep Sleep
################

Deep Sleep AKA Suspend-to-RAM is a low-power mode that allows an embedded
device to retain its state in RAM while the processor is turned off.
This can save a significant amount of power, especially in devices that are battery-powered.

The benefits of using deep sleep in embedded devices are faster wake-up time and
better efficiency.

Hardware Requirements
#####################

1. BeaglePlay board.
2. A smart camera sensor like TEVI-OV5640
3. Optionally, you can also make do with an USB camera
4. HDMI monitor/ cable
5. Ethernet cable and a laptop/ desktop with Ethernet port
6. A Grove PIR sensor or a Grove button

Software Requirements
#####################

First, make sure that you have the latest U-Boot which packages the right firmwares
to make deep sleep work on beagleplay. You will also need to use ti-linux-kernel for
basic suspend-to-RAM because the patches are yet to make it into upstream.

You can always use Robert Nelson's latest default debian images which should come with the
right uboot and kernel required.

On debian, you may also need to make sure you have gstreamer installed, refer to
https://gstreamer.freedesktop.org/documentation/installing/on-linux.html?gi-language=c
for further details on how to install gstreamer.

Devicetree changes
##################

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

If using the smart sensor like tevi-ov5640 then be sure to also apply the
k3-am625-beagleplay-csi2-tevi-ov5640.dtbo overlay.

Linux commands
##############

Once your hardware, software and devicetree changes are all set, and
you boot till linux prompt we can finally start with the final bit!

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

Resources
#########

1. https://software-dl.ti.com/processor-sdk-linux/esd/AM62X/09_02_01_09/exports/docs/linux/Foundational_Components/Kernel/Kernel_Drivers/Power_Management/pm_low_power_modes.html#deep-sleep
2. https://software-dl.ti.com/processor-sdk-linux/esd/AM62X/09_02_01_09/exports/docs/linux/Foundational_Components/Kernel/Kernel_Drivers/Camera/CSI2RX.html

