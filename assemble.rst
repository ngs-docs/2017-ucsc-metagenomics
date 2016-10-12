Run the MEGAHIT assembler
=========================

`MEGAHIT <https://github.com/voutcn/megahit>`__ is a very fast, quite
good assembler designed for metagenomes.

First, install it::

   cd
   git clone https://github.com/voutcn/megahit.git
   cd megahit
   make

Now, download some data::

   cd /mnt/data
   curl -O https://s3-us-west-1.amazonaws.com/dib-training.ucdavis.edu/metagenomics-scripps-2016-10-12/SRR1976948.abundtrim.subset.pe.fq.gz
   curl -O https://s3-us-west-1.amazonaws.com/dib-training.ucdavis.edu/metagenomics-scripps-2016-10-12/SRR1977249.abundtrim.subset.pe.fq.gz

These are data that have been run through the @@trimming.

And, finally, run the assembler! ::

   mkdir /mnt/assembly
   cd /mnt/assembly
   ln -fs ../data/*.subset.pe.fq.gz .

   ~/megahit/megahit --12 SRR1976948.abundtrim.subset.pe.fq.gz,SRR1977249.abundtrim.subset.pe.fq.gz \
       -o combined

This will take about 25 minutes; at the end you should see output like
this::

   ... 12787984 bp, min 200 bp, max 61353 bp, avg 1377 bp, N50 3367 bp
   ... ALL DONE. Time elapsed: 1592.503825 seconds

The output assembly will be in ``combined/final.contigs.fa``.

While the assembly runs...
--------------------------

.. Graph assembly / What doesn’t get assembled? (Repeats, strain variation)
.. Sherine work on metagenomics
.. Our read length figure / soil

How assembly works - whiteboarding the De Bruijn graph approach.

Interpreting the MEGAHIT working output :)

What does, and doesn't, assemble?

How good is assembly anyway?

Discussion:

Why would we assemble, vs looking at raw reads?  What are the
advantages and disadvantages?

What are the technology tradeoffs between Illumina HiSeq, Illumina
MiSeq, and PacBio?

What kind of experimental design considerations should you have if you
plan to assemble?


After the assembly is finished
------------------------------

At this point we can do a bunch of things:

* annotate the assembly;
* evaluate the assembly's inclusion of k-mers and reads;
* set up a BLAST database so that we can search it for genes of interest;
* quantify the abundance of the contigs in the assembly in the original read
  data set;
* bin the contigs in the assembly into species bins;
