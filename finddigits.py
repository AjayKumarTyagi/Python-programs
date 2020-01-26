import re
name=input("enter the file name: ")
handle=open(name)
sum=0
y=list()
for line in handle:
    x=re.findall('[0-9]+',line)
    if len(x)!=0:
        for a in x:
            y.append(a)
print(y)
for data in y:
    sum=sum+int(data)
print(sum)
handle.close()
