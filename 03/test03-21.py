# 3-30 1 : 덧셈 , 2: 뺄셈 , 3 : 곱셈, 4 : 나눗셈 으로 정수를 입력하면 연산을 해줌.


i = int(input('어떤연산을 원하는지 입력하세요'))

a, b = input(" 연산을 원하는 숫자 두개를 입력하세요 ").split(' ')

a = int(a)
b = int(b)

if (a and b > 0) and 1<= i<= 4:
    if i == 1 :
        print(f'{a} + {b} = {a + b}')
    elif i == 2 : 
        print(f'{a} - {b} = {a - b}')
    elif i == 3 :
        print(f'{a} * {b} = {a * b}')
    elif i == 4 :
        print(f'{a} / {b} = {a / b}')
else :
    print("잘못 입력하였습니다.") 