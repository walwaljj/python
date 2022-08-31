

for i in range(5):
    print(i, end = ' ')

for i in range(5):#7번에서 줄바꿈이 일어나지 않음.
    print(i)

print(1,2,3,4,5)
print(1,2,3,4,5, sep = '와',end="....") #sep = '문자' 로 스페이스가 아닌 다른문자로 변경. 

print()

sum = 0
for i in range(0,11,2):
    sum +=i
print (sum)
