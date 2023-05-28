#6-8 튜플의 중복원소를 집합에 넣기

tup=(1,2,5,4,3,2,9,1,4,7,8,9,9)
dup=set()
for n in tup :
    if tup.count(n) !=1:
        dup.add(n)
print(dup)

#6-9 튜플의 중복요소를 없게 튜플을 수정하기

tup2=(1,2,5,4,3,2,1,4,7,8,9,9,3,7,3)

tup2=set(tup2)
print(tup2)

#6-10 튜플에서 가장많이 나타나는 요소를 출력

tup3=(1,2,5,4,3,2,1,4,7,8,9,9,3,7,3)
max_n=0
for n2 in tup3 :
    if tup3.count(max_n) <= tup.count(n2) :
        max_n=n2
    

print(max_n)
        