def bus_fare(age, way):
    if age < 8:
        pay = 0
    elif age < 14:
        pay = 450
    elif age < 20:
        if way == "카드":
            pay = 720
        else:
            pay = 1000
    elif age < 75:
        if way == "카드":
            pay = 1200
        else:
            pay = 1300
    elif age >= 75:
            pay = 0
    return pay

x = int(input("나이를 숫자로 입력하시오.: "))
y = input("지불유형(카드or 현금)을 입력하시오: ")

z = bus_fare(x, y)

print("나이:", x, "세")
print("지불유형:", y)
print("버스요금:", z, "원")