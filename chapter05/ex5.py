n_list = [11,22,33,1,44,55,66]

#최소값을 찾아서 인덱스를 리턴하는 find_min()함수 작성하기
def find_min(n_list):
    #numbers에서 최소값을 찾아 그 인덱스를 리턴
    min_value = n_list[0]#n_list[] 의 값을 저장하는 변수
    min_index = 0 
    for ix,n in enumerate(n_list):
        print(n,min_value)
        if n < min_value: #최소값을 변경 

            min_value = n 
            min_index = ix
    return min_index

print(n_list)
min_index = find_min(n_list)
print(min_index, n_list[min_index])