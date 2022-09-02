from re import I


i = 0 
while i < 5 :
    print('welcome')
    i +=1

n = int(input('합계구할수 : '))
total = 0
i = 1
while i <= n :
    total += i
    i +=1
print(f'1부터 {n}까지의 합계는 {total}입니다.')