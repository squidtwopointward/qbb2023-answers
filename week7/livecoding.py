#!/usr/bin/env python

import sys
import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import statsmodels.api as sm
import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt

sns.set()


def main():
    # Load file names from command line
    # normal_fname, tumor_fname, out_fname = sys.argv[1:4]

    normal_ONT, normal_bisul, tumor_bisul, tumor_normal, out_fname = sys.argv[1:6]

    # Load data from files
    # normal = load_data(normal_fname)
    # tumor = load_data(tumor_fname)

    ONT = pd.DataFrame(load_data(normal_ONT))
    #print(ONT)
    bisul = pd.DataFrame(load_data(normal_bisul))

    bisul_tumor = pd.DataFrame(load_data(tumor_bisul))
    ONT_tumor = pd.DataFrame(load_data(tumor_normal))
    #print(ONT_tumor)

    # ONT_Cpg = load_data(Cpg_ONT)
    # bisul_Cpg = load_data(Cpg_bisul)


    
    # print(ONT)
    # # Find reads that appear more than once in datasets
    # normal_set = set()
    # normal_multi = set()
    # for i in range(len(normal)):
    #     if normal[i][0] not in normal_set:
    #         normal_set.add(normal[i][0])
    #     else:
    #         normal_multi.add(normal[i][0])
    # normal_single = normal_set.difference(normal_multi)

    # tumor_set = set()
    # tumor_multi = set()
    # for i in range(len(tumor))
    #     if tumor[i][0] not in tumor_set:
    #         tumor_set.add(tumor[i][0])
    #     else:
    #         tumor_multi.add(tumor[i][0])
    # tumor_single = tumor_set.difference(tumor_multi)
    # Find reads that appear more than once in datasets bisultate and ONT
    
    # ONT_set = set()
    # for i in range(len(ONT)):
    #     ONT_set.add(ONT[i][1])
    
    # bisul_set = set()
    # for i in range(len(bisul)):
    #     bisul_set.add(bisul[i][1])






    # ONT_coverage = []
    # for i in range(len(ONT)):
    #     ONT_coverage.append(ONT[i][3])
    # # print(ONT_coverage)
    
    # bisul_coverage = []
    # for i in range(len(bisul)):
    #     bisul_coverage.append(bisul[i][3])
    # print(bisul_coverage)

#     ONT_ = np.array(list(ONT_set))
#     bisul_ = np.array(list(bisul_set))



#     # print("Percent unique to ONT")
#     # print(len(ONT_set.difference(bisul_set)) / (len(ONT_set.difference(bisul_set))  + len(bisul_set)))
#     # #differences = ((ONT_set - bisul_set)/ (ONT_set + bisul_set) * 100) 


#     # Print statistics about unique vs multimapping reads
#     # print(f"Normal unique reads: {len(normal_single)} ({len(normal_single) / len(normal_set) * 100}) %")
#     # print(f"Normal multi reads: {len(normal_multi)} ({len(normal_multi) / len(normal_set) * 100}) %")
#     # print(f"Tumor unique reads: {len(tumor_single)} ({len(tumor_single) / len(tumor_set) * 100}) %")
#     # print(f"tumor multi reads: {len(tumor_multi)} ({len(tumor_multi) / len(tumor_set) * 100}) %")
#     # print(f"ONT unique reads: {len(ONT_single)} ({len(ONT_single) / len(ONT_set) * 100}) %")
#     # # print(f"ONT multi reads: {len(ONT_multi)} ({len(ONT_multi) / len(ONT_set) * 100}) %")
#     # print(f"Bisul unique reads: {len(bisul_single)} ({len(bisul_single) / len(bisul) * 100}) %")
#     # print(f"Bisul multi reads: {len(bisul_multi)} ({len(bisul_multi) / len(bisul_set) * 100}) %")

#     # Parse data into unique and multi-mapping reads for plotting
#     # N_multi, N_single = split_data(normal_multi, normal)
#     # T_multi, T_single = split_data(tumor_multi, tumor)

# #     N_single = split_data(ONT)
# #     T_single = split_data(bisul)

#     # 3b) Plot 2 panels, ONT and Bisul
   

    # plot_data(N_single, ax[0, 0], "ONT Singletons")
    # plot_data(ONT_set, "ONT")
    # plot_data(bisul_set, "bisul")
    # plt.savefig(out_fname)

    
    # width = 0.35
    # ax.scatter(ONT_set,label='ONT')
    # ax.scatter(bisul_set, label='Bisulfate')

    # fig, ax = plt.subplots(2,2 ,figsize =(8,8))
    # ax[0,0].hist(ONT_coverage, bins = 500, color='blue', alpha =.5)
    # ax[0,0].hist(bisul_coverage, bins= 500, color ='red', alpha =.5)
    # ax[0,0].set_xlim(0,100)

    # ax[0,0].set_xlabel("CpG Sites")
    # ax[0,0].set_ylabel("Distribution of Coverages")
    # ax[0,0].set_title('Histogram of CpG Sites')
    # plt.savefig(out_fname)

    # ONT_methylation = ONT_set
    # bisul_methylation = bisul_set
    # hist, x_edges, y_edges = np.histogram2d(ONT_, bisul_, bins=100)
    # hist_transformed = np.log10(hist + 1) 
    # plt.imshow(hist_transformed, extent=[x_edges[0], x_edges[-1], y_edges[0], y_edges[-1]], origin='lower', cmap='viridis')
    # plt.colorbar(label='log10(Frequency + 1)')
    # pearson_r = np.corrcoef(ONT_methylation, bisul_methylation)[0, 1]
    # plt.title(f'Methylation Scores Relationship\nPearson R: {pearson_r:.3f}')
    # plt.xlabel('Methylation Scores of ONT')
    # plt.ylabel('Methylation Scores of Bilsufate')
    # plt.savefig(out_fname)
    # plt.show()

#     #Step 3c
  

    # common_site= bisul_set.intersection(ONT_set)
    # # print(common_site)
    
    # common_ONT =[]
    # for i in ONT:
    #     if i[1] in common_site:
    #         common_ONT.append(i[2])
    # # print(common_ONT)

    # common_bisul = []
    # for i in bisul:
    #     if i[1] in common_site:
    #         common_bisul.append(i[2])
    # # print(common_bisul)

    # hist, x_edges, y_edges = np.histogram2d(common_ONT, common_bisul, bins =100)
    # transformed_hist = np.log2(hist +1)

    # plt.imshow(transformed_hist, origin='lower', cmap ='viridis')
    # plt.colorbar(label='log10(count +1)')
    # plt.title('Transformed Histogram')


    # pearson_r = np.corrcoef(common_ONT, common_bisul)[0,1]
    # plt.title(f'Transformed Histogram\nPearson R:{pearson_r:.3f}')
    # plt.xlabel('ONT Scores')
    # plt.ylabel('Bisul Scores')
    # plt.savefig(out_fname)
    # plt.show()


# Create a reusable plotting function
    # 

#Step 3d:
    ONT_common_site= set(ONT.loc[:,1]).intersection(set(ONT_tumor.loc[:,1]))
    # print(ONT_common_site)

    bisul_common_site = set(bisul.loc[:,1]).intersection(set(bisul_tumor.loc[:,1]))
    # print(bisul_common_site)


    ONT = ONT.set_index(1)
    ONT_tumor = ONT_tumor.set_index(1)
    #print(ONT)

    ONT_data = []
    for location in ONT_common_site:
        difference = ONT_tumor.loc[location,2] - ONT.loc[location,2]
        # print(difference)
        if difference != 0:
            ONT_data.append(difference)
    #print(ONT_data)

    bisul = bisul.set_index(1)
    bisul_tumor = bisul_tumor.set_index(1)


    bisul_data = []
    for locations in bisul_common_site:
        difference1 = bisul_tumor.loc[locations,2] - bisul.loc[locations,2]
        # print(difference)
        if difference1 != 0:
            bisul_data.append(difference1)
    # print(bisul_data)

    combined_data = [ONT_data, bisul_data]
    pearson_r = np.corrcoef(combined_data)
    plt.title(f'Violin Plot of Methylation Changes\nPearson R: {pearson_r:.3f}')

    combined_data = [ONT_data, bisul_data]
    # pearson_r = np.corrcoef(common_ONT, common_ONT)
    labels = ['Nanopore', 'Bisulfite']
    legend_labels = ['Nanopore', 'Bisulfite']


    sns.violinplot(data=combined_data, inner='box', palette='pastel', legend = labels)
    plt.xlabel('Methylation Approach')
    plt.ylabel('Methylation Changes')
    plt.savefig('methylation_changes_violin_plot.png')
    plt.show()

# Create a reusable data loading function. Record read name, actual size, and mapped size
def load_data(fname):
    data = []
    for line in open(fname):
        line = line.rstrip().split()
        # key = [line[0], line[1]]
        # data[key] = [float(line[3]), int(line[4])]





        data.append([
            line[0], int(line[1]), float(line[3]), int(line[4])])   
    return  data

# def split_data(multi, data):
#     output1 = [[], []]
#     output2 = [[], []]
#     for i in range(len(data)):
#         name = data[i][0]
#         if name in multi:
#             output1[0].append(data[i][1])
#             output1[1].append(data[i][2])
#         else:
#             output2[0].append(data[i][1])
#             output2[1].append(data[i][2])
#     return output1, 




main()