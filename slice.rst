==============================
Slicing and dicing with k-mers
==============================

(Note, this won't work with amplified data.)

Extra resources:

* `plotting notebook <https://github.com/ngs-docs/2016-metagenomics-sio/blob/master/files/coverage.ipynb>`__

---

At the command line, create a new directory and extract some data::

   cd /mnt
   mkdir slice
   cd slice

We're going to work with half the read data set for speed reasons -- ::

   gunzip -c ../mapping/SRR1976948.abundtrim.subset.pe.fq.gz | \
      head -6000000 > SRR1976948.half.fq
   

In a Jupyter Notebook (go to 'http://' + machine name + ':8000'), password
'davis', create new Python notebook "conda root", run::

   cd /mnt/slice

and then in another cell::
  
   !load-into-counting.py -M 4e9 -k 31 SRR1976948.kh SRR1976948.half.fq

and in another cell::
   
   !abundance-dist.py SRR1976948.kh SRR1976948.half.fq SRR1976948.dist

and in yet another cell::

  %matplotlib inline
  import numpy
  from pylab import *
  dist1 = numpy.loadtxt('SRR1976948.dist', skiprows=1, delimiter=',')
  plot(dist1[:,0], dist1[:,1])
  axis(ymax=10000, xmax=1000)  

Then::

   python2 ~/khmer/sandbox/calc-median-distribution.py SRR1976948.kh \
      SRR1976948.half.fq SRR1976948.readdist

And::
  
   python2 ~/khmer/sandbox/slice-reads-by-coverage.py SRR1976948.kh SRR1976948.half.fq slice.fq -m 0 -M 60

Assemble the slice
------------------

(Re)install megahit::

   cd
   git clone https://github.com/voutcn/megahit.git
   cd megahit
   make

Go back to the slice directory and extract paired ends::

  cd /mnt/slice
  extract-paired-ends.py slice.fq

Assemble! ::
  
   ~/megahit/megahit --12 slice.fq.pe -o slice

The contigs will be in ``slice/final.contigs.fa``.
