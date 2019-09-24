# Calculate the avgerae of values in the lines starting with X-DSPAM-Confidence:
fname = input("Enter file name: ")
fh = open(fname)
avg=0
count=0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:") :
        count=count+1
        a=line.find(" ")
        b=line[a+1:]
        flt=float(b)
        avg=avg+flt

avg=avg/count
print("Average spam confidence:",avg)
