*****************************
Things to mention and discuss
*****************************

When do disks go away?
----------------------

* never on reboot;
* ephemeral disks go away on stop;
* AMI-attached volumes go away on terminate;
* attached volumes never go away on terminate and have to be
  explicitly deleted;
* snapshots only go away when you explicitly delete them.

What are you charged for?
-------------------------

* you are charged for a running instance at the @@instance price rates;
* ephemeral storage/instance-specific storage is included within that.

* when you stop an instance, you are charged at disk-space rates for
  the stopped disk;

* when you create a volume, you are charged for that volume until you delete
  it;

* when you create a snapshot, you are charged for that snapshot until you
  delete it.

To make sure you're not getting charged, go to your Instance view and
clear all search filters; anything that is "running" or "stopped" is
costing you.  Also check your volumes and your snapshots - they should be
empty.

.. @@ account details/running costs link?

----

Regions vs zones:
-----------------

* AMIs and Snapshots (and keys and security groups) are per region;
* Volumes and instances are per zone;

.. @@ image
