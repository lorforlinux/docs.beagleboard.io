.. _beagleplay-connect-wifi:

Connect WiFi
#############

wpa_gui
********

Simplest way to connect to WiFi is to use ``wpa_gui`` tool pre-installed on your BeaglePlay. 
Follow simple steps below to connect to any WiFi access point.

Step1. Starting wpa_gui
========================

You can start ``wpa_gui`` either from ``Applications > Internet > wpa_gui`` or double click on the ``wpa_gui`` desktop application shortcut.

.. figure:: images/wpa_gui_step1a.png
    :align: center
    :alt: Starting wpa_gui from Applications > Internet > wpa_gui

    Starting wpa_gui from Applications > Internet > wpa_gui

.. figure:: images/wpa_gui_step1b.png
    :align: center
    :alt: Starting wpa_gui from Desktop application shortcut

    Starting wpa_gui from Desktop application shortcut    

Step2. Understanding wpa_gui interface
=======================================

The ``wpa_gui`` interface is very simple to understand and use.

1. ``Adapter`` is the WiFi interface device, it should be ``wlan0`` (on-board WiFi) by default.
2. ``Network`` shows the WiFi access point ``SSID`` if you are connected to that network.
3. ``Current Status`` tab shows you network information if you are connected to any network.
    - Click on ``Connect`` to connect if not automatically done.
    - Click on ``Disconnect`` to disconnect/reset the connection.
    - Click on ``Scan`` to scan nearby WiFi access points.
4. ``Manage Network`` tab shows you all the saved networks and options to manage those.

.. figure:: images/wpa_gui_step2.png
    :align: center
    :alt: wpa_gui interface

    wpa_gui interface

Step3. Scanning & Connecting to WiFi access points
===================================================

To scan the WiFi access points around you, just click on ``Scan`` button availale under 
``wpa_gui > Current Status > Scan``.

.. figure:: images/wpa_gui_step3a.png
    :align: center
    :alt: Scanning WiFi access points

    Scanning WiFi access points

A new window will open up with,

1. SSID (WiFi name)
2. BSSID
3. Frequency
4. Signal strenght
5. flags

Now, you just have to double click on the Network you want to connect to as shown below.

.. note:: 
    SSIDs and BSSIDs are not fully visible in screenshot below 
    but you can change the column length to see the WiFi names better.

.. figure:: images/wpa_gui_step3b.png
    :align: center
    :alt: Selecting WiFi access point

    Selecting WiFi access point

Final step is to type your WiFi access point password under ``PSK`` input field and 
click on ``Add`` (as shown in screenshot below) which will automatically connect 
your board to WiFi (if password is correct). 

.. figure:: images/wpa_gui_step3c.png
    :align: center
    :alt: Connecting to WiFi access point

    Connecting to WiFi access point
