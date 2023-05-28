#4-7 세 수의 평균, 최대, 최소를 반환하는 함수정의

a,b,c,d,e = map(int,input("다섯 수를 입력하세요 >").split(' '))

def mean3(a, b, c,d,e):
    return (a+b+c+d+e)/5
def max3(a,b,c,d,e):
    return max(a,b,c,d,e)
print(mean3(a,b,c,d,e))
print(max3(a,b,c,d,e))