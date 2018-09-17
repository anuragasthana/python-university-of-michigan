hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate per Hour:")
r = float(rate)
pay = 0.0
if h > 40 :
    initial = 40 * r
    overtime = (h-40) * (r*1.5)
    pay = initial + overtime
else :
    pay = h * r
print(pay)

