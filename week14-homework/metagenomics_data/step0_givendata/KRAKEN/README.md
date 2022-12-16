#QBB Assignment: Week 14 Homework

Step 1B:
used conversion code named "code.py"
ran on bash using commands:
python code.py SRR492197.kraken SRR492197
python code.py SRR492194.kraken SRR492194
python code.py SRR492193.kraken SRR492193
python code.py SRR492190.kraken SRR492190
python code.py SRR492189.kraken SRR492189
python code.py SRR492188.kraken SRR492188
python code.py SRR492186.kraken SRR492186
python code.py SRR492183.kraken SRR492183

Step 1C:
ktImportText -q SRR492183_krona.txt -o SRR492183.html
ktImportText -q SRR492186_krona.txt -o SRR492186.html
ktImportText -q SRR492188_krona.txt -o SRR492188.html
ktImportText -q SRR492189_krona.txt -o SRR492189.html
ktImportText -q SRR492190_krona.txt -o SRR492190.html
ktImportText -q SRR492193_krona.txt -o SRR492193.html
ktImportText -q SRR492194_krona.txt -o SRR492194.html
ktImportText -q SRR492197_krona.txt -o SRR492197.html
ktImportText -q SRR492188_krona.txt -o SRR492188.html

A majority of the microbiome is composed of Enterococcus genus, and a small percentage of Staphylococcus. Overtime, Staphylococcus increases.

Step 2A:
bwa index assembly.fasta
bwa mem -t 4 -o SRR492183.sam assembly.fasta READS/SRR492183_1.fastq READS/SRR492183_2.fastq
bwa mem -t 4 -o SRR492186.sam assembly.fasta READS/SRR492186_1.fastq READS/SRR492186_2.fastq
bwa mem -t 4 -o SRR492188.sam assembly.fasta READS/SRR492188_1.fastq READS/SRR492188_2.fastq
bwa mem -t 4 -o SRR492189.sam assembly.fasta READS/SRR492189_1.fastq READS/SRR492189_2.fastq
bwa mem -t 4 -o SRR492190.sam assembly.fasta READS/SRR492190_1.fastq READS/SRR492190_2.fastq
bwa mem -t 4 -o SRR492193.sam assembly.fasta READS/SRR492193_1.fastq READS/SRR492193_2.fastq
bwa mem -t 4 -o SRR492194.sam assembly.fasta READS/SRR492194_1.fastq READS/SRR492194_2.fastq
bwa mem -t 4 -o SRR492197.sam assembly.fasta READS/SRR492197_1.fastq READS/SRR492197_2.fastq

Step 2B:
samtools sort -o SRR492183 SRR492183.sam
samtools sort -o SRR492186 SRR492186.sam
samtools sort -o SRR492188 SRR492188.sam
samtools sort -o SRR492189 SRR492189.sam
samtools sort -o SRR492190 SRR492190.sam
samtools sort -o SRR492193 SRR492193.sam
samtools sort -o SRR492194 SRR492194.sam
samtools sort -o SRR492197 SRR492197.sam

Step 2D:
jgi_summarize_bam_contig_depths --outputDepth depth.txt SRR492183 SRR492186 SRR492188 SRR492189 SRR492190 SRR492193 SRR492194 SRR492197

metabat2 -i assembly.fasta -a depth.txt -o bins_dir/bin

Question 3A:
We got 6 bins

Question 3B:
grep ">" bin.1.fa| wc -l  55
grep ">" bin.2.fa| wc -l  78
grep ">" bin.3.fa| wc -l  8
grep ">" bin.4.fa| wc -l  37
grep ">" bin.5.fa| wc -l  13
grep ">" bin.6.fa| wc -l  6
grep ">" assembly.fasta| wc -l 4103

Question 3C:
samtools faidx bin.1.fa
samtools faidx bin.2.fa
samtools faidx bin.3.fa
samtools faidx bin.4.fa
samtools faidx bin.5.fa
samtools faidx bin.6.fa
cut -f 2 bin.1.fa.fai | paste -sd+ - | bc 2705023
cut -f 2 bin.2.fa.fai | paste -sd+ - | bc 2251850
cut -f 2 bin.3.fa.fai | paste -sd+ - | bc 1656034
cut -f 2 bin.4.fa.fai | paste -sd+ - | bc 1227903
cut -f 2 bin.5.fa.fai | paste -sd+ - | bc 2483660
cut -f 2 bin.6.fa.fai | paste -sd+ - | bc 2862852
Yes, this looks correct, since the prokaryotic genome is about 5Mb, we are assembling about half of the genome using this method. 

Question 3D:
Compare our sequences to the reference genome of the bacteria that we expect to see, see how complete it is. To check for contamination, by comparing the sequence to the reference genome we would be able to see what sequences of bacteria there are in our reads that we do not expect to see. 

Step 3
refer to bash.sh

Question 4
We could be more strict about the classification, so if we set a threshold, such as if a bin is not more than 70% more one species, then we would not classify it.



