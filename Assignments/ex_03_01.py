hrs = input("Enter Hours:")
h=float(hrs)
rate = input("Enter rate:")
r=float(rate)
if h<40:
    pay = h*r
else:
    pay = (h-40)*1.5*r+40*r
print("Pay:",pay)
