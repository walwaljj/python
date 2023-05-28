for n in range(100,1000):
    a=(n//100)**3
    b=((n%100)//10)**3
    c=(n%10)**3
    if a+b+c == n:
        print(n)

