list1 = [22,99,7,6,44,66,83,5,677,33]

'''이렇게 만들어보자 !
[7, 6, 44, 66, 83, 5, 677]
[6, 44, 66, 83, 5, 677]
[44, 66, 83, 5, 677]
[66, 83, 5, 677]
[66, 83, 5, 677]
[83, 5, 677]
[5, 677]
[677]'''

end = len(list1) #1.  list의 길이를 end에 대입한다.

for i in range(end) : #2.  i에 0부터 end의 길이의 값까지 저장
    print(list1[:i], list1[i:]) #[:i] 로 처음부터 i까지
    #list[0~끝까지] 슬라이싱, 출력하기
   # print(list1[i:]) #  == > 첫번째 요소들이 반복문을 돌며 슬라이싱 되고 새로운 리스트로 출력

    #슬라이싱 된 리스트의 최솟값을 찾는다.
    min_v = min(list1[i:]) #min대신 max를 쓰게되면 내림차순
    min_ix=list1[i:].index(min_v)+i
    # print(min_v, min_ix)

    #list[i]와 list[min_ix]의 값을 교환하기
    list1[i],list1[min_ix] =list1[min_ix],list1[i]#언패킹을 이용
print(list1)#오름차순 정렬되어 출력된다.


'''합계와 평균을 구하는 함수'''
def calc(numbers):
    size = len(numbers)
    total = sum(numbers)
    avg = total / size

    return  total , avg#튜플을 리턴

#합계 : xxx, 평균 : xxx로 출력하기
t , a =calc(list1)
print(f'합계 : {t}, 평균 : {a}')
