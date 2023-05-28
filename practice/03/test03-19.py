#3-28 n숫자를 입력받아 이 수가 거꾸로정수인지 아닌지 판단하는 프로그램 만들기

num = input("정수를 입력하세요 : >")
rnum=False
for n in range(len(num)) :
    if num[n] == num [len(num)-(n+1)] :
        if n>=len(num)-(n+1) :
            rnum=True
            break
    else :
        rnum = False
        break
print(rnum)
        