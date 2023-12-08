#!/usr/bin/env python

import sys

import scanpy as sc
import numpy
import matplotlib.pyplot as plt

# filtered_data =load

##STEP 1
# Read the 10x dataset filtered down to just the highly-variable genes
adata = sc.read_h5ad("variable_data.h5")
adata.uns['log1p']['base'] = None

sc.pp.neighbors(adata, n_neighbors=10, n_pcs=40)
# print(adata.obsp['connectivities'])


sc.tl.leiden(adata)
# print(adata.obs['leiden'])

sc.tl.umap(adata, maxiter=900)
sc.tl.tsne(adata)
fig, axes = plt.subplots(ncols=2, figsize=(12, 5))
sc.pl.umap(adata, color='leiden', ax=axes[0], title='UMAP', show=False)
sc.pl.tsne(adata, color='leiden', ax=axes[1], title='t-SNE', show=False)
plt.tight_layout()
plt.savefig('Clusters')

##STEP 2

# wilcoxon_adata=sc.tl.rank_genes_groups(adata, method='wilcoxon', groupby='leiden', use_raw=True, copy=True)



# logreg_adata= sc.tl.rank_genes_groups(adata, method='logreg', groupby='leiden', use_raw=True, copy=True)



# fig, axes = plt.subplots(ncols=2, figsize=(12, 5))
# sc.pl.rank_genes_groups(wilcoxon_adata, n_genes=25, ax=axes[0], title='Wilcoxon Rank-Sum Method', sharey=False, show=False, use_raw=True)
# axes[0].set_ylabel('Cluster')
# plt.savefig('wilcon_rankings_plot.png')

# sc.pl.rank_genes_groups(logreg_adata, n_genes=25, ax=axes[1], title='Logistic Regression Method', sharey=False, show=False, use_raw=True)
# axes[1].set_ylabel('') 
# plt.tight_layout()
# plt.savefig('gene_rankings_plot.png')
# plt.show()

##STEP 3
# leiden = adata.obs['leiden']
# umap = adata.obsm['X_umap']
# tsne = adata.obsm['X_tsne']
# adata = sc.read_h5ad('filtered_data.h5')
# adata.obs['leiden'] = leiden
# adata.obsm['X_umap'] = umap
# adata.obsm['X_tsne'] = tsne

# marker_genes = ['CCL5','PPBP', 'CD3D']

# fig, axes = plt.subplots(ncols=3)
# sc.pl.umap(adata, ax=axes[0], color=marker_genes[0], show=False)
# sc.pl.umap(adata, ax=axes[1],color=marker_genes[1], show=False)
# sc.pl.umap(adata, ax=axes[2],color=marker_genes[2], show=False)
# fig.savefig('basic_bitch.png', dpi=300)
        
adata.rename_categories('leiden', ['IL7R', 'S100A8', 'CST3', ' ', '  ', '   ', '     ', '            '])
sc.tl.tsne(adata)
sc.pl.umap(adata, color='leiden', legend_loc='on data', legend_fontsize=8, show=False)
plt.title('Overall UMAP with Labeled Cell Types')
fig.savefig('basic_bitch2')
plt.show()



