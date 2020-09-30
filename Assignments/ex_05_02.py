largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" :
         break
    try:
        no=int(num)
    except :
        print("Invalid input")
        continue
    if smallest is None:
        smallest=no
    elif no<smallest:
        smallest=no
    if largest is None:
        largest=no
    elif no>largest or no is None:
        largest=no

print("Maximum is", largest)
print("Minimum is", smallest)
