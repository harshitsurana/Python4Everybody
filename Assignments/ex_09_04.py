name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
dt=dict()
for lines in handle:
    lines=lines.rstrip()
    if lines.startswith('From '):
        wds=lines.split()
        w=wds[1]
        dt[w]=dt.get(w,0)+1
largest=-1
theword=None
for k,v in dt.items():
    if v>largest:
        theword=k
        largest=v
print(theword,largest)
