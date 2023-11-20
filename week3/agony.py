#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import sys

from fasta import readFASTA

#BLSOUM62 
fasta_file = sys.argv[1] 
scoring_matrix = sys.argv[2] 
gap_penalty = int(sys.argv[3]) 
file_name = sys.argv[4]


input_sequences = readFASTA(open(fasta_file)) 
print(input_sequences) 

sequence1_id, sequence1 = input_sequences[0]
sequence2_id, sequence2 = input_sequences[1]


print(sequence1_id)
print(sequence1)
print(type(sequence1_id))
print(type(sequence1))
print(sequence2)
print(sequence2_id)

sequence_1 = 'TGTTACGG' 
sequence_2 = 'GGTTGACTA'

scoring_matrix_df = pd.read_csv(scoring_matrix, sep = '\s+')

print(scoring_matrix_df) 

F_matrix = np.zeros((len(sequence1)+ 1, len(sequence2) +1)) 
print(F_matrix) 

for i in range(len(sequence1)+ 1):
	F_matrix[i, 0] = i * gap_penalty

for j in range(len(sequence2)+ 1):
	F_matrix[0, j] = j * gap_penalty

print(F_matrix)

traceback_matrix = np.zeros((len(sequence1)+ 1, len(sequence2) +1), dtype='str')  

for i in range(1, F_matrix.shape[0]):
	for j in range(1, F_matrix.shape[1]): 
		match_score =  scoring_matrix_df.loc[sequence1[i-1], sequence2[j-1]] 
		d = F_matrix[i-1, j-1] + match_score 
		h = F_matrix[i, j-1] + gap_penalty 
		v = F_matrix[i-1, j] + gap_penalty 
		F_matrix[i, j] = max(d, h, v) 

print(F_matrix) 


i = len(sequence1)  
j = len(sequence2)  


while i != -1 and j != -1:
	d = F_matrix[i-1, j-1] 
	h = F_matrix[i, j-1] 
	v = F_matrix[i-1, j] 
	if max(d, v, h) == d:
		traceback_matrix[i, j] = 'd'
		i -= 1 #move up one
		j -= 1 #move over one
	elif max(d, v, h) == v:
		traceback_matrix[i, j] = "v" 
		i -=1 #move up one
	elif max(d, v, h) == h:
		traceback_matrix[i, j] = 'h' 
		j -= 1
	elif max(d, v, h) == d and h: 
		traceback_matrix[i, j] = 'd'
		i -= 1 
		j -= 1 
	elif max(d, v, h) == d and v:
		traceback_matrix[i, j] = 'd'
		i -= 1 
		j -= 1 
	elif max(d, v, h) == v and h:
		traceback_matrix[i, j] = 'h'
		i -= 1 

print(traceback_matrix) 

# #Exercise 1.4


sequence1_align = "" 
sequence2_align = "" 

row = len(sequence1)  
col = len(sequence2)  
print(row)
print(col)
print(traceback_matrix[row, col])


while row > 0 and col > 0: 
	if traceback_matrix[row, col] == 'd':
		sequence1_align = sequence1[row-1] + sequence1_align 
		sequence2_align = sequence2[col-1] + sequence2_align 
		row -= 1 
		col -= 1 
	elif traceback_matrix[row, col] == 'h':
		sequence1_align = "-" + sequence1_align
		sequence2_align = sequence2[col-1] + sequence2_align 
		col -= 1
	elif traceback_matrix[row, col] == 'v':
		sequence1_align = sequence1[row-1] + sequence1_align 
		sequence2_align = "-" + sequence2_align
		row -= 1
print(sequence1_align) 
print(sequence2_align)

#Exercise 1.5:

alignment_score = F_matrix[len(sequence1), len(sequence2)] 

gap_num_seq1 = 0
gap_num_seq2 = 0

for position in range(len(sequence1_align)): 
	if sequence1_align[position] == '-':
		gap_num_seq1 += 1 
		position+=1 

for position in range(len(sequence2_align)): 
	if sequence2_align[position] == '-':
		gap_num_seq2 += 1 
		position+=1 

print(gap_num_seq1) 
print(gap_num_seq2) 


with open(file_name, 'w') as f:
	f.write("Sequence 1 alignment \n") 
	f.write(sequence1_align)
	f.write("\nSequence 2 alignment: \n") 
	f.write(sequence2_align) 
	f.write("\nThis number of gaps in the first sequence is:\n")
	f.write(str(gap_num_seq1))
	f.write("\nThis number of gaps in the second sequence is:\n")
	f.write(str(gap_num_seq2)) 
	f.write("\nThe score of this alignment is: \n") 
	f.write(str(alignment_score)) 


# #HOXD70
# fasta_file = sys.argv[1] 
# scoring_matrix = sys.argv[2] 
# gap_penalty = int(sys.argv[3]) 
# file_name = sys.argv[4]


# input_sequences = readFASTA(open(fasta_file)) 
# # print(input_sequences) 

# sequence1_id, sequence1 = input_sequences[0]
# sequence2_id, sequence2 = input_sequences[1]


# # print(sequence1_id)
# # print(sequence1)
# # print(type(sequence1_id))
# # print(type(sequence1))
# # print(sequence2)
# # print(sequence2_id)

# sequence_1 = 'TGTTACGG' 
# sequence_2 = 'GGTTGACTA'

# scoring_matrix_df = pd.read_csv(scoring_matrix, sep = '\s+')

# F_matrix = np.zeros((len(sequence1)+ 1, len(sequence2) +1)) 
# # print(F_matrix) 

# for i in range(len(sequence1)+ 1):
# 	F_matrix[i, 0] = i * gap_penalty

# for j in range(len(sequence2)+ 1):
# 	F_matrix[0, j] = j * gap_penalty

# # print(F_matrix)

# traceback_matrix = np.zeros((len(sequence1)+ 1, len(sequence2) +1), dtype='str')  

# for i in range(1, F_matrix.shape[0]):
# 	for j in range(1, F_matrix.shape[1]): 
# 		match_score =  scoring_matrix_df.loc[sequence1[i-1], sequence2[j-1]] 
# 		d = F_matrix[i-1, j-1] + match_score 
# 		h = F_matrix[i, j-1] + gap_penalty 
# 		v = F_matrix[i-1, j] + gap_penalty 
# 		F_matrix[i, j] = max(d, h, v) 

# # print(F_matrix) 


# i = len(sequence1)  #starting off traceback matrix by defining values to begin with (value at last row, last column)- row position
# j = len(sequence2)  #starting off traceback matrix by defining values to begin with (value at last row, last column)- column position

# while i != -1 and j != -1:
# 	d = F_matrix[i-1, j-1] 
# 	h = F_matrix[i, j-1] 
# 	v = F_matrix[i-1, j] 
# 	if max(d, v, h) == d:
# 		traceback_matrix[i, j] = 'd'
# 		i -= 1 #move up one
# 		j -= 1 #move over one
# 	elif max(d, v, h) == v:
# 		traceback_matrix[i, j] = "v" 
# 		i -=1 #move up one
# 	elif max(d, v, h) == h:
# 		traceback_matrix[i, j] = 'h' 
# 		j -= 1
# 	elif max(d, v, h) == d and h: 
# 		traceback_matrix[i, j] = 'd'
# 		i -= 1 
# 		j -= 1 
# 	elif max(d, v, h) == d and v:
# 		traceback_matrix[i, j] = 'd'
# 		i -= 1 
# 		j -= 1 
# 	elif max(d, v, h) == v and h:
# 		traceback_matrix[i, j] = 'h'
# 		i -= 1 

# # print(traceback_matrix) 

# # #Exercise 1.4

# # #Generate the alignment:
# # #Use traceback matrix to generate the alignment. 
# # # If diagonal: match (sequence1[bp/AA] = sequence2[bp/AA])
# # # If horizontal: sequence 2 aa, sequence 1 = gap
# # # If vertical: sequence1 aa, sequence 2 = gap

# sequence1_align = "" 
# sequence2_align = "" 

# row = len(sequence1)  #defining row as the last value in sequence 1 
# col = len(sequence2)  #defining column as the last value in sequence 2
# # print(row)
# # print(col)
# # print(traceback_matrix[row, col])


# while row > 0 and col > 0: 
# 	if traceback_matrix[row, col] == 'd':
# 		sequence1_align = sequence1[row-1] + sequence1_align 
# 		sequence2_align = sequence2[col-1] + sequence2_align 
# 		row -= 1 
# 		col -= 1 
# 	elif traceback_matrix[row, col] == 'h':
# 		sequence1_align = "-" + sequence1_align
# 		sequence2_align = sequence2[col-1] + sequence2_align 
# 		col -= 1
# 	elif traceback_matrix[row, col] == 'v':
# 		sequence1_align = sequence1[row-1] + sequence1_align 
# 		sequence2_align = "-" + sequence2_align
# 		row -= 1
# # print(sequence1_align) 
# # print(sequence2_align)

# #Exercise 1.5:

# alignment_score = F_matrix[len(sequence1), len(sequence2)] 

# gap_num_seq1 = 0
# gap_num_seq2 = 0

# for position in range(len(sequence1_align)): 
# 	if sequence1_align[position] == '-':
# 		gap_num_seq1 += 1 
# 		position+=1 

# for position in range(len(sequence2_align)): 
# 	if sequence2_align[position] == '-':
# 		gap_num_seq2 += 1 
# 		position+=1 

# # print(gap_num_seq1) 
# # print(gap_num_seq2) 


# with open(file_name, 'w') as f:
# 	f.write("Sequence 1 alignment \n") 
# 	f.write(sequence1_align)
# 	f.write("\nSequence 2 alignment: \n") 
# 	f.write(sequence2_align) 
# 	f.write("\nThis number of gaps in the first sequence is:\n")
# 	f.write(str(gap_num_seq1))
# 	f.write("\nThis number of gaps in the second sequence is:\n")
# 	f.write(str(gap_num_seq2)) 
# 	f.write("\nThe score of this alignment is: \n") 
# 	f.write(str(alignment_score)) 