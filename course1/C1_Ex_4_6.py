def computepay(h,r):
    if h > 40 :
    	initial = 40 * r
    	overtime = (h-40) * (r*1.5)
    	pay = initial + overtime
    else :
    	pay = h * r
    return pay

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate")
r = float(rate)
p = computepay(h,r)
print(p)