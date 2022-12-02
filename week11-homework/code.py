#!/usr/bin/env python
import scanpy as sc

# Read 10x dataset
adata = sc.read_10x_h5("neuron_10k_v3_filtered_feature_bc_matrix.h5")
# Make variable names (in this case the genes) unique
adata.var_names_make_unique()

#step 1
#before filtering
# sc.tl.pca(adata, svd_solver ='arpack')
# # sc.pl.pca(adata)
# sc.pl.pca(adata, save="unfiltered.png")
#
# #after filtering
sc.pp.recipe_zheng17(adata, n_top_genes=1000, log=True, plot=False, copy=False)
# sc.tl.pca(adata, svd_solver='arpack')
# # sc.pl.pca(adata)
# sc.pl.pca(adata, save='filtered.png')
#
# #step 2 clustering u-map
sc.pp.neighbors(adata, n_neighbors=10, n_pcs=40)
sc.tl.leiden(adata)
# sc.tl.umap(adata, maxiter=1000)
# sc.pl.umap(adata, save='umap.png')
#
sc.tl.tsne(adata)
sc.pl.tsne(adata, save='tsne.png')

# #step 3 distinguishing genes
# sc.tl.rank_genes_groups(adata, 'leiden', method='t-test')
# sc.pl.rank_genes_groups(adata, n_genes=25, sharey=False, save='t-test.png')
#
# sc.tl.rank_genes_groups(adata, 'leiden', method='logreg')
# sc.pl.rank_genes_groups(adata, n_genes=25, sharey=False, save='logreg.png')

#step 4 cell types
sc.pl.tsne(adata, color=["Olig2", "Apold1", "Sst", "Reln", "Fth1", "Htr3a"],
    save="_colored.png", show = False)
    
# figure out of my gene of interest is in the dataset:
# genes = adata.var.gene_ids.index
# candidates = ["Olig2", "Apold1", "Sst", "Reln", "Fth1", "Htr3a"]
# present = [x for x in candidates if x in genes]
# # the above is basically this for loop
# # present = []
# # for x in candidates:
# #     if x in genes:
# #         present.append(x)
# print(present)

sc.pl.tsne(adata, color="leiden", save="_leiden.png", show = False)
# create a dictionary to map cluster to annotation label
cluster2annotation = {
    "0": "",
    "1": "",
    "2": "Oligodendrocytes-2",
    "3": "",
    "4": "",
    "5": "",
    "6": "",
    "7": "Interneurons-7",
    "8": "",
    "9": "",
    "10": "",
    "11": "",
    "12": "Oligodendrocytes-12",
    "13": "Astrocytes-13",
    "14": "Astrocytes-14",
    "15": "Endothelial Cells-15",
    "16": "",
    "17": "",
    "18": "",
    "19": "",
    "20": "Oligodendrocytes-20",
    "21": "Oligodendrocytes-21",
    "22": "Microglia-22",
    "23": "",
    "24": "Astrocytes-24",
    "25": "Pericytes-25",
    "26": "Microglia-26",
    "27": "Microglia-27"
}
# add a new `.obs` column called `cell type` by mapping clusters to annotation using pandas `map` function
adata.obs['cell type'] = adata.obs['leiden'].map(cluster2annotation).astype('category')

# tsne plot
sc.pl.tsne(adata, color='cell type', legend_loc='on data',
	save="_labeled.png", show = False)