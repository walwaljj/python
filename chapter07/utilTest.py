import util#모듈을 이용 . 모듈 : 다른파일에서 import했을때 --> 그때 모듈이됨.

# print('ex06.py')#단독으로 실행된 이름은 파일명과 상관없이 __name__ 
# print("module name:",__name__)

print("1inch = " , util.INCH)
print("~10",util.calcsum(10))

#모듈로 실행되고있어 실행안됨
'''if __name__ == "__main__":#단독으로 자체 실행했다면
    #(모듈 테스트코드)
    print(calcsum(10))
    print(calcsum(10))
'''
