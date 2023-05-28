#4-14 3개의 숫자를 입력받고 숫자를 오름차순으로 출력하는 테스트프로그램


num1,num2,num3 = map(int,input("세 수를 입력하세요 ").split(' '))

def sort3(num1,num2,num3):
    a=[]
    a.append(num1)
    a.append(num2)
    a.append(num3)
    a.sort()
    for num in a:
        print(num,end=' ')

sort3(num1,num2,num3)