#16
#num=int(input("Enter a number"))
#if num <= 17:
#    print("The difference is:", 17-num)
#else:
#    print("The difference is:", 2*abs(17-num))

#17

#def num(n):
#    if abs(1000-n)<100:
#        print("Number is within 100 of 1000")
#    elif 2000-n < 100:
#        print ("Number is within 100 of 2000")

#num(50)
#num(910)
#num(1950)


#18

#def sum(a,b,c):
#    if a==b==c:
#        print("Value :",3*(a+b+c))
#    else:
#        print("Sum: ",a+b+c)

#sum(1,3,4)
#sum(3,3,3)

#19
#def newstr(a):
#    if (a[0:2]== 'is'):
#        print("Output is: ",a)
#    else:
#        print("Output is: ","is"+a)

#newstr("isempty")
#newstr("full")


#20

#def nonnegcpy(a,c):
#      b=' '
#      count=0
#      while(count<c):
#         b=b+a
#          count =count+1

#      print("Output ",b)

#nonnegcpy("message",2)
#nonnegcpy("output",3)
#nonnegcpy("lenovo",1)

#21
#def evenodd(num):
#    if num%2 == 0:
#        print('The number is even')
#    else:
#        print('The number is odd')

#evenodd(3)
#evenodd(4)

#22
#def cntnum(arr,num):
#    count1=0
#    count=0
#   while(count < len(arr)):
#        if arr[count]==num:
#            count1=count1+1
#        count=count+1
#    print("the occurrence is ", count1)
#cntnum([2,3,1,2],2)
#cntnum([4,6,7,8,9],5)

#23

#def nonnegcpy(a,c):
#      b=' '
#      count=0
#      while(count<c):
#       if len(a) < 2:
#            b=b+a
#            count=count+1
#        else:
#            b=b+a[:2]
#            count =count+1

#      print("Output ",b)

#nonnegcpy("message",2)
#nonnegcpy("ou",3)
#nonnegcpy("lenovo",1)

#24

#def vow(a):
#    if a == "a"or\
#       a== "e" or \
#      a=="i" or \
#      a=="o" or \
#       a=="u":
#        print("It is a vowel")
#    else:
#        print ("It is not a vowel")

#vow("a")
#vow("c")


#25

def value(n,a):
    count = 0
    count1 =0

    while(count < len(a)):
        if n == a[count]:
            count1=count1 + 1
            count=count + 1
        else:
            count =count + 1
    if count1 > 0:
        print("The number is found")
    else:
        print("The number is not found")



value(2,[1,2,3,4])
value(3,[5,4,6,7,8])
