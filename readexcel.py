import xlrd

#input files location
loc=("C:/Users/Sahana Rangarajan/Desktop/input files/Pythontestfile.xls")

inpfile1=xlrd.open_workbook(loc)
sheet = inpfile1.sheet_by_index(0)
keys=[]
f=[]
i=0
while (i<sheet.nrows):
    keys.append(sheet.cell_value(i, 0))
    l=[]
    j=1
    while(j<sheet.ncols):
        l.append(sheet.cell_value(i,j))
        j=j+1

    d= {keys[i]:l}
    f.append(d)
    i = i + 1
print(f)



