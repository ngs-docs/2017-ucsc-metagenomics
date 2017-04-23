=================================
Day 2 - installation instructions
=================================

(Instructions mostly copied from :doc:`quality`!)

Use image "Ubuntu 14.04.3"

Run::

  sudo apt-get -y update && \
  sudo apt-get -y install trimmomatic fastqc python-pip \
     samtools zlib1g-dev ncurses-dev python-dev

Install anaconda::

   curl -O https://repo.continuum.io/archive/Anaconda3-4.2.0-Linux-x86_64.sh
   bash Anaconda3-4.2.0-Linux-x86_64.sh

Then update your environment and install [khmer](http://khmer.readthedocs.io)
and [sourmash](http://sourmash.readthedocs.io/en/latest/)::

   source ~/.bashrc
   
   pip install -U pip
   pip install -U setuptools
   pip install -U Cython
   pip install https://github.com/dib-lab/khmer/archive/master.zip
   pip install https://github.com/dib-lab/sourmash/archive/2017-ucsc-metagenome.zip

(See [the sourmash docs for this workshop](sourmash.html) for some details on the sourmash install.)

Running Jupyter Notebook
------------------------

Let's also run a Jupyter Notebook in your home directory.  Configure
it a teensy bit more securely, and also have it run in the background.

Generate a config::

  jupyter notebook --generate-config

Add a password, have it not run a browser, and put it on port 8000
by default::
  
  cat >>/home/ubuntu/.jupyter/jupyter_notebook_config.py <<EOF
  c = get_config()
  c.NotebookApp.ip = '*'
  c.NotebookApp.open_browser = False
  c.NotebookApp.password = u'sha1:5d813e5d59a7:b4e430cf6dbd1aad04838c6e9cf684f4d76e245c'
  c.NotebookApp.port = 8000

  EOF

Now, run! ::

  jupyter notebook &

You should be able to visit port 8000 on your computer and see the
Jupyter console; to get the URL to Jupyter, run::

  echo http://$(hostname):8000/
