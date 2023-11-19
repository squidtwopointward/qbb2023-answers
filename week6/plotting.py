#!/usr/bin/env python

import sys
import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import statsmodels.api as sm
import pandas as pd



# components = np.loadtxt('plink.eigenvec', usecols=(2, 3))



# plt.figure(figsize=(8, 6))
# plt.scatter(components[:, 0], components[:, 1])

# plt.xlabel('Principal Component 1')
# plt.ylabel('Principal Component 2')
# plt.title('Genetic Relatedness Between Cell Lines')
# plt.savefig('Readiness')

# plt.grid(True)
# # plt.show()


# frequency = np.loadtxt('allele_frequencies.frq', skiprows=1, usecols=(4,))


# plt.hist(frequency)
# plt.xlabel('Allele Frequency')
# plt.ylabel('Count')
# plt.title('Allele Frequency Spectrum (AFS)')
# plt.savefig('Frequency Spectrum')


# plt.show()

#Manhattan Plot

phenotype1 = pd.read_csv('phenotype_gwas_results_CB1908.assoc.linear', delim_whitespace = True)
phenotype2 = pd.read_csv('phenotype_gwas_results_GS451.assoc.linear', delim_whitespace = True)



# fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))

# def significant_snps(data, ax):
#     snps = data[data['P'] < 1e-5]
#     ax.scatter(snps.index, -1 * np.log(snps['P']),color='red', label='p<1e-5', zorder=5)
#     ax.legend(loc='upper right')


# axes[0].scatter(phenotype1.index, -1 * np.log(phenotype1['P']), s=5, color='blue')
# significant_snps(phenotype1, axes[0])
# axes[0].set_title('Manhattan Plot CB1908')
# axes[0].set_xlabel('SNP')
# axes[0].set_ylabel('-log10(p-value')


# axes[1].scatter(phenotype2.index, -1 * np.log(phenotype2['P']), s=5, color='blue')
# significant_snps(phenotype2, axes[1])
# axes[1].set_title('Manhattan Plot GS451')
# axes[1].set_xlabel('SNP')
# axes[1].set_ylabel('-log10(p-value')

# plt.tight_layout()
# plt.savefig('Manhattan Plot')
# plt.show()
# plt.close()

# ID the SNPs

minimum_index = phenotype1['P'].idxmin()
residue = phenotype1['SNP'][minimum_index]
phenotype_sample = pd.read_csv('CB1908_IC50.txt', delim_whitespace = True)
phenotype_values = phenotype_sample.iloc[:,2]
homo_reference = []
hetero =[]
homozygous = []

for line in open('genotypes.vcf'):
    if line.startswith('#'):
        continue
    fields = line.rstrip('\n').split('\t')
    if fields[2] == residue:
        print(residue)
        samples = fields[9:]
        for i in range(len(samples)):
            if samples[i] == '0/0':
                if not np.isnan(phenotype_values[i]):
                    homo_reference.append(phenotype_values[i])
            if samples[i] == '0/1' or samples == '1/0':
                if not np.isnan(phenotype_values[i]):
                    hetero.append(phenotype_values[i])
            if samples[i] == '1/1':
                if not np.isnan(phenotype_values[i]):
                    homozygous.append(phenotype_values[i])
        break

stratified = [homozygous, hetero, homo_reference]

genotypes = ['homozygous', 'hetero', 'homo_reference']

plt.boxplot(stratified, labels = genotypes)
plt.xlabel('Genotypes')
plt.ylabel('Score of Phenotype')
plt.title(f'GS Score by {residue} Genotype')
plt.savefig('boxplot.png')
plt.show()
plt.close()












