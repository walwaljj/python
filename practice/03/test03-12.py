#3-16. 1~9사이 숫자 를 입력받고 작성.

dan = int(input("1~9까지의 숫자를 입력하세요>>"))
while True :
    if 1<=dan<=9 :
        for a in range(1,10) :
            print(f'{dan} x {a} = {dan * a}')
        break    
    else :
        dan = int ( input ('1부터 9 까지 수를 다시 입력하세요.>'))