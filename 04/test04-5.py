#4-9 연속적인 숫자를 받아 통계


num=[]
num=(input("수를 입력하세요").split(' '))
ttl = 0
result = 0
def mean(num1):
    
    for i in num1:
        print(i)
        ttl+=i
    result= ttl/len(num1)
    return result

mean(num)
