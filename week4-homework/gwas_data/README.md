#QB Week 4 Homework 

Bash Commands 

Part 2
plink --vcf genotypes.vcf --pca 10

Part 3
plink --vcf genotypes.vcf --freq

Part 4 
plink --vcf genotypes.vcf --assoc --pheno CB1908_IC50.txt --allow-no-sex --covar plink.eigenvec --linear --out gwasCB1908
plink --vcf genotypes.vcf --assoc --pheno GS451_IC50.txt --allow-no-sex --covar plink.eigenvec --linear --out gwasIC50

Part 7

for the most signficant snp in CB1908, we see that there is an association in the DIP2B intron region. 