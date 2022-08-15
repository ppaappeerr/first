#Q1
number = int(input("몇 단? : "))
print(number, "단")

for value in range(51) :
    if value % 2 != 1 :
        continue
    else :
        result = number * value
        if result <= 50 :
            print(number, "X", value, "=", result)
        else :
            print("more than 50")
            break
        