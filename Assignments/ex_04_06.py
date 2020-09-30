def computepay(h,r):
    if h<40:
        return h*r
    else:
        return (h-40)*1.5*r+40*r

hrs = input("Enter Hours:")
h=float(hrs)
rate = input("Enter rate:")
r=float(rate)
p = computepay(h,r)
print("Pay",p)
