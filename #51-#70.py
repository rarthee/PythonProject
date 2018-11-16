#51
#import profile
#def sum():
#    print(1+2)
#print("Profile ",profile.run('sum()'))

#52

#import sys

#print(sys.stderr,"spam")

#53

#import os
#print("Output ",os.environ)

#54

#import getpass
#print(getpass.getuser())

#55

#import socket
#print(socket.AddressInfo)

#56 --tough

#57
#import time
#def sum(x,y):
#    sttime=time.time()
#    c=x+y
#    edtime=time.time()
#    time1=edtime-sttime
#print(sum(5,4))

#58

#def sum(n):
#    s=int(n)*(int(n)+1)/2
#    print(s)
#sum(10)

#59
#def conv(h):
#    cm=h*30.48
#    print(cm)
#conv(5.67)

#60
#import math
#def hyp(x,y):
#    hy=math.hypot(x,y)
#    print (hy)
#hyp(2,3)

#61

#def conv1(f):
#    print("Distance in Yards ",0.3333*int(f))
#    print("Distance in Miles ",0.0001893*int(f))
#    print("Distance in Inches ",12*f)

#conv1(40000)


#62
#def conv1(h,m,s):
#    print(int(h)*3600+int(m)*60+s)
#conv1(6,30,40)

#63
#import os
#def abfpath(file1):
#    print(os.path.abspath(file1))
#abfpath("Hello.txt")

#64

#import time
#import os
#print(time.ctime(os.path.getatime("Hello.txt")))

#65
#import math
#def conv1(s):
#    a,b=divmod(s,86400)
#    print("Days ",a)

#c,d=divmod(b,3600)
#    print("Hours ",c)


#e,f=divmod(d,60)
#    print("Minutes",e)
#    print("Seconds ",f)

#conv1(1234565)


#66

#def bmi(w,h):
#    bm=round(w/h,2)
#    bm1=round(bm/h,2)
#    print("BMI ",bm1)

#bmi(62,1.54)


#67--just formula

#68
import math
#def sumdg(n):
#    th,a=divmod(n,1000)
#    h,b=divmod(a,100)
#    te,o=divmod(b,10)
#    print("Sum of digits ",th+h+te+o)

#sumdg(1234)

#69
#def num1(a,b,c):
#    l1=min(a,b,c)
#    l3=max(a,b,c)
#    l2=a+b+c-l1-l3
#    print("increasing order", l1,l2,l3)

#num1(3,4,5)
#num1(4,5,3)
#num1(4,3,5)

#or another method
#print(sorted([4,5,3]))

#70
#import glob
#import os
#files=glob.glob("*.txt")
#files.sort(key=os.path.getmtime)
#print("\n".join(files))

#71--tough

#72
#import math
#print("Details", dir(math))

#73

#def midp(x1,y1,x2,y2):
#    mpx=(x2+x1)/2
#    mpy=(y2+y1)/2
#    print("Midpoint",mpx,mpy)

#midp(2,2,4,4)

#74--tough

#75
#print(license(copyright()))

#76
#import sys

#print("Name "),sys.argv[0]
#print("length"),len(sys.argv)
#print("Arguments"),str(sys.argv)

#77

#import sys
#print(sys.byteorder)

#78

#import sys
#print(sys.builtin_module_names)

#79
#import sys
#str1="one"
#print(sys.getsizeof(str1))

#80
#import sys
#print(sys.getrecursionlimit())
