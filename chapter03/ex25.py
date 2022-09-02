#팩토리얼 구하기 
#n*n-1*n-2*n-3...

n = int(input('수를 입력하세요 : '))
fact = 1

for num in range(n) :
    fact *=n-num
print(f'{n}! = {fact}')

#구구단 만들기
dan = int(input('단을 입력하세요 : '))
# for i in range(dan):
for j in range(1,10) :
    print(f'{dan}*{j}={dan*j:2d}',end=' ')
print()

# #찍기
star = ' '
for shap in range(0,7):
    star+=' '
    print(star,'#')