#3.9 하나의 정수를 입력받아 이 정수가 2로 나누어지는지, 3으로 나누어지는지 ,
#두 정수모두 나누어지는지 알려주는 프로그램
def ev(num):
    if num%2 == 0 and num%3==0 :
        print(f'{num}은(는) 2와 3 모두 나누어집니다.')
    else :
        print(f'{num}은(는) 2와 3 모두 나누어지지 않습니다.')
    if num%2==0 :
      print(f'{num}은(는) 2로 나누어집니다.')
    else :
        print(f'{num}은(는) 2로 나누어지지 않습니다.')
    if num%3==0 :
      print(f'{num}은(는) 3으로 나누어집니다.')
    else :
        print(f'{num}은(는) 3으로 나누어지지 않습니다.')
    # elif num%2 != 0 and num%3!=0  :
    #     print(f'{num}은(는) 2와 3 모두 나누어지지 않습니다.')

num = int(input("정수를 입력하세요 : >"))
ev(num)