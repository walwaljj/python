#섭씨온도를 매개변수로 받아 화씨로 반환하는 함수 
#함수 호출해 섭씨 10도에서 50도단위로 10도씩변화시켜 결과를 화씨로 출력
#섭ㅆㅣ -> 화씨 fahrenheit = (9/5) * celsius +32

def cel2fah(cel) :
    for n in range(cel,60,10) :
        fah = (9/5) * n +32
        print(f'섭씨 {n} 도 = 화씨 {fah}')


cel2fah(10)