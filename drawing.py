import csv
import math
import gc
import numpy as np
import matplotlib.pyplot as plt

paircsv=[]
onlypaircsv=[]
pairlist=[]
SFR=[]
L=[]
with open('pair.csv')as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        paircsv.append(row)

with open('onlypair.csv')as f2:
    f_csv = csv.reader(f2)
    for row in f_csv:
        onlypaircsv.append(row)


for i in range (1,len(onlypaircsv)):
    for j1 in range (2,len(paircsv)):
        if onlypaircsv[i][0]==paircsv[j1][0]:
            KMK20FE1=float(paircsv[j1][6])
            redshift1=float(paircsv[j1][4])
            w4mpro1=float(paircsv[j1][7])
            petroMag_r1=float(paircsv[j1][3])
            ra1=float(paircsv[j1][1])
            dec1=float(paircsv[j1][2])
            d1=299792.458*redshift1*1000000/67.8
            break

    for j2 in range (2,len(paircsv)):
        if onlypaircsv[i][1]==paircsv[j2][0]:
            KMK20FE2=float(paircsv[j2][6])
            redshift2=float(paircsv[j2][4])
            w4mpro2=float(paircsv[j2][7])
            petroMag_r2=float(paircsv[j2][3])
            ra2=float(paircsv[j2][1])
            dec2=float(paircsv[j2][2])
            d2=299792.458*redshift2*1000000/67.8
            break
    maxd=max(d1,d2)
    cosA=math.cos(dec1*math.pi/180)*math.cos(dec2*math.pi/180)+math.sin(dec1*math.pi/180)*math.sin(dec2*math.pi/180)*math.cos((ra1-ra2)*math.pi/180)
    if cosA >1 :
        touying=0
    elif cosA <-1:
        touying=maxd*math.pi
    else:
        touying=maxd*math.acos(cosA)           
    sfr=(w4mpro1-KMK20FE1+w4mpro2-KMK20FE2)/2
    l=(math.exp(KMK20FE2)*math.exp(KMK20FE1))*(((1+redshift1)**2-1)/(1+(1+redshift1)**2)-((1+redshift2)**2-1)/(1+(1+redshift2)**2))*299792.458*maxd/(math.exp(KMK20FE2)+math.exp(KMK20FE1))
    SFR.append(sfr)
    L.append(l)

plt.scatter(L,SFR)
plt.show()


