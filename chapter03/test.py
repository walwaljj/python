#상황1 : 나이가 20세 미만이면 ‘청소년 할인’을 출력하는 기능

age = 30
if age <20 :
    print('청소년 할인')
else : print('표준요금')

#상황 2 : 1000 걸음 이상을 걸으면 ‘목표 달성’을 출력하는 기능

walk = 999
if (walk>1000) :
    print('목표달성')
else : print('조금만 더 걸으세요')

'''상황 3: 시간이 12시가 안되면 ‘오전입니다’, 12시 이후이면 ‘오후입니다
를 출력하는 기능'''

time = 155
if time<12 :
    print('오전입니다.')
elif time>12 :
    print('오후입니다.')

#상황 3 : 3과 5의 배수인지 여부 판단

number = int(input("숫자를 입력하세요 : "))
if(number%3==0 and number %5==0) :
    print("3과 5의 배수입니다.")
    if(number%300==0) :
        print("축하합니다!")
elif(number%3==0) : 
    print("3의 배수")
elif( number %5==0) :
        print("5의 배수")
else : print("3과 5의 배수가 아니군요.")


'''윤년검사하기'''

year = int(input("년도를 입력하세요 : "))

if year%4==0 :
    if (year%100==0 and year%400==0) :
                 print("윤년입니다.")
    elif year%100==0 :
        print("평년입니다.")

    else : print("아무것도아님")
else : print("아무것도아님")