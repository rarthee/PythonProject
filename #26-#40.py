#26
#def hist(l):
 #   count=0
 #   char1=' '
 #   while count < len(l):
 #       b=l[count]
 #       count1 = 0
 #       char1=' '
 #       while count1 < b:
 #           char1=char1+'@'
 #           count1=count1+1
 #       count=count +1
 #       print(char1)

#hist([2,3,7,4])
#hist([4,1,2,9])

#27

#def conc(l):
#    count = 0
#    s=' '
#    while (count < len(l)):
#        s=s+str(l[count])
#        count = count + 1
#    print("output ",s)

#conc([3,'var','arthee',5,6])


#28

#def ord(l):
#    count= 0

#   while(l[count]!= 237):
#        count=count+1
#    print("Output ",l[:count])

#ord([1,3,4,5,77,32,123,5678,237,890,765,665,443])


#29

#def col(l1,l2):
#    count=0
#    while(count <len(l1)):
#        if l1[count] not in l2:
#            print(l1[count])
#        count=count+1

#col(["White","Black","Red"],["Red","Green"])

#30
#area of triangle

#31
#def gcd(x,y):
#    if x%y==0:
#         return y
#    for k in range(int(y/2),0,-1):
#        if x%k==0 and y%k==0:
#            return k


#print(gcd(12,18))


#32
#def lcm(x,y):
#    if(x%y==0):
#        return x
#    for k in range(int(y/2),0,-1):
#        if x%k==0 and y%k==0:
#            b=(int(x)*int(y))/k
#            return b
#print(lcm(12,18))

#33

#def sum(a):
#    count=0
#    s=0
#    while(count < len(a)):
#        if a[count] not in a[count+1:]:
#            s=s+int(a[count])
#        else:
#            s=0
#            break
##        count=count+1
#   print("output ",s)

#sum([1,3,4])
#sum([2,3,2])


#34

#def sum(x,y):
#    if (int(x)+int(y) > 15 and int(x)+int(y)<20):
#        return 20
#    else:
#        return (int(x)+int(y))
#print(sum(2,4))
#print(sum(14,4))

#35

#def sum(x,y):
#    if (x==y) or\
#        int(x)+int(y)==5 or\
#        abs(int(x)-int(y))==5:
#            return True

#print(sum(2,3))
#print(sum(7,2))
#print(sum(2,1))
#print(sum(6,6))


#36

#def add1(x,y):
#    if isinstance(x,int) and isinstance(y,int):
#        print("output ",x+y)

#add1(2,3)
#add1("a",2)

#37
#print("Name ","Arthee")
#print("Address ","Tanah Merah""\n","\t\t","Singapore")
#print("Age",36)

#38
#def sqr(x,y):
#    result = x*x + 2*x*y + y*y
#    print("({} + {}) ^ 2 = {}".format(x,y,result))

#sqr(3,4)
#sqr(1,2)

#39
#def intr(p,r,t):
#    val=float(p)*(1+float(r)/100)**(float(t))
#    print("Value ",val)

#intr(10000,3.5,7)

#40
def dist(x1,x2,y1,y2):
    print("Distance ",(((x2-x1)**2)+((y2-y1)**2))**0.5)

dist(4,6,0,6)