# Cmd Line Tools Lecture Notes

#### *Jeanna Clark*

#### *August 3, 2015*

# Command Line Tools Lecture Notes

## Module 1: Basic Unix Commands

**Unix commands**:

- date
- echo hello
- pwd (print working directory)
- cd (change directory)
- cd . (current directory)
- cd .. (parent directory)
- ls (list files in directory)
- ls -l (list files in directory + additional file info)
- ls -lt (list files in directory + additional file info in chron order)
- man ls (info re: command ls)

**File Naming**:

- ls apple.* (lists all files with apple)
- ls ?pple.genome (returns A/apple.genome)
- ls [a-z]*.genome (returns all files with extensions .genome)
- ls p*.genome (returns all files with p.genome in title)
- ls {pear, peach}.genome (lists all files with pear or peach)

**Content Creation**:

- mkdir apple pear peach (makes directories named apple, pear, and peach)
- ls apple.* (lists all apple. file types)
- cp apple.* apple (copies all apple file types into apple directory)
- mv pear.* pear (moves all pear file types into pear directory)
- rm -i apple.genome (removes apple.genes with a prompt to remove file)
- rmdir Old.stuff (removes empty directories)
- rm -r Old.stuff (removes all sub-directories & itself, recursively)

**Accessing Content in Unix**:

- more apple.genome (shows file’s content one page at time (space bar))
- more apple.genome /> (shows file’s content one page at time & looks for next sequence (major page heading)) [fast.a files?]
- less apple.genome (shows file’s content one page at time and in reverse (space bar + up arrow))
- head peach.genome (gives first ten lines of file)
- head -50 peach.genome (gives first 50 lines of file)
- tail peach.genome (gives last ten lines of file)
- tail -15 peach.genome (gives last 15 lines of file)
- cat */*.genes (combines all directories genes files)

**redirecting content**:

- wc apple/apple.genome (prints file’s #lines; #words; #char; file name)
- wc -l apple/apple.genome (prints #lines in file)
- wc -l apple/apple.genome > nlines (stores info into nlines)
- wc -l < apple/apple.genes (stores info)
- ls | wc -l (pipes input of wc to be output of ls command)
- cat */*.genome | more (allows us to see one page of file at a time)

**querying content**:

- sort months (lists contents of file in alphabetical order)
- sort -r months (lists contents of file in reverse alphabetical order)
- vi months (in command prompt text editor)
- sort -k2 months (sorts file by column 2)
- sort -kn2 months (sorts file by column 2 numerically)
- sort -k 2nr months (sorts file by column 2 numerically, in reverse)
- sort -k 3 -k 2n months (sorts column 3 first then column 2 numerically)
- cut -f1 months (prints column 1 only)
- cut -f1-3 months (prints columns 1-3 only)
- cut -d ‘’ -f1 months (prints column 1 by the defined delimiter (e.g., space))
- cut -d ‘’ -f3 months > seasons (stores space delimited column 3 into seasons)
- sort -u seasons (prints unique sorted list)
- uniq seasons | sort -u (gives unique seaons in alphabetical order)
- uniq -c seasons (gives number of occurances)
- grep root */*.samples (prints the parents of the path)
- grep " 12 winter" months (tells where this appears)
- grep -n “12 winter” months (tells the content of line with the line number)

**comparing content**:

- diff orchard orchard.1 (tells all differences b/w files & their locations)
- comm apple/apple.samples pear/pear.samples
- comm -1 -2 apple/apple.samples pear/pear.samples (ignores items in lines 1 &2)

**archiving content**:

- gzip apple.genome (creates .gz compressed file)
- gunzip apple.genome.gz (uncompresses .gz file)
- bzip2 apple.genome (creates .bz2 compressed file [better compression than gzip])
- bunzip apple.genome.bz2 (uncompresses .bz2 file)
- tar -cvf Apple.tar apple.genes apple.genome apple.samples (c = compress; v = vost; f = files; combines files into archive)
- gzip Apple.tar
- gunzip Apple.tar.gz
- tar -xvf Apple.tar
- tar -cvf AppleD.tar apple/
- bzip2 AppleD.tar
- tar -xvf AppleD.tar
- gzip apple.genome
- apple.genome.gz

## Module 2: Sequences & Genomic Features

### Microbiology Primer

**Genomes**

- one copy lives in nucleus

**Eukaryotic gene expression**

- gene goes through transcription
- Pre-mRNA strand created by transcription
- Pre-mRNA exons spliced into one mRNA strand (introns removed)
- mRNA translated into protein

**different exon combinations produced during transcription will produce different protein products**

- called splice variants or transcripts

**Major computational biology questions to ask:**

- What are the genes?
- What are the proteins?
- What are their sequences?
- Quantify their abundance.
- What is their role in the cell?

### Sequence Representation & Generation

**Questions:**

- What do sequences look like?
- What do they do?
- How many are there?

**Genomic sequences**

- Adenine (A)
- Guanine (G)
- Thyamine (T)
- Cytosine (C)

**mRNA sequences**

- Uracil replaces Thyamine (U)

**Sequence Generation**

- shear DNA / RNA to roughly same length fragments
- amplifiy fragments if more material needed
- sequence from one end only = single-end reads
- sequence from both ends = paired-end reads
- Assembly graph
  - node fragments are called reads
  - algorithm needed to put these reads together so that all are included

**Sequencing methods**

- Sanger (used until 2008)
  - FASTA / Pearson format
  - 1 line header starts with “>” followed by unique identifier and metadata
  - be careful not to include any blank lines
- Next Generation Sequencing (NGS; 2008 - present)
  - FASTQ format
  - 4 line record
  - 1st line starts with “@” and ends with “/1” or “/2” to indicate single / paired reads
  - 2nd line is gene sequence; N codes for unknown
  - 3rd line starts with “+”
  - 4th line is base quality score (codes for confidence of matching line 2 gene)

**Base quality scores (FASTQ format; line 4)**

- p = probability that call at bse is correct
- quality value = Q = -10log(base10)p
- represented by ASCII symbols (33 - 126)
- values below 20 are low
- max value is ~ 40

### Annotation

**Genomic features**

- genome annotation: determine precise location and structure of genomic features along genome
- genomic features:
  - genes
  - promoters
  - protein binding sites
  - translation start / stop sites
  - SNasel sites
  - et cetera

**BED format**

- browser extensible data (BED) format
- coordinates are 0-based
- basic format
  - column 1: chromosome / scaffold
  - column 2: start of feature (0-based; count from 0 instead of 1)
  - column 3: end of feature
- extended format
  - columns 1-3 plus…
  - name: exon position
  - score: value b/w 0 - 1000 to indicate color intensity
  - strand direction (+/-)
  - thick_start: start region of protein coding
  - thick_end: end region of protein coding
  - rgb: (red, green, blue)
  - block coordinates can be included

**GTF format**

- genomic transfer format (GTF)
- each interval feature takes 1 line
- columns are separeted by “”
- fields within column 9 separated by " "
- coordinates are 1-based (count starting with 1)
- column 1: chromosome / scaffold ID
- column 2: source (program / website / etc)
- column 3: type of feature
- column 4: beginning of feature along axis
- column 5: end of feature
- column 6: score (confidence)
- column 7: strand (forward + / reverse -)
- column 8: frame (0/1/2)
- column 9: composite with two fields
  - field 1: gene ID followed by name of gene
  - field 2: transcript ID
  - et cetera…

**GFF3 format**

- genomic feature format version 3 (GFF3)
- column 1: chromosome / scaffold ID
- column 2: source (cufflinks / URL / etc)
- column 3: type of feature (mRNA / exon / etc)
- column 4: start coordinate of feature on genome
- column 5: end coordinate of feature on genome
- column 6: score
- column 7: strand
- column 8: coding frame (“.” = unknown)
- column 9: fields (e.g., ID, name, parent cluster)

### Alignment

- sequence a fragment of the gene (RNA) or region (DNA), then map (align) it to the genome
- Alignment: a mapping between the letters of the two sequences, with some spaces (indels)
- Alignment adjusts for differences caused by:
  - polymorphisms
  - sequencing errors
  - introns
  - insertion / deletion / substitution

**Alignment types**

- contiguous alignment e.g., DNA fragments can be aligned to genome contiguously
- spliced alignment e.g., mRNA splices info that’s located at exons
  - if read exists entirely within an exon, it’ll be contiguous alignment (one piece)
  - if read spans boundary b/w two exons, it needs to be divided (two pieces)

**Next generation sequencing alignments**

- NGS produces normally distributed fragment lengths
  - mapping should have same distance between reads & same orientation
  - concordant (properly paired): distance boundary same & same orientation
  - non-concordant: reads not mapping in same orientations or distance between reads are too far apart

**SAM format**

- header lines start with “@”
- @HD: tells what file type is
- @SQ: tells sequence (SN) info & length (LN)
- @PG: tells program version (VN), name (ID), etc
- alignments are broken into 1 line each
- each alignment field is separated with ‘’ (tab)
  - Field 1: Read ID - pulled from FASTQ file header
  - Field 2: FLAG
  - Field 3: scaffold / chromosome ID
  - Field 4: Start position of alignment
  - Field 5: mapping quality
  - Field 6: CIGAR (compressed representation of alignment)
  - Field 7: mate’s chromosome location; “=” codes for same; “*" codes for mate not mapped (e.g., concordant)
  - Field 8: mate start location
  - Field 9: mate distance measured along genomic axis
  - Field 10: query sequence
  - Field 11: query base quality
  - Field 12: tags (program specific)

**sample SAM tags**

- AS: alignment score
- NM: edit distance to reference
- NH: number of hits
- XS: strand
- HI: hit index for this alignment

**SAM field 2: FLAG**

- binary represented data
- 0x1: multiple segments (mates)
- 0x2: each segment properly aligned
- 0x4: segment unmapped
- 0x8: next segment unmapped
- 0x10: SEQ is reverse completed in the alignment
- 0x20: SEQ of next segment is reverse complemented
- 0x40: first segment (mate)
- 0x80: last segment (mate)
- 0x100: secondary alignment
- 0x200: not passing quality checks
- 0x400: PCR or optical duplicate
- 0x800: supplementary alignment
- e.g., 0000 0110 0011 (base 2)
  - paired, proper pair, mapped, mate mapped
  - forward, mate reverse, first in pair, not second (last) in pair,
  - passed quality check, not PCR duplicate, not a suppl. alignment

**SAM field 6: CIGAR**

- sequence of short strings coding editing operations
- M: match (sequence match or subsitution)
- I: insertion to the reference
- D: deletion from the reference
- N: skipped region (intron); very special case
- S: soft clipping (sequence start or end not aligned; seq appears in SEQ)
- H: hard clipping (seq not in SEQ)
- P: padding first segment (mate)
- =: sequence match
- X: sequence mismatch

### Recreating Sequences & Features Retrival

**NCBI Data Repository**

- ncbi.nlm.nih.gov
- example transcript data search
  - search for IL-2 homo sapiens mRNA (nucleotide database type)
  - click FASTA to get format
  - send to file & download in FASTA format
- example RNA-seq data search
  - search for strawberry RNA-seq species (SRA - short read archive database type)
  - click data file to go to the data table
  - download tab -> downloading SRA data using command line utilities
  - write down the ID for the data
  - use “wget” URL in terminal window
  - paste wget command into terminal
  - modify URL to be just the ID for the URL
  - nohup fastq-dump filename.sra &
  - head filename.fastq
  - fastq-dump –help (gives info on parameters)

**UCSC Genomic Data Repository**

- genome.ucsc.edu
- gene prediction data example
  - clade: mammal
  - genome: human
  - assembly: latest version of genome
  - group: genes & gene predictions
  - track: refseq genes
  - table: refGene
  - region: position chr22
  - output format: GTF
  - file -> save as… -> filename.gtf.txt
  - output format: BED -> whole gene
  - file -> save as… -> filename.bed.txt
- repeats data example
  - clade: mammal
  - genome: human
  - assembly: latest version of genome
  - group: repeats
  - track: repeatmaster
  - position: chr22
  - filter: repName -> match: “Alu*"
  - output: BED
  - file -> save as… -> alus.bed.txt

### SAMtools

**Installation**

- www.htslib.org/download
- download SAMtools package
- in terminal window cd to downloads
- unarchive SAMtools
- cd into SAMtools directory
- type ‘make prefix=/path/to/dir install’

**Command Line Prompts for SAMtools**

- samtools1 = version, commands, etc (need package installed)
- cd example.bam -> samtools1 flagstat = useful summary stats
- nohup samtools1 sort example.bam example.sorted & = expensive operation, so run in background
- samtools index example.sorted.bam =
- zcat NA12814_1.fastq.gz | wc -l = count the # of lines
- nohup samtools1 merge NA12814.bam NA12814_1.bam NA12814_2.bam & = run in background & merge files
- samtools view -h example.bam = view data with header
- samtools1 view -bT /data1/igm3/genomes/hg38/hg38c.ga example.sam > example.sam.bam = converts sam to bam file formats
- samtools1 view
- samtools1 view example.bam “chr22:24000000-25000000” | head = view ‘head’ chromosome 22 @ index 240000000 - 250000000
- samtools1 view -H example.bam
- samtools1 index example.bam
- samtools1 view -L example.bed example.bam | head = view lines + coordinate ranges

### BEDtools

**Tools include**

- genome arithmetic
- multi-way file compairson
- paired-end manipulations
- format conversion
- et cetera…

**Installation**

- [https://github.com/arq5x/bedtools2](https://github.com/arq5x/bedtools2)
- download BEDtools package
- in terminal…. ….

**Command Line Prompts for BEDtools**

- bedtools = lists all operations / sub-commands available
- bedtools >& bedtools.log
- bedtools intersect -wo -a RefSeq.gtf -b Alus.bed | more =
- bedtools intersect -wo -a RefSeq.gtf -b Alux.bed | cut -f9 | cut -d ‘’ -f2 | sort -u | wc -l
- bedtools intersect -split -wao -a RefSeq.bed -b Alus.bed | more
- bedtools bamtobed –help
- bedtools bamtobed -split -i NA12814.bam | grep ERR1880081.370400
- bedtools bedtobam –help
- more hg38c.hdrs = header file == very specific!
- bedtools bedtobam -i RefSeq.gtf -g hg38c.hdrs > refseq.bam
- samtools view refseq.bam
- bedtools bedtobam -i RefSeq.bed -g hg38c.hdrs > refseq.bam
- samtools view refseq.bam | more
- bedtools bedtobam -bed12 -i RefSeq.bed -g hg38c.hdrs > refseq.bam
- samtools view refseq.bam | more
- bedtools getfasta –help
- bedtools getfasta -fi /data1/igm3/genomes/hg38/hg38c.fa - bed RefSeq.gtf -fo RefSeq.gtf.fasta
- more RefSeq.gtf.fasta
- bedtools getfasta -fi /data1/igm3/genomes/hg38/hg38c.fa - bed RefSeq.bed -fo RefSeq.bed.fasta (more useful)
- more RefSeq.bed.fasta
- bedtools getfasta -split -fi /data1/igm3/genomes/hg38/hg38c.fa -bed RefSeq.bed -fo RefSeq.bed.fasta
- more RefSeq.bed.fasta

## Module 3: Alignment & Sequence Variation

### Overview

- each human genome is unique (.1% difference)
- 1% difference between monkeys
- substitution / insertion / deletions
- whole genome shotgun (WGS) variation
- whole exome shotgun (WES) variation

### Detection Tools

**samtools mpileup format**

- column 1: chromosome number

- column 2: position

- column 3: reference letter (atgc)

- column 4: number of reads that align

- column 5: string of characters that codes for bases in each of reads at that position

  - . = match, forward

  - , = match, reverse

  - T = mismatch forward

  - t = mismatch reverse

  - ^ = beginning of read

  - $ = end of read

  - - = insertion

  - - = deletion

  - > = reference skip

- column 6: qualities

- column 7 (opitional): specific position

**VCF / BCF format**

- [https://samtools.github.io/hts-specs/VCFv4.2.pdf](https://samtools.github.io/hts-specs/VCFv4.2.pdf)

- ## starts each line

- header data

- INFO lines

  - NS = # of samples
  - DP = depth
  - AF = allele frequency
  - AA = assessor allele
  - DB = debisink memberhsip?
  - H2 = hack2 membership?

- FILTER lines

- FORMAT lines

  - GT = genotype
  - GQ = genotype quality
  - DP = read depth
  - HQ = haplotype
  - FT = filter pass
  - GL = genotype liklihood
  - MQ = mapping quality

- column 1: chromosome number

- column 2: position of the genome

- column 3: identifier

- column 4: variant (letter) that’s in the reference genome

- column 5: alternate variant letter that’s present in the sequence reads

- column 6: quality of variant call

- column 7: filter – whether the variant passed filter

- column 8: info re: reads that support quality

- column 9: form

- entries:

  - SNP
  - DEL
  - Mixed

**Bowtie**

- contiguous matches
- DL bowtie index of human genomes / mouse genomes / etc
- mkdir hpv
- bowtie2-build HPV_all.fasta hpv/hpv: creates index
- ls hpv = list of index genome
- ( wc -l exome.fastq )/ 4 = how many sequences there are
- bowtie2 >& bowtie2.log
- bowtie2 -p 4 -x /data1/igm3/gemones exome.fastq -S exome.bt2.sam = aligns the exon reads to human genome
- samtools view -bT /data1/igm/gemoes exome.bt2.sam > exome.bt2.bam
- bowtie2 -p 4 –local -x /data1/igm3/gemones exome.fastq -S exome.bt2.sam = aligns the exon reads to human genome (local finds partial matches per read, so it’s more values)

**BWA**

- bwa index HPV_all.fasta = creates index
- ls -lt
- bwa mem -t 4 /data1/igm3/genomes.fa exome.fastq > exome.bwa.sam = maps exon reads to human genome
- more exome.bwa.sam
- samtools view -bT /data1/igm3/genomes.fa exome.bwa.sam > exome.bwa.bam
- samtools view exome.bwa.bam

**SAMtools MPileup**

- samtools index sample.bam = creates sample.bam.bai index file
- samtools mpileup -f /data1/igm3/gemones.fasta sample.bam > sample.mpileup (file needs to be sorted & indexed)
- samtools flagstat sample.bam
- samtools mpileup -v -u -f /data1/igm3/gemones.fasta sample.bam > sample.vcf (file needs to be sorted & indexed)
- samtools mpileup -g -f /data1/igm3/gemones.fasta sample.bam > sample.bcf (file needs to be sorted & indexed)

### BCFtools

- manipulates VCF / BCF files
- bcftools view sample.bcf
- bcftools call -v -m -O z -o sample.vcf.gz sample.bcf = use mpileup location data to make bcf calls
- zcat sample.vcf.gz = view file
- 1 line for each variant that was alled
- zcat sample.vcf.gz | grep -v “^#” | wc -l (remove all lines beginning with #) = # of variants

### Variant Calling

- ls sample.bam
- samtools index sample.bam = sort & index file
- ls -l
- samtools mpileup -g -f /data1/igm3/gemones.fasta sample.bam > sample.bcf
- bcftools call -v -m -O z -o sample.vcf.gz sample.bcf
- zcat sample.vcf.gz (shows variants only per line)
- samtools tview -p 17:7579600 -d T sample.bam /data1/igm3/genomes.fasta (remove -d T to view in terminal)

## Exam 3

As part of the effort to catalog genetic variation in the plant Arabidopsis thaliana, you re-sequenced the genome of one strain (‘wu\_0\_A’; genome file: ‘wu\_0.v7.fas’), to determine genetic variants in this organism. The sequencing reads produced are in the file ‘wu\_0\_A_wgs.fastq’. Using the tools bowtie2, samtools and bcftools, develop a pipeline for variant calling in this genome. NOTE: Genome and re-sequencing data have been obtained and modified from those generated by the 1001 Genomes Project, accession ‘Wu\_0\_A’.

Apply to questions 1 - 5:

- Generate a bowtie2 index of the wu\_0\_A genome using bowtie2-build, with the prefix ‘wu_0’.

Apply to questions 6 - 10:

- Run bowtie2 to align the reads to the genome, under two scenarios: first, to report only full-length matches of the reads; and second, to allow partial (local) matches. All other parameters are as set by default.

For the following set of questions (11 - 20), use the set of full-length alignments calculated under scenario 1 only. Convert this SAM file to BAM, then sort the resulting BAM file.

Apply to questions 11 - 15:

Compile candidate sites of variation using SAMtools mpileup for further evaluation with BCFtools. Provide the reference fasta genome and use the option “-uv” to generate the output in uncompressed VCF format for easy examination.

Apply to questions 16 - 20:

Call variants using ‘BCFtools call’ with the multiallelic-caller model. For this, you will need to first re-run SAMtools mpileup with the BCF output format option (‘-g’) to generate the set of candidate sites to be evaluated by BCFtools. In the output to BCFtools, select to show only the variant sites, in uncompressed VCF format for easy examination.

1 - How many sequences were in the genome? 2 - What was the name of the third sequence in the genome file? Give the name only, without the “>” sign. 3 - What was the name of the last sequence in the genome file? Give the name only, without the “>” sign. 4 - How many index files did the operation create? 5 - What is the 3-character extension for the index files created? 6 - How many reads were in the original fastq file? 7 - How many matches (alignments) were reported for: i) the original (full-match) setting? and ii) with the local-match setting? Exclude lines in the file containing unmapped reads. Give these two numbers separated by a space (e.g., 23 53). 8 - How many reads were mapped, in each scenario? Use the format above. 9 - How many reads had multiple matches, in each scenario? Use the format above. You can find this in the bowtie2 summary; note that by default bowtie2 only reports the best match for each read. 10 -How many alignments contained insertions and/or deletions, in each scenario? Use the format above. 11 - How many entries were reported for Chr3? 12 - How many entries have ‘A’ as the corresponding genome letter? 13 - How many entries have exactly 20 supporting reads (read depth)? 14 - How many entries represent indels? 15 - How many entries are reported for position 175672 on Chr1? 16 - How many variants are called on Chr3? 17 - How many variants represent an A->T SNP? If useful, you can use ‘grep –P’ to allow tabular spaces in the search term. 18 - How many entries are indels? 19 - How many entries have precisely 20 supporting reads (read depth)? 20 - What type of variant (i.e., SNP or INDEL) is called at position 11937923 on Chr3?