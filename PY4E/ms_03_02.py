import random
#from xml.dom.expatbuilder import parseString

sel = ['가위', '바위', '보']

user = input("가위, 바위, 보: ")
com = random.randint(0,2)
com = sel[com]

games = int(input("몇 판을 진행하시겠습니까?:"))

print("컴퓨터:", com)

if user == com :
    print("비겼습니다.")
elif user == "가위" :
    if com == "가위" :
        print("비겼습니다.")
    elif com == "바위" :
        print("졌습니다.")
    else :
        print("이겼습니다.")
elif user == "바위" :
    if com == "바위" :
        print("비겼습니다")
    elif com == "보" :
        print("졌습니다.")
    else :
        print("이겼습니다.")
elif user == "보" :
    if com == "보" :
        print("비겼습니다.")
    elif com == "가위" :
        print("졌습니다.")
    else :
        print("이겼습니다.")
