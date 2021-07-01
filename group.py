import csv
import math
import sys
import numpy as np
from itertools import combinations
paircsv=[]
groupcsv=[]
onlypair=[]
with open('newpair.csv')as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        paircsv.append(row)

for i in range (1,len(paircsv)):
    sum=1
    for j in range (1,len(paircsv)):
        if i !=j:
            if paircsv[i][0] == paircsv[j][0] or paircsv[i][0] == paircsv[j][1] or paircsv[i][1] == paircsv[j][0] or paircsv[i][1] == paircsv[j][1]:
                sum=sum+1
    if sum ==1:
        onlypair.append([paircsv[i][0],paircsv[i][1]])
    groupcsv.append([paircsv[i][0],paircsv[i][1],sum])
    print(i/len(paircsv))


headers = ['objid1','objid2','group']
with open('newgroup.csv','w',newline='')as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(groupcsv)
    f.close()
    
headers2 = ['objid1','objid2']
with open('onlypair.csv','w',newline='')as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers2)
    f_csv.writerows(onlypair)
    f.close()