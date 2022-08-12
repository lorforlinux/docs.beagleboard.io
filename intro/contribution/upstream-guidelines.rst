.. _beagleboard-contribute:

Upstream Kernel Contributions
#########

.. note::
    For detailed information on Kernel Developmement checkout the official
    `kernel.org <https://www.kernel.org/doc/html/latest/>`_
    kernel docs.

For a person or company who wishes to submit a change to the Linux kernel,
the process can sometimes be daunting if you’re not familiar with “the system.”
This text is a collection of suggestions which can help you get started and greatly increase the chances
of your change being accepted.

.. note:: This version is an unofficial draft and is subject to change.

Pre-requisites
---------------

The following are the skills that are needed before you actually start to contribute to the linux kernel:
    - git
    - C-Programming
    - Cross-arch Development
    - Basics of embedded buses (I2C, UART, SPI, etc.)
    - Device Trees
    - Drivers in Embedded Systems

More Git!
---------

It is highly recommended that you go through
`Git Usage <https://docs.beagleboard.io/contribution/git-usage.html>`_ before starting
to read and follow these guidelines. You will need to have a proper git setup on your
computer inorder to effectively follow these steps.

Creating your first patch
*************************

When you first enter the world of Linux Kernel development from a background in
contributing over gitlab or github, the terminologies slightly change.

Your Pull Requests (PRs) now become Patches or Patch Series. You no longer just
go to some website and click on a "Create Pull Request" button. Whatever code/changes you
want to add will have to be sent as patches via emails.

As an example, let's consider a commit to add the git section to these docs.
I stage these changes first using ``git add -p``.

.. code-block::

    diff --git a/contribution/contribute.rst b/contribution/contribute.rst
    index def100b..0af08c5 100644
    --- a/contribution/contribute.rst
    +++ b/contribution/contribute.rst

Then, commit the above changes.

**Note:** Don't forget to make your commit message descriptive of the feature
you are adding or the work that you have done in that commit. The commit
has to be self explanatory in itself. Link any references if you have used
and paste any logs to prove your code works or if there is a fix.

.. code-block::

    git commit -vs

    [linux-contrib 3bc0821] contribute.rst: Add git section
     1 file changed, 27 insertions(+), 1 deletion(-)

Now, let's say we want to send this new feature to upstream kernel. You then have to create
a patch file using the following command:

.. code-block::

    git format-patch -1 HEAD

    0001-contribute.rst-Add-git-section.patch

This will generate one file that is generally referred to as the patch file.
This is what you will now be sending upstream inorder to get your patch merged.
But wait, there are a few more things we need to setup for sending a patch via e-mail.
That is, ofcourse your email!

For configuring your email ID for sending patches refer to this excellent stackoverflow thread,
`configure git-send-email
<https://stackoverflow.com/questions/68238912/how-to-configure-and-use-git-send-email-to-work-with-gmail-to-email-patches-to>`_.

Finally, after you have configured you email properly, you can send out a patch using:

.. code-block::
    git send-email 0001-contribute.rst-Add-git-section.patch

replacing ofcourse the above patchfile name with whatever was your own patch.
This command will then ask you ``To whom should the emails be sent (if anyone)?``
Here, you have to write the email address of the list you want to send out the patch to.

``git send-email`` also has command line options like ``--to`` and ``--cc`` that you can also use
to add more email addresses of whoever you want to keep in CC. Generally it is a good idea to keep yourself
in CC.