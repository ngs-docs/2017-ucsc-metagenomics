======================================
Using and Installing Circos
======================================

Circos is a powerful visualization tool that allows for the creation of circular graphics to display complex genomic data (e.g. genome comparisons). On top of the circular ideogram generated can be layered any number of graphical information (heatmaps, scatter plots, etc.).

The goals of this tutorial are to:

*  Install circos on your Ubuntu AWS system
*  Use Circos to visualize our metagenomic data **fill me in **

Note: Beyond this brief crash course , circos is very well-documented and has a great series of `tutorials  <http://circos.ca/documentation/tutorials/>`__ and `course <http://circos.ca/documentation/course/>`__ materials that are useful.

Installing Circos
==================================================

Within your Amazon Instance make a directory called circos and navigate into it. There, we will download and extract the latest version of circos:
::
    mkdir circos
    cd circos
    wget http://circos.ca/distribution/circos-0.69-3.tgz
    tar -xvzf circos-0.69-3.tgz

Circos runs within Perl and as such does not need to be compiled to run. So, we can just add the location of circos to our path variable. (Alternatively, you can append this statement to the end of your ``.bashrc`` file.)
::
    export PATH=~/circos/circos-0.69-3/bin:$PATH

Circos does, however, require quite a few additional perl modules to opperate correctly. To see what modules are missing and need to be downloaded type the following:
::
    circos -modules > modules

Now, to download all of these we will be using CPAN, a package manager for perl. We are going to pick out all the missing modules and then loop over those modules and download them using cpan.
::
  grep missing modules |cut -f13 -d " " > missing_modules
  for mod in `cat missing_modules`;
    do
    sudo cpan install $mod;
    done

This will take a while to run. When it is done check that you now have all modules downloaded by typing:
::
  circos -modules

If you got all 'ok' then you are good to go!

Many of you might have issues installing the GD module. Here is a work around (from `stackoverflow <http://stackoverflow.com/questions/31521570/perl-gd-module-wont-install>`__) if GD did not happily install through CPAN.
::
  mkdir tmp
  cd tmp
  wget http://search.cpan.org/CPAN/authors/id/L/LD/LDS/GD-2.56.tar.gz
  tar xvzf GD-2.56.tar.gz
  cd GD-2.56
  perl -i~ -pE'say "Getopt::Long::Configure(qw( pass_through ));" if /GetOptions/;' Build.PL
  /usr/bin/perl Build.PL --installdirs site
  sudo ./Build.PL installdeps
  ./Build.PL make
  ./Build.PL test
  sudo ./Build.PL install

And with that, circos should be up and ready to go. Run the example by navigating to the examples folder within the circos folder.
::
  cd ~/circos/circos-0.69-3/example
  bash run

This will take a little bit to run but should generate a file called ``circos.png``.  Open it and you can get an idea of the huge variety of things that are possible with circos and a lot of patience. We will not be attempting anything that complex today, however.

Compairing our assembly
=======================
Create a reference database for blastn:
::
  formatdb -p F -o T -i ../data2/eighth.fa


References
===========
* http://genome.cshlp.org/content/early/2009/06/15/gr.092759.109.abstract
* http://circos.ca/documentation/tutorials
* http://circos.ca/documentation/course/
