#81

#def conc(a):
#    i=0
#    s=' '
#    while(i<len(a)):
#        s=s+a[i]
#        i=i+1
#    print("Output",s)

#conc(["A","R","T","H","E","E"])
#conc(["S","A","H","A","N","A"])
#conc(["R","A","N","G","A"])

#82

#s=sum([20,20,10])
#print("Sum= ",s)

#83

#def chge(n,a):
#    i=0
#    while(i<len(a)):
#        if n<a[i]:
#            return True
#        else:
#            return False
#        i=i+1

#print(chge(2,[3,5,4,7]))
#print(chge(2,[1,2,3,4]))

#84
#def chge(n,a):
#    i=0
#    while(i<len(a)):
#        if n==a[i]:
#            return i
#        i=i+1
#print(chge(2,[3,2,1,4]))

#or

#s=("Hello How are you")
#print(s.count('l'))

#85
#import os
#path="Hello.txt"
#if os.path.isdir(path):
#    print("It is a directory")
#elif os.path.isfile(path):
#    print("It is a file")
#else:
#    print("It is some other file")

#86
#import string
#a="A"
#print(ascii(a))
#print(ord(a))

#87
#import os

#f="Numbers.py"

#print(os.path.getsize(f))

#88
#x=30
#y=20
#z=x+y
#print('"'+str(x)+"+"+str(y)+"="+str(z)+'"')

#89--simple

#90--tough

#91

#def swap(a,b):
#    a=a+b
#    b=a-b
#    a=a-b
#    return(a,b)

#print(swap(2,3))


#92-simple

#93
#print(id("Hello.txt"))

#94
#s=b'arthee'
#print(list(s))

#95

#def check(s):
#    try:
#        i=float(s)
#    except(ValueError, TypeError):
#        print("Not numeric")


#check("Arthee")
#check("12Arth")
#check("1234566")

#96--tough
#import traceback
#traceback.print_stack()

#97--tough

#98
#import time
#print(time.ctime())

#99

#import os
#os.system('cls')

#100
#import socket
#host_name= socket.gethostname()
#print(host_name)

#test
x=12
print(type(repr(x)))