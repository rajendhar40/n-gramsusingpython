import sys
import os
from collections import OrderedDict
import collections
import time

def process(filename,trigrams,pentagrams,heptagrams):
	for line in open(filename):
		line = line.rstrip()
		# tokenize the text:
		tokens = line.split()
	
	i= len(tokens)
	##3 grams
	for k in range (0,i-2):
		word = tokens[k]+" "+tokens[k+1]+" "+tokens[k+2]
		if word in trigrams:
			trigrams[word] += 1
		else:
			trigrams[word] = 1

	for k in range (0,i-4):
		word = tokens[k]+" "+tokens[k+1]+" "+tokens[k+2]+" "+tokens[k+3]+" "+tokens[k+4]
		if word in pentagrams:
			pentagrams[word] += 1
		else:
			pentagrams[word] = 1

	for k in range (0,i-6):
		word = tokens[k]+" "+tokens[k+1]+" "+tokens[k+2]+" "+tokens[k+3]+" "+tokens[k+4]+" "+tokens[k+5]+" "+tokens[k+6]
		if word in heptagrams:
			heptagrams[word] += 1
		else:
			heptagrams[word] = 1

	
#def main(argv,args):

start=time.time()

testgrams={}
train_trigrams={}
train_pentagrams={}
train_heptagrams={}
attacks=["Adduser","Hydra_FTP","Hydra_SSH","Java_Meterpreter","Meterpreter","Web_Shell"]
d=sys.argv[1:][0]+"_"

dicta_tri=[dict() for attack in range(0,8)]
dicta_penta=[dict() for attack in range(0,8)]
dicta_hepta=[dict() for attack in range(0,8)]
normal_tri={}
normal_penta={}
normal_hepta={}
d="ADFA-LD/Training_Data_Master"
for f in os.listdir(d):
	trigrams = {}
	pentagrams = {}
	heptagrams = {}
	process(d+"/"+f,trigrams,pentagrams,heptagrams)
	
	normal_tri=trigrams
	l=len(trigrams)
	trigrams=collections.Counter(trigrams).most_common(int(l*0.3))
	for gram in trigrams:
		train_trigrams[gram[0]]=1
		
	normal_penta=pentagrams
	l=len(pentagrams)
	pentagrams=collections.Counter(pentagrams).most_common(int(l*0.3))
	for gram in pentagrams:
		train_pentagrams[gram[0]]=1	
				
	normal_hepta=heptagrams		
	l=len(heptagrams)
	heptagrams=collections.Counter(heptagrams).most_common(int(l*0.3))
	for gram in heptagrams:
		train_heptagrams[gram[0]]=1	
		
	k=0	
for attack in attacks:
	trigrams = {}
	pentagrams = {}
	heptagrams = {}
	s=sys.argv[1:][0]+"/"+attack
	print(attacks[k])
	
	for i in range(1,8):
		d=s+"_"+str(i)
		for f in os.listdir(d):
			process(d+"/"+f,trigrams,pentagrams,heptagrams)
	#if sys.argv[1:][2]=="3":
	dicta_tri[k]=trigrams
	l=len(trigrams)
	trigrams=collections.Counter(trigrams).most_common(int(l*0.3))
	for gram in trigrams:
		train_trigrams[gram[0]]=1
	#if sys.argv[1:][2]=="5":
	dicta_penta[k]=pentagrams
	l=len(pentagrams)
	pentagrams=collections.Counter(pentagrams).most_common(int(l*0.3))
	for gram in pentagrams:
		train_pentagrams[gram[0]]=1			
	#if sys.argv[1:][2]=="7":
	dicta_hepta[k]=heptagrams		
	l=len(heptagrams)
	heptagrams=collections.Counter(heptagrams).most_common(int(l*0.3))
	for gram in heptagrams:
		train_heptagrams[gram[0]]=1
	k=k+1		

output_file=open(sys.argv[1:][1]+"_3_tested","w")
for i in range(6):
	testgrams=dicta_tri[i]
	
	output_file.write(attacks[i]+"\n")
	for gram in train_trigrams:
		if gram in testgrams:
			output_file.write(str(testgrams[gram])+"\t\t"+gram+"\n")
		else:
			output_file.write("0\t\t"+gram+"\n")
testgrams=normal_tri
output_file.write("normal\n")
for gram in train_trigrams:
	if gram in testgrams:
		output_file.write(str(testgrams[gram])+"\t\t"+gram+"\n")
	else:
		output_file.write("0\t\t"+gram+"\n")
					
output_file.close()						


output_file=open(sys.argv[1:][1]+"_5_tested","w")
for i in range(6):
	testgrams=dicta_penta[i]
	
	output_file.write(attacks[i]+"\n")
	for gram in train_pentagrams:
		if gram in testgrams:
			output_file.write(str(testgrams[gram])+"\t\t"+gram+"\n")
		else:
			output_file.write("0\t\t"+gram+"\n")
testgrams=normal_penta
output_file.write("normal\n")
for gram in train_pentagrams:
	if gram in testgrams:
		output_file.write(str(testgrams[gram])+"\t\t"+gram+"\n")
	else:
		output_file.write("0\t\t"+gram+"\n")
					
output_file.close()


output_file=open(sys.argv[1:][1]+"_7_tested","w")
for i in range(6):
	testgrams=dicta_hepta[i]
	
	output_file.write(attacks[i]+"\n")
	for gram in train_heptagrams:
		if gram in testgrams:
			output_file.write(str(testgrams[gram])+"\t\t"+gram+"\n")
		else:
			output_file.write("0\t\t"+gram+"\n")
testgrams=normal_hepta
output_file.write("normal\n")
for gram in train_heptagrams:
	if gram in testgrams:
		output_file.write(str(testgrams[gram])+"\t\t"+gram+"\n")
	else:
		output_file.write("0\t\t"+gram+"\n")
					
output_file.close()




print ("time taken %s seconds"%(time.time()-start)) 
				
