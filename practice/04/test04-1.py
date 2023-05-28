def my_greet():
    print("환영합니다.")

my_greet()
my_greet()

#4_2.n이라는 이름의 매개변수를 입력받아 값의 제곱을 반환하는 함수정의

def square(n):
    return n**2

print ('3의 제곱은 : ',square(3))
print ('4의 제곱은 : ', square(4))

#4_2. m과 n 이라는 이름의 매개변수 두개를 입력받아 이 두값중 큰 값을 반환하는 max2함수와
#       작은값을 반환하는 mon2함수를 구현



def max2(m,n):
    if m>n :
        return m
    else : 
        return n
def min2(m,n):
    if  m<n :
        return m
    else : 
        return n
print("큰 수 : ",max2(100, 200))
print("작은 수 : ",min2(100, 200))