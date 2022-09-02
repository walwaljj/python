import numbers


num = [10,20,30,40,50]

s=0
avg = 1
for n in num : 
    s+=n

print('리스트의 항목 합 : ',s,'리스트의 평균 : ', s/len(num))


sr = "Hello"
list(sr)
for ch in sr :
    print (ch)

for ch in 'Hello' : 
    print (ch , end = ' ')