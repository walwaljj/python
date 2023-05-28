#4-17 n1에서 n2까지 정수의 합을 구하는함수 sum_range(n1,n2) 모든 숫자 출력문에 플레이스 홀더사용

def sum_range(n1,n2):
    ttl =0
    sum_n1 = 0
    sum_n2 = 0
    for i in range(1,n1):
        print(i,end=" ,")
        sum_n1 += i
    print()
    for j in range(1,n2+1):
        print(j,end=" ,")
        sum_n2+=j
    ttl=sum_n2-sum_n1
    print()
    return print(ttl)
sum_range(10,20)
sum_range(40,100)