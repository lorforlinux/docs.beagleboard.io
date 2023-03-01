.. _beagleplay-change-history:

Change History
###############

.. note:: 
    This section describes the change history of this document and board. 
    Document changes are not always a result of a board change. A board 
    change will always result in a document change.

.. _beagleplay-document-changes:

Document Changes
******************

.. _beagleplay-board-changes:

Board Changes
**************

.. table:: BeaglePlay Board change history

    +---------+------------------------------------------------------------+----------------------+-------+
    | Rev     |   Changes                                                  | Date                 |    By |
    +=========+============================================================+======================+=======+
    | 0.20    | DVT1 Board release                                         | September 15th 2022  | qxn   |
    +---------+------------------------------------------------------------+----------------------+-------+
    | 0.21    | 1. Modify all crystal CL value to match frequency          | November 10th 2022   | qxn   |
    |         | 2. Add serial termination resistors for RGB data lane      |                      |       |
    |         | 3. Add CMC on HDMI output                                  |                      |       |
    |         | 4. Use WKUP_CLKOUT0 for WiFi                               |                      |       |
    |         | 5. Use MCU_OBSCLK0 for GBE                                 |                      |       |
    |         | 6. Increase resistance on all board LEDs                   |                      |       |
    |         | 7. Remove R243 TP_INT Pulldown                             |                      |       |
    |         | 8. Add ferrite bead on Grove and QWIIC                     |                      |       |
    |         | 9. Add feed forward capacitor on TLV62595                  |                      |       |
    |         | 10. Remove ESDs on HDMI TMDS signals                       |                      |       |
    +---------+------------------------------------------------------------+----------------------+-------+
    | 0.22    | 1. Add feed forward capacitor on TLV62595                  | December 12th 2022   | qxn   |
    |         | 2. Remove ESDs on HDMI TMDS signals                        |                      |       |
    |         | 3. Add ferrite bead on HDMI shield                         |                      |       |
    |         | 4. Change R16 and R80 to 0R                                |                      |       |
    |         | 5. Change pullup resistors to 2.2k on I2C0-I2C3            |                      |       |
    |         | 6. Change FB30 and FB31 to 0R                              |                      |       |
    +---------+------------------------------------------------------------+----------------------+-------+
    | 1.0     | 1. Add testpoint to QWIIC                                  | December 27th 2022   | qxn   |
    |         | 2. Add serial resistors on I2C0 - I2C3 SCL                 |                      |       |
    |         | 3. Add more capacitors on VDD_1V2                          |                      |       |
    |         | 4. Add 0R on HDMI shield                                   |                      |       |
    |         | 5. Add series resistor on SPE LED control                  |                      |       |
    +---------+------------------------------------------------------------+----------------------+-------+