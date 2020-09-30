fname = input("Enter file name: ")
fh = open(fname)
total=0
count=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    ino=line.find(':')
    count=count+1
    total+=float(line[ino+1:])
print("Average spam confidence:",(total/count))
