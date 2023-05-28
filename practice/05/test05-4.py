#5-7 리스트의 원소를 합하는 프로그램

n_list = [10,20,30,50,60]
sum = 0
gop = 1
for n in n_list :
    sum += n
    gop *= n
print(sum)
print(gop)