f=open('data5.txt','r')
su = 0
for _ in range(5):
    n = int(f.readline())
    su +=n
print(f'다섯 숫자 합 = {su}, 평균 = {su//5}')
f.close()