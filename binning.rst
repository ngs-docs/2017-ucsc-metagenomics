Run the MEGAHIT assembler
=========================

A common approach following metagenome assembly is binning, a process by which assembled contigs are collected into groups or 'bins' that might then be assigned some taxonomic affiliation. There are many different tools that can be used for binning (see `CAMI review for more details<http://biorxiv.org/content/early/2017/01/09/099127>`__). Here, we will be using `MetaBAT<https://peerj.com/articles/1165/>`__, which is both user friendly and highly cited.

First, install::

   cd
   wget https://bitbucket.org/berkeleylab/metabat/downloads/metabat-static-binary-linux-x64_v0.32.4.tar.gz
   tar xzvf metabat-static-binary-linux-x64_v0.32.4.tar.gz
   cd metabat
   export PATH=$PATH:~/metabat

Now, download the assembly (so we are all using the same one) and the mapped data (.bam files)::

   cd /mnt/data
   curl -O  FILL THIS IN!!! Might not be needed if we work after the mapping step

Binning the assembly
--------------------

Now, finally, run the assembler! ::

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
MiSeq, and PacBio? (Also see `this paper
<http://ivory.idyll.org/blog/2015-sharon-paper.html>`__.)

What kind of experimental design considerations should you have if you
plan to assemble?

Some figures: the first two come from work by Dr. Sherine Awad on
analyzing the data from Shakya et al (2014).  The third comes from
an analysis of read search vs contig search of a protein database.

.. thumbnail:: files/assembler-runtimes.png
   :width: 20%

.. thumbnail:: files/assembler-mapping.png
   :width: 20%

.. thumbnail:: files/read-vs-contig-alignment.png
   :width: 20%


After the assembly is finished
------------------------------

At this point we can do a bunch of things:

* annotate the assembly (:doc:`prokka_tutorial`);
* evaluate the assembly's inclusion of k-mers and reads;
* set up a BLAST database so that we can search it for genes of interest;
* quantify the abundance of the contigs or genes in the assembly, using the original read data set (:doc:`salmon_tutorial`);
* bin the contigs in the assembly into species bins;
