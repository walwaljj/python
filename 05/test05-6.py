#5-17

animals = ['dog', 'cat', 'tiger', 'lion']
print(f'animals = {animals}')

pop1 = animals.pop(0)

animals.append(pop1)
print(f'animals = {animals}')

for ani in animals :
    print(f'I love {ani}')

s_list = ['abc','bcd','bcdefg','abba','cbbc','opq']
result=[]
min_len=len(s_list[0])
for ix,i in enumerate(s_list) :
    if len(s_list[ix]) <= min_len :
        min_len = len(s_list[ix])
        result.append(i)
result.sort(key=len)    
print(result)
# print(i)

