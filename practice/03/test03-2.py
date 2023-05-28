#문제 3-5 // 두개의 정수를 입력받아 작은 수 부터 큰 수 까지 나열하는 프로그램을 작성하기
number1 = int(input("정수를 입력하세요 : "))
number2 = int(input("정수를 입력하세요 : "))
min_num = 0
max_num = 0
if number1>number2 : 
    min_num = number2
    max_num = number1
else :
    min_num= number1
    max_num = number2
print(min_num, max_num)

#문제 3-5 // 세개의 정수를 입력받아 작은 수 부터 큰 수 까지 나열하는 프로그램을 작성하기
numlist = []
for n in range(3):
    number = int(input("정수를 입력하세요 : "))
    numlist.append(number)

for n in range(3) :
    if n==2 :
        break
    if numlist[n] > numlist[n+1] :
        min_num = numlist[n+1]
        numlist[n+1] = numlist[n]
        numlist[n] = min_num
print(numlist) 
