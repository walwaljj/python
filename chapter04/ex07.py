

def get_sum(a=10,b=40):
    return a+b

print(f'{get_sum(10,20)}')

n = get_sum(10,30)
print(n)

n1=get_sum()
print(n1)


def get_sum(a=10,b=40):
   a+b# 위와다르게 리턴타입을 안줌.
n2 = get_sum(1,2)
print(n2)# 호출시 결과는 none이다. ==> 값이 없다.(js에서 undefined) 인터프리터언어에서는 에러는 아님.