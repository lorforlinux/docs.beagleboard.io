.. _beagley-ai-pwm:

.. note:: This page is a work in progress. Further testing and images will be added soon


Pulse Width Modulation (PWM)
#############################

What is it
************

PWM, or Pulse Width Modulation, is a technique used to control the amount of power delivered to an electronic device by breaking up the power signal into discrete ON and OFF periods. 
The amount of time the signal spends ON during each cycle determines the output power level (brightness of the LED).

.. image:: ../images/gpio/pwm.jpg
   :width: 50%
   :align: center


How do we do it
*****************

First we unbind the pin as GPIO 

.. code:: bash

    echo hat-08-gpio > /sys/bus/platform/drivers/gpio-aggregator/unbind

Now we override the driver

.. code:: bash

    echo gpio-aggregator > /sys/devices/platform/hat-08-pwm/driver_override 

Then we bind the pin

.. code:: bash

    echo hat-08-pwm > /sys/bus/platform/drivers/gpio-aggregator/bind

.. todo:: Add note about matching PWM channel to Pin

Let's write a script called **fade.sh** that contains the following:

.. code:: bash

    #!/bin/bash

    PWMPIN="/sys/devices/platform/bus@f0000/23000000.pwm/pwm/pwmchip3/pwm1"


    echo 1000 > $PWMPIN/period
    echo 0 > $PWMPIN/duty_cycle
    echo 0 > $PWMPIN/enable
    sleep 1

    for i in {1..500};
    do
	    echo $i > $PWMPIN/duty_cycle
	    echo 1 > $PWMPIN/enable
	    echo $i
	    sleep 0.0005
    done

    for i in {500..1};
    do
        echo $i > $PWMPIN/duty_cycle
        echo 1 > $PWMPIN/enable
        echo $i
        sleep 0.0005
    done

Now execute it by typing:

.. code:: console

   bash shade.sh

.. image:: ../images/gpio/pwm.gif
   :align: center

.. todo:: Add section about driving Servo Motors at 50KHz

Troubleshooting
*******************


Going Further
*******************
