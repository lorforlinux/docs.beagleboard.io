.. _beaglev-fire-quick-start:

Quick Start
################

What's included in the box?
****************************

When you purchase a brand new BeagleV-Fire, In the box you'll get:

.. todo:: add image & information about box content.

Unboxing
*********

.. only:: latex
    
   .. image:: https://img.youtube.com/vi/5cylv1R-1mc/maxresdefault.jpg
      :alt: BeagleV Ahead Unboxing YouTube video
      :width: 1280
      :target: https://www.youtube.com/watch?v=5cylv1R-1mc

.. only:: html

    .. raw:: html

        <iframe style="display: block; margin: auto;" width="1280" height="720" style="align:center" 
        src="https://www.youtube.com/embed/5cylv1R-1mc" 
        title="YouTube video player" 
        frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
        allowfullscreen>
        </iframe>


Tethering to PC
****************

To connect BeagleV-Fire board to PC via USB Type C receptacle you need a USB type C cable. Connection guide for the same is shown below:
  
.. tip::

    To get a USB type C cable you can checkout links below:

    1. `USB C cable 0.3m (mouser) <https://www.mouser.com/ProductDetail/Adafruit/4474?qs=CUBnOrq4ZJz9F%2FNF%252BRRALQ%3D%3D>`_
    2. `USB C cable 1.83m (digikey) <https://www.digikey.com/en/products/detail/coolgear/USB3-AC2MB/16384570>`_

.. figure:: media/usb-guide/tethered-connection.*
    :align: center
    :alt: BeagleV-Fire tethered connection
    
    BeagleV-Fire tethered connection

Flashing eMMC
**************

Flash the latest image on eMMC
===============================


Access UART debug console
**************************

.. note:: 
    
    Some tested devices that are working good includes:

    1. `Adafruit CP2102N Friend - USB to Serial Converter <https://www.adafruit.com/product/5335>`_
    2. `Raspberry Pi Debug Probe Kit for Pico and RP2040 <https://www.adafruit.com/product/5699>`_

To access a BeagleV-Fire serial debug console you can connected a USB to UART 
to your board as shown below:

.. figure:: media/debug/BeagleV-Fire-UART-Debug.*
    :align: center
    :alt: BeagleV-Fire UART debug port connection

    BeagleV-Fire UART debug port connection

To see the board boot log and access your BeagleV-Fire's console you can use application like ``tio`` 
to access the console. If you are using Linux your USB to UART converter may appear as ``/dev/ttyUSB``. 
It will be different for Mac and Windows operatig systems. To find serial port for your system you can checkout 
`this guide <https://www.mathworks.com/help/supportpkg/arduinoio/ug/find-arduino-port-on-windows-mac-and-linux.html>`_.

.. code-block:: shell

    [lorforlinux@fedora ~] $ tio /dev/ttyUSB0 
    tio v2.5
    Press ctrl-t q to quit
    Connected

Demos and Tutorials
*******************

* :ref:`beaglev-fire-gateware-version`
* :ref:`beaglev-fire-flashing-board`
* :ref:`beaglev-fire-gateware-design`
* :ref:`beaglev-fire-mchp-fpga-tools-installation-guide`

