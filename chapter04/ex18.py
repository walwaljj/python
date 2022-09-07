def sum_nums(*numbers):
    result = 0
    for n in numbers:
        result +=n
    return result

print(sum_nums(10,20,30))
print(sum_nums(10,20,30,40))

n_list = [10,50,44,86,90]

#sum_nums(n_list)#int랑 list결합은 안된다.
#호출시 변수 하나(list)를 넘긴것과 같다.

print(n_list)#하나의 list가 프린트 됨.
print(*n_list)#5개의 값이 프린트됨 / 자바스크립트의 [...arr,...arr2]와 같다.

print(sum_nums(*n_list))#*list는 펼침연산자

n_list2 = [*n_list,100,101]
print(n_list2)

