.. _beagleconnect-freedom-using-arduino-zephyr-template:

Using Arduino Zephyr Template 
##############################

Using this template you can run arduino code on your BeagleConnect Freedom.

.. todo::

    Add pin diagram for BeagleConnect Freedom that can be used in the template.

Setup Arduino workspace
***********************

If this is your first time using zephyr, `Install Zephyr SDK <https://docs.zephyrproject.org/latest/develop/getting_started/index.html#install-the-zephyr-sdk>`_  and install ``cc1352-flasher`` 
using command ``pip install cc1352-flasher`` before following the steps below.

1. Create a workspace folder:

.. code:: shell-session

    mkdir arduino-workspace
    cd arduino-workspace

2. Setup virtual environment

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
which contains your arduino code. The default code prints ``Hello World`` on the serial monitor. 

.. code:: shell-session

    nano arduino-workspace/arduino-zephyr-template/src/main.cpp

main.cpp

.. code:: shell-session
   :caption: main.py

    #include <Arduino.h>

    void setup() {
        Serial.begin(115200);
    }

    void loop() {
        Serial.println("Hello World");
        delay(5000);
    }

Press ``CTRL+O`` and ``ENTER`` to save, ``CTRL+X`` to exit.

.. important::
    
    You must start your ``main.cpp`` code with ``#include <Arduino.h>``.

Build the Arduino directory
===========================

Before flashing, run the command below to build the ``arduino-zephyr-template`` for the board 
``beagleconnect_freedom``.

.. code:: shell-session

    west build -b beagleconnect_freedom arduino-zephyr-template -p

.. note:: 

    Only if you are following the steps from the beginning then the above command will work. 
    Otherwise, make sure that you are in the ``arduino-workspace`` directory and setup
    virtual environment using command ``source .venv/bin/activate``.

Flash BeagleConnect Freedom
============================

Make sure that your BeagleConnect Freedom is connected with your linux system
via USB.

.. code:: shell-session

    west flash

Serial Output
=============

Considering your BeagleConnect Freedom is connected to ``/dev/ttyACM0`` you can see the serial output coming from your BeagleConnect Freedom.

.. code:: shell-session

    tio /dev/ttyACM0

Arduino blink code running on BeagleConnect Freedom
***************************************************

For BeagleConnect Freedom LNK LED will work as ``LED_BUILTIN`` in Arduino code.

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

Finally, flash using below command. The LNK LED of BeagleConnect will start blinking after flashing
is complete.

.. code:: shell-session

    west flash
