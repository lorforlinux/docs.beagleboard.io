.. _play-kernel-development:

Introduction
#############

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

Kernel sources can directly be fetched from GIT:

.. code-block:: bash

        git clone https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git

Preparing to Build
******************

.. todo::
        Add Compiler download link and env setup instructions

Configuring the Kernel
**********************

.. todo::
        Add steps to config kernel for play

Sources
*******

This documentation is heavily based on the `official TI-SDK documentation for
AM62X <https://software-dl.ti.com/processor-sdk-linux/esd/AM62X/08_06_00_42/exports/docs/linux/Foundational_Components_Kernel_Users_Guide.html>`_
