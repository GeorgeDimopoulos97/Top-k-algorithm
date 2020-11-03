#GEORGIOS DIMOPOULOS
#A.M. 2964

import sys
import time
from heapq import heappop, heappush, heapify

start=time.time()
def yield_function(file):
    field = next(file,"finish").split(",") #lista me tin grammi
    field = [f.strip() for f in field] #bgazo to \n sto telos
    yield field

#Algorithomos A top-k join
def A_top_k_join():
	global heap
	global p2_max,p2_cur
	global males_hash,females_hash
	global p1_max,p2_max
	global males,females
	global valid_male,valid_female

	while True:
		males_line=next(yield_function(males))
		while int(males_line[1])<18 or males_line[8][0:7]=="Married":
			males_line=next(yield_function(males))
		valid_male=valid_male+1
		p1_cur=float(males_line[25])
		T=max((p1_max+p2_cur),(p1_cur+p2_max))
		if males_line[1] in males_hash:
			males_hash.get(males_line[1]).append([males_line[0],males_line[25]])
		else:
			males_hash.update({males_line[1] : [[males_line[0],males_line[25]]]})
		if males_line[1] in females_hash:
			for i in range(0,len(females_hash.get(males_line[1]))):
				heappush(heap,[-((float(females_hash.get(males_line[1])[i][1])+p1_cur)),males_line[0],females_hash.get(males_line[1])[i][0]])
		while len(heap)>0 and -heap[0][0]>=T:
			element=heappop(heap)
			yield "pair: "+str(element[1])+","+str(element[2])+" score: "+str(-element[0])

		females_line=next(yield_function(females))
		while int(females_line[1])<18 or females_line[8][0:7]=="Married":
			females_line=next(yield_function(females))
		valid_female=valid_female+1
		p2_cur=float(females_line[25])
		T=max((p1_max+p2_cur),(p1_cur+p2_max))
		if females_line[1] in females_hash:
			females_hash.get(females_line[1]).append([females_line[0],females_line[25]])
		else:
			females_hash.update({females_line[1] : [[females_line[0],females_line[25]]]})
		if females_line[1] in males_hash:
			for i in range(0,len(males_hash.get(females_line[1]))):
				heappush(heap,[-((float(males_hash.get(females_line[1])[i][1])+p2_cur)),males_hash.get(females_line[1])[i][0],females_line[0]])
		while len(heap)>0 and -heap[0][0]>=T:
			element=heappop(heap)
			yield "pair: "+str(element[1])+","+str(element[2])+" score: "+str(-element[0])

#Telos algorithomou A top-k join
K=int(sys.argv[1])
heap = [] 
heapify(heap) #max heap
p2_cur=0 #p2_cur for female
males_hash={} #dictionari for male
females_hash={} #dictionari for female
males=open("males_sorted")
females=open("females_sorted")
max1=males.readline().split(",")[25][1:]
max2=females.readline().split(",")[25][1:]
p1_max=float(max1) #max p1 for male
p2_max=float(max2) #max p2 for female
valid_male=0 #egkires grammes gia male
valid_female=0 #egkires grammes gia female
males.seek(0) #pao pali stin arxi tou arxeiou
females.seek(0) #pao pali stin arxi tou arxeiou
k=0
for result in A_top_k_join():
	print str(k+1)+". "+result
	k=k+1
	if k==K:
		break

males.close()
females.close()
end=time.time()
print "----------------------------"
print "Total time:",end-start
print "Valid lines of male:",valid_male
print "Valid lines of female:",valid_female
print "----------------------------"