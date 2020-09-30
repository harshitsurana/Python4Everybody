import re
name = input("Enter file:")
handle = open(name)
total=0
for lines in handle:
    lines=lines.rstrip()
    numbers = re.findall('[0-9]*',lines)
    new_list = []
    for i in numbers :
        if i :
            i = int(i)
            new_list.append(i)
    total=total+sum(new_list)
print(total)
