Short read quality and trimming
===============================

First, `Log into your computer <login.html>`__.

OK, you should now be logged into your Amazon computer!  You should see
something like this::

   ubuntu@ip-172-30-1-252:~$

this is the command prompt.

Prepping the computer
---------------------

Before we do anything else, we need to set up a place to work and
install a few things.

First, let's set up a place to work::

   sudo chmod a+rwxt /mnt

This makes '/mnt' a place where we can put data and working files.

.. note::

   /mnt is the location we're going to use on Amazon computers, but
   if you're working on a local cluster, it will have a different
   location.  Talk to your local sysadmin and ask them where they
   recommend putting lots of short-term working files, i.e. the
   "scratch" space.

----

Data source
-----------

We're going to be using a subset of data from `Tulin et al., 2013 <http://pubmed.org/pubmed/23731568>`__, a paper looking at early transcription in the
organism *Nematostella vectensis*, the sea anemone.

1. Copying in some data to work with.
-------------------------------------

We've loaded subsets of the data onto an Amazon location for you, to
make everything faster for today's work.  We're going to put the
files on your computer locally under the directory /mnt/data::

   mkdir /mnt/data

Next, let's grab part of the data set::

   cd /mnt/data
   curl -O -L http://dib-training.ucdavis.edu.s3.amazonaws.com/mRNAseq-non-2015-05-04/0Hour_ATCACG_L002_R1_001.extract.fastq.gz
   curl -O -L http://dib-training.ucdavis.edu.s3.amazonaws.com/mRNAseq-non-2015-05-04/0Hour_ATCACG_L002_R2_001.extract.fastq.gz

Now if you type::

   ls -l

you should see something like::

   -r--r--r-- 1 ubuntu ubuntu   7874107 Dec 14  2013 0Hour_ATCACG_L002_R1_001.extract.fastq.gz
   -r--r--r-- 1 ubuntu ubuntu   7972058 Dec 14  2013 0Hour_ATCACG_L002_R1_002.extract.fastq.gz
   ...

These are subsets of the original data, where we selected for reads
that belong to a few particular transcripts.

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

   less 0Hour_ATCACG_L002_R1_001.extract.fastq.gz

(use the spacebar to scroll down, and type 'q' to exit 'less')

Question:

* why do the files have DNA in the name?
* why are there R1 and R2 in the file names?
* why don't we combine all the files?

Links:

* `FASTQ Format <http://en.wikipedia.org/wiki/FASTQ_format>`__

2. FastQC
---------

We're going to use `FastQC
<http://www.bioinformatics.babraham.ac.uk/projects/fastqc/>`__ to
summarize the data. We already installed 'fastqc' on our computer for
you.

Now, run FastQC on two files::

   fastqc 0Hour_ATCACG_L002_R1_001.extract.fastq.gz
   fastqc 0Hour_ATCACG_L002_R2_001.extract.fastq.gz

Now type 'ls'::

   ls -d *fastqc*

to list the files, and you should see::


   0Hour_ATCACG_L002_R1_001.extract_fastqc
   0Hour_ATCACG_L002_R1_001.extract_fastqc.zip
   0Hour_ATCACG_L002_R2_001.extract_fastqc
   0Hour_ATCACG_L002_R2_001.extract_fastqc.zip

We are *not* going to show you how to look at these files right now -
you need to copy them to your local computer to do that.  We'll show
you that tomorrow.  But! we can show you what they look like, because
I've made copies of them for you:

* `0Hour_ATCACG_L002_R1_001.extract_fastqc/fastqc_report.html <http://2015-may-nonmodel.readthedocs.org/en/latest/_static/0Hour_ATCACG_L002_R1_001.extract_fastqc/fastqc_report.html>`__
* `0Hour_ATCACG_L002_R2_001.extract_fastqc/fastqc_report.html <http://2015-may-nonmodel.readthedocs.org/en/latest/_static/0Hour_ATCACG_L002_R2_001.extract_fastqc/fastqc_report.html>`__

Questions:

* What should you pay attention to in the FastQC report?
* Which is "better", R1 or R2? And why?

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

   TrimmomaticPE 0Hour_ATCACG_L002_R1_001.extract.fastq.gz \
                 0Hour_ATCACG_L002_R2_001.extract.fastq.gz \
        0Hour_ATCACG_L002_R1_001.qc.fq.gz s1_se \
        0Hour_ATCACG_L002_R2_001.qc.fq.gz s2_se \
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

For a discussion of optimal RNAseq trimming strategies, see `MacManes,
2014
<http://journal.frontiersin.org/Journal/10.3389/fgene.2014.00013/abstract>`__.

Links:

* `Trimmomatic <http://www.usadellab.org/cms/?page=trimmomatic>`__

4. FastQC again
---------------

Run FastQC again on the trimmed files::

   fastqc 0Hour_ATCACG_L002_R1_001.qc.fq.gz
   fastqc 0Hour_ATCACG_L002_R2_001.qc.fq.gz

And now view my copies of these files: 

* `0Hour_ATCACG_L002_R1_001.qc.fq_fastqc/fastqc_report.html <http://2015-may-nonmodel.readthedocs.org/en/latest/_static/0Hour_ATCACG_L002_R1_001.qc.fq_fastqc/fastqc_report.html>`__
* `0Hour_ATCACG_L002_R2_001.qc.fq_fastqc/fastqc_report.html <http://2015-may-nonmodel.readthedocs.org/en/latest/_static/0Hour_ATCACG_L002_R2_001.qc.fq_fastqc/fastqc_report.html>`__

Let's take a look at the output files::

   less 0Hour_ATCACG_L002_R1_001.qc.fq.gz

(again, use spacebar to scroll, 'q' to exit less).

Questions:

* is the quality trimmed data "better" than before?
* Does it matter that you still have adapters!?

5. Trim the rest of the sequences
---------------------------------

First download the rest of the data::

   cd /mnt/data
   curl -O -L http://dib-training.ucdavis.edu.s3.amazonaws.com/mRNAseq-non-2015-05-04/0Hour_ATCACG_L002_R1_002.extract.fastq.gz
   curl -O -L http://dib-training.ucdavis.edu.s3.amazonaws.com/mRNAseq-non-2015-05-04/0Hour_ATCACG_L002_R1_003.extract.fastq.gz
   curl -O -L http://dib-training.ucdavis.edu.s3.amazonaws.com/mRNAseq-non-2015-05-04/0Hour_ATCACG_L002_R1_004.extract.fastq.gz
   curl -O -L http://dib-training.ucdavis.edu.s3.amazonaws.com/mRNAseq-non-2015-05-04/0Hour_ATCACG_L002_R1_005.extract.fastq.gz
   curl -O -L http://dib-training.ucdavis.edu.s3.amazonaws.com/mRNAseq-non-2015-05-04/0Hour_ATCACG_L002_R2_002.extract.fastq.gz
   curl -O -L http://dib-training.ucdavis.edu.s3.amazonaws.com/mRNAseq-non-2015-05-04/0Hour_ATCACG_L002_R2_003.extract.fastq.gz
   curl -O -L http://dib-training.ucdavis.edu.s3.amazonaws.com/mRNAseq-non-2015-05-04/0Hour_ATCACG_L002_R2_004.extract.fastq.gz
   curl -O -L http://dib-training.ucdavis.edu.s3.amazonaws.com/mRNAseq-non-2015-05-04/0Hour_ATCACG_L002_R2_005.extract.fastq.gz
   curl -O -L http://dib-training.ucdavis.edu.s3.amazonaws.com/mRNAseq-non-2015-05-04/6Hour_CGATGT_L002_R1_001.extract.fastq.gz
   curl -O -L http://dib-training.ucdavis.edu.s3.amazonaws.com/mRNAseq-non-2015-05-04/6Hour_CGATGT_L002_R1_002.extract.fastq.gz
   curl -O -L http://dib-training.ucdavis.edu.s3.amazonaws.com/mRNAseq-non-2015-05-04/6Hour_CGATGT_L002_R1_003.extract.fastq.gz
   curl -O -L http://dib-training.ucdavis.edu.s3.amazonaws.com/mRNAseq-non-2015-05-04/6Hour_CGATGT_L002_R1_004.extract.fastq.gz
   curl -O -L http://dib-training.ucdavis.edu.s3.amazonaws.com/mRNAseq-non-2015-05-04/6Hour_CGATGT_L002_R1_005.extract.fastq.gz
   curl -O -L http://dib-training.ucdavis.edu.s3.amazonaws.com/mRNAseq-non-2015-05-04/6Hour_CGATGT_L002_R2_001.extract.fastq.gz
   curl -O -L http://dib-training.ucdavis.edu.s3.amazonaws.com/mRNAseq-non-2015-05-04/6Hour_CGATGT_L002_R2_002.extract.fastq.gz
   curl -O -L http://dib-training.ucdavis.edu.s3.amazonaws.com/mRNAseq-non-2015-05-04/6Hour_CGATGT_L002_R2_003.extract.fastq.gz
   curl -O -L http://dib-training.ucdavis.edu.s3.amazonaws.com/mRNAseq-non-2015-05-04/6Hour_CGATGT_L002_R2_004.extract.fastq.gz
   curl -O -L http://dib-training.ucdavis.edu.s3.amazonaws.com/mRNAseq-non-2015-05-04/6Hour_CGATGT_L002_R2_005.extract.fastq.gz

And link it in::

   cd /mnt/work
   ln -fs /mnt/data/*.fastq.gz .

Now we have a lot of files -- and we really don't want to trim each and
every one of them by typing in a command for each pair! Here we'll
make use of a great feature of the UNIX command line -- the ability to
automate such tasks.

Here's a for loop that you can run - we'll walk through what it does
while it's running::

  rm -f orphans.fq

  for filename in *_R1_*.extract.fastq.gz
  do
        # first, make the base by removing .extract.fastq.gz
        base=$(basename $filename .extract.fastq.gz)
        echo $base

        # now, construct the R2 filename by replacing R1 with R2
        baseR2=${base/_R1_/_R2_}
        echo $baseR2

        # finally, run Trimmomatic
        TrimmomaticPE ${base}.extract.fastq.gz ${baseR2}.extract.fastq.gz \
           ${base}.qc.fq.gz s1_se \
           ${baseR2}.qc.fq.gz s2_se \
           ILLUMINACLIP:TruSeq2-PE.fa:2:40:15 \
           LEADING:2 TRAILING:2 \                            
           SLIDINGWINDOW:4:2 \
           MINLEN:25

        # save the orphans
        cat s1_se s2_se >> orphans.fq
  done

Things to mention --

* # are comments;
* anywhere you see a '$' is replaced by the value of the variable
  after it, so e.g. $filename is replaced by each of the files
  matching *_R1_*.extract.fastq.gz, once for each time through the
  loop;
* we have to do complicated things to the filenames to get this to work, which
  is what the ${base/_R1_/_R2_} stuff is about.
* what's with 'orphans.fq'??

Questions:

* how do you figure out if it's working?
   - copy/paste it from Word
   - put in lots of echo
   - edit one line at a time
* how on earth do you figure out how to do this?!

6. Interleave the sequences
---------------------------

Next, we need to take these R1 and R2 sequences and convert them into
interleaved form ,for the next step.  To do this, we'll use scripts
from the `khmer package <http://khmer.readthedocs.org>`__, which we
installed for you.

Now let's use a for loop again - you might notice this is only a minor
modification of the previous for loop... ::

  for filename in *_R1_*.qc.fq.gz
  do
        # first, make the base by removing .extract.fastq.gz
        base=$(basename $filename .qc.fq.gz)
        echo $base

        # now, construct the R2 filename by replacing R1 with R2
        baseR2=${base/_R1_/_R2_}
        echo $baseR2

        # construct the output filename
        output=${base/_R1_/}.pe.qc.fq.gz

        interleave-reads.py ${base}.qc.fq.gz ${baseR2}.qc.fq.gz | \
            gzip > $output
  done

  gzip orphans.fq

----
   
Next: :doc:`n-diginorm`

