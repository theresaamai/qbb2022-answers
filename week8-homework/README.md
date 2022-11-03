Part 1:
`medaka_variant -i methylation.bam -f hg38.fa -r "chr11:1900000-2800000" -o chr11 -p chr11_phased.vcf`
`medaka_variant -i methylation.bam -f hg38.fa -r "chr14:100700000-100990000" -o chr14 -p chr14_phased.vcf`
`medaka_variant -i methylation.bam -f hg38.fa -r "chr15:23600000-25900000" -o chr15 -p chr15_phased.vcf`
`medaka_variant -i methylation.bam -f hg38.fa -r "chr20:58800000-58912000" -o chr20 -p chr20_phased.vcf`

Part 2:
whatshap haplotag -o phased11.bam --reference hg38.fa --regions chr11:1900000:2800000  --output-haplotag-list haplotag11 chr11/round_0_hap_mixed_phased.vcf.gz methylation.bam
whatshap haplotag -o phased14.bam --reference hg38.fa --regions chr14:100700000:100990000  --output-haplotag-list haplotag14 chr14/round_0_hap_mixed_phased.vcf.gz methylation.bam
whatshap haplotag -o phased15.bam --reference hg38.fa --regions chr15:23600000:25900000  --output-haplotag-list haplotag15 chr15/round_0_hap_mixed_phased.vcf.gz methylation.bam
whatshap haplotag -o phased20.bam --reference hg38.fa --regions chr20:58800000:58912000  --output-haplotag-list haplotag20 chr20/round_0_hap_mixed_phased.vcf.gz methylation.bam

Part 3: 
whatshap split phased11.bam --output-h1 output_h1_11 --output-h2 output_h2_11 haplotag11
whatshap split phased14.bam --output-h1 output_h1_14 --output-h2 output_h2_14 haplotag14
whatshap split phased15.bam --output-h1 output_h1_15 --output-h2 output_h2_15 haplotag15
whatshap split phased20.bam --output-h1 output_h1_20 --output-h2 output_h2_20 haplotag20

samtools cat -o concat_h1 output_h1_11 output_h1_14 output_h1_15 output_h1_20
samtools cat -o concat_h2 output_h2_11 output_h2_14 output_h2_15 output_h2_20

Part 6: 
No, based on the information that we have now, we can not expect that each region would correspond to the same parent of origin. 
  