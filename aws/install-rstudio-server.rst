***********************************
Running RStudio Server in the cloud
***********************************

In this section, we will run RStudio Server on a remote Amazon machine.
This will require starting up an instance, configuring its network firewall,
and installing and running some software.

.. @@remember to terminate
.. @@can we reboot and have it sart up again?
.. @@diagram laying out zone etc.

Reference documentation for running RStudio Server on Ubuntu:

   https://www.rstudio.com/products/rstudio/download-server/

-----

1. Start up an Amazon instance
------------------------------

Start an ami-05384865 on an m4.xlarge machine, as per the instructions here:

:doc:`boot`.

2. Configure your network firewall
----------------------------------

Normally, Amazon computers only allow shell logins via ssh.
Since we want to run a Web service, we need to give the outside world
access to other network locations on the computer.

Follow these instructions:

:doc:`configure-firewall`

(You can do this while the computer is booting.)

3. Log in via the shell
-----------------------

Follow these instructions to log in via the shell:

:doc:`login-shell`.

4. Set a password for the 'ubuntu' account
------------------------------------------

Amazon Web Services computers normally require a key (the .pem file)
instead of a login password, but RStudio Server will need us to log in
with a password.  So we need to configure a password for the account
we're going to use (which is 'ubuntu')

Create a password like so::
  
     sudo passwd ubuntu

and set it to something you'll remember.

5. Install R and the gdebi tool
-------------------------------

.. @@ reference debian install instructions https://help.ubuntu.com/community/AptGet/Howto and https://www.debian.org/doc/manuals/debian-faq/ch-pkgtools.en.html

Update the software catalog and install a few things::

     sudo apt-get update && sudo apt-get -y install gdebi-core r-base

This will take a few minutes.

6. Download & install RStudio Server
------------------------------------

::
   
     wget https://download2.rstudio.org/rstudio-server-0.99.891-amd64.deb
     sudo gdebi -n rstudio-server-0.99.891-amd64.deb

Upon success, you should see::

   Mar 07 15:20:18 ip-172-31-6-68 systemd[1]: Starting RStudio Server...
   Mar 07 15:20:18 ip-172-31-6-68 systemd[1]: Started RStudio Server.

7. Open your RStudio Server instance
------------------------------------

Finally, go to 'http://' + your hostname + ':8787' in a browser,
eg. ::

   http://ec2-XX-YY-33-165.us-west-1.compute.amazonaws.com:8787/

and log into RStudio with username 'ubuntu' and the password
you set it to above.

Voila!

----

You can now just go ahead and use this, or you can "stop" it, or you
can freeze into an AMI for later use.

Note that on reboot, RStudio Server will start up again and all your files
will be there.

Go back to the index: :doc:`index`.

.. @@CTB demonstrate graphing, etc.
.. revisiting what we did...

.. @@ rebooting; converting to AMI
   
.. @@ meditations on file transfer
