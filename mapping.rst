=======
Mapping
=======

Download bwa::

  cd
  curl -L https://sourceforge.net/projects/bio-bwa/files/bwa-0.7.15.tar.bz2/download > bwa-0.7.15.tar.bz2

Unpack and build it::

  tar xjvf bwa-0.7.15.tar.bz2
  cd bwa-0.7.15
  make

Install it::

  sudo cp bwa /usr/local/bin

Downloading data
-----------------

Now, go to a new directory and grab the data::

  mkdir /mnt/mapping
  cd /mnt/mapping

  curl -O https://s3-us-west-1.amazonaws.com/dib-training.ucdavis.edu/metagenomics-scripps-2016-10-12/SRR1976948.abundtrim.subset.pe.fq.gz
  curl -O https://s3-us-west-1.amazonaws.com/dib-training.ucdavis.edu/metagenomics-scripps-2016-10-12/SRR1977249.abundtrim.subset.pe.fq.gz

And extract the files::

  for file in *fq.gz:
    do
    gunzip $file
  done

We will also need the assembly; rather than rebuilding it, you can download
a copy that we saved for you::

  curl -O https://s3-us-west-1.amazonaws.com/dib-training.ucdavis.edu/metagenomics-scripps-2016-10-12/subset_assembly.fa.gz
  gunzip subset_assembly.fa

Mapping the reads
-----------------

First, we will need to to index the megahit assembly::

  bwa index subset_assembly.fa

to The reads are in paired-end/interleaved format, so you'll need to add the -p flag to indicate to bwa that these are paired end data::

Map the reads::

  for i in *fq
    do
    bwa mem -p subset_assembly.fa $i > ${i}.aln.sam
  done

Converting to BAM to visualize
------------------------------

First, index the assembly for samtools::

  samtools faidx subset_assembly.fa

Then, convert both SAM files to BAM files::

  for i in *.sam
  do
     samtools import subset_assembly.fa $i $i.bam
     samtools sort $i.bam $i.bam.sorted
     samtools index $i.bam.sorted.bam
  done

Visualizing the read mapping
----------------------------

Find a contig name to visualize::

    grep -v ^@ SRR1976948.sam | \
        cut -f 3 | sort | uniq -c | sort -n

Pick one e.g. k99_13588.

Now execute::

  samtools tview SRR1976948.sam.bam.sorted.bam subset_assembly.fa -p k99_13588:400

(use arrow keys to scroll, 'q' to quit)

Look at it in both mappings::

  samtools tview SRR1977249.sam.bam.sorted.bam subset_assembly.fa -p k99_13588:400

Why is the mapping so good??

Note: no strain variation :).

----

Grab some untrimmed data::

   curl -O https://s3-us-west-1.amazonaws.com/dib-training.ucdavis.edu/metagenomics-scripps-2016-10-12/SRR1976948_1.fastq.gz
   curl -O https://s3-us-west-1.amazonaws.com/dib-training.ucdavis.edu/metagenomics-scripps-2016-10-12/SRR1976948_2.fastq.gz

Now align this untrimmed data::

   gunzip -c SRR1976948_1.fastq.gz | head -800000 > SRR1976948.1
   gunzip -c SRR1976948_2.fastq.gz | head -800000 > SRR1976948.2

   bwa aln subset_assembly.fa SRR1976948.1 > SRR1976948_1.untrimmed.sai
   bwa aln subset_assembly.fa SRR1976948.2 > SRR1976948_2.untrimmed.sai

   bwa sampe subset_assembly.fa SRR1976948_1.untrimmed.sai SRR1976948_2.untrimmed.sai SRR1976948.1 SRR1976948.2 > SRR1976948.untrimmed.sam

   i=SRR1976948.untrimmed.sam
   samtools import subset_assembly.fa $i $i.bam
   samtools sort $i.bam $i.bam.sorted
   samtools index $i.bam.sorted.bam

And now look::

   samtools tview SRR1976948.untrimmed.sam.bam.sorted.bam subset_assembly.fa -p k99_13588:500

You can also use 'Tablet' to view the downloaded BAM file - see `the Tablet paper <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2815658/>`__.
