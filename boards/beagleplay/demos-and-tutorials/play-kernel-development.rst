.. _play-kernel-development:

BeaglePlay Kernel Development
#############################

This guide is for all those who want to kick start their kernel development
journey on the TI AM625x SoC Based BeaglePlay.

Getting the Kernel Source Code
******************************

The Linux kernel is hosted on a number of servers around the world. The main
repository is hosted on the kernel.org website, but there are also mirrors
hosted by other organizations, such as GitHub and Bootlin.

The `Linux Torvalds tree <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/>`_
is the most up-to-date source of the Linux kernel.
It is used by Linux distributions and other projects to build their own kernels.
The tree is also a popular destination for kernel developers who want to
contribute to the kernel.

Kernel sources can directly be fetched using ``git``:

.. code-block:: bash

        git clone https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git

A big advantage of using ``git`` to fetch the kernel sources is that you'll easily be able to manage your
changes, keeping track of what you might edit. If you are looking for a quicker way to download a single
version of the Linux kernel sources to get started, you might consider fetching a "tarball" using ``wget``.

.. code-block:: bash

       wget https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/snapshot/linux-6.6.tar.gz
       tar xf linux-6.6.tar.gz

.. note::

       While fetching a tarball with ``wget`` might be faster than fetching the full history with ``git``,
       the ability to track changes with ``git`` is significant.

For more information on using ``git``, see :ref:`beagleboard-git-usage`.

Preparing to Build
******************

These instructions should be valid on any Debian-based system, but were tested on a BeaglePlay itself.

.. code-block:: bash

        sudo apt update
        sudo apt install fakeroot build-essential libncurses-dev xz-utils libssl-dev flex libelf-dev bison

Configuring the Kernel
**********************

The easiest way to configure the kernel is to start with a configuration known to work. A running BeaglePlay
is a great source for that configuration, as it gets compiled into the running kernel.

.. note::

        If you don't have a BeaglePlay booted, you can copy a known good kernel configuration from the
        BeagleBoard.org Linux git repository at https://git.beagleboard.org/beagleboard/linux. On each release
        branch, the last commit typically contains a ``bb.org_defconfig`` file. For BeaglePlay, you should
        look for an ``arm64`` branch.

        Example: https://git.beagleboard.org/beagleboard/linux/-/blob/f47f74d11b19d8ae2f146de92c258f40e0930d86/arch/arm64/configs/bb.org_defconfig

Running on a BeaglePlay, you can configure your kernel using ``/proc/config.gz``. You'll also want
to ``make olddefconfig`` to update your config for the newer kernel. If you want to look at configuration
options that haven't previously been configured, then use ``make oldconfig`` instead. Once you've
got an initial configuration, you can edit the configuration various ways including ``make menuconfig``.

.. code-block:: bash

        zcat /proc/config.gz > .config
        make olddefconfig

You can also take advantage of the running system to provide the WiFi regulatory database (regulatory.db). This
is needed such that your kernel sets the WiFi signals appropriately for compliance with regional restrictions.

For more information, see `Linux wireless regulatory documentation <https://www.kernel.org/doc/html/latest/networking/regulatory.html>`_ and
the signed database images at https://git.kernel.org/pub/scm/linux/kernel/git/sforshee/wireless-regdb.git/tree/.

.. code-block:: bash

        mkdir -p firmware
        cp /lib/firmware/regulatory.db* firmware/

Building the Kernel
*******************

Once you're set on your configuration, you'll want to build the kernel and build any external modules.

.. note::

        Building the kernel on BeaglePlay might take a while. For me, it took about an hour.

.. code-block:: bash

        make

Installing and Booting the Kernel
*********************************

.. important::

        In case your new kernel fails, you'll want to be prepared to either reflash the board
        or to use a serial cable to halt u-boot and request loading a working kernel still
        available on the board.

        See :ref:`beagleplay-serial-console` to setup access over the debug serial port.

.. code-block:: bash

        sudo make install modules_install

References
**********

For more details on the Linux kernel build system, see `The kernel build system <https://www.kernel.org/doc/html/latest/kbuild/index.html>`_ on kernel.org.

For additional guidance, see the `official TI-SDK documentation for
AM62X <https://software-dl.ti.com/processor-sdk-linux/esd/AM62X/08_06_00_42/exports/docs/linux/Foundational_Components_Kernel_Users_Guide.html>`_
