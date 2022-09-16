#4-9 연속적인 숫자를 받아 평균,최소,최대값구하기


num=[]
num=input("수를 입력하세요").split(' ')

def mean(*num1):
    ttl = 0
    result = 0
    for i in num1:
        for j in i :
            j = int(j)
            ttl +=j
            result = ttl/len(i)
    return print(f'평균값 : {result:.1f}')
        # ttl+=int(i)
    # result= ttl/len(num1)
    # return result
def max_of(*num1):
    maxN = 0
    for i in num1 :
        for j in i :
            # print(j)
            maxN = max(i)
    return print(maxN)
        # maxN = max(int(i))
    # return  print(maxN)
# mean(num)
max_of(num)
