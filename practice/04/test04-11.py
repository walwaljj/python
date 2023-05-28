#4-15 가변인수로 입력받고 오름차순으로 정렬해 출력하는 함수

def my_sort(*nums):
    a=[]
    for i in nums:
        a.append(i)
        a.sort()
    print(a)

my_sort(45,3,4,56,5)
my_sort(9,8,7,6,5,4,3)