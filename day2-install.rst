=================================
Day 2 - installation instructions
=================================

(Instructions mostly copied from :doc:`quality`!)

Use ami-05384865, with a 500 GB local disk (see: :doc:`aws/boot`)

Run::

  sudo apt-get -y update && \
  sudo apt-get -y install trimmomatic fastqc python-pip \
     samtools zlib1g-dev ncurses-dev python-dev

Install anaconda::

  curl -O https://repo.continuum.io/archive/Anaconda3-4.2.0-Linux-x86_64.sh
  bash Anaconda3-4.2.0-Linux-x86_64.sh

Then update your environment and install khmer::

  source ~/.bashrc

  cd
  git clone https://github.com/dib-lab/khmer.git
  cd khmer
  sudo python2 setup.py install

Running Jupyter Notebook
------------------------

Let's also run a Jupyter Notebook in /mnt. First, configure it a teensy bit
more securely, and also have it run in the background::

  jupyter notebook --generate-config
  
  cat >>/home/ubuntu/.jupyter/jupyter_notebook_config.py <<EOF
  c = get_config()
  c.NotebookApp.ip = '*'
  c.NotebookApp.open_browser = False
  c.NotebookApp.password = u'sha1:5d813e5d59a7:b4e430cf6dbd1aad04838c6e9cf684f4d76e245c'
  c.NotebookApp.port = 8000

  EOF

Now, run! ::

  cd /mnt
  jupyter notebook &

You should be able to visit port 8000 on your AWS computer and see the
Jupyter console.  (The password is 'davis'.)


install khmer
