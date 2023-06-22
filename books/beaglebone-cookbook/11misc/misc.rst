.. _beaglebone-cookbook-misc:

.. |I2C| replace:: I\ :sup:`2`\ C

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
Then, on the bone enter **wget** and paste the link.  Mine looks like the following, yours will be similar.

.. code-block:: bash

  bone$ wget https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/plain/drivers/iio/temperature/tmp117.c?h=v6.4-rc7
  bone$ mv 'tmp117.c?h=v6.4-rc7' tmp117.c
  bone$ cp tmp117.c tmp114.c

The **mv** command moves the downloaded file to a usable name and the **cp** copies to a new file with the new name.

Compiling the module
^^^^^^^^^^^^^^^^^^^^

Next we need to compile the driver.  To do this we need to load the corresponding header files for the
version of the kernel that's beening run.

.. code-block:: bash

  bone$ uname -r
  5.10.168-ti-arm64-r105

Here you see which version I'm running, yours will be similar.  Now load the headers.

.. code-block:: bash

  bone$ sudo apt install linux-headers-`uname -r`

Next create a *Makefile*.  Put the following in a file called *Makefile*.

.. _misc_makefile:

.. literalinclude:: figures/Makefile
   :caption: Makefile for compiling module (Makefile)
   :linenos:

:download:`Makefile <figures/Makefile>`

Now you are ready to compile:

.. code-block:: bash

    bone$ make
    make -C /lib/modules/5.10.168-ti-arm64-r105/build M=/home/debian/play modules
    make[1]: Entering directory '/usr/src/linux-headers-5.10.168-ti-arm64-r105'
    CC [M]  /home/debian/play/tmp114.o
    /home/debian/play/tmp114.c: In function ‘tmp117_identify’:
    /home/debian/play/tmp114.c:150:7: error: implicit declaration of function ‘i2c_client_get_device_id’; did you mean ‘i2c_get_device_id’? [-Werror=implicit-function-declaration]
    150 |  id = i2c_client_get_device_id(client);
        |       ^~~~~~~~~~~~~~~~~~~~~~~~
        |       i2c_get_device_id
    /home/debian/play/tmp114.c:150:5: warning: assignment to ‘const struct i2c_device_id *’ from ‘int’ makes pointer from integer without a cast [-Wint-conversion]
    150 |  id = i2c_client_get_device_id(client);
        |     ^
    cc1: some warnings being treated as errors
    make[2]: *** [scripts/Makefile.build:286: /home/debian/play/tmp114.o] Error 1
    make[1]: *** [Makefile:1822: /home/debian/play] Error 2
    make[1]: Leaving directory '/usr/src/linux-headers-5.10.168-ti-arm64-r105'
    make: *** [Makefile:7: all] Error 2

Well, the good news is, it is compiling, that means it found the correct headers.  
But now the work begins converting to the tmp114.

Converting to the tmp114
^^^^^^^^^^^^^^^^^^^^^^^^

You are mostly on your own for this part, but here are some suggestions:

- First get it to compile without errors.  In this case, the function at line 150 isn't defined.
  Try commenting it out and recompiling.
- Once it's compiling without errors, try running it. First open another window and login to beagle.
  Then run:

  .. code-block:: bash

    bone$ dmesg -Hw

This will display the kernel messages.  The **-H** put them in *human* readable form, and the **-w** waits for 
more messages.

- Next, "insert" it in the running kernel:

.. code-block:: bash

    bone$ sudo insmod tmp114.ko 

If all worked you shouldn't see any messages, either after the command or in the dmesg window.
If you want to insert the module again, you will have to remove it first.
Remove with:
.. code-block:: bash

    bone$ sudo rmmod tmp114

Now we need to tell the kernel we have an |I2C| device and which bus and which address.

Finding your |I2C| device
^^^^^^^^^^^^^^^^^^^^^^^^^

Each |I2C| device appears at a certain address on a given bus.  My device is on bus 3,
so I run:

.. code-block:: bash

     i2cdetect -y -r 3
        0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
    00:                         -- -- -- -- -- -- -- --
    10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    40: -- -- -- -- -- -- -- -- -- -- -- -- -- 4d -- --
    50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    70: -- -- -- -- -- -- -- --

This shows there is a device at address **0x4d**. If you don't know your bus number, 
just try a few until you find it.

The temperature is in register 0 for my device and it's 16 bits (one word),
it is read with:

.. code-block:: bash

    bone$  i2cget -y 3 0x4d 0 w
    0xb510

The tmp114 swaps the two bytes, so the real temperature is **0x10b5**, or so.
You need to look up the datawsheet to learn how to comvert it.

Registers and IDs
^^^^^^^^^^^^^^^^^

Each |I2C| device has a number of internal registers that interact with the device.
The tmp114 uses different register numbers than the tmp117, so you need to change these values.
To do this, Google for the data sheets for each and look them up. 
I found them at: https://www.ti.com/lit/gpn/tmp114 and https://www.ti.com/lit/gpn/TMP117.

Creating a new device
^^^^^^^^^^^^^^^^^^^^^

Once you've converted the module for the tmp114 and inserted it, you can now create a new device.

.. code-block:: bash

    bone$ cd /sys/class/i2c-adapter/i2c-3
    bone$ sudo chgrp gpio *
    bone$ sudo chmod g+w *
    bone$ ls -ls
    total 0
    0 --w--w---- 1 root gpio 4096 Jun 22 18:24 delete_device
    0 lrwxrwxrwx 1 root root    0 Jan  1  1970 device -> ../../20030000.i2c
    0 drwxrwxr-x 3 root gpio    0 Jun 22 18:20 i2c-dev
    0 -r--rw-r-- 1 root gpio 4096 Jun 22 18:20 name
    0 --w--w---- 1 root gpio 4096 Jun 22 18:20 new_device
    0 lrwxrwxrwx 1 root root    0 Jan  1  1970 of_node -> ../../../../../firmware/devicetree/base/bus@f0000/i2c@20030000
    0 drwxrwxr-x 2 root gpio    0 Jun 22 18:20 power
    0 lrwxrwxrwx 1 root root    0 Jan  1  1970 subsystem -> ../../../../../bus/i2c
    0 -rw-rw-r-- 1 root gpio 4096 Jun 22 18:20 uevent

The first line changes to the directory to where we can create the new device.
The final **3** in the path is for bus **3**, your milage may vary.
We then change the group to **gpio** and give it write permission.
You only need to do this once.

Now make the device.

.. code-block:: bash

    bone$ echo tmp114 0x4d > new_device

Look in the demsg window and you should see:

.. code-block:: bash

    [Jun22 19:24] tmp114 3-004d: tmp114_identify id (0x1114)
    [  +0.000027] tmp114 3-004d: tmp114_probe id (0x1114)
    [  +0.000502] i2c i2c-3: new_device: Instantiated device tmp114 at 0x4d

It's been found! Let's see what it knows about it.

.. code-block:: bash

    bone$ iio_info
    Library version: 0.24 (git tag: v0.24)
    ...
            iio:device1: tmp114
                    1 channels found:
                            temp:  (input)
                            2 channel-specific attributes found:
                                    attr  0: raw value: 4257
                                    attr  1: scale value: 7.812500
                    No trigger on this device

I've left out some of the lines, at the bottom you see the tmp114, and
two values (**raw** and **scale**) that were read from it.  Let's read them ourselves.
Do an *ls* and you'll see a new directory, **3-004d**.  This is address 0x4d on bus 3,
just what we wanted.

.. code-block:: bash

    bone$ cd 3-004d/iio:device1
    bone$ ls
    dev  in_temp_raw  in_temp_scale  name  power  subsystem  uevent
    bone$ cat in_temp_raw
    4275

You'll have to look in the datasheet to learn how to convert the temperature.

If you try to run i2cget again, you'll get an error:

.. code-block:: bash

    bone$ i2cget -y 3 0x4d 0 w
    Error: Could not set address to 0x4d: Device or resource busy

This is because the module is using it.  Delete the driver and you'll have access again.

.. code-block:: bash

    bone$ echo 0x4d > /sys/class/i2c-adapter/i2c-3/delete_device
    bone$ i2cget -y 3 0x4d 0 w
    0x8e10

You should also see a message in dmesg.
