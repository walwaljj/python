#5-7 리스트의 합을 구하는 함수

n_list=[10,20,30,50,60]
result = 0
for sum in n_list :
    result+=sum
print(result)

#5-8 리스트의 곱을 구하기
result = 1
for gop in n_list :
    result*=gop
print(result)

#5-9 리스트에서 가장 큰 값을 구하기
max = n_list[0]
for n in n_list :
    if n<=max :
        max = n
    else :
        break
print(max)