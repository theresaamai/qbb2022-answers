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