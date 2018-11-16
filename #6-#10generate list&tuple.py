#6
#str=input("Enter the numbers ")
#st=str.split(",")
#print("list: ",list(st))
#print("tuple: ",tuple(st)
##################################################################

#7
## print the file type from a file name

#fname=input("Enter file name: ")
#fextn=fname.split(".")
#print("File type is ",fextn[1])

#8
##Display first and last colors from a list

#list1 = ["Red","Green","White","Black"]
#print("first and last colors are ",list1[0],list1[-1])

#9 Print Examination schedule

exam_st_date=input("Enter exam starting date ")
st_date=list(exam_st_date.split(","))
print("The examination will start from :",st_date[0]+"/"+st_date[1]+"/"+st_date[2])

#10
##Compute the value of n+nn+nnn

#num=int(input("Enter an integer"))
#a=int("%s" %num)
#b=int("%s%s" %(num,num))
#c=int("%s%s%s" %(num,num,num))
#print("The answer is :",a+b+c)