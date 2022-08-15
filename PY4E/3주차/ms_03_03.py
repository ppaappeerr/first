#Q3
n = int(input("아무 숫자나 입력하세요 : n="))
m = int(input("아무 숫자나 입력하세요 : m="))
average = (n+m) / 2
a = []

print("입력값:", n,",", m)
numbers = [i for i in range(n,m+1)]
for number in numbers :
    if number % 2 == 1 :
        continue
    else :
        a.append(number)
print("입력값 사이 짝수:", a)
if (n+m) % 2 != 1:
    print("중앙값:", average)