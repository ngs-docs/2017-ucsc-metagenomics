*************************
Terminating your instance
*************************

Amazon will happily charge you for running instances and/or associated
ephemeral storage until the cows come home - it's your responsibility
to turn things off.  The Right Way to do this for running instances
is to terminate.

The caveat here is that *everything ephemeral* will be deleted
(excluding volumes that you created/attached).  So you want to make sure
you transfer off anything you care about.

To terminate:

1. Select Actions, Instance State, Terminate
--------------------------------------------

In the 'Instances' tab, select your instance and then go to the Actions menu.

.. thumbnail:: images/terminate-1.png
   :width: 20%

2. Agree to terminate.
----------------------

.. thumbnail:: images/terminate-2.png
   :width: 20%

3. Verify status on your instance page.
---------------------------------------

Instance state should be either "shutting down" or "terminated".

.. thumbnail:: images/terminate-3.png
   :width: 20%

-----

Return to index: :doc:`index`
