#!/usr/bin/env python
import numpy as np
import pandas as pd
from pydeseq2 import preprocessing
from matplotlib import pyplot as plt

# read in data
counts_df = pd.read_csv("gtex_whole_blood_counts_formatted.txt", index_col = 0)

# read in metadata
metadata = pd.read_csv("gtex_metadata.txt", index_col = 0)

# normalize
counts_df_normed = preprocessing.deseq2_norm(counts_df)[0]

# log
counts_df_logged = np.log2(counts_df_normed + 1)


# merge with metadata
full_design_df = pd.concat([counts_df_logged, metadata], axis=1)

# Step1.1
# GTEX113jc = counts_df_logged.loc['GTEX-113JC'][counts_df_logged.loc['GTEX-113JC'] > 0]

# plt.figure(figsize=(10, 6))
# plt.hist(GTEX113jc, bins=30, edgecolor='black')
# plt.title('Distribution of Expression (Logged Normalized Counts) for GTEX-113JC')
# plt.xlabel('Expression (Logged Normalized Counts)')
# plt.ylabel('Frequency')
# plt.grid(True)
# plt.savefig('expression_distribution.png')
# plt.show()

# Step1.2



# male_data = full_design_df[full_design_df['SEX'] == 1]['MXD4']
# female_data = full_design_df[full_design_df['SEX'] == 2]['MXD4']

# plt.figure(figsize=(10, 6))
# plt.hist(male_data, bins= 20, color = 'red', alpha = 0.7, label = "Male")
# plt.hist(female_data, bins= 20, color = 'green', alpha = 0.7, label = "Females")
# plt.title('Distribution of Expression (MXD4) in Males vs Females')
# plt.xlabel('Sex')
# plt.ylabel('Logged Normalized Counts')
# plt.savefig('Sex Distribution.png')
# plt.show()


#Step 1.3

# metadata.grouped = metadata[['AGE', 'DTHHRDY']]

# metadata.grouped.plot(kind='bar', stacked=True, figsize=(12, 8), colormap='viridis')


# plt.title('Relative Proportion of Subjects in Each Hardy Scale Category by Age')
# plt.xlabel('Age Category')
# plt.ylabel('Relative Proportion')
# plt.legend(title='Hardy Scale Category', bbox_to_anchor=(1.05, 1), loc='upper right')
# plt.savefig('Distribution.png')
# plt.show()




#Step 1.4

agony = full_design_df[['AGE', 'SEX', 'LPXN']]

grouped_data = agony.groupby(['AGE', 'SEX'])['LPXN'].median().unstack()
labels_sex = {'1': 'Male', '2': 'Female'}
colors = {'1': 'blue', '2': 'pink'}

grouped_data.reset_index(inplace=True)

plt.figure(figsize=(12, 8))

print(grouped_data)
print(grouped_data.columns)

c = 0
for person in [1,2]:
	plt.bar(np.arange(len(grouped_data.loc[:, person])) + c, grouped_data.loc[:, person], width = 0.5) #, label=labels_sex[person], color=colors[person], alpha=0.7)
	c += 0.5
plt.xticks(np.arange(len(grouped_data.loc[:, person])), labels = grouped_data.loc[:, 'AGE'])

plt.title('Median Expression of LPXN Over Time Stratified by Sex')
plt.xlabel('Age Category')
plt.ylabel('Median Logged Normalized Counts')
plt.legend(title='Sex', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig('LPXN_Median_Expression_Over_Time.png')
plt.show()



# #Step 2.1
# df = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20231201.csv', header=0)

# # what are squirrels up to?
# df_behavior = df.dropna(subset=['Running', 'Chasing', 'Climbing', 'Eating', 'Foraging', 'Kuks', 'Quaas', 'Moans'])

# behavior_counts = df_behavior[['Running', 'Chasing', 'Climbing', 'Eating', 'Foraging', 'Kuks', 'Quaas', 'Moans']].apply(pd.Series.value_counts)

# plt.figure(figsize=(12, 8))
# behavior_counts.T.plot(kind='bar', width=0.8, edgecolor='black')
# plt.title('Distribution of Squirrel Behaviors')
# plt.xlabel('Behavior')
# plt.ylabel('Count')
# plt.legend(title='Behavior', loc='upper right', bbox_to_anchor=(1.15, 1))
# plt.tight_layout()
# plt.savefig('behavior.png')
# plt.close()
# # Are squirrels flagging or twitching their tails?
# df_tails = df.dropna(subset=['Tail flags', 'Tail twitches'])
# behavior_counts = df_tails[['Tail flags', 'Tail twitches']].apply(pd.Series.value_counts)

# plt.figure(figsize=(14, 10))
# behavior_counts.T.plot(kind='bar', width=0.8, color=['blue', 'green'], edgecolor='black')
# plt.title('Comparison of Tail Flags and Tail Twitches in Squirrels')
# plt.xlabel('Behavior')
# plt.ylabel('Count')
# plt.legend(title='Tail Behavior')
# plt.tight_layout()
# plt.savefig('tail_behavior.png')
# plt.close()
# # plot spatial distribution colored by fur color
# fur_df = df.dropna(subset=['Primary Fur Color'])

# fur_df.loc[:, 'Primary Fur Color'] = fur_df['Primary Fur Color'].replace('Cinnamon', 'Brown')

# colors = fur_df['Primary Fur Color'].map({'Gray': 'gray', 'Brown': 'brown', 'Black': 'black'})

# plt.figure(figsize=(12, 8))
# plt.scatter(fur_df['X'], fur_df['Y'], c=colors, alpha=0.5)
# plt.title('Spatial Distribution of Squirrels Colored by Their Fur Color')
# plt.xlabel('Longitude')
# plt.ylabel('Latitude')

# legend_labels = {'gray': 'Gray', 'brown': 'Brown', 'black': 'Black'}
# legend_handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10, label=label) for color, label in legend_labels.items()]
# plt.legend(handles=legend_handles, title='Fur Color')
# plt.savefig('spatial-colored-squirrels.png')
# plt.close()