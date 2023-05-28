#4-9 사용자로부터 수를 연속적으로 입력받고 , 평균값, 최댓값, 최소값을 반환하는 함수를 구현하기



import enum


nums=[]
nums=map(int,input("정수를 여러개 입력하시오 : >").split(' '))

men = 0
print(nums)

def mean_of_n(*li) :
    for ix, n in li :
        men = sum(n)/ix
    return men
mean_of_n(nums)