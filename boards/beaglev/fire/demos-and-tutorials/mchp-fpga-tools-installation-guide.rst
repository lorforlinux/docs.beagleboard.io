.. _beaglev-fire-mchp-fpga-tools-installation-guide:

Microchip FPGA Tools Installation Guide
#########################################

Instructions for installing the Microchip FPGA tools on a Ubuntu 20.04 desktop.

.. important::

   We will be providing instances of Libero that you can run from git.beagleboard.org's gitlab-runners such that you do not need to install the tools on
   your local machine.

.. todo::

   Make sure people know about the alternative and we provide links to details on that before we send them down this process.

Install Libero 2022.3
************************

- Download installer from the `Microchip's fpga and soc design tools section <https://www.microchip.com/en-us/products/fpgas-and-plds/fpga-and-soc-design-tools/fpga/libero-software-later-versions>`_.
- Install Libero

.. code-block::

  unzip Libero_SoC_v2022.3_lin.zip

  cd Libero_SoC_v2022.3_lin/

  ./launch_installer.sh

.. important:: 
    Do not use the default location suggested by the Libero installer. 
    Instead of /usr/local/Microchip/Libero_SoC_v2022.3 install into ~/Microchip/Libero_SoC_v2022.3
    
Run the post installation script which will install missing packages:

.. code-block::

  sudo /home/<USER-NAME>/Microchip/Libero_SoC_v2022.3/Logs/req_to_install.sh

No need to run the FlashPro hardware installation scripts. This will be taken care of as part of the SoftConsole installation.

Install SoftConsole 2022.2
***************************

- Download intaller from `Microchip website <https://www.microchip.com/en-us/products/fpgas-and-plds/fpga-and-soc-design-tools/soc-fpga/softconsole>`_.

.. code-block::

  sudo chmod +x Microchip-SoftConsole-v2022.2-RISC-V-747-linux-x64-installer.run

  ./Microchip-SoftConsole-v2022.2-RISC-V-747-linux-x64-installer.run

Accept the license, Click Forward, Finish.

Perform the post installation steps as described in the html file opened when you click Finish.

.. important:: 

  Please pay special attention to the "Enabling non-root user to access FlashPro" section of the post-installation instructions. 
  This will actually allow you to program the board using Libero.

Install the Libero licensing daemon
************************************

Download the 64 bit Licensing Daemons from the `Microchip's daemons section <https://ww1.microchip.com/downloads/aemdocuments/documents/fpga/media-content/FPGA/daemons/Linux_Licensing_Daemon_11.16.1_64-bit.tar.gz>`_


Copy the downloaded file to the Microchip directory within your home directory and untar it.

.. code-block::

  cd ~/Microchip

  tar -xvf Linux_Licensing_Daemon_11.16.1_64-bit.tar.gz


Install the Linux Standard Base:

.. code-block:: 

  sudo apt-get update

  sudo apt-get -y install lsb


Request a Libero Silver license
********************************

- Visit `microchip's fpga and soc design tool licensing page <www.microchip.com/en-us/products/fpgas-and-plds/fpga-and-soc-design-tools/fpga/licensing>`_
- Click on Register a free license button and Register or login.
- Click "Request Free License" and choose "Libero Silver 1Yr Floating License for Windows/Linux Server" from the list.
- Enter you MAC address and click register. 
  
.. note::
    
    A MAC address looks something like 12:34:56::78:ab:cd when you use the "ip address" command to find out 
    its value on your Linux machine. However, you need to enter it as 123456abcd in this dialog box.

You will get an email with a license.dat file. Copy it into the ~/Microchip/license directory. Edit the License.dat file to replace the <put.hostname.here> string with... localhost.

Download tool setup script
***************************

.. code-block:: 

  git clone https://git.beagleboard.org/beaglev-fire/Microchip-FPGA-Tools-Setup


Source the script:

.. code-block::

  . ./setup-microchip-tools.sh

.. important:: 
  
  Do not forget the leading dot. It matters. You will need to run this every time you restart your machine.

You can then start Libero to open an existing Libero project.

.. code-block:: 

  libero

However you will more than likely want to use Libero to run a TCL script that will build a design for you.

.. code-block:: 
    
  libero SCRIPT:BUILD_A_DESIGN.tcl
