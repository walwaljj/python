def print_star(n):
    for _ in range(n):
        print('*****')

print_star(2)

def print_ch(n , ch) :
    for _ in range(n):
        print(ch*3)

print_ch(2,"q")
print_ch(1)#  missing 1 required positional argument: 'ch ch를 더 해야한다고..
print_ch(3,"w",1)# positional arguments but 3 were given 매개변수를 잘못주면 이렇게나옴.