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
filename= "rrr_t_opt.log"
#filename = sys.argv[1]
openold = open(filename,"r")



rline = openold.readlines()

tmp = []
for i in range(len(rline)):
	if "Standard orientation" in rline[i]:	
		tmp = []
	tmp.append(i)
	if "Stationary " in rline[i]:
		start.append(tmp[0])
		tmp=[]
	else:
		pass

#start contain the start line for the optimized structure which are ended by "Stationary Point" string
#the first xyz line is the 5th



for i in start:
       for m in range (int(i) + 5, len(rline)):
               if "---" in rline[m]:
                       end.append(m)
                       break
#end contain the end line of the structures

n_atoms=end[0]-start[0]-5 


for i in range(len(start)):
	newfile = "geom_" + str(i) + ".xyz"
	opennew = open(newfile,"w")
	print(r'%i'%n_atoms, file=opennew)
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


