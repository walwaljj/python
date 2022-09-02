
from xml.dom.minidom import Document



line = 5

for i in range(line) : #line의 index가 i에 0 부터담김
    for k in range(line-(i+1)):#공백을 출력할 횟수를 k에 담는데
                                #5,횟수를
        print(' ',end='')
    for j in range(i*2+1):
        print("+",end='')
    print()

n=int(input("숫자를 입력하세여 :"))

is_prime = True
for num in range(2,n):
    if n % num == 0:
        is_prime = False
print(n,'is prime : ', is_prime)



for num2 in range(2,101):
    is_prime2 = True
    for n2 in range(2,num2):
        if num2%n2==0:
            is_prime2 = False
    if is_prime2 :
        print(num2, end=' ,')
            
        
    
    
