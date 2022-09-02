n = int(input('수를 입력하세요 : '))

is_prime = True
for num in range(2,n) :
    if n % n==0 :
        is_prime = False
        break
print(f'{n}은 프라임수일까? {is_prime}')