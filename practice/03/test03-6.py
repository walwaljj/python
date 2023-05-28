#3.10 사용자로부터 2개의 정수 a,b를 입력받고 a가 b의 배수인지를 판단하여 출력하는 프로그램

num1, num2 = map (int,input("정수를 입력하세요 : ").split())
print(num1,num2)

if num1 % num2 == 0 :
    print(f'{num1}은 {num2}의 배수입니다.')
else :
    print(f'{num1}은 {num2}의 배수가 아닙니다.')