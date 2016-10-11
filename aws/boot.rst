**************************************
Start an Amazon Web Services computer:
**************************************

This page shows you how to create a new "AWS instance", or a running
computer.

----

Start at the Amazon Web Services console (http://aws.amazon.com/ and
sign in to the console).

0. Select "EC2 - virtual servers in the cloud"
==============================================

.. thumbnail:: images/boot-0.png
   :width: 20%
           
1. Switch to zone US West (N California)
========================================

.. thumbnail:: images/boot-1.png
   :width: 20%

2. Click on "Launch instance."
==============================

3. Select "Community AMIs."
===========================

.. thumbnail:: images/boot-2.png
   :width: 20%

4. Search for ami-05384865 (ubuntu-wily-15.10-amd64-server)
===========================================================

Use ami-05384865.

.. thumbnail:: images/boot-3.png
   :width: 20%

5. Click on "Select."
=====================

6. Choose m4.large.
===================

.. thumbnail:: images/boot-4.png
   :width: 20%

7. Click "Review and Launch."
=============================

8. Click "Launch."
==================

.. thumbnail:: images/boot-5.png
   :width: 20%

9. Select "Create a new key pair."
==================================

Note: you only need to do this the first time you create an instance.
If you know where your amazon-key.pem file is, you can select 'Use an
existing key pair' here.  But you can always create a new key pair if
you want, too.

If you have an existing key pair, go to step 12, "Launch instance."

.. thumbnail:: images/boot-6.png
   :width: 20%

10. Enter name 'amazon-key'.
============================

11. Click "Download key pair."
==============================

12. Click "Launch instance."
============================

13. Select View instances (lower right)
=======================================

.. thumbnail:: images/boot-8.png
   :width: 20%

14. Bask in the glory of your running instance
==============================================

Note that for your instance name you can use either "Public IP" or
"Public DNS". Here, the machine only has a public IP.

.. thumbnail:: images/boot-9.png
   :width: 20%

You can now :doc:`login-shell` or :doc:`configure-firewall`.
