#5-11
num = input("num을 입력하세요")
n_list = []
n_list = (input(f"{num}개의 수를 입력하세요 : ").split(' '))
print(n_list)

n_list = [int(n) for n in n_list]
print(f'원소 : {n_list} \n 합 : {sum(n_list)}\n 평균 : {sum(n_list)/len(n_list)}\n 최소값 : {min(n_list)}\n 최대값 : {max(n_list)} ')
sum(n_list)
min(n_list)
max(n_list)

avg=(sum(n_list)/len(n_list))
ttl=sum(n_list)
length = len(n_list)
# sd=(((ttl-avg)**2)/len(n_list))**0.5
nsd = 0
for i in n_list :
    nsd += ((i-avg)**2)/length

print(nsd**0.5)