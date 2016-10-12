=============================
K-mer Spectral Error Trimming
=============================

(Optional)

If you plot a k-mer abundance histogram @@ of the samples, you'll
notice something: there's an awful lot of unique (abundance=1) k-mers.
These are erroneous k-mers caused by sequencing errors.

@@plot

Many of these errors remain even after you do the Trimmomatic run.  This is for
two reasons:

* first, Trimmomatic trims based solely on the quality score, which is
  a statistical statement about the correctness of a base - a Q score
  of 30 means that, of 10000@ bases with that Q score, 1 of those
  bases will be wrong.  So, a base can have a high Q score and still
  be wrong! (and **many** bases will have a low Q score and still be
  correct)

* second, we trimmed **very** lightly - only bases that had a very low
  quality were removed.  This was intentional because with assembly,
  you want to retain as much coverage as possible, and the assembler
  will generally figure out what the "correct" base is from the coverage.

An alternative to trimming based on the quality scores is to trim based on
k-mer abundance - this is known as k-mer spectral error trimming.
(@@qingpeng)

The logic is this: if you see low abundance k-mers in a high coverage data
set, those k-mers are almost certainly wrong.

In metagenomic data sets we do have the problem that we may have very
low and very high coverage data.  So we don't necessarily want to get
rid of all low-abundance k-mers, because they may represent truly low
abundance (but useful) data.

As part of the khmer@@ project in my lab, we have developed an approach
that sorts reads into high abundance and low abundance reads, and only
error trims the high abundance reads.

@@image

This does mean that many errors may get left in the data set, because we
have no way of figuring out if they are errors or simply low coverage,
but that's OK (and you can always trim them off if you really care).

Error profile@@

To run such error trimming, use the command ``trim-low-abund.py``::

  trim-low-abund.py -V -M 8e9 $datafile

Why (or why not) do k-mer trimming?
-----------------------------------

If you can assemble your data set without k-mer trimming, there's no
reason to do it.  The reason we're error trimming here is to speed up
the assembler (by removing data) and to decrease the memory requirements
of the assembler (by removing a number of k-mers).

To see how many k-mers we removed, @@count k-mers.

