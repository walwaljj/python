total = 0
for i in range(1,101):
    total +=i
    if total > 50:
        print(f'계산 중단, i = {i}, total = {total}')
        break

num = 20
for j in range(num):
    if j%2!=0:
        continue
    print(j)

numbers = [10,20,30,40,50]

s=0

for k in numbers:
    s+=k
print(f'총 합은 : {s}')

s=0
for k in numbers:
    s+=k
print(f'총 합은 : {s} , 평균은 : {s/(len(numbers))}')

for ix,i in enumerate(numbers):
    print(ix,i)