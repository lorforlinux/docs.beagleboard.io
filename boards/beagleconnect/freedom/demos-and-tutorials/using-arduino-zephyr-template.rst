.. _beagleconnect-freedom-using-arduino-zephyr-template:

Using Arduino Zephyr Template 
##############################

Using this template you can run arduino code on your BeagleConnect Freedom.

Setup Arduino workspace
***********************

If this is your first time using zephyr, `Install Zephyr SDK <https://docs.zephyrproject.org/latest/develop/getting_started/index.html#install-the-zephyr-sdk>`_  and install CC1352-FLASHER 
using command ``pip install cc1352-flasher`` before following the steps below.

1. Create a workspace folder:

.. code:: shell-session

    mkdir arduino-workspace
    cd arduino-workspace

2. Setup virtualenv

.. code:: shell-session

    python -m venv .venv
    source .venv/bin/activate
    pip install west

3. Setup Zephyr app:

.. code:: shell-session
    
    west init -m https://openbeagle.org/beagleconnect/arduino-zephyr-template .
    west update

4. Setup Arduino module

.. code:: shell-session
    
    ln -srf modules/lib/ArduinoCore-API/api modules/lib/Arduino-Zephyr-API/cores/arduino/.

5. Install python deps

.. code:: shell-session

    pip install -r zephyr/scripts/requirements-base.txt

Arduino Code
============

You can find ``main.cpp`` file in the directory ``arduino-workspace/arduino-zephyr-template/src/``
in which you can edit ``main.cpp`` with your arduino code. For now this file contains code which print ``Hello World``
on the serial monitor. Must add ``#include <Arduino.h>`` before writing your code.

.. code:: shell-session

    nano arduino-workspace/arduino-zephyr-template/src/main.cpp

main.cpp

.. code:: shell-session

    #include <Arduino.h>

    void setup() {
        Serial.begin(115200);
    }

    void loop() {
        Serial.println("Hello World");
        delay(5000);
    }

Press CTRL+O and ENTER to save, CTRL+X to exit.

Build
=====

Before flashing, Run the below command. 

.. code:: shell-session

    west build -b beagleconnect_freedom arduino-zephyr-template -p

.. note:: 

    If you are following the steps from the beginning then above command will work. 
    Otherwise make sure that you are in ``arduino-workspace`` directory and setup
    virtualenv using command ``source .venv/bin/activate``.

Flash
=====

Make sure that your BeagleConnect Freedom is connected with your linux system
via USB.

.. code:: shell-session

    west flash

.. note::

    If ``west flash`` gives you an error then add user to dialout group.

Serial Output
=============
you can see the serial output coming from your BeagleConnect Freedom.

.. code:: shell-session

    cd ~
    tio /dev/ttyACM0

Arduino Blink Code Running on BeagleConnect Freedom
***************************************************

For BeagleConnect Freedom LINK LED will work as ``LED_BUILTIN`` in arduino code.

First you have to modify ``main.cpp`` located in the directory  ``arduino-workspace/arduino-zephyr-template/src/``
created at the time of setup. 

main.cpp

.. code:: shell-session

    #include <Arduino.h>
    
    void setup() {
    // initialize digital pin LED_BUILTIN as an output.
    pinMode(LED_BUILTIN, OUTPUT);
    }

    // the loop function runs over and over again forever
    void loop() {
    digitalWrite(LED_BUILTIN, HIGH);  // turn the LED on (HIGH is the voltage level)
    delay(1000);                      // wait for a second
    digitalWrite(LED_BUILTIN, LOW);   // turn the LED off by making the voltage LOW
    delay(1000);                      // wait for a second
    }

Before Build and Flash, Activate virtual environment in the ``arduino-workspace`` directory which has been created earlier.

.. code:: shell-session

    source .venv/bin/activate

Now, execute the build command.

.. code:: shell-session

    west build -b beagleconnect_freedom arduino-zephyr-template -p

Make sure your BeagleConnect Freedom is connected to your linux system via USB.

Finally, flash using below command. The LINK LED of BeagleConnect will start blinking after flashing
is complete.

.. code:: shell-session

    west flash
