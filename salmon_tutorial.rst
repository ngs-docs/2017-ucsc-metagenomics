======================================
Gene Abundance Estimation with Salmon
======================================

Salmon is one of a breed of new, very fast RNAseq counting packages. Like Kallisto and Sailfish, Salmon counts fragments without doing up-front read mapping. Salmon can be used with edgeR and others to do differential expression analysis (if you are quantifying RNAseq data).

Today we will use it to get a handle on the relative distribution of genomic reads across the predicted protein regions.

The goals of this tutorial are to:

*  Install salmon
*  Use salmon to estimate gene coverage in our metagenome dataset

Installing Salmon
==================================================

Download and extract the latest version of Salmon and add it to your PATH:
::
    wget https://github.com/COMBINE-lab/salmon/releases/download/v0.7.2/Salmon-0.7.2_linux_x86_64.tar.gz
    tar -xvzf Salmon-0.7.2_linux_x86_64.tar.gz
    cd Salmon-0.7.2_linux_x86_64
    export PATH=$PATH:$HOME/Salmon-0.7.2_linux_x86_64/bin

Running Salmon
==============

Go to the data directory and download the prokka annotated sequences, assembled metagenome, and fastq files:
::
  cd /mnt/data
  curl -L -O https://s3-us-west-1.amazonaws.com/dib-training.ucdavis.edu/metagenomics-scripps-2016-10-12/SRR1976948.abundtrim.subset.pe.fq.gz
  curl -L -O https://s3-us-west-1.amazonaws.com/dib-training.ucdavis.edu/metagenomics-scripps-2016-10-12/SRR1977249.abundtrim.subset.pe.fq.gz
  curl -L -O **** prokka_annotation_assembly.tar.gz ***
  tar -xvzf prokka_annotation_assembly.tar.gz

Make a new directory for the quantification of data with Salmon:
::
    mkdir /mnt/quant
    cd quant


Grab the nucleotide (``*ffn``) predicted protein regions from Prokka and link them here. Also grab the trimmed sequence data (``*fq``)
::
    ln -fs /mnt/data/prokka_annotation/*ffn .
    ln -fs /mnt/data/*.abundtrim.subset.pe.fq.gz .

Create the salmon index:
::
  salmon index -t metagG.ffn -i transcript_index --type quasi -k 31

Salmon requires that paired reads be separated into two files. We can split the reads using the ``split-paired-reads.py`` from the khmer package:
::
  for file in *.abundtrim.subset.pe.fq.gz
  do
    tail=.fq.gz
    BASE=${file/$tail/}
    split-paired-reads.py $BASE$tail -1 ${file/$tail/}.1.fq -2 ${file/$tail/}.2.fq
  done

Now, we can quantify our reads against this reference:
::
  for file in *.pe.1.fq
  do
  tail1=.abundtrim.subset.pe.1.fq
  tail2=.abundtrim.subset.pe.2.fq
  BASE=${file/$tail1/}
  salmon quant -i transcript_index --libType IU \
        -1 $BASE$tail1 -2 $BASE$tail2 -o $BASE.quant;
   done
(Note that --libType must come before the read files!)

This will create a bunch of directories named after the fastq files that we just pushed through. Take a look at what files there are within one of these directories:
::
  find SRR1976948.quant -type f

Working with count data
=======================

Now, the ``quant.sf`` files actually contain the relevant information about expression – take a look:
::
  head -10 SRR1976948.quant/quant.sf

The first column contains the transcript names, and the fourth column is what we will want down the road - the normalized counts (TPM). However, they’re not in a convenient location / format for use; let's fix that.

Download the gather-counts.py script:
::
  curl -L -O https://raw.githubusercontent.com/ngs-docs/2016-metagenomics-sio/master/gather-counts.py
and run it:

  python ./gather-counts.py

This will give you a bunch of .counts files, which are processed from the quant.sf files and named for the directory from which they emanate.

References
===========
* http://salmon.readthedocs.io/en/latest/salmon.html
* http://biorxiv.org/content/early/2016/08/30/021592
