#---------------------------------------------------------------#
#								#
#	python gaussian_extract.py file_output_gaussian.out	#
#								#
#	it produces n file.xyz which are the stationary 	#
#	points of the opt scan 					#
#								#
#---------------------------------------------------------------#

import sys
import re
import numpy
start = []
end = [] 
filename = sys.argv[1]
openold = open(filename,"r")



rline = openold.readlines()

count_sp=0
count_so=0

for i in range(len(rline)):
	if "Stationary " in rline[i]:
		count_sp=1
	elif "Standard orientation" in rline[i]:
		count_so=1
		if count_sp==1 and count_so==1:
			start.append(i)
			count_sp=0
			count_so=0
		else:
			count_sp=0
			count_so=0
	else:
		count_so=0


for i in start:
	for m in range (i + 5, len(rline)):
		if "---" in rline[m]:
			end.append(m)
			break

numero_atomi=end[0]-start[0]-5 


for i in range(len(start)):
	newfile = "geom_" + str(i) + ".xyz"
	opennew = open(newfile,"w")
	print(r'%i'%numero_atomi, file=opennew)
	print("",file=opennew)
	for line in rline[start[i]+5 : end[i]] :
		words = line.split()
		word1 = int(words[1])
		word3 = str(words[3])
		if   word1 ==   1 : word1 = "H"
		elif word1 ==   2 : word1 = "He"
		elif word1 ==   3 : word1 = "Li"
		elif word1 ==   4 : word1 = "Be"
		elif word1 ==   5 : word1 = "B"
		elif word1 ==   6 : word1 = "C"
		elif word1 ==   7 : word1 = "N"
		elif word1 ==   8 : word1 = "O"
		elif word1 ==   9 : word1 = "F"
		elif word1 ==  14 : word1 = "Si"
		elif word1 ==  15 : word1 = "P"
		elif word1 ==  16 : word1 = "S"
		elif word1 ==  17 : word1 = "Cl"
		## copy from atom list.
		print("%s%s" % (word1,line[30:-1]), file=opennew)
	opennew.close()
openold.close()


