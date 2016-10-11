Run the MEGAHIT assembler
=========================

Assemble! ::

   cd
   git clone https://github.com/voutcn/megahit.git
   cd megahit
   make

   cd /mnt/data
   curl -O https://s3-us-west-1.amazonaws.com/dib-training.ucdavis.edu/metagenomics-scripps-2016-10-12/SRR1976948.abundtrim.subset.pe.fq.gz
   curl -O https://s3-us-west-1.amazonaws.com/dib-training.ucdavis.edu/metagenomics-scripps-2016-10-12/SRR1977249.abundtrim.subset.pe.fq.gz

   mkdir /mnt/assembly
   cd /mnt/assembly
   ln -fs ../data/*.subset.pe.fq.gz .

   ~/megahit/megahit --12 SRR1976948.abundtrim.subset.pe.fq.gz,SRR1977249.abundtrim.subset.pe.fq.gz -o combined
