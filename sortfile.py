fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    word=line.split()
    for w in word:
        if w not in lst:
            lst.append(w)
lst.sort()
print(lst)
