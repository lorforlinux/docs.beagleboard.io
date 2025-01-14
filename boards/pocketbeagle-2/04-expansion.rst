.. _pocketbeagle-2-expansion:

Expansion
############

.. _pocketbeagle-2-pinout-diagrams:

Pinout Diagrams
***************

PocketBeagle 2 ``P1`` & ``P2`` cape headers are designed to be compatible with PocketBeagle classic as much as possible. 
Below pinout diagrams are design to simplify cape header pin usage and cape design process for PB2. To start 
using P1 / P2 cape header choose respective pinout diagram tab below.

.. tab-set::

   .. tab-item:: P1 cape header

        .. todo: Add PB2 P1 cape header pinout

   .. tab-item:: P2 cape header

        .. todo: Add PB2 P2 cape header pinout

.. _pocketbeagle-2-connectors:

Cape Header Connectors
**********************

Beagle cape expansion interface on PocketBeagle 2 like other Beagles is comprised of two 
headers P1 & P2. All signals on the expansion headers are **3.3V** unless 
otherwise indicated. **On some of the cape header pins on PocketBeagle 2 multiple SoC pins are shorted and 
only one of them should be used at a time.** Information regarding the double/shorted pins is provided 
in the :ref:`pocketbeagle-2-pinout-diagrams` above (simplified) and cape header pin tables below (detailed).

.. danger:: 
    Do not connect 5V logic level signals to these pins or the board will be damaged.

    **NO PINS ARE TO BE DRIVEN UNTIL AFTER THE SYS_RESET LINE GOES HIGH. DO NOT APPLY 
    VOLTAGE TO ANY I/O PIN WHEN POWER IS NOT SUPPLIED TO THE BOARD. 
    IT WILL DAMAGE THE PROCESSOR AND VOID THE WARRANTY.**

Connector P1
==============

The following tables show the pinout of the **P1** expansion header. The
SW is responsible for setting the default function of each pin. Refer to
the processor documentation for more information on these pins and
detailed descriptions of all of the pins listed. In some cases there may
not be enough signals to complete a group of signals that may be
required to implement a total interface.

The column heading is the pin number on the expansion header.

The **GPIO** row is the expected gpio identifier number in the Linux
kernel. 

Each row includes the gpiochipX and pinY in the format of 
`X Y`. You can use these values to directly control the GPIO pins with the 
commands shown below.

.. code:: bash

    # to set the GPIO pin state to HIGH
    debian@BeagleBone:~$ gpioset X Y=1

    # to set the GPIO pin state to LOW
    debian@BeagleBone:~$ gpioset X Y=0

    For Example:

    +---------+----------+
    | Pin     | P1.03    |
    +=========+==========+
    | GPIO    | 1 20     |
    +---------+----------+

    Use the commands below for controlling this pin (P1.03) where X = 1 and Y = 20

    # to set the GPIO pin state to HIGH
    debian@BeagleBone:~$ gpioset 1 20=1

    # to set the GPIO pin state to LOW
    debian@BeagleBone:~$ gpioset 1 20=0

The **BALL** row is the pin number on the processor.

The **REG** row is the offset of the control register for the processor
pin.

The **MODE #** rows are the mode setting for each pin. Setting each mode
to align with the mode column will give that function on that pin.


.. important::

    **DO NOT APPLY VOLTAGE TO ANY I/O PIN WHEN POWER IS NOT SUPPLIED TO THE
    BOARD. IT WILL DAMAGE THE PROCESSOR AND VOID THE WARRANTY.**

    **NO PINS ARE TO BE DRIVEN UNTIL AFTER THE SYS_RESET LINE GOES HIGH.**

P1.02-P1.03
-------------

+------------+--------------------------+-----------------+------------------+
| Pin        | P1.02                    | P1.02A          | P1.03            |
+============+==========================+=================+==================+
| GPIO       | 1 10                     | 0 87            | 1 51             |
+------------+--------------------------+-----------------+------------------+
| BALL       | E18                      | AA19            | F18              |
+------------+--------------------------+-----------------+------------------+
| REG        | MCASP0_AXR0              | RGMII2_TX_CTL   | USB1_DRVVBUS     |
+------------+--------------------------+-----------------+------------------+


P1.04-P1.06
-------------

+------------+------------------+------------------+------------------+------------------+
| Pin        | P1.04            | P1.04A           | P1.06            | P1.06A           |
+============+==================+==================+==================+==================+
| GPIO       | 1 12             | 0 89             | 1 13             | 0 78             |
+------------+------------------+------------------+------------------+------------------+
| BALL       | D20              | Y18              | E19              | AD18             |
+------------+------------------+------------------+------------------+------------------+
| REG        | MCASP0_AFSX      | RGMII2_TD0       | MCASP0_AFSR      | RGMII1_TD3       |
+------------+------------------+------------------+------------------+------------------+

.. todo:: Add complete P1 cape header pin tables

Connector P2
==============

The following tables show the pinout of the **P2** expansion header. The
SW is responsible for setting the default function of each pin. Refer to
the processor documentation for more information on these pins and
detailed descriptions of all of the pins listed. In some cases there may
not be enough signals to complete a group of signals that may be
required to implement a total interface.

The column heading is the pin number on the expansion header.

The **GPIO** row is the expected gpio identifier number in the Linux
kernel.

Each row includes the gpiochipX and pinY in the format of 
`X Y`. You can use these values to directly control the GPIO pins with the 
commands shown below.

.. code:: shell-session

    # to set the GPIO pin state to HIGH
    debian@BeagleBone:~$ gpioset X Y=1

    # to set the GPIO pin state to LOW
    debian@BeagleBone:~$ gpioset X Y=0

    For Example:

    +---------+----------+
    | Pin     | P2.11    |
    +=========+==========+
    | GPIO    | 1 1      |
    +---------+----------+

    Use the commands below for controlling this pin (P2.11) where X = 1 and Y = 1

    # to set the GPIO pin state to HIGH
    debian@BeagleBone:~$ gpioset 1 20=1

    # to set the GPIO pin state to LOW
    debian@BeagleBone:~$ gpioset 1 20=0

The **BALL** row is the pin number on the processor.

The **REG** row is the offset of the control register for the processor
pin.

The **MODE #** rows are the mode setting for each pin. Setting each mode
to align with the mode column will give that function on that pin.

If included, the **2nd BALL** row is the pin number on the processor for
a second processor pin connected to the same pin on the expansion
header. Similarly, all row headings starting with **2nd** refer to data
for this second processor pin.

.. important::

    **DO NOT APPLY VOLTAGE TO ANY I/O PIN WHEN POWER IS NOT SUPPLIED TO THE
    BOARD. IT WILL DAMAGE THE PROCESSOR AND VOID THE WARRANTY.**

    **NO PINS ARE TO BE DRIVEN UNTIL AFTER THE SYS_RESET LINE GOES HIGH.**


.. todo:: Add P2 cape header pin details.
