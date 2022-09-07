#QBB - Day 3 - Homework Exercises Submission
Exercise 1
plink --vcf ALL.chr21.shapeit2_integrated_v1a.GRCh38.20181129.phased.vcf.gz --pca 3

Exercise 2
import matplotlib.pyplot as plt
import numpy as np

eigenvector = np.genfromtxt("plink.eigenvec", dtype = None, encoding = None, names = ["locus1", "locus2", "val1", "val2", "val3"])

fig, ax = plt.subplots(nrows = 2)
ax[0].set_ylabel("PC2")
ax[0].set_xlabel("PC1")
ax[1].set_ylabel("PC3")
ax[1].set_xlabel("PC1")
ax[0].scatter(eigenvector["val1"], eigenvector["val2"])
ax[1].scatter(eigenvector["val1"], eigenvector["val3"])
fig.tight_layout()
plt.savefig("ex2_a_and_b.png")

these figures show us the different cross sections of the similarities between genotypes of individuals - basically this shows us the similarities between individuals at different angles. We do observe some structure, we see that there is some clustering this could possibly be due to similar SNPs amongst individuals from similar geographic regions. 

Exercise 3
join <(sort plink.eigenvec) <(sort integrated_call_samples.panel) > joined_file.txt #this is to join the 2 files together in unix
np.genfromtxt("joined_file.txt") #this is to apply the file to a numpy array 

Based off the plot, genetic variation is more dependent on super population, compared to sex or population. 
