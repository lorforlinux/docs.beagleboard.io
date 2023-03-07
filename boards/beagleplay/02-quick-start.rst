.. _beagleplay-quick-start:

Quick Start Guide
####################

What's included in the box?
****************************

When you purchase a brand new BeaglePlay, In the box you'll get:

1. BeaglePlay board
2. A sub-GHz antenna
3. Three (3) 2.5GHz/5GHz antennas
4. Plastic standoff hardware
5. Quick-start card

.. image:: images/45fontall.png
    :width: 1400
    :align: center
    :alt: BeaglePlay box contents

Attaching antennas
******************

.. note::
   Attaching the antennas can be complicated. This is not the expected BeaglePlay
   experience and we hope to fix it in the future. This is necessary if you
   plan to use any of the wireless connectivity features.

.. important::
   Add documentation on attaching antennas here.

Tethering to PC
****************

.. tip:: 
    Checkout :ref:`beagleboard-getting-started` for,

    1. Updating to latest software.
    2. Power and Boot.
    3. Network connection.
    4. Browsing to your Beagle.
    5. Troubleshooting.

For tethering to your PC you'll need a USB-C to USB-A data cable.

.. figure:: images/tethered-connection.jpg
    :width: 1400
    :align: center
    :alt: Tethering BeaglePlay to PC

    Tethering BeaglePlay to PC

Access VSCode
****************

Once connected, you can browse to `192.168.7.2:3000 <http://192.168.7.2:3000>`_ to access the VSCode IDE 
to browse documents and start programming your BeaglePlay!

.. note::

   You may get a warning about an invalid or self-signed certificate. This is a limitation of
   not having a public URL for your board. If you have any questions about this, please as on
   https://forum.beagleboard.org/tag/play.

.. figure:: images/vscode.png
    :width: 1400
    :align: center
    :alt: BeaglePlay VSCode IDE (192.168.7.2:3000)

    BeaglePlay VSCode IDE (192.168.7.2:3000)


Demos and Tutorials
*******************

.. toctree::
   :maxdepth: 1

   demos-and-tutorials/using-serial-console
   demos-and-tutorials/connect-wifi
   demos-and-tutorials/using-grove
   demos-and-tutorials/using-mikrobus
   demos-and-tutorials/using-qwiic
   demos-and-tutorials/using-oldi
   demos-and-tutorials/using-csi
   demos-and-tutorials/zephyr-cc1352-development
