********************************
Configure your instance firewall
********************************

Normally, Amazon computers only allow shell logins via ssh (port 22
access).  If we want to run a Web service or something else, we need
to give the outside world access to other network locations on the
computer.

Below, we will open ports 8000-9000, which will let us run things like
RStudio Server.  If you want to run other things, like a Web server,
you'll need to find the port(s) associated with those services and
open those instead of 8000-9000.  (Tip: Web servers run on port 80.)

1. Select 'Security Groups'
---------------------------

Find "Security Groups" in the lower pane of your instance's
information page, and click on "launch-wizard-N".

.. thumbnail:: images/network-0.png
   :width: 20%
           
2. Select 'Inbound'
-------------------

.. thumbnail:: images/network-1.png
   :width: 20%

3. Select 'Edit'
----------------

.. thumbnail:: images/network-2.png
   :width: 20%

4. Select 'Add Rule'
--------------------

.. thumbnail:: images/network-3.png
   :width: 20%

5. Enter rule information
-------------------------

Add a new rule: Custom TCP, 8000-9000, Source Anywhere.

6. Select 'Save'.
-----------------

7. Return to the Instances page.
--------------------------------

.. thumbnail:: images/network-4.png
   :width: 20%
 
----

You're done!

Go back to the index: :doc:`index`
