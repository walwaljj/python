#3-20 for문을 사용해 삼각형 출력하는 프로그램.

line = int(input("숫자를 입력하세요 : > "))

for n in range(1,line+1):
    print(n*'*')
    for n2 in range(line+1,-1):
        print(n*" ",end=' ')

#3-21 소수인지 아닌지 판별하는 프로그램

for n3 in range(2,line) :
    if n3%(n3-1)==0:
        print(f'{line}은 소수가 아닙니다.')
        
    elif n3%(n3-1)!=0 :
        print(f'{line}은 소수입니다.')
        