
name=input("Enter student's name")
s1= ['Ahmad', 18, 17, 19.5, 8, 25]
s2= ['Sami', 20, 20, 19, 9, 28]
s3= ['Faris', 14.5, 16, 13, 7, 23]
if name==s1[0]:
    name=s1[0]
    result=sum(s1[1:])
elif name==s2[0]:
     name=s2[0]
     result=sum(s2[1:])
elif name==s3[0]:
    name=s2[0]
    result=sum(s3[1:])
else:
    name='student is not recorded'
    result=0

print(name,result)
