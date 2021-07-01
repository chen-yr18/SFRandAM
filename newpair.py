import csv
import math
import sys
import gc
import numpy as np
from itertools import combinations
paircsv=[]
pairlist=[]
with open('pair.csv')as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        paircsv.append(row)

combin=np.linspace(2, len(paircsv)-1, len(paircsv)-1-1, endpoint=True, retstep=False, dtype=None)
for i in range(2,len(paircsv)):
    for j in range(i+1,len(paircsv)):
        ra1=float(paircsv[i][1])
        ra2=float(paircsv[j][1])
        dec1=float(paircsv[i][2])
        dec2=float(paircsv[j][2])
        redshift1=float(paircsv[i][4])
        redshift2=float(paircsv[j][4])
        d1=299792.458*redshift1*1000000/67.8
        d2=299792.458*redshift2*1000000/67.8
        maxd=max(d1,d2)
        cosA=math.cos(dec1*math.pi/180)*math.cos(dec2*math.pi/180)+math.sin(dec1*math.pi/180)*math.sin(dec2*math.pi/180)*math.cos((ra1-ra2)*math.pi/180)
        if cosA >1 :
            touying=0
        elif cosA <-1:
            touying=maxd*math.pi
        else:
            touying=maxd*math.acos(cosA)
        deltaz=abs(((1+redshift1)**2-1)/(1+(1+redshift1)**2)-((1+redshift2)**2-1)/(1+(1+redshift2)**2))*299792.458
        if touying < 200000 and deltaz < 500 and paircsv[i][0] != paircsv[j][0]:
            pairlist.append([min(paircsv[i][0],paircsv[j][0]),max(paircsv[i][0],paircsv[j][0])])
    gc.collect()
    if i % 50 ==0:
        print(i/len(combin))
    

headers = ['objid1','objid2']
with open('newpair.csv','w',newline='')as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(pairlist)
    f.close()



