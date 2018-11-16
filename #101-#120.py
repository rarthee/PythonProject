#101--tough
#import http.client
#print(http)

#102-tough

#103

#import os
#print(os.path.basename('/Users/Sahana Rangarajan/PycharmProjects/Pythontutorials/#6-#10generate list&tuple.py'))

#104
#import os
#print(os.getegid())
#print(os.geteuid())
#print(os.getgid())
#print(os.getgroups())

#105
#import os
#print(os.environ)

#106-tough
#107

#import os.path
#import time
#print(time.ctime(os.path.getatime(__file__)))

#108
#import os.path
#print(os.path.isdir("\Sahana Rangarajan\PycharmProjects\Pythontutorials"))
#print(os.path.isfile("\Sahana Rangarajan\PycharmProjects\Pythontutorials"))

#109
#def pnz(a):
#    if int(a)>0:
#        print("Positive")
#    elif int(a) < 0:
#        print("Negative")
#    else:
#        print("Zero")

#pnz(1)
#pnz(-2)
#pnz(0)

#110
#import math
#def dv15(a):
#    i=0
#    while(i<len(a)):
#        if math.remainder(int(a[i]),15)==0:
#             print(a[i],"is divisible by 15")
#        i=i+1

#dv15([22,15,34,30,75,76])

#111
#import glob
#print(glob.glob('*.*'))

#112
#def ls(s):
#    del(s[0])
#    print(s)
#ls([1,'a',3,5])

#113

#def check(s):
#    try:
#        i=int(s)
#    except(ValueError, TypeError):
#        print("Not numeric")


#check("Arthee")
#check(1)
#check(2)
#check("Sahana")

#114

#a=[1,-2,3,-4,2,4,-5,-7,9,0]
#i=0
#while(i<len(a)):
#    if a[i]<0:
#        del a[i]

#    else:
#        i=i+1
#print(a)

#115
#x=lambda a,b,c,d:a*b*c*d
#print(x(1,3,4,5))

#116
#print("u'\u0050\u0056'")

#117
import sys
#str1="Python"
#str2=str1
#print(hex(id(str1)))
#print(hex(id(str2)))

#118
#ls=[1,2,4,6,7]
#a=bytearray(ls)
#for x in a:print(x)
#print()

#119

#fn=1.234
#print('%f' %fn)
#print('%.2f' %fn)

#120
st="arthee R"
print('%.6s' %st)








