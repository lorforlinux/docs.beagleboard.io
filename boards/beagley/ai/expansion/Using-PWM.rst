.. _beagley-ai-pwm:

.. note:: This page is a work in progress. Further testing and images will be added soon


Pulse-Width Modulation (PWM)
#############################

First we unbind the pin as GPIO 

echo hat-08-gpio > /sys/bus/platform/drivers/gpio-aggregator/unbind

Now we override the driver

echo gpio-aggregator > /sys/devices/platform/hat-08-pwm/driver_override 

Then we bind the pin

echo hat-08-pwm > /sys/bus/platform/drivers/gpio-aggregator/bind


cd ./pwm1/ ;\
echo 1000 > period ;\
echo 500 > duty_cycle ;\
echo 1 > enable


Troubleshooting
*******************


Going Further
*******************
