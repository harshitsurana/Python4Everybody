name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
dt=dict()
for lines in handle:
    lines=lines.rstrip()
    if lines.startswith('From '):
        wds=lines.split()
        w=wds[5]
        time=w.split(':')
        hour=time[0]
        dt[hour]=dt.get(hour,0)+1
lst=list()
for k,v in dt.items():
    lst.append((k,v))
lst.sort()
for k,v in lst:
    print(k,v)
