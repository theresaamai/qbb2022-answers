#!/usr/bin/env python

import matplotlib.pyplot as plt 
import numpy as np

# genotype = np.genfromtxt("plink.eigenvec", dtype = None, encoding = None, names = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"])
#
# #plotting first 2 components PCA of genetic relatedness
# fig, ax = plt.subplots(nrows = 2)
# ax[0].set_ylabel("PC2")
# ax[0].set_xlabel("PC1")
# ax[1].set_ylabel("PC3")
# ax[1].set_xlabel("PC1")
# ax[0].scatter(genotype["j"], genotype["k"])
# ax[1].scatter(genotype["j"], genotype["l"])
# fig.tight_layout()
# plt.savefig("ex2.png")
# plt.show()

# freq = np.genfromtxt("plink.frq", dtype = None, encoding = None, names = ["chr", "snp", "A1", "A2", "MAF", "NCHROBS"])
#
# val = []
# for each in freq[1:]:
#     val.append(float(each[4]))
#
# #plotting histogram of allele frequency
# fig, ax = plt.subplots()
# ax.hist(val, alpha = 0.5, label = "")
# ax.set_xlabel("allele")
# ax.set_ylabel("frequency")
# ax.set_title("allele frequency")
# plt.savefig("af_plot")
# plt.show()

file = open("gwasCB1908.assoc.linear")
bp = []
pval = []
chrom = []
for line in file:
    new = line.rstrip("\n").split() #need to split string along spaces (line is a string)
    if new[4] == "ADD": #only want lines where column 5 = ADD
        bp.append(int(new[2])) #3rd column is bp convert into integer
        # p = float(new[8])
        # logp = -1 * np.log10(p)
        # pval.append(logp)
        pval.append(-1 * np.log10(float(new[8]))) #need to convert pval to -log10 use numpy
        chrom.append(int(new[0])) #need to make chromosome list for graphing later
pos = []
for i, item in enumerate(bp):
    pos.append(i)
#this highlights significant pvals
sigpval = []
sigpos = []
for p, item in enumerate(pval): #p is item on item  is actual p value
    if item > 5:
        sigpval.append(item)
        sigpos.append(pos[p]) #add correspodning position
#go through chromosome list and see first place where we see chrom number and last place then take average which is where tick mark for graph will be
xtick = []
for i in range(1, 23):
    first_pos = None
    last_pos = None
    for c, item in enumerate(chrom):
        if item == i:
            if first_pos == None:
                first_pos = c
            if last_pos == None or c > last_pos: #this updates last position
                last_pos = c
    middle = (last_pos + first_pos)/2
    xtick.append(middle)
    
#nowplot Manhattan
fig, ax = plt.subplots(figsize = (10, 6)) #wide then tall
ax.scatter(pos, pval)
ax.scatter(sigpos, sigpval, color = "red")
ax.set_xticks(xtick)
ax.set_xticklabels(range(1, 23))
ax.set_xlabel("chromosome position")
ax.set_ylabel("-log10(pval)")
ax.set_title("Manhattan CB1908")
fig.savefig("Manhattan CB1908")
# plt.show()

