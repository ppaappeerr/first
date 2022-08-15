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