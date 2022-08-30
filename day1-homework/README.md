#QBB2022 - Day 1 - Homework Exercises Submission 
1. Error message is awk: illegal field $(), name "nuc". To fix this, in the script we need to define the bash variable for awk. So we need to use: awk -v var=$nuc '/^#/{next} {if ($4 == var) {print $5}}' $1 | sort | uniq -c
Considering  A
 354 C
1315 G
 358 T
Considering  C
 484 A
 384 G
2113 T
Considering  G
2041 A
 405 C
 485 T
Considering  T
 358 A
1317 C
 386 G
Yes, this make sense because for the example of A to G occuring at 1315, this is an example of a transition (purine to purine). Transitions are a common mutation. 

2. No, using this segmentation the promoters are not clearly defined. 
commands: genefile=~/data/vcf_files/random_snippet.vcf 
bedfile=~/data/bed_files/chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed
awk '{if ($4 == 1) {print}}' $bedfile > st1.bed
bedtools intersect -a $genefile -b st1.bed > intersect.bed
awk '{if ($4 == "C") {print $5}}' intersect.bed | sort | uniq -c
ooutput:  5 A
   7 G
  15 T
This shows us that the most common alternate allele is Thymine which makes sense because C -> T is very common. 

3. awk '/^#/{next} {print $1,$2-1, $2}' $1 > variants.bed #ignores the headers, and prints out all the columns and makes it as a new variable which will now be stored in variants.bed
sort -k1,1 -k2,2n ~/data/bed_files/genes.bed > genes.sorted.bed - this sorts the gene file by column and stores it into the new sorted file named genes.sorted.bed
bedtools closest -a variants.bed -b genes.sorted.bed - this tells us the closest gene for each variant 
Error #1 = we need to make sure the file is TAB delimited - to fix this error, we need to add the command "\t"
Error #2: Sorted input specified, but the file variants.bed has the following out of order record - to fix this error we need to sort the variants.bed file, so we will pipe sort to the awk command. 
Correct script: awk '/^#/{next} {print $1"\t" $2-1"\t" $2}' $1 | sort -k1,1 -k2,2n > variants.bed
sort -k1,1 -k2,2n ~/data/bed_files/genes.bed > genes.sorted.bed 
bedtools closest -a variants.bed -b genes.sorted.bed

There are 10,293 variants and 200 unique genes. With the bedtools closest, there are about 51 variants connected to a gene. 

