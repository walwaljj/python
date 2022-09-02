numbers = [11,44,55,88,54,22,33,44]
numbers2 = [111,333,666,1133,443,22]
#list의 요소 중 홀수의 값만 찾아 odd_list에 저장하기
odd_list = list()

for num in numbers:
   if num%2==1 :
        odd_list.append(num)

print(odd_list)

odd2_list = []
def func():
    for num in numbers:
        if num%2==1 :
            odd2_list.append(num)

func()
print(odd2_list)

#일반화 시켜서 의존하지 않게 만듦 --> 필요한 전역변수를 매개변수로 받으면 일반화가 가능하다.
def func2(numbers):
    #global
    odd2_list = [] #지역변수 , 전역으로 만드려면 global사용
    for n in numbers:
        if n%2==1 :
            odd2_list.append(n)
    return odd2_list

odd2_list = func2(numbers)
print(odd2_list)

odd3_list = func2(numbers2)
print(odd3_list)