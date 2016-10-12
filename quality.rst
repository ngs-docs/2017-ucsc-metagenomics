Short read quality and trimming
===============================

@@Harriet, (Boot ami-05384865 and add 100 GB of storage on sdb.)

First, `Log into your computer <aws/login-shell.html>`__.

OK, you should now be logged into your Amazon computer!  You should see
something like this::

   ubuntu@ip-172-30-1-252:~$

this is the command prompt.

Prepping the computer
---------------------

Before we do anything else, we need to set up a place to work and
install a few things.

.. @@CTB /dev/xvdb
   
First, let's set up a place to work::

   mkfs -t ext4 /dev/xvdb
   mount /dev/xvdb /mnt
   sudo chmod a+rwxt /mnt

This makes '/mnt' a place where we can put data and working files.

.. note::

   /mnt is the location we're going to use on Amazon computers, but
   if you're working on a local cluster, it will have a different
   location.  Talk to your local sysadmin and ask them where they
   recommend putting lots of short-term working files, i.e. the
   "scratch" space.

----

Installing some software
------------------------

Run::

  sudo apt-get -y update && \
  sudo apt-get -y install r-base python3-matplotlib libzmq3-dev python3.5-dev \
     texlive-latex-extra texlive-latex-recommended python3-virtualenv \
     trimmomatic fastqc python-pip python-dev \
     bowtie samtools zlib1g-dev ncurses-dev

  sudo pip install -U setuptools khmer==2.0 jupyter jupyter_client ipython


Data source
-----------

.. @@ CTB

We're going to be using a subset of data from `Hu et al.,
2016 <http://mbio.asm.org/content/7/1/e01669-15.full>`__. This paper
from the Banfield lab does cool stuff.

1. Copying in some data to work with.
-------------------------------------

We've loaded subsets of the data onto an Amazon location for you, to
make everything faster for today's work.  We're going to put the
files on your computer locally under the directory /mnt/data::

   mkdir /mnt/data

Next, let's grab part of the data set::

   cd /mnt/data
   curl -O -L https://s3-us-west-1.amazonaws.com/dib-training.ucdavis.edu/metagenomics-scripps-2016-10-12/SRR1976948_1.fastq.gz
   curl -O -L https://s3-us-west-1.amazonaws.com/dib-training.ucdavis.edu/metagenomics-scripps-2016-10-12/SRR1976948_2.fastq.gz
   
Now if you type::

   ls -l

you should see something like::

   total 346936
   -rw-rw-r-- 1 ubuntu ubuntu 169620631 Oct 11 23:37 SRR1976948_1.fastq.gz
   -rw-rw-r-- 1 ubuntu ubuntu 185636992 Oct 11 23:38 SRR1976948_2.fastq.gz

These are 1m read subsets of the original data, taken from the beginning
of the file.

One problem with these files is that they are writeable - by default, UNIX
makes things writeable by the file owner.  Let's fix that before we go
on any further::

   chmod u-w *

We'll talk about what these files are below.

1. Copying data into a working location
---------------------------------------

First, make a working directory; this will be a place where you can futz
around with a copy of the data without messing up your primary data::

   mkdir /mnt/work
   cd /mnt/work

Now, make a "virtual copy" of the data in your working directory by
linking it in -- ::

   ln -fs /mnt/data/* .

These are FASTQ files -- let's take a look at them::

   less SRR1976948_1.fastq.gz

(use the spacebar to scroll down, and type 'q' to exit 'less')

Question:

* where does the filename come from?
* why are there 1 and 2 in the file names?

Links:

* `FASTQ Format <http://en.wikipedia.org/wiki/FASTQ_format>`__

2. FastQC
---------

We're going to use `FastQC
<http://www.bioinformatics.babraham.ac.uk/projects/fastqc/>`__ to
summarize the data. We already installed 'fastqc' on our computer for
you.

Now, run FastQC on two files::

   fastqc SRR1976948_1.fastq.gz
   fastqc SRR1976948_2.fastq.gz

Now type 'ls'::

   ls -d *fastqc*

to list the files, and you should see::

.. @@
   SRR1976948_1.extract_fastqc
   SRR1976948_1.extract_fastqc.zip
   SRR1976941_2.extract_fastqc
   SRR1976948_2.extract_fastqc.zip

We are *not* going to show you how to look at these files right now -
you need to copy them to your local computer to do that.  We'll show
you that tomorrow.  But! we can show you what they look like, because
I've made copies of them for you:

* `0Hour_ATCACG_L002_R1_001.extract_fastqc/fastqc_report.html <http://2015-may-nonmodel.readthedocs.org/en/latest/_static/0Hour_ATCACG_L002_R1_001.extract_fastqc/fastqc_report.html>`__
* `0Hour_ATCACG_L002_R2_001.extract_fastqc/fastqc_report.html <http://2015-may-nonmodel.readthedocs.org/en/latest/_static/0Hour_ATCACG_L002_R2_001.extract_fastqc/fastqc_report.html>`__

Questions:

* What should you pay attention to in the FastQC report?
* Which is "better", file 1 or file 2? And why?

Links:

* `FastQC <http://www.bioinformatics.babraham.ac.uk/projects/fastqc/>`__
* `FastQC tutorial video <http://www.youtube.com/watch?v=bz93ReOv87Y>`__

3. Trimmomatic
--------------

Now we're going to do some trimming!  We'll be using
`Trimmomatic <http://www.usadellab.org/cms/?page=trimmomatic>`__, which
(as with fastqc) we've already installed via apt-get.

The first thing we'll need are the adapters to trim off::

  curl -O -L http://dib-training.ucdavis.edu.s3.amazonaws.com/mRNAseq-semi-2015-03-04/TruSeq2-PE.fa

Now, to run Trimmomatic::

   TrimmomaticPE SRR1976948_1.fastq.gz \
                 SRR1976948_2.fastq.gz \
        SRR1976948_1.qc.fq.gz s1_se \
        SRR1976948_2.qc.fq.gz s2_se \
        ILLUMINACLIP:TruSeq2-PE.fa:2:40:15 \
        LEADING:2 TRAILING:2 \                            
        SLIDINGWINDOW:4:2 \
        MINLEN:25

You should see output that looks like this::

   ...
   Quality encoding detected as phred33
   Input Read Pairs: 140557 Both Surviving: 138775 (98.73%) Forward Only Surviving: 1776 (1.26%) Reverse Only Surviving: 6 (0.00%) Dropped: 0 (0.00%)
   TrimmomaticPE: Completed successfully   ...

Questions:

* How do you figure out what the parameters mean?
* How do you figure out what parameters to use?
* What adapters do you use?
* What version of Trimmomatic are we using here? (And FastQC?)
* Do you think parameters are different for RNAseq and genomic data sets?
* What's with these annoyingly long and complicated filenames?
* why are we running R1 and R2 together?

For a discussion of optimal trimming strategies, see `MacManes, 2014
<http://journal.frontiersin.org/Journal/10.3389/fgene.2014.00013/abstract>`__
-- it's about RNAseq but similar arguments should apply to metagenome
assembly.

Links:

* `Trimmomatic <http://www.usadellab.org/cms/?page=trimmomatic>`__

4. FastQC again
---------------

Run FastQC again on the trimmed files::

   fastqc SRR1976948_1.qc.fastq.gz
   fastqc SRR1976948_2.qc.fastq.gz

And now view my copies of these files: 

* `0Hour_ATCACG_L002_R1_001.qc.fq_fastqc/fastqc_report.html <http://2015-may-nonmodel.readthedocs.org/en/latest/_static/0Hour_ATCACG_L002_R1_001.qc.fq_fastqc/fastqc_report.html>`__
* `0Hour_ATCACG_L002_R2_001.qc.fq_fastqc/fastqc_report.html <http://2015-may-nonmodel.readthedocs.org/en/latest/_static/0Hour_ATCACG_L002_R2_001.qc.fq_fastqc/fastqc_report.html>`__

Let's take a look at the output files::

   less SRR1976948_1.qc.fq.gz

(again, use spacebar to scroll, 'q' to exit less).

Questions:

* is the quality trimmed data "better" than before?
* Does it matter that you still have adapters!?

Optional: trim

Next: :doc:`assemble`
