..
    BeagleBoard projects Blink LED demo

.. _blinkLED:

Blink LED
#########

The "Hello World!" of the embedded world is to blink and LED. 
Here we'll show you hw to do just that in three simple steps. 

#. Plug in the Beagle
#. Log into the Beagle
#. Blink the LED

These steps will work for any of the Beagles.

Plug in the Beagle
------------------

For this step you need to get a USB cable and attached your Beagle 
to your host computer with it.
Once attached you will see some LEDs blinking.
Wait a bit and the blinks will settle down to a steady
heart beat.

The Beagle is now up and running, but you didn't have to 
load up Linux.  This is because all Beagles 
(except the PocketBeagle) have built-in flash memory 
that has the Debian distribution of Linux preinstalled.

Login
-----

Next you login to the Beagle from your host computer. 
This is slightly different if you host is running Windows.

Login from Windows
^^^^^^^^^^^^^^^^^^

If you are running Window you need to run an ``ssh`` client 
to connect to the Beagle. I suggest you use ``putty``. 
You can download it here: https://www.putty.org/. 
Once installed, launch it and connect to your Beagle 
by sshing to ``192.168.7.2``.  Login with user ``debian`` 
and password ``temppwd``.  

Login from Linux
^^^^^^^^^^^^^^^^

If you are running a Linux host, open a terminal widow and run 

.. code-block:: shell-session

    host:~$ ssh debian@192.168.7.2

Use password ``temppwd``.

Blink the LED
-------------

One logged in the rest is easy.  First:

.. code-block:: shell-session

    bone:~$ cd /sys/class/LEDs
    bone:~$ ls
    beaglebone:green:usr0  beaglebone:green:usr2  mmc0::
    beaglebone:green:usr1  beaglebone:green:usr3  mmc1::
   
Here you see a list of LEDs. Your list may be slightly 
different depending on which Beagle you are running. 
You can blink any of them.  Let's try usr1.

.. code-block:: shell-session
    
    bone:~$ cd beaglebone\:green\:usr1/
    bone:~$ ls
    brightness  device  max_brightness  power  subsystem  trigger  uevent
    bone:~$ echo 1 > brightness
    bone:~$ echo 0 > brightness

When you echo 1 into ``brightness`` the LED turns on. 
Echoing a 0 turns it off.  Congratulations! you've blinked 
your first LED.
