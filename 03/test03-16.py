
# 깊이가 30미터인 우물 , 이 우물의 달팽이는 하루에 +7미터, -5미터 이동한다.
high = 0
day = 1
while True :
    high += 7
    print(f'day :{day:02}\t 달팽이의 위치 : {high:02}미터')
    if high < 30 :
        high -= 5
        day += 1
    else :
        break