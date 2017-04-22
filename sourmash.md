# A sourmash tutorial

[sourmash](http://sourmash.readthedocs.io/en/latest/) is our lab's
implementation of an ultra-fast lightweight approach to
nucleotide-level search and comparison, called MinHash.

You can read some background about MinHash sketches in this paper:
[Mash: fast genome and metagenome distance estimation using MinHash. Ondov BD, Treangen TJ, Melsted P, Mallonee AB, Bergman NH, Koren S, Phillippy AM. Genome Biol. 2016 Jun 20;17(1):132. doi: 10.1186/s13059-016-0997-x.](http://genomebiology.biomedcentral.com/articles/10.1186/s13059-016-0997-x)

## Installing sourmash

To install sourmash, run:

```
pip install https://github.com/dib-lab/sourmash/archive/2017-ucsc-metagenome.zip
```

(Note, we are installing from [a development branch](https://github.com/dib-lab/sourmash/pull/188); many of the features below are not part of an official sourmash release yet.  They should be included in sourmash 2.0.)

## Fingerprint reads

Use case: how much do two (or more!) unassembled metagenomes resemble each
other?

Compute a scaled MinHash fingerprint from our reads:

```
mkdir ~/sourmash
cd ~/sourmash

sourmash compute --scaled 10000 ~/data/SRR*.pe.fq.gz -k 21,31
```

## Compare reads to assemblies

Use case: how much of the read content is contained in the assembly?

Fingerprint the assembly:

```
sourmash compute --scaled 10000 -k 21,31 ~/assembly/combined/final.contigs.fa
```

and now evaluate *containment*, that is, what fraction of the read content is
contained in the assembly:

```
sourmash search -k 21 SRR1976948.abundtrim.subset.pe.fq.gz.sig \
    final.contigs.fa.sig  --containment
```

and you should see:

```
1 matches; showing 3:
         /home/titus/assembly/combined/final.contigs.fa          0.573   final.contigs.fa.sig
```


Try the reverse - why is it bigger?
         
```
sourmash search -k 21 final.contigs.fa.sig \
    SRR1976948.abundtrim.subset.pe.fq.gz.sig --threshold=0.0 --containment
```

what do you get if you do this with the other set of reads?

## What's in my metagenome?

Download and unpack the k=21 RefSeq index described in
[CTB's blog post](http://ivory.idyll.org/blog/2016-sourmash-sbt-more.html):

```
mkdir ~/search_refseq
cd ~/search_refseq
curl -O http://spacegraphcats.ucdavis.edu.s3.amazonaws.com/microbe-sbt-k21-2016-11-27.tar.gz
tar xzf microbe-sbt-k21-2016-11-27.tar.gz
```

This produces a file `microbes.sbt.json` and a whole bunch of hidden
files in the directory `.sbt.microbes`.  This is an index of about 60,000
microbial genomes from RefSeq.

SRA: https://www.ncbi.nlm.nih.gov/sra/?term=SRR1976948

```
p_query p_genome
  1.3    84.2   NZ_LN515531.1 Methanobacterium formicicum genome assembly DSM1535, chromosome : chrI
  1.1     5.0   NZ_LN734822.1 Methanobacterium formicicum genome assembly isolate Mb9, chromosome : I
  0.5    27.4   NC_007759.1 Syntrophus aciditrophicus SB, complete genome
  0.3    19.3   NC_017934.1 Mesotoga prima MesG1.Ag.4.2, complete genome
  0.2    16.3   NZ_JXOJ01000001.1 Methanoculleus sp. S3Fa S3Fa_contig_1, whole genome shotgun sequence
  0.2     7.3   NZ_JMIO01000001.1 Methanoculleus sp. MH98A c1, whole genome shotgun sequence
  0.2    20.4   NC_010003.1 Petrotoga mobilis SJ95, complete genome
  0.1     4.6   NC_018227.2 Methanoculleus bourgensis MS2T complete genome
  0.1     1.7   NZ_BCAG01000001.1 Desulfatitalea tepidiphila DNA, contig: contig1, strain: S28bF, whole genome shotgun sequence
  0.1     2.1   NZ_KK211100.1 Desulfitibacter alkalitolerans DSM 16504 genomic scaffold K364DRAFT_scaffold00001.1, whole genome shotgun sequence
  0.0     5.1   NC_000916.1 Methanothermobacter thermautotrophicus str. Delta H, complete genome
  0.0     1.7   NZ_KK020675.1 Pseudomonas stutzeri KOS6 genomic scaffold scaffold1, whole genome shotgun sequence
  0.0     3.1   NC_017527.1 Methanosaeta harundinacea 6Ac, complete genome
  0.0     2.5   NZ_ACJX03000001.1 Anaerobaculum hydrogeniformans ATCC BAA-1850 A_hydrogeniformans-1.0.1_Cont0.1, whole genome shotgun sequence
  0.0     1.8   NZ_CGIH01000001.1 Syntrophomonas zehnderi OL-4 genome assembly Syntrophomonas Zehnderi OL-4, scaffold OL-4DRAFT_scaffold-1, whole genome shotgun sequence
  0.0     2.6   NC_016148.1 Thermovirga lienii DSM 17291, complete genome
  0.0     1.0   NZ_LGIA01000001.1 Sunxiuqinia dokdonensis strain SK contig00001, whole genome shotgun sequence
  3.2%          (percent of query identified)
```
