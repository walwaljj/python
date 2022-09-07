INCH = 2.54

def calcsum(n):
    sum = 0
    for num in range(n+1):
        sum +=num
    return sum
print(__name__)#main
print('util.py')
print('module name : ' , __name__)

if __name__ == "__main__":#단독으로 자체 실행했다면
    #(모듈 테스트코드)
    print(calcsum(10))
    print(calcsum(10))


