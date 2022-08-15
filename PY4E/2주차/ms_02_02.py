def tax(y):
    if y <= 1200:
        pay = 0.96 * y
    elif y <= 4600:
        pay = 0.85 * y
    elif y <= 8800:
        pay = 0.76 * y
    elif y <= 15000:
        pay = 0.65 * y
    elif y <= 30000:
        pay = 0.062 * y
    elif y <= 50000:
        pay = 0.60 * y
    elif y > 50000:
        pay = 0.58 * y
    return pay

monthly_payment = float(input("월급을 만원단위로 입력: ",))
y = 12 * monthly_payment

yearly_payment = tax(y)

print("세전 연봉:", y, "만원")
print("세후 연봉:", yearly_payment, "만원")