2016 / October / Metagenomics
=============================

This workshop was given on October 12th and 13th, 2016,
by Harriet Alexander and C. Titus Brown, at the Scripps Institute of
Oceanography.

For more information, please `contact Titus directly
<mailto:ctbrown@ucdavis.edu>`__.

`We have an EtherPad for sharing text and asking questions <https://public.etherpad-mozilla.org/p/2016-sio>`__.

Rough schedule:

* Wed, 9am-noon: Amazon Web Services; short reads, QC, and trimming.
 - Logging into AWS
 - Read quality evaluation and FASTQ trimming (FASTQC, Trimmomatic)
 - (Optional) K-mer spectral error analysis and trimming (khmer)
* Wed, 1-4pm: Assembly, annotation, and evaluation.
 - Short-read assembly with MEGAHIT
 - Advantages and drawbacks to assembly (discussion)
 - Evaluating assembly results (mapping rates, mapping viz, etc.)
 - Annotating assembly (Prokka)
 - Abundance calculations
* Thursday: topics TBD from below, or others:
 - Biolog and bioinformatics:
  - Abundance comparisons between samples
  - Taxonomic analysis of reads and assemblies
  - Genome binning
  - CIRCOS plots
  - ShotMap for annotating shotgun reads
 - Moar computing:
  - Jupyter Notebook or RMarkdown
  - git for version control
  - Docker execution environments
  - Workflow strategies (scripting, make, doit, etc.)
  - More Amazon Web Services: EC2, S3, ...?
 - Miscellany:
  - Visualizing assembly graphs
  - MinHash sketches for comparing genomes and metagenomes
  - Tricks with sequences using Python libraries (screed & khmer)

Tutorials:

.. toctree::
   :maxdepth: 2

   welcome
   aws/index
   quality
   kmer_trimming
   assemble
   prokka_tutorial
   salmon_tutorial
   
Technical information
~~~~~~~~~~~~~~~~~~~~~

The github repository for this workshop is public at
https://github.com/ngs-docs/2016-metagenomics-sio
