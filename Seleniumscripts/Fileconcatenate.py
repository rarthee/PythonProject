import os
import glob
import csv

#input files location
csvfiles=glob.glob("C:/Users/Sahana Rangarajan/Desktop/input files/*.csv")
#output file
wf=csv.writer(open("C:/Users/Sahana Rangarajan/Desktop/input files/concatenated.csv",'wb'),delimiter = ',')


for files in csvfiles:
    print(files)
    rd=csv.reader(open(files,'r'),delimiter = ',')
    for row in rd:
        wf.writerow(row)










