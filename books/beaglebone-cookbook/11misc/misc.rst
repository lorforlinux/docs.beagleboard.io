.. _beaglebone-cookbook-misc:

Misc
####

Here are bits and pieces of ideas that are being developed.

Converting a tmp117 to a tmp 114
================================

Problem
-------

You have a tmp114 temperature sensor and you need a driver for it.

Solution
--------

Find a similar driver and convert it to the tmp114.

Let's first see if there is a driver for it already. Run the following on the bone using the tab key in place 
of <tab>.

.. code-block:: bash

  bone$ modinfo tmp<tab><tab>
  tmp006  tmp007  tmp102  tmp103  tmp108  tmp401  tmp421  tmp513
  bone$ modinfo tmp

Here you see a list of modules that match *tmp*, unfortunately *tmp114* is not there.
Let's see if there are any matches in */lib/modules*.

.. code-block:: bash

    bone$  find /lib/modules/ -iname "*tmp*"
    /lib/modules/5.10.168-ti-arm64-r104/kernel/drivers/iio/temperature/tmp006.ko.xz
    /lib/modules/5.10.168-ti-arm64-r104/kernel/drivers/iio/temperature/tmp007.ko.xz
    /lib/modules/5.10.168-ti-arm64-r104/kernel/drivers/hwmon/tmp103.ko.xz
    /lib/modules/5.10.168-ti-arm64-r104/kernel/drivers/hwmon/tmp421.ko.xz
    /lib/modules/5.10.168-ti-arm64-r104/kernel/drivers/hwmon/tmp108.ko.xz
    /lib/modules/5.10.168-ti-arm64-r104/kernel/drivers/hwmon/tmp513.ko.xz
    /lib/modules/5.10.168-ti-arm64-r104/kernel/drivers/hwmon/tmp401.ko.xz
    /lib/modules/5.10.168-ti-arm64-r104/kernel/drivers/hwmon/tmp102.ko.xz

Looks like the same list, but here we can see what type of driver it is, either *hwmon* or *iio*.
hwmon is an older `harware monitor <https://docs.kernel.org/hwmon/hwmon-kernel-api.html>`_.  
iio is the newer, and prefered, `Industrial IO driver
<https://www.kernel.org/doc/html/v4.12/driver-api/iio/index.html>`_.
Googling tmp006 and tmp007 shows that they are Infrared Thermopile Sensors, not the same at the *tmp114*.
(Google it).  Let's keep looking for a more compatible device.

Browse over to http://kernel.org to see if there are tmp114 drivers in the newer versions of the kernel.
The first line in the table is **mainline**.  Click on the **browse** link on the right.
Here you will see the top level of the Linux sourse tree for the *mainline* version of the kernel.
Click on **drivers** and then **iio**. Finally, since tmp114 is a temperture sensor, click on **temperature**.
Here you see all the source code for the iio temperature drivers for the mainline version of the kernel. 
We've seen tmp006 and tmp007 before, tmp117 is new. Maybe it will work.  Click on **tmp117.c** to see the code.
Looks like it also works for the tmp116.  Let's try convering it to work with the tmp114.

A quick way to copy the code to the bone is to right-click on the **plain** link and select *Copy link address*.
Then, on the bone enter **wget** and past the link.  Mine looks like the following, yours will be similar.

.. code-block:: bash

  bone$ wget https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/plain/drivers/iio/temperature/tmp117.c?h=v6.4-rc7
  bone$ mv 'tmp117.c?h=v6.4-rc7' tmp117.c
  bone$ cp tmp117.c tmp114.c


