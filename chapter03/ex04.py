number = int(input("정수를 입력하세요 :"))

if(number % 3 ) == 0 and (number % 5 ) == 0:
    print (number , ' 은 3의 배수이면서 5의 배수입니다.')
else : print (number,'는 조건에 부합하지 않습니다.')