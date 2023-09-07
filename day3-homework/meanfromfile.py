#!/usr/bin/env python
import sys

fname = sys.argv[1]
f = open(fname)


# hello = []
# for i in f:
# 	hello.append(int(i.rstrip("\n")))
# 	print(i)

hello = []
for i in f:
	i_stripped = i.rstrip("\n")
	i_int = int(i_stripped)
	hello.append(i_int)

def average(hello):
	addition = sum(hello)
	length = len(hello)
	return addition/length


print(average(hello))
 
