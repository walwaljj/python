#5-4 리스트의 순서를 바꾸는 기능 for-in , pop()이용 . reverse()없이

a = [2,3,4,5,6]
rev_a = []
for i in range(len(a)) :
    rev_a.append(a.pop())

print(rev_a)

#5-5 리스트를 조합하여 출력
list1 = ['I like','I love']
list2 = ['pancakes.','kiwi juice.','espresso']

for l1 in list1 :
    for l2 in list2 :
        print(f'{l1} {l2}')

