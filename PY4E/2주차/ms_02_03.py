def grader(name, score):
    if score < 60:
        grade = "F"
    elif score <= 64:
        grade = "D"
    elif score <= 69:
        grade = "D+"
    elif score <= 74:
        grade = "C"
    elif score <= 79:
        grade = "C+"
    elif score <= 84:
        grade = "B"
    elif score <= 89:
        grade = "B+"
    elif score <= 94:
        grade = "A"
    elif score <= 100:
        grade = "A+"
    return grade

x = (input("이름을 입력해 주세요.: "))
y = float(input("점수를 입력해 주세요.: "))

z = grader(x,y)

print("이름:",x)
print("점수:", y, "점")
print("학점:", z)