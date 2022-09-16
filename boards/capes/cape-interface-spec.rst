.. _beaglebone-cape-interface-spec:

BeagleBone cape interface spec
###############################

.. |I2C| replace:: I\ :sup:`2`\ C

This page is a fork of `BeagleBone cape interface spec <https://elinux.org/Beagleboard:BeagleBone_cape_interface_spec>`_ page on elinux. This is the new official home.

Background and overview
***********************

.. important::

   Resources 
   
   * See `Device Tree: Supporting Similar Boards - The BeagleBone Example blog post <https://beagleboard.org/blog/2022-03-31-device-tree-supporting-similar-boards-the-beaglebone-example>`_ on BeagleBoard.org
   * See `spreadsheet with pin header details <https://docs.google.com/spreadsheets/d/1fE-AsDZvJ-bBwzNBj1_sPDrutvEvsmARqFwvbw_HkrE/edit?usp=sharing>`_ 
   * See `elinux.org Cape Expansion Headers for BeagleBone page <https://elinux.org/Beagleboard:Cape_Expansion_Headers>`_
   * See :ref:`BeagleBone Black System Reference Manual Connectors section <beagleboneblack-connectors>`
   * See :ref:`BeagleBone AI System Reference Manual Connectors section <beaglebone-ai-connectors>`
   * See :ref:`BeagleBone AI-64 System Reference Manual Connectors section <TODO>`

.. note:: Below, when mentioning "Black", this is true for all AM3358-based BeagleBone boards. "AI" is AM5729-based. "AI-64" is TDA4VM-based.

The device tree symbols for the BeagleBone Cape Compatibility Layer are provided in `BeagleBoard-DeviceTrees <https://git.beagleboard.org/beagleboard/BeagleBoard-DeviceTrees>`_ at:

* Black: `bbb-bone-buses.dtsi <https://git.beagleboard.org/beagleboard/BeagleBoard-DeviceTrees/-/blob/v5.10.x-ti-unified/src/arm/bbb-bone-buses.dtsi>`_
* AI: `bbai-bone-buses.dtsi <https://git.beagleboard.org/beagleboard/BeagleBoard-DeviceTrees/-/blob/v5.10.x-ti-unified/src/arm/bbai-bone-buses.dtsi>`_
* AI-64: `k3-j721e-beagleboneai-64-bone-buses.dtsi <https://git.beagleboard.org/beagleboard/BeagleBoard-DeviceTrees/-/blob/v5.10.x-ti-unified/src/arm64/k3-j721e-beagleboneai64-bone-buses.dtsi>`_

The udev rules used to create the userspace symlinks for the BeagleBone Cape Compatibility Layer are provided in `usr-customizations <https://git.beagleboard.org/beagleboard/usr-customizations>`_ at:

More details can be found in :ref:`bone-methodology`.

.. table:: Overall

	+-----------------------------------------------+-----+--------------------------------------+
	| .. centered:: P9                              |     |    .. centered:: P8                  |
	+===============+=====+======+==================+=====+============+=====+======+============+
	|   Functions   | odd | even |    Functions     |     | Functions  | odd | even | Functions  |
	+---------------+-----+------+------------------+-----+------------+-----+------+------------+
	| USB D+        | E1  | E2   | USB D-           |     |            |     |      |            |
	+---------------+-----+------+------------------+-----+------------+-----+------+------------+
	| 5V OUT        | E3  | E4   | GND              |     |            |     |      |            |
	+---------------+-----+------+------------------+-----+------------+-----+------+------------+
	| GND           | 1   | 2    | GND              |     | GND        | 1   | 2    | GND        |
	+---------------+-----+------+------------------+-----+------------+-----+------+------------+
	| 3V3 OUT       | 3   | 4    | 3V3 OUT          |     | D M        | 3   | 4    | D M        |
	+---------------+-----+------+------------------+-----+------------+-----+------+------------+
	| 5V IN         | 5   | 6    | 5V IN            |     | D M C4t    | 5   | 6    | D M C4r    |
	+---------------+-----+------+------------------+-----+------------+-----+------+------------+
	| 5V OUT        | 7   | 8    | 5V OUT           |     | D C2r      | 7   | 8    | D C2t      |
	+---------------+-----+------+------------------+-----+------------+-----+------+------------+
	| PWR BUT       | 9   | 10   | RESET            |     | D C3r      | 9   | 10   | D C3t      |
	+---------------+-----+------+------------------+-----+------------+-----+------+------------+
	| D U4r         | 11  | 12   | D                |     | D P0o      | 11  | 12   | D Q2a P0o  |
	+---------------+-----+------+------------------+-----+------------+-----+------+------------+
	| D U4t         | 13  | 14   | D E1a            |     | D E2b      | 13  | 14   | D          |
	+---------------+-----+------+------------------+-----+------------+-----+------+------------+
	| D             | 15  | 16   | D E1b            |     | D P0i      | 15  | 16   | D P0i      |
	+---------------+-----+------+------------------+-----+------------+-----+------+------------+
	| D I1c S00     | 17  | 18   | D I1d S0o        |     | D          | 17  | 18   | D          |
	+---------------+-----+------+------------------+-----+------------+-----+------+------------+
	| C0r D I2c     | 19  | 20   | C0t D I2d        |     | D E2a      | 19  | 20   | D M P1     |
	+---------------+-----+------+------------------+-----+------------+-----+------+------------+
	| D E0b S0i U2t | 21  | 22   | D E0a S0c U2r    |     | D M P1     | 21  | 22   | D M Q2b    |
	+---------------+-----+------+------------------+-----+------------+-----+------+------------+
	| D S01         | 23  | 24   | C1r D I3c U1t    |     | D M        | 23  | 24   | D M        |
	+---------------+-----+------+------------------+-----+------------+-----+------+------------+
	| D P0          | 25  | 26   | C1t D I3d U1r    |     | D M        | 25  | 26   | D          |
	+---------------+-----+------+------------------+-----+------------+-----+------+------------+
	| D P0 Q0b      | 27  | 28   | D P0 S10         |     | D L P1     | 27  | 28   | D L P1 U6r |
	+---------------+-----+------+------------------+-----+------------+-----+------+------------+
	| D E S1i P0    | 29  | 30   | D P0 S1o         |     | D L P1 U6t | 29  | 30   | D L P1     |
	+---------------+-----+------+------------------+-----+------------+-----+------+------------+
	| D E S1c P0    | 31  | 32   | ADC VDD          |     | D L        | 31  | 32   | D L        |
	+---------------+-----+------+------------------+-----+------------+-----+------+------------+
	| A4            | 33  | 34   | ADC GND          |     | D L Q1b    | 33  | 34   | D E L      |
	+---------------+-----+------+------------------+-----+------------+-----+------+------------+
	| A6            | 35  | 36   | A5               |     | D L Q1a    | 35  | 36   | D E L      |
	+---------------+-----+------+------------------+-----+------------+-----+------+------------+
	| A2            | 37  | 38   | A3               |     | D L U5t    | 37  | 38   | D L U5r    |
	+---------------+-----+------+------------------+-----+------------+-----+------+------------+
	| A0            | 39  | 40   | A1               |     | D L P1     | 39  | 40   | D L P1     |
	+---------------+-----+------+------------------+-----+------------+-----+------+------------+
	| D P0          | 41  | 42   | D Q0a S11 U3t P0 |     | D L P1     | 41  | 42   | D L P1     |
	+---------------+-----+------+------------------+-----+------------+-----+------+------------+
	| GND           | 43  | 44   | GND              |     | D L P1     | 43  | 44   | D L P1     |
	+---------------+-----+------+------------------+-----+------------+-----+------+------------+
	| GND           | 45  | 46   | GND              |     | D E L P1   | 45  | 46   | D E L P1   |
	+---------------+-----+------+------------------+-----+------------+-----+------+------------+

.. note::

    Legend

    * A: :ref:`bone-analog`
    * B: :ref:`bone-i2s`
    * C: :ref:`bone-can`
    * D: :ref:`bone-gpio`
    * E: :ref:`bone-pwm`
    * I: :ref:`bone-i2c`
    * L: :ref:`bone-lcd`
    * M: :ref:`bone-mmc`
    * P: :ref:`bone-pru`
    * Q: :ref:`bone-capture`
    * S: :ref:`bone-spi`
    * U: :ref:`bone-uart`
    * Y: :ref:`bone-ecap`

.. _bone-gpio:

Digital GPIO 
************

The compatibility layer comes with simple reference nodes for attaching the Linux gpio-leds or gpio-keys to any cape header GPIO pin. This provides simple userspace general purpose input or output with various trigger modes.

The format followed for the gpio-leds nodes is **bone_led_P8_## / bone_led_P9_##**. The **gpio-leds** driver is used by these reference nodes internally and allows users to easily create compatible led nodes in overlays for Black, AI and AI-64.


.. code-block:: c
   :linenos:
   :caption: Example device tree overlay to enable LED driver on header P8 pin 3
   :name: bone_cape_spec_led_example

   /dts-v1/;
   /plugin/;

   &bone_led_P8_03 {
       status = "okay";
   }

In :ref:`bone_cape_spec_led_example`, it is possible to redefine the default label
and other properties defined in the
`gpio-leds schema <https://elixir.bootlin.com/linux/v5.10/source/Documentation/devicetree/bindings/leds/leds-gpio.yaml>`_.

.. table:: Bone GPIO LEDs interface

	+------------------------+-------------+----------+-----------+-----------+
	| LED SYSFS              | Header pin  | Black    | AI        | AI-64     |
	+========================+=============+==========+===========+===========+
	| /sys/class/leds/P8_03  | P8_03       | gpio1_6  | gpio1_24  | gpio0_20  |
	+------------------------+-------------+----------+-----------+-----------+
	| /sys/class/leds/P8_04  | P8_04       | gpio1_7  | gpio1_25  | gpio0_48  |
	+------------------------+-------------+----------+-----------+-----------+
	| /sys/class/leds/P8_05  | P8_05       | gpio1_2  | gpio7_1   | gpio0_33  |
	+------------------------+-------------+----------+-----------+-----------+
	| /sys/class/leds/P8_06  | P8_06       | gpio1_3  | gpio7_2   | gpio0_34  |
	+------------------------+-------------+----------+-----------+-----------+
	| /sys/class/leds/P8_07  | P8_07       | gpio2_2  | gpio6_5   | gpio0_15  |
	+------------------------+-------------+----------+-----------+-----------+
	| /sys/class/leds/P8_08  | P8_08       | gpio2_3  | gpio6_6   | gpio0_14  |
	+------------------------+-------------+----------+-----------+-----------+
	| /sys/class/leds/P8_09  | P8_09       | gpio2_5  | gpio6_18  | gpio0_17  |
	+------------------------+-------------+----------+-----------+-----------+
	| /sys/class/leds/P8_10  | P8_10       | gpio2_4  | gpio6_4   | gpio0_16  |
	+------------------------+-------------+----------+-----------+-----------+
	| /sys/class/leds/P8_11  | P8_11       | gpio1_13 | gpio3_11  | gpio0_60  |
	+------------------------+-------------+----------+-----------+-----------+
	| /sys/class/leds/P8_12  | P8_12       | gpio1_12 | gpio3_10  | gpio0_59  |
	+------------------------+-------------+----------+-----------+-----------+
	| /sys/class/leds/P8_13  | P8_13       | gpio0_23 | gpio4_11  | gpio0_89  |
	+------------------------+-------------+----------+-----------+-----------+
	| /sys/class/leds/P8_14  | P8_14       | gpio0_26 | gpio4_13  | gpio0_75  |
	+------------------------+-------------+----------+-----------+-----------+
	| /sys/class/leds/P8_15  | P8_15       | gpio1_15 | gpio4_3   | gpio0_61  |
	+------------------------+-------------+----------+-----------+-----------+
	| /sys/class/leds/P8_16  | P8_16       | gpio1_14 | gpio4_29  | gpio0_62  |
	+------------------------+-------------+----------+-----------+-----------+
	| /sys/class/leds/P8_17  | P8_17       | gpio0_27 | gpio8_18  | gpio0_3   |
	+------------------------+-------------+----------+-----------+-----------+
	| /sys/class/leds/P8_18  | P8_18       | gpio2_1  | gpio4_9   | gpio0_4   |
	+------------------------+-------------+----------+-----------+-----------+
	| /sys/class/leds/P8_19  | P8_19       | gpio0_22 | gpio4_10  | gpio0_88  |
	+------------------------+-------------+----------+-----------+-----------+
	| /sys/class/leds/P8_20  | P8_20       | gpio1_31 | gpio6_30  | gpio0_76  |
	+------------------------+-------------+----------+-----------+-----------+
	| /sys/class/leds/P8_21  | P8_21       | gpio1_30 | gpio6_29  | gpio0_30  |
	+------------------------+-------------+----------+-----------+-----------+
	| /sys/class/leds/P8_22  | P8_22       | gpio1_5  | gpio1_23  | gpio0_5   |
	+------------------------+-------------+----------+-----------+-----------+
	| /sys/class/leds/P8_23  | P8_23       | gpio1_4  | gpio1_22  | gpio0_31  |
	+------------------------+-------------+----------+-----------+-----------+
	| /sys/class/leds/P8_24  | P8_24       | gpio1_1  | gpio7_0   | gpio0_6   |
	+------------------------+-------------+----------+-----------+-----------+
	| /sys/class/leds/P8_25  | P8_25       | gpio1_0  | gpio6_31  | gpio0_35  |
	+------------------------+-------------+----------+-----------+-----------+
	| /sys/class/leds/P8_26  | P8_26       | gpio1_29 | gpio4_28  | gpio0_51  |
	+------------------------+-------------+----------+-----------+-----------+
	| /sys/class/leds/P8_27  | P8_27       | gpio2_22 | gpio4_23  | gpio0_71  |
	+------------------------+-------------+----------+-----------+-----------+
	| /sys/class/leds/P8_28  | P8_28       | gpio2_24 | gpio4_19  | gpio0_72  |
	+------------------------+-------------+----------+-----------+-----------+
	| /sys/class/leds/P8_29  | P8_29       | gpio2_23 | gpio4_22  | gpio0_73  |
	+------------------------+-------------+----------+-----------+-----------+
	| /sys/class/leds/P8_30  | P8_30       | gpio2_25 | gpio4_20  | gpio0_74  |
	+------------------------+-------------+----------+-----------+-----------+
	| /sys/class/leds/P8_31  | P8_31       | gpio0_10 | gpio8_14  | gpio0_32  |
	+------------------------+-------------+----------+-----------+-----------+
	| /sys/class/leds/P8_32  | P8_32       | gpio0_11 | gpio8_15  | gpio0_26  |
	+------------------------+-------------+----------+-----------+-----------+
	| /sys/class/leds/P8_33  | P8_33       | gpio0_9  | gpio8_13  | gpio0_25  |
	+------------------------+-------------+----------+-----------+-----------+
	| /sys/class/leds/P8_34  | P8_34       | gpio2_17 | gpio8_11  | gpio0_7   |
	+------------------------+-------------+----------+-----------+-----------+
	| /sys/class/leds/P8_35  | P8_35       | gpio0_8  | gpio8_12  | gpio0_24  |
	+------------------------+-------------+----------+-----------+-----------+
	| /sys/class/leds/P8_36  | P8_36       | gpio2_16 | gpio8_10  | gpio0_8   |
	+------------------------+-------------+----------+-----------+-----------+
	| /sys/class/leds/P8_37  | P8_37       | gpio2_14 | gpio8_8   | gpio0_106 |
	+------------------------+-------------+----------+-----------+-----------+
	| /sys/class/leds/P8_38  | P8_38       | gpio2_15 | gpio8_9   | gpio0_105 |
	+------------------------+-------------+----------+-----------+-----------+
	| /sys/class/leds/P8_39  | P8_39       | gpio2_12 | gpio8_6   | gpio0_69  |
	+------------------------+-------------+----------+-----------+-----------+
	| /sys/class/leds/P8_40  | P8_40       | gpio2_13 | gpio8_7   | gpio0_70  |
	+------------------------+-------------+----------+-----------+-----------+
	| /sys/class/leds/P8_41  | P8_41       | gpio2_10 | gpio8_4   | gpio0_67  |
	+------------------------+-------------+----------+-----------+-----------+
	| /sys/class/leds/P8_42  | P8_42       | gpio2_11 | gpio8_5   | gpio0_68  |
	+------------------------+-------------+----------+-----------+-----------+
	| /sys/class/leds/P8_43  | P8_43       | gpio2_8  | gpio8_2   | gpio0_65  |
	+------------------------+-------------+----------+-----------+-----------+
	| /sys/class/leds/P8_44  | P8_44       | gpio2_9  | gpio8_3   | gpio0_66  |
	+------------------------+-------------+----------+-----------+-----------+
	| /sys/class/leds/P8_45  | P8_45       | gpio2_6  | gpio8_0   | gpio0_79  |
	+------------------------+-------------+----------+-----------+-----------+
	| /sys/class/leds/P8_46  | P8_46       | gpio2_7  | gpio8_1   | gpio0_80  |
	+------------------------+-------------+----------+-----------+-----------+
	| /sys/class/leds/P9_11  | P9_11       | gpio0_30 | gpio8_17  | gpio0_1   |
	+------------------------+-------------+----------+-----------+-----------+
	| /sys/class/leds/P9_12  | P9_12       | gpio1_28 | gpio5_0   | gpio0_45  |
	+------------------------+-------------+----------+-----------+-----------+
	| /sys/class/leds/P9_13  | P9_13       | gpio0_31 | gpio6_12  | gpio0_2   |
	+------------------------+-------------+----------+-----------+-----------+
	| /sys/class/leds/P9_14  | P9_14       | gpio1_18 | gpio4_25  | gpio0_93  |
	+------------------------+-------------+----------+-----------+-----------+
	| /sys/class/leds/P9_15  | P9_15       | gpio1_16 | gpio3_12  | gpio0_47  |
	+------------------------+-------------+----------+-----------+-----------+
	| /sys/class/leds/P9_16  | P9_16       | gpio1_19 | gpio4_26  | gpio0_94  |
	+------------------------+-------------+----------+-----------+-----------+
	| /sys/class/leds/P9_17  | P9_17       | gpio0_5  | gpio7_17  | gpio0_28  |
	+------------------------+-------------+----------+-----------+-----------+
	| /sys/class/leds/P9_18  | P9_18       | gpio0_4  | gpio7_16  | gpio0_40  |
	+------------------------+-------------+----------+-----------+-----------+
	| /sys/class/leds/P9_19  | P9_19       | gpio0_13 | gpio7_3   | gpio0_78  |
	+------------------------+-------------+----------+-----------+-----------+
	| /sys/class/leds/P9_20  | P9_20       | gpio0_12 | gpio7_4   | gpio0_77  |
	+------------------------+-------------+----------+-----------+-----------+
	| /sys/class/leds/P9_21  | P9_21       | gpio0_3  | gpio3_3   | gpio0_39  |
	+------------------------+-------------+----------+-----------+-----------+
	| /sys/class/leds/P9_22  | P9_22       | gpio0_2  | gpio6_19  | gpio0_38  |
	+------------------------+-------------+----------+-----------+-----------+
	| /sys/class/leds/P9_23  | P9_23       | gpio1_17 | gpio7_11  | gpio0_10  |
	+------------------------+-------------+----------+-----------+-----------+
	| /sys/class/leds/P9_24  | P9_24       | gpio0_15 | gpio6_15  | gpio0_13  |
	+------------------------+-------------+----------+-----------+-----------+
	| /sys/class/leds/P9_25  | P9_25       | gpio3_21 | gpio6_17  | gpio0_127 |
	+------------------------+-------------+----------+-----------+-----------+
	| /sys/class/leds/P9_26  | P9_26       | gpio0_14 | gpio6_14  | gpio0_12  |
	+------------------------+-------------+----------+-----------+-----------+
	| /sys/class/leds/P9_27  | P9_27       | gpio3_19 | gpio4_15  | gpio0_46  |
	+------------------------+-------------+----------+-----------+-----------+
	| /sys/class/leds/P9_28  | P9_28       | gpio3_17 | gpio4_17  | gpio1_11  |
	+------------------------+-------------+----------+-----------+-----------+
	| /sys/class/leds/P9_29  | P9_29       | gpio3_15 | gpio5_11  | gpio0_53  |
	+------------------------+-------------+----------+-----------+-----------+
	| /sys/class/leds/P9_30  | P9_30       | gpio3_16 | gpio5_12  | gpio0_44  |
	+------------------------+-------------+----------+-----------+-----------+
	| /sys/class/leds/P9_31  | P9_31       | gpio3_14 | gpio5_10  | gpio0_52  |
	+------------------------+-------------+----------+-----------+-----------+
	| /sys/class/leds/P9_33  | P9_33       | *n/a*    | *n/a*     | gpio0_50  |
	+------------------------+-------------+----------+-----------+-----------+
	| /sys/class/leds/P9_35  | P9_35       | *n/a*    | *n/a*     | gpio0_55  |
	+------------------------+-------------+----------+-----------+-----------+
	| /sys/class/leds/P9_36  | P9_36       | *n/a*    | *n/a*     | gpio0_56  |
	+------------------------+-------------+----------+-----------+-----------+
	| /sys/class/leds/P9_37  | P9_37       | *n/a*    | *n/a*     | gpio0_57  |
	+------------------------+-------------+----------+-----------+-----------+
	| /sys/class/leds/P9_38  | P9_38       | *n/a*    | *n/a*     | gpio0_58  |
	+------------------------+-------------+----------+-----------+-----------+
	| /sys/class/leds/P9_39  | P9_39       | *n/a*    | *n/a*     | gpio0_54  |
	+------------------------+-------------+----------+-----------+-----------+
	| /sys/class/leds/P9_40  | P9_40       | *n/a*    | *n/a*     | gpio0_81  |
	+------------------------+-------------+----------+-----------+-----------+
	| /sys/class/leds/P9_41  | P9_41       | gpio0_20 | gpio6_20  | gpio1_0   |
	+------------------------+-------------+----------+-----------+-----------+
	| /sys/class/leds/P9_42  | P9_42       | gpio0_7  | gpio4_18  | gpio0_123 |
	+------------------------+-------------+----------+-----------+-----------+
	| /sys/class/leds/A15    | A15         | gpio0_19 | NA        | NA        |
	+------------------------+-------------+----------+-----------+-----------+

.. _bone-i2c:

|I2C|
*****

Compatibility layer provides simple I2C bone bus nodes for creating compatible overlays for Black, AI and AI-64. The format followed for these nodes is **bone_i2c_#**.

.. table:: Bone I2C

	+------------------+--------------+--------+-------+------------+-----------------+--------+-----------+
	| SYSFS            | DT symbol    | Black  | AI    | AI-64      | SCL             | SDA    | Overlay   |
	+==================+==============+========+=======+============+=================+========+===========+
	| /dev/bone/i2c/0  | bone_i2c_0   | I2C0   | I2C1  | TBD        | .. centered:: N/A (On-board)         |
	+------------------+--------------+--------+-------+------------+-----------------+--------+-----------+
	| /dev/bone/i2c/1  | bone_i2c_1   | I2C1   | I2C5  | MAIN_I2C6  | P9.17           | P9.18  | BONE-I2C1 |
	+------------------+--------------+--------+-------+------------+-----------------+--------+-----------+
	| /dev/bone/i2c/2  | bone_i2c_2   | I2C2   | I2C4  | MAIN_I2C3  | P9.19           | P9.20  | BONE-I2C2 |
	+------------------+--------------+--------+-------+------------+-----------------+--------+-----------+
	| /dev/bone/i2c/3  | bone_i2c_3   | I2C1   | I2C3  | MAIN_I2C4  | P9.24           | P9.26  | BONE-I2C3 |
	+------------------+--------------+--------+-------+------------+-----------------+--------+-----------+
	| /dev/bone/i2c/4  | bone_i2c_4   | I2C2   | -     | MAIN_I2C3  | P9.21           | P9.22  | BONE-I2C4 |
	+------------------+--------------+--------+-------+------------+-----------------+--------+-----------+


.. important::

   In the case the same controller is used for 2 different bone bus nodes, usage of those nodes is mutually-exclusive.

.. code-block:: c
   :linenos:
   :caption: Example device tree overlay to enable I2C driver
   :name: bone_cape_spec_i2c_example

   /dts-v1/;
   /plugin/;

   &bone_i2c_1 {
       status = "okay";
       accel@1c {
           compatible = "fsl,mma8453";
           reg = <0x1c>;
       };
   }

In :ref:`bone_cape_spec_i2c_example`, you can specify what driver you want to load and provide any properties it might need.

* https://www.kernel.org/doc/html/v5.10/i2c/summary.html
* https://www.kernel.org/doc/html/v5.10/i2c/instantiating-devices.html#method-1-declare-the-i2c-devices-statically
* https://www.kernel.org/doc/Documentation/devicetree/bindings/i2c/

.. _bone-spi:

SPI
***

SPI bone bus nodes allow creating compatible overlays for Black, AI and AI-64.

.. table:: Bone bus SPI

	+--------------------+------------+--------+-------+------------+--------+--------+--------+---------------------------------------+---------------+
	| Bone bus           | DT symbol  | Black  | AI    | AI-64      | SDO    | SDI    | CLK    | CS                                    | Overlays      |
	+====================+============+========+=======+============+========+========+========+=======================================+===============+
	| /dev/bone/spi/0.x  | bone_spi_0 | SPI0   | SPI2  | MAIN_SPI6  | P9.18  | P9.21  | P9.22  | - P9.17 (CS0)                         | - BONE-SPI0_0 |
	|                    |            |        |       |            |        |        |        | - P9.23 (CS1 - BBAI and BBAI64 only)  | - BONE-SPI0_1 |
	+--------------------+------------+--------+-------+------------+--------+--------+--------+---------------------------------------+---------------+
	| /dev/bone/spi/1.x  | bone_spi_1 | SPI1   | SPI3  | MAIN_SPI7  | P9.30  | P9.29  | P9.31  | - P9.28 (CS0)                         | - BONE-SPI1_0 |
	|                    |            |        |       |            |        |        |        | - P9.42 (CS1)                         | - BONE-SPI1_1 |
	+--------------------+------------+--------+-------+------------+--------+--------+--------+---------------------------------------+---------------+


.. code-block:: c
   :linenos:
   :caption: Example device tree overlay to enable SPI driver
   :name: bone_cape_spec_spi_example

   /dts-v1/;
   /plugin/;

   &bone_spi_0 {
       status = "okay";
        pressure@0 {
            compatible = "bosch,bmp280";
            reg = <0>;      /* CS0 */
            spi-max-frequency = <5000000>;
        };
   }

In :ref:`bone_cape_spec_spi_example`, you can specify what driver you want to load and provide any properties it might need.

* https://www.kernel.org/doc/html/v5.10/spi/spi-summary.html
* https://www.kernel.org/doc/Documentation/devicetree/bindings/spi/

.. _bone-uart:

UART
*****

UART bone bus nodes allow creating compatible overlays for Black, AI and AI-64.

.. table:: Bone bus UART

	+-------------------+--------------+--------+--------+-----------------------+--------+--------+---------------------------------------------+---------------------------------------------+------------+
	| Bone bus          | DT symbol    | Black  | AI     | AI-64                 | TX     | RX     | RTSn                                        | CTSn                                        | Overlays   |
	+===================+==============+========+========+=======================+========+========+=============================================+=============================================+============+
	| /dev/bone/uart/0  | bone_uart_0  | UART0  | UART1  | MAIN_UART0            | .. centered:: NA (console debug header pins)                                                                             |
	+-------------------+--------------+--------+--------+-----------------------+--------+--------+---------------------------------------------+---------------------------------------------+------------+
	| /dev/bone/uart/1  | bone_uart_1  | UART1  | UART10 | MAIN_UART2            | P9.24  | P9.26  | P9.19 P8.4 (N/A on AM3358)                  | P9.20 P8.3 (N/A on AM3358)                  | BONE-UART1 |
	+-------------------+--------------+--------+--------+-----------------------+--------+--------+---------------------------------------------+---------------------------------------------+------------+
	| /dev/bone/uart/2  | bone_uart_2  | UART2  | UART3  | *n/a*                 | P9.21  | P9.22  | P8.38 (N/A on AM5729)                       | P8.37 (N/A on AM5729)                       | BONE-UART2 |
	+-------------------+--------------+--------+--------+-----------------------+--------+--------+---------------------------------------------+---------------------------------------------+------------+
	| /dev/bone/uart/3  | bone_uart_3  | UART3  | *n/a*  | *n/a*                 | P9.42  | *n/a*  | *n/a*                                       | *n/a*                                       | BONE-UART3 |
	+-------------------+--------------+--------+--------+-----------------------+--------+--------+---------------------------------------------+---------------------------------------------+------------+
	| /dev/bone/uart/4  | bone_uart_4  | UART4  | UART5  | MAIN_UART0 (console)  | P9.13  | P9.11  | P8.33 (N/A on AM5729) P8.6 (N/A on AM3358)  | P8.35 (N/A on AM5729) P8.5 (N/A on AM3358)  | BONE-UART4 |
	+-------------------+--------------+--------+--------+-----------------------+--------+--------+---------------------------------------------+---------------------------------------------+------------+
	| /dev/bone/uart/5  | bone_uart_5  | UART5  | UART8  | MAIN_UART5            | P8.37  | P8.38  | P8.32                                       | P8.31                                       | BONE-UART5 |
	+-------------------+--------------+--------+--------+-----------------------+--------+--------+---------------------------------------------+---------------------------------------------+------------+
	| /dev/bone/uart/6  | bone_uart_6  | *n/a*  | *n/a*  | MAIN_UART8            | P8.29  | P8.28  | *n/a*                                       | *n/a*                                       | BONE-UART6 |
	+-------------------+--------------+--------+--------+-----------------------+--------+--------+---------------------------------------------+---------------------------------------------+------------+
	| /dev/bone/uart/7  | bone_uart_7  | *n/a*  | *n/a*  | MAIN_UART2            | P8.34  | P8.22  | *n/a*                                       | *n/a*                                       | BONE-UART7 |
	+-------------------+--------------+--------+--------+-----------------------+--------+--------+---------------------------------------------+---------------------------------------------+------------+


.. _bone-can:

CAN
*****

CAN bone bus nodes allow creating compatible overlays for Black, AI and AI-64.

.. table:: Bone bus CAN

	+------------------+--------+--------------------------+------------+--------+--------+-----------+
	| Bone bus         | Black  | AI                       | AI-64      | TX     | RX     | Overlays  |
	+==================+========+==========================+============+========+========+===========+
	| /dev/bone/can/0  | CAN0   | -                        | MAIN_MCAN0 | P9.20  | P9.19  | BONE-CAN0 |
	+------------------+--------+--------------------------+------------+--------+--------+-----------+
	| /dev/bone/can/1  | CAN1   | CAN2                     | MAIN_MCAN4 | P9.26  | P9.24  | BONE-CAN1 |
	+------------------+--------+--------------------------+------------+--------+--------+-----------+
	| /dev/bone/can/2  | -      | CAN1 (rev A2 and later)  | MAIN_MCAN5 | P8.08  | P8.07  | BONE-CAN2 |
	+------------------+--------+--------------------------+------------+--------+--------+-----------+
	| /dev/bone/can/3  | -      | -                        | MAIN_MCAN6 | P8.10  | P8.09  | BONE-CAN3 |
	+------------------+--------+--------------------------+------------+--------+--------+-----------+
	| /dev/bone/can/4  | -      | -                        | MAIN_MCAN7 | P8.05  | P8.06  | BONE-CAN4 |
	+------------------+--------+--------------------------+------------+--------+--------+-----------+


.. _bone-analog:

ADC
*******

* TODO: We need a udev rule to make sure the ADC shows up at /dev/bone/adc! There's nothing for sure that IIO devices will show up in the same place.
* TODO: I think we can also create symlinks for each channel based on which device is there, such that we can do /dev/bone/adc/Px_y 

.. table:: Bone ADC

	+--------+-------------+------------------+------------------+
	| Index  | Header pin  | Black/AI-64      | AI               |
	+========+=============+==================+==================+
	| 0      | P9_39       | in_voltage0_raw  | in_voltage0_raw  |
	+--------+-------------+------------------+------------------+
	| 1      | P9_40       | in_voltage1_raw  | in_voltage1_raw  |
	+--------+-------------+------------------+------------------+
	| 2      | P9_37       | in_voltage2_raw  | in_voltage3_raw  |
	+--------+-------------+------------------+------------------+
	| 3      | P9_38       | in_voltage3_raw  | in_voltage2_raw  |
	+--------+-------------+------------------+------------------+
	| 4      | P9_33       | in_voltage4_raw  | in_voltage7_raw  |
	+--------+-------------+------------------+------------------+
	| 5      | P9_36       | in_voltage5_raw  | in_voltage6_raw  |
	+--------+-------------+------------------+------------------+
	| 6      | P9_35       | in_voltage6_raw  | in_voltage4_raw  |
	+--------+-------------+------------------+------------------+


.. table:: Bone ADC Overlay

	+-----------+----------------------+--------+-------------------------------------------------------------------------------------------------------------------------------------------+
	| Black     | AI                   | AI-64  | overlay                                                                                                                                   |
	+===========+======================+========+===========================================================================================================================================+
	| Internal  | External (STMPE811)  | TBD    | `BONE-ADC.dts <https://git.beagleboard.org/beagleboard/BeagleBoard-DeviceTrees/blob/v4.19.x-ti-overlays/src/arm/overlays/BONE-ADC.dts>`_  |
	+-----------+----------------------+--------+-------------------------------------------------------------------------------------------------------------------------------------------+


PWM
-------

PWM bone bus nodes allow creating compatible overlays for Black, AI and AI-64. For the definitions, you can see `bbai-bone-buses.dtsi#L415 <https://github.com/lorforlinux/BeagleBoard-DeviceTrees/blob/97a6f0daa9eab09633a2064f68a53b107d6e3968/src/arm/bbai-bone-buses.dtsi#L415>`_ & `bbb-bone-buses.dtsi#L432 <https://github.com/lorforlinux/BeagleBoard-DeviceTrees/blob/97a6f0daa9eab09633a2064f68a53b107d6e3968/src/arm/bbb-bone-buses.dtsi#L432>`_

.. table:: Bone bus PWM

	+------------------+--------+-------+--------+--------+--------+--------------------------------------------------------------------------------------------------------+
	| Bone bus         | Black  | AI    | AI-64  | A      | B      | Overlay                                                                                                |
	+==================+========+=======+========+========+========+========================================================================================================+
	| /dev/bone/pwm/0  | PWM0   | -     | PWM1   | P9.22  | P9.21  | `BONE-PWM0.dts <https://github.com/lorforlinux/bb.org-overlays/blob/bone_pwm/src/arm/BONE-PWM0.dts>`_  |
	+------------------+--------+-------+--------+--------+--------+--------------------------------------------------------------------------------------------------------+
	| /dev/bone/pwm/1  | PWM1   | PWM3  | PWM2   | P9.14  | P9.16  | `BONE-PWM1.dts <https://github.com/lorforlinux/bb.org-overlays/blob/bone_pwm/src/arm/BONE-PWM1.dts>`_  |
	+------------------+--------+-------+--------+--------+--------+--------------------------------------------------------------------------------------------------------+
	| /dev/bone/pwm/2  | PWM2   | PWM2  | PWM0   | P8.19  | P8.13  | `BONE-PWM2.dts <https://github.com/lorforlinux/bb.org-overlays/blob/bone_pwm/src/arm/BONE-PWM2.dts>`_  |
	+------------------+--------+-------+--------+--------+--------+--------------------------------------------------------------------------------------------------------+

TIMER PWM
-------------

TIMER PWM bone bus uses ti,omap-dmtimer-pwm driver, and timer nodes that allow creating compatible overlays for Black, AI and AI-64. For the timer node definitions, you can see `bbai-bone-buses.dtsi#L449 <https://github.com/lorforlinux/BeagleBoard-DeviceTrees/blob/97a6f0daa9eab09633a2064f68a53b107d6e3968/src/arm/bbai-bone-buses.dtsi#L449>`_ & `bbb-bone-buses.dtsi#L466 <https://github.com/lorforlinux/BeagleBoard-DeviceTrees/blob/97a6f0daa9eab09633a2064f68a53b107d6e3968/src/arm/bbb-bone-buses.dtsi#L466>`_.

.. table:: Bone TIMER PWMs

	+----------------------------------------------+-------------+--------+----------+-------------------------------------------------------------------------------------------------------------------------+
	| Bone bus                                     | Header pin  | Black  | AI       | overlay                                                                                                                 |
	+==============================================+=============+========+==========+=========================================================================================================================+
	| /sys/bus/platform/devices/bone_timer_pwm_0/  | P8.10       | timer6 | timer10  | `BONE-TIMER_PWM_0.dts <https://github.com/lorforlinux/bb.org-overlays/blob/bone_timer/src/arm/BONE-TIMER_PWM_0.dts>`_   |
	+----------------------------------------------+-------------+--------+----------+-------------------------------------------------------------------------------------------------------------------------+
	| /sys/bus/platform/devices/bone_timer_pwm_1/  | P8.07       | timer4 | timer11  | `BONE-TIMER_PWM_1.dts <https://github.com/lorforlinux/bb.org-overlays/blob/bone_timer/src/arm/BONE-TIMER_PWM_1.dts>`_   |
	+----------------------------------------------+-------------+--------+----------+-------------------------------------------------------------------------------------------------------------------------+
	| /sys/bus/platform/devices/bone_timer_pwm_2/  | P8.08       | timer7 | timer12  | `BONE-TIMER_PWM_2.dts <https://github.com/lorforlinux/bb.org-overlays/blob/bone_timer/src/arm/BONE-TIMER_PWM_2.dts>`_   |
	+----------------------------------------------+-------------+--------+----------+-------------------------------------------------------------------------------------------------------------------------+
	| /sys/bus/platform/devices/bone_timer_pwm_3/  | P9.21       | -      | timer13  | `BONE-TIMER_PWM_3.dts <https://github.com/lorforlinux/bb.org-overlays/blob/bone_timer/src/arm/BONE-TIMER_PWM_3.dts>`_   |
	+----------------------------------------------+-------------+--------+----------+-------------------------------------------------------------------------------------------------------------------------+
	| /sys/bus/platform/devices/bone_timer_pwm_4/  | P8.09       | timer5 | timer14  | `BONE-TIMER_PWM_4.dts <https://github.com/lorforlinux/bb.org-overlays/blob/bone_timer/src/arm/BONE-TIMER_PWM_4.dts>`_   |
	+----------------------------------------------+-------------+--------+----------+-------------------------------------------------------------------------------------------------------------------------+
	| /sys/bus/platform/devices/bone_timer_pwm_5/  | P9.22       | -      | timer15  | `BONE-TIMER_PWM_5.dts <https://github.com/lorforlinux/bb.org-overlays/blob/bone_timer/src/arm/BONE-TIMER_PWM_5.dts>`_   |
	+----------------------------------------------+-------------+--------+----------+-------------------------------------------------------------------------------------------------------------------------+


eCAP
-------

#TODO: This doesn't include any abstraction yet.

.. table:: Black eCAP PWMs

	+-----------------------------------------------+-------------+--------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
	| Bone bus                                      | Header pin  | peripheral         | overlay                                                                                                                                     |
	+===============================================+=============+====================+=============================================================================================================================================+
	| /sys/bus/platform/drivers/ecap/48302100.ecap  | P9.42       | eCAP0_in_PWM0_out  | `BBB-ECAP0.dts <https://git.beagleboard.org/beagleboard/BeagleBoard-DeviceTrees/blob/v4.19.x-ti-overlays/src/arm/overlays/BBB-ECAP0.dts>`_  |
	+-----------------------------------------------+-------------+--------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
	| /sys/bus/platform/drivers/ecap/48304100.ecap  | P9.28       | eCAP2_in_PWM2_out  | `BBB-ECAP2.dts <https://git.beagleboard.org/beagleboard/BeagleBoard-DeviceTrees/blob/v4.19.x-ti-overlays/src/arm/overlays/BBB-ECAP2.dts>`_  |
	+-----------------------------------------------+-------------+--------------------+---------------------------------------------------------------------------------------------------------------------------------------------+

.. table:: AI eCAP PWMs

	+-----------------------------------------------+-------------+--------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
	| Bone bus                                      | Header pin  | peripheral         | overlay                                                                                                                                        |
	+===============================================+=============+====================+================================================================================================================================================+
	| /sys/bus/platform/drivers/ecap/4843e100.ecap  | P8.15       | eCAP1_in_PWM1_out  | `BBAI-ECAP1.dts <https://git.beagleboard.org/beagleboard/BeagleBoard-DeviceTrees/blob/v4.19.x-ti-overlays/src/arm/overlays/BBAI-ECAP1.dts>`_   |
	+-----------------------------------------------+-------------+--------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
	| /sys/bus/platform/drivers/ecap/48440100.ecap  | P8.14       | eCAP2_in_PWM2_out  | `BBAI-ECAP2.dts <https://git.beagleboard.org/beagleboard/BeagleBoard-DeviceTrees/blob/v4.19.x-ti-overlays/src/arm/overlays/BBAI-ECAP2.dts>`_   |
	+-----------------------------------------------+-------------+--------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
	| /sys/bus/platform/drivers/ecap/48440100.ecap  | P8.20       | eCAP2_in_PWM2_out  | `BBAI-ECAP2A.dts <https://git.beagleboard.org/beagleboard/BeagleBoard-DeviceTrees/blob/v4.19.x-ti-overlays/src/arm/overlays/BBAI-ECAP2A.dts>`_ |
	+-----------------------------------------------+-------------+--------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
	| /sys/bus/platform/drivers/ecap/48442100.ecap  | P8.04       | eCAP3_in_PWM3_out  | `BBAI-ECAP3.dts <https://git.beagleboard.org/beagleboard/BeagleBoard-DeviceTrees/blob/v4.19.x-ti-overlays/src/arm/overlays/BBAI-ECAP3.dts>`_   |
	+-----------------------------------------------+-------------+--------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
	| /sys/bus/platform/drivers/ecap/48442100.ecap  | P8.26       | eCAP3_in_PWM3_out  | `BBAI-ECAP3A.dts <https://git.beagleboard.org/beagleboard/BeagleBoard-DeviceTrees/blob/v4.19.x-ti-overlays/src/arm/overlays/BBAI-ECAP3A.dts>`_ |
	+-----------------------------------------------+-------------+--------------------+------------------------------------------------------------------------------------------------------------------------------------------------+


eMMC
------

.. table:: Bone eMMC

	+-------------+--------------+
	| Header pin  | Description  |
	+=============+==============+
	| P8.3        | DAT6         |
	+-------------+--------------+
	| P8.4        | DAT7         |
	+-------------+--------------+
	| P8.5        | DAT2         |
	+-------------+--------------+
	| P8.6        | DAT3         |
	+-------------+--------------+
	| P8.20       | CMD          |
	+-------------+--------------+
	| P8.21       | CLK          |
	+-------------+--------------+
	| P8.22       | DAT5         |
	+-------------+--------------+
	| P8.23       | DAT4         |
	+-------------+--------------+
	| P8.24       | DAT1         |
	+-------------+--------------+
	| P8.25       | DAT0         |
	+-------------+--------------+

.. table:: Bone eMMC Overlay

	+--------+-------+---------------------------------------------------------------------------------------------------------------------------------------------+
	| Black  | AI    | overlay                                                                                                                                     |
	+========+=======+=============================================================================================================================================+
	| MMC2   | MMC3  | `BONE-eMMC.dts <https://git.beagleboard.org/beagleboard/BeagleBoard-DeviceTrees/blob/v4.19.x-ti-overlays/src/arm/overlays/BONE-eMMC.dts>`_  |
	+--------+-------+---------------------------------------------------------------------------------------------------------------------------------------------+


LCD
------

.. table:: 16bit LCD interface

	+-------------+-----------------+
	| Header pin  | Description     |
	+=============+=================+
	| P8_45       | lcd_data0       |
	+-------------+-----------------+
	| P8_46       | lcd_data1       |
	+-------------+-----------------+
	| P8_43       | lcd_data2       |
	+-------------+-----------------+
	| P8_44       | lcd_data3       |
	+-------------+-----------------+
	| P8_41       | lcd_data4       |
	+-------------+-----------------+
	| P8_42       | lcd_data5       |
	+-------------+-----------------+
	| P8_39       | lcd_data6       |
	+-------------+-----------------+
	| P8_40       | lcd_data7       |
	+-------------+-----------------+
	| P8_37       | lcd_data8       |
	+-------------+-----------------+
	| P8_38       | lcd_data9       |
	+-------------+-----------------+
	| P8_36       | lcd_data10      |
	+-------------+-----------------+
	| P8_34       | lcd_data11      |
	+-------------+-----------------+
	| P8_35       | lcd_data12      |
	+-------------+-----------------+
	| P8_33       | lcd_data13      |
	+-------------+-----------------+
	| P8_31       | lcd_data14      |
	+-------------+-----------------+
	| P8_32       | lcd_data15      |
	+-------------+-----------------+
	| P8_27       | lcd_vsync       |
	+-------------+-----------------+
	| P8_29       | lcd_hsync       |
	+-------------+-----------------+
	| P8_28       | lcd_pclk        |
	+-------------+-----------------+
	| P8_30       | lcd_ac_bias_en  |
	+-------------+-----------------+

.. table:: 16bit LCD interface Overlay

	+--------+-----+----------+
	| Black  | AI  | overlay  |
	+========+=====+==========+
	| lcdc   | dss |          |
	+--------+-----+----------+


eQEP
--------

On BeagleBone's without an eQEP on specific pins, consider using the PRU to perform a software counter function.

.. table:: Bone eQEP

	+----------------------+--------+--------+--------+--------+--------+-------------------------------+-------------------------------+----------+
	| Bone bus             | Black  | AI     | AI-64  | A      | B      | strobe                        | index                         | overlay  |
	+======================+========+========+========+========+========+===============================+===============================+==========+
	| /dev/bone/counter/0  | eQEP0  | eQEP2  | eQEP0  | P9.42  | P9.27  | - Black/AI-64: P9.25          | - Black/AI-64: P9.41          |          |
	|                      |        |        |        |        |        | - AI: P8.06                   | - AI: P8.05                   |          |
	+----------------------+--------+--------+--------+--------+--------+-------------------------------+-------------------------------+----------+
	| /dev/bone/counter/1  | eQEP1  | eQEP0  | eQEP1  | P8.35  | P8.33  | - Black/AI-64: P8.32          | - Black/AI-64: P8.31          |          |
	|                      |        |        |        |        |        | - AI: P9.21                   | - AI: ‒                       |          |
	+----------------------+--------+--------+--------+--------+--------+-------------------------------+-------------------------------+----------+
	| /dev/bone/counter/2  | eQEP2  | eQEP1  | ‒      | P8.12  | P8.22  | - Black: P8.15                | - Black: P8.16                |          |
	|                      |        |        |        |        |        | - AI: P8.18                   | - AI: P9.15                   |          |
	+----------------------+--------+--------+--------+--------+--------+-------------------------------+-------------------------------+----------+


McASP
---------

.. table:: Bone McASP0

	+-------------+-----------------------+
	| Header pin  | Description           |
	+=============+=======================+
	| P9.12       | aclkr                 |
	+-------------+-----------------------+
	| P9.25       | ahclkx                |
	+-------------+-----------------------+
	| P9.27       | fsr                   |
	+-------------+-----------------------+
	| P9.28       | Black: axr2 AI: axr9  |
	+-------------+-----------------------+
	| P9.29       | fsx                   |
	+-------------+-----------------------+
	| P9.30       | Black: axr0 AI: axr10 |
	+-------------+-----------------------+
	| P9.31       | aclkx                 |
	+-------------+-----------------------+

.. table:: Bone McASP0 Overlay

	+--------+---------+----------+
	| Black  | AI      | overlay  |
	+========+=========+==========+
	| McASP0 | McASP1  |          |
	+--------+---------+----------+

PRU
-------

The overlay situation for PRUs is a bit more complex than with other peripherals. The mechanism for loading, starting and stopping the PRUs can go through either [https://www.kernel.org/doc/html/latest/driver-api/uio-howto.html UIO] or [https://software-dl.ti.com/processor-sdk-linux/esd/docs/latest/linux/Foundational_Components/PRU-ICSS/Linux_Drivers/RemoteProc_and_RPMsg.html RemoteProc].

* /dev/remoteproc/prussX-coreY (AM3358 X = "", other x = "1|2")

.. table:: Bone PRU eCAP

	+-------------+------------+------------+
	| Header Pin  | Black      | AI         |
	+=============+============+============+
	| P8.15       | pr1_ecap0  | pr1_ecap0  |
	+-------------+------------+------------+
	| P8.32       | -          | pr2_ecap0  |
	+-------------+------------+------------+
	| P9.42       | pr1_ecap0  | -          |
	+-------------+------------+------------+

.. table:: AI PRU UART

	+-------------+--------+--------+-------+-------+-----------+
	| UART        | TX     | RX     | RTSn  | CTSn  | Overlays  |
	+=============+========+========+=======+=======+===========+
	| PRU1 UART0  | P8_31  | P8_33  | P8_34 | P8_35 |           |
	+-------------+--------+--------+-------+-------+-----------+
	| PRU2 UART0  | P8_43  | P8_44  | P8_45 | P8_46 |           |
	+-------------+--------+--------+-------+-------+-----------+

.. table:: Bone PRU

	+-------------+--------------------+------------------+
	| Header Pin  | Black              | AI               |
	+=============+====================+==================+
	| P8.03       | -                  | pr2_pru0 10      |
	+-------------+--------------------+------------------+
	| P8.04       | -                  | pr2_pru0 11      |
	+-------------+--------------------+------------------+
	| P8.05       | -                  | pr2_pru0 06      |
	+-------------+--------------------+------------------+
	| P8.06       | -                  | pr2_pru0 07      |
	+-------------+--------------------+------------------+
	| P8.07       | -                  | pr2_pru1 16      |
	+-------------+--------------------+------------------+
	| P8.08       | -                  | pr2_pru0 20      |
	+-------------+--------------------+------------------+
	| P8.09       | -                  | pr2_pru1 06      |
	+-------------+--------------------+------------------+
	| P8.10       | -                  | pr2_pru1 15      |
	+-------------+--------------------+------------------+
	| P8.11       | pr1_pru0 15 (Out)  | pr1_pru0 04      |
	+-------------+--------------------+------------------+
	| P8.12       | pr1_pru0 14 (Out)  | pr1_pru0 03      |
	+-------------+--------------------+------------------+
	| P8.13       | -                  | pr1_pru1 07      |
	+-------------+--------------------+------------------+
	| P8.14       | -                  | pr1_pru1 09      |
	+-------------+--------------------+------------------+
	| P8.15       | pr1_pru0 15 (In)   | pr1_pru1 16      |
	+-------------+--------------------+------------------+
	| P8.16       | pr1_pru0 14 (In)   | pr1_pru1 18      |
	+-------------+--------------------+------------------+
	| P8.17       | -                  | pr2_pru0 15      |
	+-------------+--------------------+------------------+
	| P8.18       | -                  | pr1_pru1 05      |
	+-------------+--------------------+------------------+
	| P8.19       | -                  | pr1_pru1 06      |
	+-------------+--------------------+------------------+
	| P8.20       | -                  | pr2_pru0 03      |
	+-------------+--------------------+------------------+
	| P8.21       | -                  | pr2_pru0 02      |
	+-------------+--------------------+------------------+
	| P8.22       | -                  | pr2_pru0 09      |
	+-------------+--------------------+------------------+
	| P8.23       | -                  | pr2_pru0 08      |
	+-------------+--------------------+------------------+
	| P8.24       | -                  | pr2_pru0 05      |
	+-------------+--------------------+------------------+
	| P8.25       | -                  | pr2_pru0 04      |
	+-------------+--------------------+------------------+
	| P8.26       | -                  | pr1_pru1 17      |
	+-------------+--------------------+------------------+
	| P8.27       | -                  | pr2_pru1 17      |
	+-------------+--------------------+------------------+
	| P8.28       | -                  | pr2_pru0 17      |
	+-------------+--------------------+------------------+
	| P8.29       | -                  | pr2_pru0 18      |
	+-------------+--------------------+------------------+
	| P8.30       | -                  | pr2_pru0 19      |
	+-------------+--------------------+------------------+
	| P8.31       | -                  | pr2_pru0 11      |
	+-------------+--------------------+------------------+
	| P8.32       | -                  | pr2_pru1 00      |
	+-------------+--------------------+------------------+
	| P8.33       | -                  | pr2_pru0 10      |
	+-------------+--------------------+------------------+
	| P8.34       | -                  | pr2_pru0 08      |
	+-------------+--------------------+------------------+
	| P8.35       | -                  | pr2_pru0 09      |
	+-------------+--------------------+------------------+
	| P8.36       | -                  | pr2_pru0 07      |
	+-------------+--------------------+------------------+
	| P8.37       | -                  | pr2_pru0 05      |
	+-------------+--------------------+------------------+
	| P8.38       | -                  | pr2_pru0 06      |
	+-------------+--------------------+------------------+
	| P8.39       | -                  | pr2_pru0 03      |
	+-------------+--------------------+------------------+
	| P8.40       | -                  | pr2_pru0 04      |
	+-------------+--------------------+------------------+
	| P8.41       | -                  | pr2_pru0 01      |
	+-------------+--------------------+------------------+
	| P8.42       | -                  | pr2_pru0 02      |
	+-------------+--------------------+------------------+
	| P8.43       | -                  | pr2_pru1 20      |
	+-------------+--------------------+------------------+
	| P8.44       | -                  | pr2_pru0 00      |
	+-------------+--------------------+------------------+
	| P8.45       | -                  | pr2_pru1 18      |
	+-------------+--------------------+------------------+
	| P8.46       | -                  | pr2_pru1 19      |
	+-------------+--------------------+------------------+
	| P9.11       | -                  | pr2_pru0 14      |
	+-------------+--------------------+------------------+
	| P9.13       | -                  | pr2_pru0 15      |
	+-------------+--------------------+------------------+
	| P9.14       | -                  | pr1_pru1 14      |
	+-------------+--------------------+------------------+
	| P9.15       | -                  | pr1_pru0 5       |
	+-------------+--------------------+------------------+
	| P9.16       | -                  | pr1_pru1 15      |
	+-------------+--------------------+------------------+
	| P9.17       | -                  | pr2_pru1 09      |
	+-------------+--------------------+------------------+
	| P9.18       | -                  | pr2_pru1 08      |
	+-------------+--------------------+------------------+
	| P9.19       | -                  | pr1_pru1 02      |
	+-------------+--------------------+------------------+
	| P9.20       | -                  | pr1_pru1 01      |
	+-------------+--------------------+------------------+
	| P9.24       | pr1_pru0 16 (In)   | -                |
	+-------------+--------------------+------------------+
	| P9.25       | pr1_pru0 07        | pr2_pru1 05      |
	+-------------+--------------------+------------------+
	| P9.26       | pr1_pru1 16 (In)   | pr1_pru0 17      |
	+-------------+--------------------+------------------+
	| P9.27       | pr1_pru0 05        | pr1_pru1 11      |
	+-------------+--------------------+------------------+
	| P9.28       | pr1_pru0 03        | pr2_pru1 13      |
	+-------------+--------------------+------------------+
	| P9.29       | pr1_pru0 01        | pr2_pru1 11      |
	+-------------+--------------------+------------------+
	| P9.30       | pr1_pru0 02        | pr2_pru1 12      |
	+-------------+--------------------+------------------+
	| P9.31       | pr1_pru0 00        | pr2_pru1 10      |
	+-------------+--------------------+------------------+
	| P9.41       | pr1_pru0 06        | pr1_pru1 03      |
	+-------------+--------------------+------------------+
	| P9.42       | pr1_pru0 04        | pr1_pru1 10      |
	+-------------+--------------------+------------------+

GPIO
----------

TODO<br>
For each of the pins with a GPIO, there should be a symlink that comes from the names 
*


.. _bone-methodology:

Methodology
***************

The methodology for applied in the kernel and software images to expose the software interfaces is to be documented here. The most fundamental elements are the device tree entries, including overlays, and udev rules.

Device Trees
=============

udev rules
=========================

10-of-symlink.rules
------------------------

.. code-block::

	#From: https://github.com/mvduin/py-uio/blob/master/etc/udev/rules.d/10-of-symlink.rules
	# allow declaring a symlink for a device in DT
	ATTR{device/of_node/symlink}!="", \
		ENV{OF_SYMLINK}="%s{device/of_node/symlink}"

	ENV{OF_SYMLINK}!="", ENV{DEVNAME}!="", \
		SYMLINK+="%E{OF_SYMLINK}", \
		TAG+="systemd", ENV{SYSTEMD_ALIAS}+="/dev/%E{OF_SYMLINK}"

TBD
****************

.. code-block::

	# Also courtesy of mvduin
	# create symlinks for gpios exported to sysfs by DT
	SUBSYSTEM=="gpio", ACTION=="add", TEST=="value", ATTR{label}!="sysfs", \
			RUN+="/bin/mkdir -p /dev/bone/gpio", \
			RUN+="/bin/ln -sT '/sys/class/gpio/%k' /dev/bone/gpio/%s{label}"


Verification
----------------

TODO: The steps used to verify all of these configurations is to be documented here. It will serve to document what has been tested, how to reproduce the configurations, and how to verify each major triannual release. All faults will be documented in the issue tracker.

References
-------------

- `Device Tree: Supporting Similar Boards - The BeagleBone Example <https://beagleboard.org/blog/2022-03-31-device-tree-supporting-similar-boards-the-beaglebone-example>`_
- `Google drive with summary of expansion signals on various BeagleBoard.org designs <https://docs.google.com/spreadsheets/d/1fE-AsDZvJ-bBwzNBj1_sPDrutvEvsmARqFwvbw_HkrE/edit?usp=sharing>`_
- `Beagleboard:Cape Expansion Headers <https://elinux.org/Beagleboard:Cape_Expansion_Headers>`_
