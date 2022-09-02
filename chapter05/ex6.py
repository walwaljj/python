from msilib.schema import TypeLib


list1 = [10,20,30,40,50]
i=0
for n in list1 :
    list1[i] = n *10
    i = i+1

print(list1)
list2 = [10,20,30,40,50]

for x,n in enumerate(list2) : #n은 엘리먼트, x는 인덱스 잘 기억해두기
    list2[x] = n*10#n은 엘리먼트기 때문에 list2[n]하면 인덱스범위를 벗어난다. 
print(list2)

list1=[n * 10 for n in list1]

print(list1)

tuple = 1,2,3,4
print(tuple)
#tuple[0]=10  'tuple' object does not support item assignment
tuple[1]
print(tuple[0])

list1.append('a')
print(list1)
list3=[n for n in list1 ]
print(list3)