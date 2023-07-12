.. _beaglev-ahead-quick-start:

Quick Start
################

What's included in the box?
****************************

When you purchase a brand new BeagleV Ahead, In the box you'll get:

1. BeagleV Ahead board
2. One (1) 2.4GHz/5GHz antenna
3. microUSB OTG cable
4. Quick-start card

.. image:: media/BeagleV-Ahead-all.*
    :width: 724
    :align: center
    :alt: BeaglePlay box contents

Unboxing
*********

.. only:: latex
    
   .. image:: https://img.youtube.com/vi/SVC9peUUzE0/maxresdefault.jpg
      :alt: BeagleV Ahead Unboxing YouTube video
      :width: 1280
      :target: https://www.youtube.com/watch?v=SVC9peUUzE0

.. only:: html

    .. raw:: html

        <iframe style="display: block; margin: auto;" width="1280" height="720" style="align:center" 
        src="https://www.youtube.com/embed/SVC9peUUzE0" 
        title="YouTube video player" 
        frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
        allowfullscreen>
        </iframe>


Antenna guide
*************

.. warning:: uFL antenna connectors are very delicate and should be handled with care.

.. tabs::

   .. group-tab:: Connecting antenna

      To use WiFi you are **required** to connect the 2.4GHz/5GHz antenna provided 
      in BeagleV Ahead box. Below is a guide to connect the antenna to your 
      BeagleV Ahead board.

      .. figure:: media/antenna-guide/connect.*
          :align: center
          :alt: Connecting 2.4GHz/5GHz antenna to BeagleV Ahead.

          Connecting 2.4GHz/5GHz antenna to BeagleV Ahead.

   .. group-tab:: Disconnecting antenna


      If for some reason you want to disconnect the antenna from your BeagleV Ahead board 
      you can follow the guide below to remove the antenna without beaking the uFL antenna connector.

      .. figure:: media/antenna-guide/disconnect.*
          :align: center
          :alt: Removing 2.4GHz/5GHz antenna to BeagleV Ahead.

          Removing 2.4GHz/5GHz antenna to BeagleV Ahead.

Tethering to PC
****************

To connect the board to PC via USB 3.0 port you can use either a standard microUSB cable 
or a USB 3.0 microB cable. Connection guide for both are shown below:

.. warning:: microUSB will support only USB 2.0 speeds but microB cable will support USB 3.0 super speed connection.

.. tabs::

   .. group-tab:: microB connection (USB 3.0 super speed)

      For super speed USB 3.0 connection it's recommended to use microB USB cable.  
      To get a microB cable you can checkout links below:

      1. `USB 3.0 Micro-B Cable - 1m (sparkfun) <https://www.sparkfun.com/products/14724>`_
      2. `Stewart Connector microB (DigiKey) <https://www.digikey.com/en/products/detail/stewart-connector/SC-3ATK003F/8544565>`_
      3. `CNC Tech microB (DigiKey) <https://www.digikey.com/en/products/detail/cnc-tech/103-1092-BL-00100/5023751>`_
      4. `Assmann WSW Components microB (DigiKey) <https://www.digikey.com/en/products/detail/assmann-wsw-components/A-USB30AM-30MBM-200/10408379>`_

      .. note:: If you only have a microUSB cable you can checkout microUSB connection guide.

      .. figure:: media/usb-guide/microB-connection.*
          :align: center
          :alt: microB (USB 3.0) connection guide for BeagleV Ahead.
          
          microB (USB 3.0) connection guide for BeagleV Ahead.

   .. group-tab:: microUSB connection (USB 2.0)


      For USB 2.0 connection it's recommended to use microUSB USB cable.  
      To get a microUSB cable you can checkout links below:

      1. `USB micro-B Cable - 6 Foot (sparkfun) <https://www.sparkfun.com/products/10215>`_
      2. `Stewart Connector microUSB (DigiKey) <https://www.digikey.com/en/products/detail/stewart-connector/SC-2AMK003F/8544577>`_
      3. `Assmann WSW Components microUSB  (DigiKey) <https://www.digikey.com/en/products/detail/assmann-wsw-components/AK67421-0-3-VM/5428793>`_
      4. `Cvilux USA microUSB (DigiKey) <https://www.digikey.com/en/products/detail/cvilux-usa/DH-20M50055/13175849>`_

      .. note:: Make sure the microUSB cable you have is a data cable as some microUSB cables are power only.        

      .. figure:: media/usb-guide/microUSB-connection.*
          :align: center
          :alt: microUSB (USB 2.0) connection guide BeagleV Ahead.

          microUSB (USB 2.0) connection guide BeagleV Ahead.

Flashing eMMC
**************

To flash your BeagleV Ahead you need either a microB or microUSB cable as shown in section above.

.. note:: Only microB is shown in graphic below but you can use 
    a microUSB cable. Only difference will be lower flash speeds.

To put your BeagleV Ahead board into eMMC flash mode you can follow the steps below:

1. Press and hold USB button.
2. Connect to PC with microB or microUSB cable.
3. Release USB button.

.. figure:: media/usb-guide/Flash-eMMC.*
    :align: center
    :alt: Connecting BeagleV Ahead to flash eMMC

    Connecting BeagleV Ahead to flash eMMC

.. important:: If you want to put the board into eMMC flashing while it is already 
    connected to a PC you can follow these steps:

    1. Press and hold USB button.
    2. Press reset button once.
    3. Release USB button.

Demos and Tutorials
*******************


