#3-23 양의 정수 n 을 입력받고 1*1+2*2+3*3+4*4.. 구하는 프로그램
                            #(1+2+3+4)(1+2+3+4)
n = int ( input("정수를 입력하세요. > "))
ttl = 0
even = 0
for num in range(1,n+1) :
    # print(num)
    ttl += num**2
    even += (1/num)**2
print(ttl)
print(even)
