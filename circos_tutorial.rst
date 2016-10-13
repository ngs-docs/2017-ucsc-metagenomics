======================================
Using and Installing Circos
======================================

.. 

Circos is a powerful visualization tool that allows for the creation of circular graphics to display complex genomic data (e.g. genome comparisons). On top of the circular ideogram generated can be layered any number of graphical information (heatmaps, scatter plots, etc.).

The goals of this tutorial are to:

*  Install circos on your Ubuntu AWS system
*  Use Circos to visualize our metagenomic data

Note: Beyond this brief crash course , circos is very well-documented and has a great series of `tutorials  <http://circos.ca/documentation/tutorials/>`__ and `course <http://circos.ca/documentation/course/>`__ materials that are useful.

Installing Circos
==================================================

You'll need to install one additional ubuntu package, libgd::

   sudo apt-get -y install libgd-perl

Within your Amazon Instance make a directory called circos and navigate into it. There, we will download and extract the latest version of circos:
::
    cd /mnt
    mkdir circos
    cd circos
    curl -O http://dib-training.ucdavis.edu.s3.amazonaws.com/metagenomics-scripps-2016-10-12/circos-0.69-3.tar.gz
    tar -xvzf circos-0.69-3.tar.gz

Circos runs within Perl and as such does not need to be compiled to run. So, we can just add the location of circos to our path variable. (Alternatively, you can append this statement to the end of your ``.bashrc`` file.)
::
    export PATH=/mnt/circos/circos-0.69-3/bin:$PATH

Circos does, however, require quite a few additional perl modules to operate correctly. To see what modules are missing and need to be downloaded type the following:
::
    circos -modules > modules

Now, to download all of these we will be using CPAN, a package manager for perl. We are going to pick out all the missing modules and then loop over those modules and download them using cpan.
::
  grep missing modules |cut -f13 -d " " > missing_modules
  for mod in $(cat missing_modules);
    do
    sudo cpan install $mod;
    done

This will take a while to run. When it is done check that you now have all modules downloaded by typing:
::
  circos -modules

If you got all 'ok' then you are good to go!

And with that, circos should be up and ready to go. Run the example by navigating to the examples folder within the circos folder.
::
  cd /mnt/circos/circos-0.69-3/example
  bash run

This will take a little bit to run but should generate a file called ``circos.png``.  Open it and you can get an idea of the huge variety of things that are possible with circos and a lot of patience. We will not be attempting anything that complex today, however.

Visualizing Gene Coverage and Orientation
==========================================
First, let's make a directory where we will be doing all of our work for plotting:
::
  mkdir /mnt/circos/plotting
  cd /mnt/circos/plotting

Now, link in the ``*gff`` file output from prokka (which we will use to define the location of genes in each of our genomes), the genome assembly file ``final.contigs.fa``, and the ``SRR*counts`` files that we generated with salmon:
::
  ln -fs /mnt/data/prokka_annotation/*gff .
  ln -fs /mnt/data/final.contigs.fa .
  ln -fs /mnt/quant/*counts .

We also need to grab a set of useful scripts and config files for this plotting exercise:
::
  curl -L -O https://s3-us-west-1.amazonaws.com/dib-training.ucdavis.edu/metagenomics-scripps-2016-10-12/circos-build.tar.gz
  tar -xvzf circos-build.tar.gz
  curl -L -O https://s3-us-west-1.amazonaws.com/dib-training.ucdavis.edu/metagenomics-scripps-2016-10-12/subset_assembly.fa.gz
  gunzip subset_assembly.fa.gz
  mv subset_assembly.fa final.contigs.fa
  
We are going to limit the data we are trying to visualize and get longest contigs from our assembly. We can do this using a script from the khmer package:
::
  extract-long-sequences.py  final.contigs.fa -l 24000 -o final.contigs.long.fa

Next, we will run a script that processes the data from the the files that we just moved to create circos-acceptable files. This is really the crux of using circos: figuring out how to get your data into the correct format.
::
  python parse_data_for_circos.py

If you are interested-- take a look at the script and the input files to see how these data were manipulated.

Circos operates off of three main types of files: 1) a config files that dictate the style and inputs to your circos plot, 2) a karyotype file that defines the size and layout of your "chromosomes", and 3) any data files that  you call in your config file that detail attributes you want to plot.

The above script generated our karyotype file and four different data files. What are they? How are they oriented?

Now, we all that is left is actually running circos. Navigate into the circos-build directory and type ``circos``:
::
  cd circos-build
  circos

This command should generate an ``circos.svg`` and ``circos.png``. Check out the ``circos.png``!

Now, let's take a look at the file that controls this crazy figure-- ``circos.config``.

Try changing a few parameters-- colors, radius, size, to see what you can do. Again, if you are into this type of visualization, do check out the extensive `tutorial  <http://circos.ca/documentation/tutorials/>`__. 
References
===========
* http://genome.cshlp.org/content/early/2009/06/15/gr.092759.109.abstract
* http://circos.ca/documentation/tutorials
* http://circos.ca/documentation/course/
