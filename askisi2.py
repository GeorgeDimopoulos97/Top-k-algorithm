#GEORGIOS DIMOPOULOS
#A.M. 2964

import sys
import time
from heapq import heappop, heappush, heapify, nlargest

start=time.time()
K=int(sys.argv[1])
heap = [] 
heapify(heap) #min heap oura
males_hash={} #leksiko gia male
males=open("males_sorted")
females=open("females_sorted")
exit=0
exit1=0
males_line=[]
females_line=[]

#Diabasma tou arxeiou male kai bazo tis pleiades se leksiko
while True: #mexri na teleiosei to arxeio
	males_line=males.readline()
	males_line=males_line.split(",")
	males_line=[f.strip() for f in males_line]
	if males_line==[""]:
		break
	while int(males_line[1])<18 or males_line[8][0:7]=="Married":
		males_line=males.readline()
		males_line=males_line.split(",")
		males_line=[f.strip() for f in males_line]
		if males_line==[""]:
			exit=1
			break
	if exit==1:
		break
	if males_line[1] in males_hash:
		males_hash.get(males_line[1]).append([males_line[0],males_line[25]])
	else:
		males_hash.update({males_line[1] : [[males_line[0],males_line[25]]]})
#Telos diabasma arxeiou male

#Diabasma kathe pleiadas tou arxeiou female kai to sygkrino me to leksiko tou male
while True: #mexri na teleiosei to arxeio
	females_line=females.readline()
	females_line=females_line.split(",")
	females_line=[f.strip() for f in females_line]
	if females_line==[""]:
		break
	while int(females_line[1])<18 or females_line[8][0:7]=="Married":
		females_line=females.readline()
		females_line=females_line.split(",")
		females_line=[f.strip() for f in females_line]
		if females_line==[""]:
			exit1=1
			break
	if exit1==1:
		break
	if females_line[1] in males_hash:
		for i in range(0,len(males_hash.get(females_line[1]))):
			if len(heap)==K:
				if (float(males_hash.get(females_line[1])[i][1])+float(females_line[25]))>heap[0][0]:
					heappop(heap)
					heappush(heap,[((float(males_hash.get(females_line[1])[i][1])+float(females_line[25]))),males_hash.get(females_line[1])[i][0],females_line[0]])
			else:
				heappush(heap,[((float(males_hash.get(females_line[1])[i][1])+float(females_line[25]))),males_hash.get(females_line[1])[i][0],females_line[0]])
#Telos diabasma arxeiou female

result=nlargest(len(heap),heap) #pairno ta stoixeia moy me tin seira pou thelo
for i in range(0,K):
	print str(i+1)+". pair: "+str(result[i][1])+","+str(result[i][2])+" score: "+str(result[i][0])
males.close()
females.close()
end=time.time()
print "----------------------------"
print "Total time:",end-start
print "----------------------------"