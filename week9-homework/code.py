#!/usr/bin/env python

import numpy as np
import numpy.lib.recfunctions as rfn
from scipy.cluster.hierarchy import dendrogram, linkage, leaves_list
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import statsmodels.api as sm
from scipy import stats
from statsmodels.stats import multitest

input_arr = np.genfromtxt("dros_gene_expression.csv", delimiter=',', names=True, dtype=None, encoding='utf-8')

col_names = list(input_arr.dtype.names)
row_names = input_arr[col_names[0]]
fpkm_values = input_arr[col_names[1:]]
stage_names = col_names[1:]


fpkm_values_2d = rfn.structured_to_unstructured(fpkm_values, dtype=float)

median = np.median(fpkm_values_2d, axis=1)
array = fpkm_values_2d[np.where(median >0)]
log_array = np.log2(array + 0.1)
final_rows = row_names[median > 0]

# cluster based on genes
Z1 = linkage(log_array)
idx1 = leaves_list(Z1)

# cluster based on samples
Z2 = linkage(log_array.T)
idx2 = leaves_list(Z2)

# reorder data matrix based on gene and sample clustering
D = log_array[idx1,:]
D = D[:,idx2]

#plot heatmap
fig, ax = plt.subplots()
plt.imshow(D, interpolation = "nearest", aspect = "auto", cmap="YlGnBu")
ax.set_xticks(np.arange(len(stage_names)))
ax.set_xticklabels(np.array(stage_names)[idx2], rotation=90)
plt.colorbar()
plt.tight_layout()
plt.savefig("heatmap.png")
plt.close()

# plot dendrogram
fig,ax = plt.subplots()
dendrogram(Z2, distance_sort = "ascending", labels = stage_names, leaf_rotation = 45)
plt.tight_layout()
plt.savefig("dendrogram.png")
plt.close()

pvalues_list = []
betavalues_list = []
for row in range(log_array.shape[0]):
    list_of_tuples = []    
    for i in range(len(stage_names)):
        fpkm = log_array[row,i]
        name = stage_names[i]
        name_split = name.split("_")
        stage = name_split[1]
        sex = name_split[0]
        list_of_tuples.append((fpkm, sex, stage))
    longdf = np.array(list_of_tuples, dtype=[('fpkm', float), ('sex', 'S6'), ('stage', int)])
    fit = smf.ols("fpkm ~ stage", data = longdf).fit()
    p_value = fit.pvalues["stage"]
    beta = fit.params["stage"]
    pvalues_list.append(p_value)
    betavalues_list.append(beta)

# qqplot using uniform distribution as comparison
# under null hypothesis, significant pvalues occur completely by chance
# so they should be uniformly distributed, with 5% significant by chance

fig, ax = plt.subplots()
sm.qqplot(np.array(pvalues_list), dist = stats.uniform, line='45')
plt.tight_layout()
plt.show()
plt.savefig("qqplot.png")

fdr_list = multitest.multipletests(pvalues_list, alpha = 0.1, method = "fdr_bh")
pvalues_list = fdr_list[0]
significant = final_rows[pvalues_list]

#controlling for sex as a covariate in the formula 
pvalues_list2 = []
betavalues_list2 = []
for row in range(log_array.shape[0]):
    list_of_tuples = []    
    for i in range(len(stage_names)):
        fpkm = log_array[row,i]
        name = stage_names[i]
        name_split = name.split("_")
        stage = name_split[1]
        sex = name_split[0]
        list_of_tuples.append((fpkm, sex, stage))
    longdf = np.array(list_of_tuples, dtype=[('fpkm', float), ('sex', 'S6'), ('stage', int)])
    fit = smf.ols("fpkm ~ stage + sex", data = longdf).fit()
    p_value2 = fit.pvalues["stage"]
    beta2 = fit.params["stage"]
    pvalues_list2.append(p_value2)
    betavalues_list2.append(beta2)
    
fdr_list2 = multitest.multipletests(pvalues_list2, alpha = 0.1, method = "fdr_bh")
pvalueslist2 = fdr_list2[0]
significant2 = final_rows[pvalueslist2]


overlap = set(significant) & set(significant2)
number_transcripts =len(overlap)
number_transcript_nosex = len(significant)
compared = (number_transcripts) / (number_transcript_nosex) * 100 

color = []
for item in pvalueslist2:
    if item == True:
        color.append("red")
    else:
        color.append("black")

fig, ax = plt.subplots()
ax.scatter(betavalues_list2, -np.log10(pvalues_list2), color = color)
plt.savefig("volcano.png") 
plt.show()
