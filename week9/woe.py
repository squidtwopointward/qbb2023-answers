#!/usr/bin/env python


import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.stats import multitest
from pydeseq2 import preprocessing
from pydeseq2.dds import DeseqDataSet
from pydeseq2.ds import DeseqStats
from scipy.stats import linregress
import matplotlib.pyplot as plt



# read in data
counts_df = pd.read_csv("gtex_whole_blood_counts_formatted.txt", index_col = 0)

# read in metadata
metadata = pd.read_csv("gtex_metadata.txt", index_col = 0)

#It normalized the data
counts_df_normed = preprocessing.deseq2_norm(counts_df)[0]
counts_df_normed_log = np.log2(counts_df_normed + 1)

#Create matrix
full_design_df = pd.concat([counts_df_normed, metadata], axis=1)

# print(full_design_df)

model = smf.ols(formula = 'Q("DDX11L1") ~ SEX', data=full_design_df)
results = model.fit()

#Male = 1
#Female = 2
slope = results.params[1]
pval  = results.pvalues[1]



genes = counts_df_normed.columns
# print(genes)

columns = ['Gene', 'Slope', 'P-value']
gene_results_df = pd.DataFrame(columns=columns)

# for gene in genes:
# 	model = smf.ols(formula = f'Q("{gene}") ~ SEX', data=full_design_df)
# 	results = model.fit()
# 	slope1 = results.params[1]
# 	pval1 = results.pvalues[1]
# 	gene_results_df.loc[len(gene_results_df), :] = [gene, slope1, pval1]

# gene_results_df.to_csv('Results.txt', header=True, index=False, sep='\t')

# for gene in genes:
# 	model = smf.ols(formula = f'Q("{gene}") ~ SEX', data=full_design_df)
# 	results = model.fit()
# 	gene_results_df.loc[len(gene_results_df), :] = [gene]

# gene_results_df.to_csv('genename.txt', header=True, index=False, sep='\t')

dds = DeseqDataSet(
    counts=counts_df,
    metadata=metadata,
    design_factors="SEX",
    n_cpus=4,
)

dds.deseq2()
stat_res = DeseqStats(dds)
stat_res.summary()
result = stat_res.results_df

# f = open('dese2results.txt', 'w')
# for i in result.loc[result['padj'] <0.1,:].index:
# 	f.write(i+ "\n")
# f.close()

# genes = []
# for lines in open('genename.txt'):
#  	gene = lines.rstrip('\n').split('\t')[0]
#  	genes.append(gene)

# genes1= []
# for lines in open('dese2results.txt'):
#  	gene1 = lines.rstrip('\n')
#  	genes1.append(gene1)
	

# geneset = set(genes)
# deseq2set = set(gene1)
# intersect = geneset.intersection(deseq2set)

# index = (len(intersect)/(len(geneset)+ len(deseq2set))) * 100
# # print(index)


fig, ax = plt.subplots()
results = result.dropna(subset=['padj'])


log2fold = results['log2FoldChange']
pvalue = results['pvalue']
padj = results['padj']

log10pvalue = -1*(np.log10(pvalue))

DEGs = (padj < 0.1) & (abs(log2fold) > 1)

ax.scatter(log2fold, log10pvalue, color='grey', alpha=0.5, label='Not DE')
ax.scatter(log2fold[DEGs], log10pvalue[DEGs], color='red', alpha=0.7, label='DEGs')
ax.set_xlabel("Log2FoldChange")
ax.set_ylabel("-log10 of P-Value")
ax.set_title("Differential expression Volcano Plot")
fig.tight_layout()
plt.show()

fig.savefig("volc.png")




































