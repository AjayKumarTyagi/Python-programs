name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
hour=list()
for line in handle:
    if line.startswith("From "):
        words=line.split()
        lst=words[5]
        time=lst.split(":")
        hour.append(time[0])
dic=dict()
for h in hour:
    dic[h]=dic.get(h,0)+1
for k,v in sorted(dic.items()):
    print(k,v)
    
