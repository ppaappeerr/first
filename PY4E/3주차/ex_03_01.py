xh = input("Enter Hours: ")
xr = input("Enter Rate: ")
fh = float(xh)
fr = float(xr)
if fh > 40:
    xp = fr * (fh + (fh-40) / 2)
else :
    xp = fr * fh
print("Pay:",xp)