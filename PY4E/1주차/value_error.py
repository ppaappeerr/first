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