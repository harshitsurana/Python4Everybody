fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    linex=line.rstrip()
    liney=line.split()
    for words in liney:
        if words in lst:
            continue
        lst.append(words)
lst.sort()
print(lst)
