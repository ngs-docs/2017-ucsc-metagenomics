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

We will also need the assembly; rather than rebuilding it, you can download
a copy that we saved for you::

  curl -O https://s3-us-west-1.amazonaws.com/dib-training.ucdavis.edu/metagenomics-scripps-2016-10-12/subset_assembly.fa.gz

Next, you'll need to index the assembly::

  bwa index subset_assembly.fa.gz

Splitting the reads
-------------------

The reads are in paired-end/interleaved format, so you'll need to split them -::

   for i in *.pe.fq.gz
   do
      split-paired-reads.py $i
   done

This will take the interleaved reads and produce .1 and .2 files from them.
   
Mapping the reads
-----------------

Map the left reads::

   for i in *.1
   do
      head -400000 $i > $i.subset
      bwa aln subset_assembly.fa.gz $i.subset > $(echo $i | cut -d. -f1)_1.sai
   done

Map the right reads::

   for i in *.2
   do
      head -400000 $i > $i.subset
      bwa aln subset_assembly.fa.gz $i.subset > $(echo $i | cut -d. -f1)_2.sai
   done

Combine the paired ends with bwa sampe::

   bwa samse subset_assembly.fa.gz SRR1976948_1.sai SRR1976948.*.1 > SRR1976948.sam
   bwa sampe subset_assembly.fa.gz SRR1976948_1.sai SRR1976948_2.sai SRR1976948.*.1 SRR1976948.*.2 > SRR1976948.sam
   bwa sampe subset_assembly.fa.gz SRR1977249_1.sai SRR1977249_2.sai SRR1977249.*.1 SRR1977249.*.2 > SRR1977249.sam


Visualizing the read mapping
----------------------------

gunzip -c subset_assembly.fa.gz > subset_assembly.fa
