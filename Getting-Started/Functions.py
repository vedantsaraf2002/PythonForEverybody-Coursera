def computepay(h, r):
    h = float(h)
    r = float(r)
    pay =0
    if(h>40):
       pay = 40*r + (h-40)*(r*1.5)
    else:
        pay = h*r
    
    return pay

hrs = input("Enter Hours:")
rate = input("Enter rate:")
p = computepay(hrs, rate)
print("Pay", p)


