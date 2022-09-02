from functools import total_ordering


n = int(input('합계를 구할 수를 입력하세요'))
total=0
for i in range(n+1) : 
    total += i
print(f'1부터 {n}까지의 합은 : {total}')


for i in range(2,10):
    for j in range(1,10):
        print(f'{i}x{j}={i*j:2d} ',end=' ')
    print()

for i in range(7):
    st = ''
    for j in range(i):
        st+=' '
    print(st+"#")

for i in range(7):
    st = ''
    for j in range(i):
        st+='#'
    print(st)