f = open('data5.txt','w')
for _ in range(5) :
    n = input('정수를 입력하세요 : ')
    f.write(n)
    f.write('\n')
f.close()