#!/usr/bin/env python

import matplotlib.pyplot as plt 
import numpy as np

#find most signficant SNP to plot, look in gwasIC50.assoc.linear 
#seperate out samples by genotype, look at vcf file 
#get corresponding phenotype, look at IC50 file 

ref = []
het = []
alt = []

file = open("gwasCB1908.assoc.linear")

pval = []
snp = []

for i in file:
    new = i.rstrip("\n").split()
    if new[4] == "ADD":
        pval.append(float(new[8]))
        snp.append(new[1])

min_value = min(pval) #lowest value in list
position = pval.index(min_value) #index of lowest value in the list 
significant = snp[position] #to find the most signficant snp 

print(significant)

genotypes = []
sampleid = []

#loop through vcf file
genotype_file = open("genotypes.vcf")
for i in genotype_file:
    if i.startswith("##"):
        continue
    geno_list = i.rstrip("\n").split("\t")
    if geno_list[2] == significant:
        genotypes = geno_list[9:]
    if i.startswith("#"):
        sampleid = geno_list[9:]
        # print(sampleid)

new_dict = dict(zip(sampleid, genotypes))

for i in pheno_file:
    if i.startswith("F"):
        continue
    pheno_list = i.rstrip("\n").split("\t")
    id_A = pheno_list[0] 
    id_B = pheno_list[1]
    combined =id_A + "_" + id_B 
    if pheno_list[2] == "NA":
        continue
    sample_val =float(pheno_list[2])
    gt = new_dict[combined]
    if gt == "0/0":
        ref.append(sample_val)
    if gt == "0/1":
        het.append(sample_val)
    if gt == "1/1":
        alt.append(sample_val)

fig, ax = plt.subplots()            
ax.boxplot([ref, het, alt])
ax.set_xlabel("Genotype")              
ax.set_ylabel("Phenotype")          
fig.savefig("boxplot.png")  
plt.show() 

