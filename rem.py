#!/usr/bin/python3 
import glob
import sys
import os

r_flag = 0
a_flag = 0

a_name = []
r_name = []

for i in sys.argv[1:]:
	#flags
	if i=='-r':
		r_flag = 1
	elif i=='-a':
		a_flag = 1
	#parameters if flags
	if r_flag and i[0]!='-':
		r_name.append(i)
	elif r_flag and i[0]=='-' and i[1]!='r':
		r_flag = 0
	if a_flag and i[0]!='-':
		a_name.append(i)
	elif a_flag and i[0]=='-' and i[1]!='a':
		a_flag = 0

if r_name:
	os.system("rm "+os.environ['HOME']+"/.todo/"+(("".join([str(i)+"_" for i in r_name]))[:-1]+".rem"))
if a_name:
	#print(os.environ['EDITOR']+" "+os.environ['HOME']+"/.todo/"+(("".join([str(i)+"_" for i in a_name]))[:-1]+".rem"))
	os.system(os.environ['EDITOR']+" "+os.environ['HOME']+"/.todo/"+(("".join([str(i)+"_" for i in a_name]))[:-1]+".rem"))

test = glob.glob(os.environ['HOME']+"/.todo/*.rem")

for i in test:
	print(str("".join(i.split('/')[-1:][0].split('.')[:-1])).replace("_"," ")+": ")
	with open(i, 'r') as f:
		for line in f:
			print("\t"+line,end='')
			if line[-1:]!='\n':
				print()