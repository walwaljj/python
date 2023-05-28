#4-18 입력받은 두 수의 최소 공배수 구하기

from unittest import result


a = int(input("범위 시작 정수 : "))
b = int(input("범위 마지막 정수 : "))
result = 1
goq=1
if a<b :
    for bn in range(a,b+1):
        
        if bn%a !=0 :
            result *= bn
            
        else :
            goq *= bn//a
            result = goq * a

print(f'{a}에서 {b}까지 정수들의 최소 공배수는 : {result}')