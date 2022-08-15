#syntax_error
print("HI') # 따음표가 일치 하지 않음
print("Hi"] #괄호가 일치 하지 않음
print("Hi") # Debugging

#type_error
Kim = 123
Lee = '123'
Park = "123"
print(Kim + '123') # Kim이 숫자열이므로 문자인 '123'과 연산 불가
print(Kim + 123) # Debugging
print(Lee + 123) # Lee가 문자열이므로 숫자인 123과 연산 불가
print(Lee + '123') # Debugging
print(Lee + "123") # Debugging
print(Park + 123) # Park이 문자열 이므로 숫자인 123과 연산 불가
print(Park + '123') # Debugging
print(Park + "123") # Debugging

#value_error
word = 'Hi'
iword = int(word)
print(iword + 1) # iword는 문자열이므로 정수화 및 계산 X
print(word + '1') # Debugging
num = '123'
#print(num + 1) #num은 문자열이므로 계산X
inum = int(num)
print(inum + 1.5) # Debugging
fnum = float(num) #int와 float 모두 수로 변환해 계산 가능
print(fnum + 1) # Debugging

#index_error
list1 = ['a', 'b', 'c', 'd', 'e']
#print(list1[5]) # 리스트에 없는 인덱스에 접근하는 오류
print(list1[4]) # Debugging

#name_error
a = 1
b = 2
#print(c) # 없는 변수를 찾으려는 오류
print(a + b) # Debugging

#zero_division_error
a = 1
b = 0
print(a/b) # 0으로 나누는 오류
print(b/a) # Debugging

#나이 문제
koa = int(input("나이: "))
birth = int(input("생일이 지났습니까? 맞으면 0 아니면 -1 : "))
usa = koa + birth -1
print(usa)