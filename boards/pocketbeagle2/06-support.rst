.. _pocketbeagle2-support:

Additional Support Information
##############################

All support for this design is through BeagleBoard.org community 
at `BeagleBoard.org forum <https://forum.beagleboard.org/tag/pocketbeagle2>`_.

.. _pocketbeagle2-certifications:

Certifications and export control
*********************************

Export designations
===================

* HS:
* US HS:
* EU HS:

.. _hardware-design:

Hardware Design
****************

You can find all PocketBeagle2 hardware files 
`here <https://openbeagle.org/pocketbeagle/pocketbeagle-2>`_ under the `design` folder.

Production board boot media
****************************

.. todo:: Add production image link with board revision information.

.. _software-updates:

Software Updates
******************

Follow instructions below to download the latest image for your PocketBeagle2:

1. Go to `BeagleBoard.org distro <https://www.beagleboard.org/distros>`_ page.
2. :ref:`filter-software-distribution-PB2` from dropdown and download the image.

.. _filter-software-distribution-PB2:

.. todo:: add distros page image selection for pocketbeagle2

.. tip::

   You can follow the :ref:`flash-latest-image` guide for more information on 
   flashing the downloaded image to your board.

To see what SW revision is loaded into the eMMC check `/etc/dogtag`.
It should look something like as shown in example below,

.. code-block:: shell

   root@BeagleBone:~# cat /etc/dogtag
   BeagleBoard.org Debian Bullseye Xfce Image 2022-01-14

.. _rma-support:

RMA Support
*****************

If you feel your board is defective or has issues, request an Return Merchandise Application (RMA) 
by filling out the form at http://beagleboard.org/support/rma . You will need the serial number and 
revision of the board. The serial numbers and revisions keep moving. Different boards can have different 
locations depending on when they were made. The following figures show the three locations of the serial 
and revision number.

.. _getting-help:

Getting Help
**************

If you need some up to date troubleshooting techniques, you can post your 
queries on link: `BeagleBoard.org forum <https://forum.beagleboard.org/tag/pocketbeagle2>`_

.. _pocketbeagle2-mechanical:

Mechanical Details
******************

.. _dimensions-and-weight:

Dimensions and Weight
======================

.. table:: Dimensions & weight

   +--------------------+----------------------------------------------------+
   | Parameter          | Value                                              |
   +====================+====================================================+
   | Size               |                                                    |
   +--------------------+----------------------------------------------------+
   | Max heigh          |                                                    |
   +--------------------+----------------------------------------------------+
   | PCB Size           |                                                    |
   +--------------------+----------------------------------------------------+
   | PCB Layers         |                                                    |
   +--------------------+----------------------------------------------------+
   | PCB Thickness      |                                                    |
   +--------------------+----------------------------------------------------+
   | RoHS compliant     |                                                    |
   +--------------------+----------------------------------------------------+
   | Gross Weight       |                                                    |
   +--------------------+----------------------------------------------------+
   | Net Weight         |                                                    |
   +--------------------+----------------------------------------------------+


