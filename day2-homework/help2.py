#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt



## read in the transcripts without using numpy
dd = open("/Users/cmdb/qbb2023-answers/day2-homework/all_annotated.csv", "r")

#Makes it read line by line
lines = dd.readlines()
 
#Excluding headers
lines = lines[1: ]

start_read = []

#Has to be at 0 since I excluded 1 in the previous statement.
for line in lines:
    line.rstrip()
    line_list = line.split()
    read_int = int(line_list[0])
    start_read.append(lin_list[])

#transcripts = np.loadtxt( "all_annotated.csv", delimiter=",", usecols=0, dtype="<U30", skiprows=1 )
#print( "transcripts: ", transcripts == 'FBtr0073461' )

samples = np.loadtxt( "all_annotated.csv", delimiter=",", max_rows=1, dtype="<U30" )[2:]
print( "samples: ", samples[0:5] )

data = np.loadtxt( "all_annotated.csv", delimiter=",", dtype=np.float32, skiprows=1, usecols=range(2, len(samples) + 2) )
print( "data: ", data[0:5, 0:5] )

# Find row with transcript of interest
for i in range(len(transcripts)):
    if transcripts[i] == 'FBtr0073461':
        row = i

# Find columns with samples of interest
cols = []
cols2 = []
for i in range(len(samples)):
    if "female" in samples[i]:
        cols.append(i)
    else:
        cols2.append(i)

females = []
males = []
for i in samples:
    if "female" in i: 
        female_strip = i.lstrip('female_')
        females.append(female_strip)
    elif 'male' in i:
        male_strip = i.lstrip('male_')
        males.append(male_strip)
print(females)


# Subset data of interest
expression = data[row, cols]
expression1 = data[row, cols2]

# Prepare data
x1 = samples[cols]
x2 = samples[cols2]
y = expression
y2 =expression1
y3 = 2 * np.array(y2)


#Plot data
fig, ax = plt.subplots()


ax.set_title( "Fly Data" )

ax.plot(females, y2, label = "Males", c = "blue")
ax.plot(females, y3, label = "Malesx2", c = "green")

ax.plot(females, y, label = "Females", c = "orange")

ax.set_xlabel('Developmental Stage')
ax.set_ylabel('mRNA abundance (RPKI)')




fig.savefig( "FlyData.png" )

plt.show()




