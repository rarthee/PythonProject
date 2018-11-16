#1
#print(len("python"))

#2
#str='google.com'
#count=0
#d={}

#for s in str:
#     keys=d.keys()
#     if s in keys:
#        d[s]+=1
#     else:
#         d[s]=1

#print(d)

#3
#str1='w3resource'
#s=str1[0:2]+str1[-2:]
#4
#str1='restart'
#output= 'resta$t'

#c=str1[0]

#print(s)

#for s in str1:
#    str1=str1.replace('r','$')

#print(c+str1[1:])

#5
#str1='abc'
#str2='xyz'
#'xyc abz'
#s1=str1[:2]
#s2=str2[2:]
#print(s1,s2)

#print(str2[:2]+str1[2]+' '+str1[:2]+str2[2])

#6

#def adding(str1):
#    if len(str1)<3:
#        return(str1)
#    else:
#        if(str1[-3:])=='ing':
#            return(str1+'ly')
#        else:
#            return(str1+'ing')

#print(adding("lying"))
#print(adding("cat"))
#print(adding("so"))

#7'The lyrics is not that poor!'

#def subst1(str1):
#    i=0
#    s1=str1.find('not')
#    s2=str1.find('poor')
#    print(s1,s2)
#    str1=str1.replace(str1[s1:s2+4],'good')
#    return(str1)
#print(subst1('The lyrics is not that poor!'))

#8

#def longwordlen(lis1):
#    i=0
#    while(i<(len(lis1)-1)):
#         lp=len(str(lis1[i]))
#         ln=len(str(lis1[i+1]))
#         if(ln>lp):
#             ln=lp

         #i=i+1
    #return(lis1[ln])
#print(longwordlen(["I","am","a","good","boy"]))


#9

#def removes(str1,n):
#    str2=str1[:n]+str1[n+1:]
#    return(str2)

#print(removes('python',1))

#10

#def changepos(str1):
#    str2=str1[-1]
#    for s in str1:
##        if (s!=str1[0]) and (s!=str1[-1]):
 #           str2+=s

 #   str2 = str2+ str1[0]
 #   return(str2)

#print(changepos('abcd'))

#11
#def changepos(str1):
#    n=len(str1)
#    i=n
#    s=''
#    for i in range(len(str1)):
#        if(i%2==0):
  #          s=s+str1[i]

 #   return(s)

#print(changepos('abcdef'))

#12

#def wordcount(str1):
#    d=dict()
#    words=str1.split()
#    for words in words:
#        if words in d:
#            d[words]+=1
#        else:
#            d[words]=1
#    return(d)
#print(wordcount('the quick brown fox jumps over the lazy dog.'))

#13
#str1=input("Enter a string")
#print(str1.upper())

#14
#list1=input('Enter comma separated words')
#words=[word for word in list1.split(',')]
#print(",".join(sorted(list(words))))

#15
#def add_tags(tag,value):
#    return("<%s>%s</%s>") %(tag,value,tag)

#print(add_tags('i','Python'))

#16
#def insstrmid(str1,str2):
#str1="[[]]"
#str2="Python"
#midpos=int((len(str1)/2))
#i=0
#print(midpos,i)
#str3=''
#while(i<len(str1)):
#    if i!=midpos:
#        str3+=str1[i]
#    else:
#        str3+=str2+str1[i]
#       i=i+1
#print(str3)

#17

#def insert_end(str1):

  #  str2=str1[-2:]
#    return(str2*4)
#print(insert_end('Python'))

#18
#def first_three(str1):
#   return(str1[:2])

#print(first_three('Python'))

#19

#def printtillch(str1,ch):

       # return(str1.rsplit('-',1)[0])

#print(printtillch('https://www.w3resource.com/python-exercises','-'))

#20

def revstr(str1):
    l1=len(str1)
    return(''.join(reversed(str1)))

print(revstr('Artheesa'))