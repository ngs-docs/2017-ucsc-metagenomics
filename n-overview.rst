Non-model organisms and RNAseq
==============================

With non-model systems, where there is neither a good genome nor a lot
of mRNAseq data, you have to build your own transcriptome from scratch
-- so-called "de novo transcriptome assembly".  There are a few
programs to do this - most notably Trinity and Oases - and `we have
found little difference <https://peerj.com/preprints/505/>`__.

.. thumbnail:: files/assembly.png
   :width: 20%

The main problem you'll run into with non-model mRNAseq is that the
output is fairly noisy with respect to splice variants.  Our
experience has been that many of these splice variants are probably
"real" -- in the sense of actually present -- but may be biological
"noise", in the sense that they are not actually functional  (See
`this excellent paper by Pickrell and Pritchard making the case
<http://www.ncbi.nlm.nih.gov/pubmed/21151575>`__).  Regardless,
there's little that you can do about this, although we will talk about
it a bit on the second day.

The overall process
-------------------

.. figure:: _static/nonmodel-rnaseq-pipeline.png

* Copy over your RNAseq data (from two or more samples);
* Trim primers and junk from sequence (:doc:`n-quality`)
* Do abundance normalization (:doc:`n-diginorm`)
* Assemble everything together (:doc:`n-assemble`)

This gives you an assembled transcriptome, consisting of many transcripts
and transcript families.

At this point you can do one or more of the following:

* Annotate your transcripts (:doc:`annotate`)
* Quantify your transcripts and examine differential expression (:doc:`quantification`)
* BLAST your transcripts individually (:doc:`n-blast`)

Next: :doc:`login`
