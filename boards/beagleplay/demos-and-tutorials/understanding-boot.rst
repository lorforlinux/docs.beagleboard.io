.. _play-understanding-boot:

Understanding Boot
##################

There are several phases to BeaglePlay boot. The simplest place to take control of
the system is using :ref:`play-distro-boot`. It is simplest because it is very generic,
not at all specific to BeaglePlay or AM62, and was included in the earliest BeagleBoard.org Debian
images shipping pre-installed in the on-board flash.

Over time, BeaglePlay images will include `SystemReady
support <https://www.arm.com/architecture/system-architectures/systemready-certification-program>`_ to
provide for the most generic boot support allowing execution of 

.. _play-distro-boot:

Distro Boot
***********

For some background on distro boot, see `the u-boot documentation on
distro boot <https://docs.u-boot.org/en/latest/develop/distro.html>`_.
