num = int(input("숫자를 입력하세요 : "))

def make_comma(num):
    try:
        print(num)
    except:
        print("숫자로 입력해 주세요.")

make_comma(num)