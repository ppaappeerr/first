count = 0
n = int(input("첫 번째 수 입력 : "))
m = int(input("두 번째 수 입력 : "))
#count_prime_number(n, m)
def count_prime_number(n,m) :
    for i in range(n,m) :
        if n <= m :
            while n % i == 0:
                continue
            count = count +1
            
print(count)