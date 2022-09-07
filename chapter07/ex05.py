import time as t
start_time = t.time()
sum = 0
for i in range(10):
    sum+=i
print(sum)

end_time = t.time()

gap = end_time -start_time

print(f'1에서 10까지의 합을 구하고 출력하는 시간 :{gap:7.4f}초')
#총 7자리 중 소수점 이하 4자리 출력하라는 뜻