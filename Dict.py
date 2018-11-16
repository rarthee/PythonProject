#1
#import operator
#dict1={"a":3,"b":2,"c":3}
#sort1=sorted(dict1.items(),key=operator.itemgetter(0))
#sort2=sorted(dict1.items(),key=operator.itemgetter(0),reverse=True)

#print(sort1)
#print(sort2)

#2
#dict1={0: 10, 1: 20}
#d2={3:30}
#dict1.update(d2)
#print(dict1)

#3

#dic1={1:10, 2:20}
#dic2={3:30, 4:40}
#dic3={5:50,6:60}
#d3={}
#d3.update(dic1)
#d3.update(dic2)
#d3.update(dic3)
#print(d3)

#4

#d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
#def is_key_present(x):
#  if x in d:
#      print('Key is present in the dictionary')#

#is_key_present(5)

#5
#d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
#for k,v in d.items():
#    print(k,"-",v)


#6
#n=int(input('Enter n'))

#d=dict()
#for x in range(1,n+1):
#    d[x]=x*x
#print(d)

#7
#d=dict()
#for x in range(1,16):
#    d[x]=x*x
#print(d)

#8
#d1={'a':1,'b':2,'c':3}
#d2={'d':4,'e':5,'f':6}
#d1.update(d2)
#print(d1)

#9
#d1={'a':1,'b':2,'c':3}

#for x,k in d1.items():
#    print(x," corresponds to ",k)

#10
#d1={'a':1,'b':2,'c':3}
#print(sum(d1.values()))

#11

#d1={'a':4,'b':2,'c':3}
#m=1
#for k,v in d1.items():
#    m=m*v
#print(m)

#12

#d1={'a':4,'b':2,'c':3}
#d1.pop('a')
#print(d1)

#13
#l1=['a','b','c','d']
#l2=[1,2,3,4]
#i=0
#d1={}
#while i < len(l1):
#    d1.update({l1[i]:l2[i]})
#    i=i+1
#print(d1)

#d2=dict(zip(l1,l2))
#print(d2)

#14


#d1={'d':4,'c':2,'a':3}
#for k in sorted(d1.keys()):
#    print(k,d1[k])

#15
#d1={'b':4,'c':2,'a':3}
#keymax=max((d1.keys()),key=lambda k:d1[k])
#print(d1[keymax])

#16--tough

#17
#d1={'b':4,'c':2,'a':3,'b':4}
#d2={}
#for k,v in d1.items():
#    if v not in d2.values():
#        d2[k]=d1[k]
#print(d2)

#18
#d1={}
#for k,v in d1.items():
 #   if k== ' ':
 #       break

#print("The list is empty")

#19
#from collections import Counter
#d1 = {'a': 100, 'b': 200, 'c':300}
#d2 = {'a': 300, 'b': 200, 'd':400}
#d = Counter(d1)+ Counter(d2)
#print(d)

#20

#dict1= [{"V":"S001"}, {"V": "S002"},
#        {"VI": "S001"}, {"VI": "S005"},
#        {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
#print(set(val for dic in dict1 for val in dic.values()))

#21


d1={'1':['a','b'], '2':['c','d']}
l1=[1]
for k,v in d1.items():
    i=0
    l1[i]=d1[k]
    while i < len(l1):
        l1[i]=l1[i]*v[k]











