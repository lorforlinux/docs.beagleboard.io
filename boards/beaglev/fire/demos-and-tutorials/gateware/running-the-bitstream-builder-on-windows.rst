.. _beagleV-fire-gateware-builder:

How to build the BeagleV-Fire gateware builder (bitstream-builder) on Windows
#############################################################################

Introduction
============
The BeagleV Fire gateware builder is a Python script that builds both the PolarFire SoC HSS bootloader and Libero FPGA project into a single programming bitstream. 
It uses a list of repositories/branches specifying the configuration of the BeagleV Fire to build.

Prerequisites
=============

repository
------------
BeagleV-Fire gateware builder: https://openbeagle.org/cyril-jean/gateware-maintenance/ 


.. note::
    If during the build process you encounter an end of line error (CRLF/LF), change the following local git configuration *core.autocrlf* to false and clone the repo again


    .. code-block::

        git config --global core.autocrlf false


To build the bitstream on windows we will need to have following tools installed in the system, and once done go to the repository linked above and follow the readme


Tools
-----------

- Msys2-Mingw
- Make 
- wsl

Msys2 installation link and guide https://www.msys2.org/wiki/MSYS2-installation/

When installing *make* in your mysys2 terminal you're recommended to use the default command 

.. code-block:: 

    pacman -S make

However some of you may need/want to install a specific *make* , use the following guide as https://www.msys2.org/wiki/Porting/

.. code-block::

    pacman -S <target>-make

Now its important to add the *msys2* bin path to you systems environmental variable PATH "*C:\\msys64\\usr\\bin*".


wsl (Windows subsystem for linux) needs to be enabled and configured. To enable wsl *Windows start menu > Turn Windows features on or off* enable Windows Subsystem for Linux and click ok. Now open a command prompt as an admin and run...

.. code-block::

    wsl.exe --install

.. note::  
    - If the build fails due to it noting finding a python package, even though it is already installed. this could be due to having multiple versions of python/pip installed. try to install the packages again using the following command.

    .. code-block::
        
        python -m pip install <package-name>

    - When setting up the product licenses ensure that the environmental variable *LM_LICENSE_FILE* contains the license to all of the programs, otherwise this can lead to a silent error when building.




