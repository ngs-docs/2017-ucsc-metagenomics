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
 - Evaluating assembly results (mapping rates, etc.)
 - Annotating assembly (Prokka)
 - Abundance calculations
* Th: topics TBD. Possible topics:
 - Abundance comparisons between samples
 - CIRCOS plots
 - ShotMap for annotating shotgun reads
 - Taxonomic analysis of reads and assemblies
 - Genome binning
 - Jupyter Notebook or RMarkdown
 - git for version control
 - Docker execution environments
 - Workflow strategies (scripting, make, doit, etc.)
 - More Amazon Web Services: EC2, S3, ...?

Tutorials:

.. toctree::
   :maxdepth: 2

   welcome
   aws/index
   
Technical information
~~~~~~~~~~~~~~~~~~~~~

The github repository for this workshop is public at
https://github.com/ngs-docs/2016-metagenomics-sio
