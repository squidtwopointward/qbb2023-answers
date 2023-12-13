#!/usr/bin/env python

import sys
import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import statsmodels.api as sm
import pandas as pd
import matplotlib.pyplot as plt


baitmap = sys.argv[1] 
washU = sys.argv[2] 
outputname = sys.argv[3]


baits = pd.read_csv(baitmap,  delim_whitespace = True, names = ('CHR', 'Bait_Start', 'Bait_End', 'ID', 'GENE')) 
washU = pd.read_csv(washU, sep= (",|\t"), names = ("CHR1", "Start_1", "End_1", "CHR2", "Start_2", "End_2", "Score"), engine = 'python') 
# print(washU)

df_UCSC= pd.DataFrame(columns=['chrom', 'chromStart', 'chromEnd', 'name', 'score', 'value', 'ex`', 'color', 'sourceChrom', 'sourceStart', 'sourceEnd', 'sourceName', 'sourceStrand', 'targetChrom', 'targetStart', 'targetEnd', 'targetName', 'targetStrand']) 
max_ = max(washU["Score"])
# print(max_)
 

for i in washU.index:
	df_UCSC.loc[i, 'chrom'] = washU.loc[i, "CHR1"] 
	df_UCSC.loc[i, 'chromStart'] = min(washU.loc[i, "Start_1"], washU.loc[i, "Start_2"])
	df_UCSC.loc[i, 'chromEnd'] = max(washU.loc[i, "End_2"], washU.loc[i, "End_1"])
	df_UCSC.loc[i, 'name'] = '.'
	df_UCSC.loc[i, 'score'] = int(int(washU.loc[i, "Score"])/max_ * 1000) #calculating score
	df_UCSC.loc[i, 'value'] = washU.loc[i, 'Score']
	df_UCSC.loc[i, 'ex`'] = '.'
	df_UCSC.loc[i, 'color'] = '0'

	if washU.loc[i, 'Start_1'] in baits['Bait_Start'].values:
		j = int(baits[baits['Bait_Start'] == washU.loc[i, 'Start_1']].index.values)
		df_UCSC.loc[i, 'sourceChrom'] = washU.loc[i, 'CHR1'] #source chromosome 
		df_UCSC.loc[i, 'sourceStart'] = washU.loc[i, 'Start_1']
		df_UCSC.loc[i, 'sourceEnd'] = washU.loc[i, 'End_1']
		df_UCSC.loc[i, 'sourceName'] = baits.loc[j , 'GENE']
		df_UCSC.loc[i, 'sourceStrand'] = '+'
		df_UCSC.loc[i, 'targetChrom'] = washU.loc[i, 'CHR2']
		df_UCSC.loc[i, 'targetStart'] = washU.loc[i, 'Start_2']
		df_UCSC.loc[i, 'targetEnd'] = washU.loc[i, 'End_2']

		if df_UCSC.loc[i, 'targetStart'] in baits['Bait_Start'].values:
			k = int(baits[baits['Bait_Start'] == washU.loc[i, 'Start_2']].index.values)
			df_UCSC.loc[i, 'targetName'] = baits.loc[k , 'GENE'] #add in gene ID
			df_UCSC.loc[i, 'targetStrand'] = '+' #+ target

		else:
			df_UCSC.loc[i, 'targetName'] = "." #no gene id
			df_UCSC.loc[i, 'targetStrand'] = '-' #- target

	elif washU.loc[i, 'Start_2'] in baits['Bait_Start'].values:
		j = int(baits[baits['Bait_Start'] == washU.loc[i, 'Start_1']].index.values)
		df_UCSC.loc[i, 'sourceChrom'] = washU.loc[i, 'CHR2']
		df_UCSC.loc[i, 'sourceStart'] = washU.loc[i, 'Start_2']
		df_UCSC.loc[i, 'sourceEnd'] = washU.loc[i, 'End_2']
		df_UCSC.loc[i, 'sourceName'] = baits.loc[j , 'GENE']
		df_UCSC.loc[i, 'sourceStrand'] = '+'
		df_UCSC.loc[i, 'targetChrom'] = washU.loc[i, 'CHR1']
		df_UCSC.loc[i, 'targetStart'] = washU.loc[i, 'Start_1']
		df_UCSC.loc[i, 'targetEnd'] = washU.loc[i, 'End_1']

		if df_UCSC.loc[i, 'targetStart'] in baits['Bait_Start'].values:
			k = int(baits[baits['Bait_Start'] == washU.loc[i, 'Start_2']].index.values)
			df_UCSC.loc[i, 'targetName'] = baits.loc[k , 'GENE']
			df_UCSC.loc[i, 'targetStrand'] = '+' #+ target

		else: #if fragment 1 is not a bait
			df_UCSC.loc[i, 'targetName'] = "." #no gene ID
			df_UCSC.loc[i, 'targetStrand'] = '-' # - target

# print(df_UCSC)

with open(outputname, 'w') as f:
	f.write('track type=interact name="pCHIC" description="Chromatin interactions" useScore=on maxHeightPixels=200:100:50 visibility=full \n') 
	UCSC_string = df_UCSC.to_string(header=False, index=False)
	f.write(UCSC_string)



# _promoter = df_UCSC[df_UCSC['sourceStrand'] == df_UCSC['targetStrand']]
# _enhancer = df_UCSC[df_UCSC['sourceStrand'] != df_UCSC['targetStrand']]

# _promoter = _promoter.sort_values(['score'], ascending = False)
# _enhancer = _enhancer.sort_values(['score'], ascending = False)

# print(_promoter.head(6))
# print(_enhancer.head(6))





