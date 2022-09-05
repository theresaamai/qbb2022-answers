# QBB2022 - Day 1 - Lunch Exercises Submission 
1. I'm excited to learn <coding>.
2a. cp ~/data/bed_files/genes.chr21.bed . 
cp ~/data/bed_files/exons.chr21.bed . 
2b. code: less exons.chr21.bed | wc to find the number of exons = 13653 
code: less genes.chr21.bed | wc to find the number of genes = 219 
13,653 exons / 219 genes = about 62 exons per gene 
2c. I would sort the genes by average number of exons, then find the gene in the middle of this list. 
3a. cp ~/data/bed_files/chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed
3b. 305 1
 678 2
  79 3
 377 4
 808 5
 148 6
1050 7
 156 8
 654 9
  17 10
  17 11
  30 12
  62 13
 228 14
 992 15
code: cut -f 4 chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed | sort -n | uniq -c
3c. Pipe sort -k 1 to the current code 
4a. cp ~/data/metadata_and_txt_files//random_snippet.vcf .
4b.  123 ACB
 112 ASW
 173 ESN
 180 GWD
 122 LWK
 128 MSL
 206 YRI
 code: cut -f 2,3 integrated_call_samples.panel | grep AFR | cut -f 1 | sort | uniq -c
 4c. You can repeat the code and individually search each population 
 5a. cp ~/data/vcf_files/random_snippet.vcf .
 5b. cut -f 1-9,13 random_snippet.vcf > HG00100.vcf
 5c. cut -f 10 HG00100.vcf > f10.txt #to cut out column for sample HG00100 and save as new file
sort -n f10.txt | uniq -c #sort and count number of each genotype
9514 0|0
 127 0|1
 178 1|0
 181 1|1
 5d. cut -f 8 HG00100.vcf > f8.txt
sed '/^#/d' f8.txt | grep AF=1 | wc -l #delete header rows find number of times AF=1 and count
34 rows contain AF =1
5e. AF=1 can appear 6 times per row (it can appear in field 4-9 of the INFO field as AF=1, EAS_AF=1, EUR_AF=1, AFR_AF=1, AMR_AF=1, SAS_AF=1)
5f. I would cut the info column out, which contains the AFR values. I would then make a list of these values that are now going to be seperated by spaces and not commas. Then I would grep for the AFR_AF Column and uniq-c this so that now I can see how many AFR values there are, and how many times they repeat. 