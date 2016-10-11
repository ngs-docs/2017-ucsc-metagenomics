**************************************************
Log into your instance from a Mac or Linux machine
**************************************************

You'll need to do two things: first, set the permissions on
``amazon-key.pem``::

   chmod og-rwx ~/Downloads/amazon-key.pem

Then, ssh into your new machine using your key::

   ssh -i ~/Downloads/amazon-key.pem -l ubuntu MACHINE_NAE

where you should replace MACHINE_NAME with the public IP or hostname
of your EC2 instance, which is located at the top of the host
information box (see screenshot below).  It should be something like
``54.183.148.114`` or ``ec2-XXX-YYY.amazonaws.com``.

Here are some screenshots!

Change permissions and execute ssh
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. thumbnail:: images/boot-10.png
   :width: 20%

Successful login
~~~~~~~~~~~~~~~~

.. thumbnail:: images/boot-11.png
   :width: 20%

Host information box - MACHINE_NAME location
============================================

.. thumbnail:: images/boot-9.png
   :width: 20%

----

Logging in is the starting point for most of the follow-on tutorials.
For example, you can now install and run software on your EC2 instance.

Go back to the top page to continue: :doc:`index`

