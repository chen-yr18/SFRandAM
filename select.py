import csv
import math
import gc
import numpy as np
import matplotlib.pyplot as plt

paircsv=[]
onlypaircsv=[]
pairlist=[]
pairlist2=[]
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
            objid1=float(paircsv[j1][0])
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
            objid2=float(paircsv[j2][0])
            KMK20FE2=float(paircsv[j2][6])
            redshift2=float(paircsv[j2][4])
            w4mpro2=float(paircsv[j2][7])
            petroMag_r2=float(paircsv[j2][3])
            ra2=float(paircsv[j2][1])
            dec2=float(paircsv[j2][2])
            d2=299792.458*redshift2*1000000/67.8
            break
    if KMK20FE2>=KMK20FE1:
        pairlist2.append(
                [objid2,ra2,dec2,redshift2,KMK20FE2,w4mpro2]
        )
        pairlist2.append(
                [objid1,ra1,dec1,redshift1,KMK20FE1,w4mpro1]
        )
    else:
        pairlist2.append(
                [objid1,ra1,dec1,redshift1,KMK20FE1,w4mpro1]
        )
        pairlist2.append(
                [objid2,ra2,dec2,redshift2,KMK20FE2,w4mpro2]
        )
   

headers = ['objid','RA','DEC','z','mk','mw4']
with open('newpair2.csv','w',newline='')as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(pairlist2)
    f.close()
