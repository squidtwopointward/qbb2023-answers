#!/usr/bin/env python

import sys
import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import statsmodels.api as sm
from collections import Counter


# # depth =[]
# for line in open('annotation.vcf'):
#     if line.startswith('#'):
#         continue
#     fields = line.rstrip('\n').split('\t')
#     # for i in fields[9:]:
#     # 	dp = i.split(':')[2]
#     # 	if dp != ".":
#     # 		depth.append(int(dp))
# print(fields)

# fig, ax = plt.subplots()
# plt.hist(depth, bins = 800)

# plt.xlabel("Depth Distribution")
# plt.ylabel("Frequnecy")
# plt.savefig('DP')





# plt.show()


# quality =[]
# for line in open('annotation.vcf'):
#     if line.startswith('#'):
#         continue
#     fields = line.rstrip('\n').split('\t')
#     for i in fields[9:]:
#     	gq = i.split(':')[1]
#     	if gq != ".":
#     		quality.append(float(gq))
# # print(quality)

# fig, ax = plt.subplots()
# plt.hist(quality, bins = 50)

# plt.xlabel("Quality Distribution")
# plt.ylabel("Frequnecy")
# plt.savefig('GQ')


# plt.show()


# frequency =[]
# for line in open('annotation.vcf'):
#     if line.startswith('#'):
#         continue
#     fields = line.rstrip('\n').split('\t')
#     af = fields[7].split(';')[3]
#     af = af.split('=')[1]

#     if "," not in af:
#     	frequency.append(float(af))
# # print(frequency)

# fig, ax = plt.subplots()
# plt.hist(frequency, bins = 50)

# plt.xlabel("Allele Frequnecy Distribution")
# plt.ylabel("Number of Allele")
# plt.savefig('AF')

# plt.show()



effects =[]
for line in open('annotation.vcf'):
    if line.startswith('#'):
        continue
    fields = line.rstrip('\n').split('\t')
    ef = fields[7].split(';')[41]
    ef = ef.split('|')[1]
    effects.append(ef)
# print(effects)



category_counts = Counter(effects)
categories, counts = zip(*category_counts.items())




# categories, counts = zip(*category_counts.items())


fig, ax = plt.subplots()


plt.barh(categories, counts, color='skyblue')

plt.xlabel("Predicted Effects Distribution")
plt.ylabel("Frequency of Effects Seen")
plt.title('Histogram of String Data')
plt.savefig('EF')

plt.show()

# 'start_lost&conservative_inframe_insertion', 
# 'splice_donor_variant&intron_variant', 
# 'splice_region_variant&intron_variant', 
# 'missense_variant&splice_region_variant', 
# 'non_coding_transcript_exon_variant', 
# 'frameshift_variant', 
# 'disruptive_inframe_insertion', 
# 'frameshift_variant&stop_lost&splice_region_variant', 
# 'conservative_inframe_deletion', 
# 'upstream_gene_variant', 
# 'stop_lost&splice_region_variant', 
# 'start_lost', 
# 'stop_gained',
# 'splice_acceptor_variant&intron_variant', 
# 'splice_region_variant&stop_retained_variant',
# 'initiator_codon_variant', 
# 'synonymous_variant', 
# 'frameshift_variant&stop_gained', 
# 'downstream_gene_variant',
# 'conservative_inframe_insertion' 
# 'frameshift_variant&splice_region_variant' 
# 'missense_variant'
# 'disruptive_inframe_deletion', 
# 'splice_region_variant&synonymous_variant', 
# 'frameshift_variant&start_lost'

