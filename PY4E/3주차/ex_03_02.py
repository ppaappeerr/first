xh = input("Enter Hours: ")
xr = input("Enter Rate: ")
try :
    fh = float(xh)
    fr = float(xr)
except :
    print("Error, please enter numeric input")
    quit()

print(fh,fr)
if fh > 40:
    xp = fr * (fh + (fh-40) / 2)
else :
    xp = fr * fh
print("Pay:",xp)