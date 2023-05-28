#4-13 도형 부피구하기
'''
정육면체 n**3 
직육면체 n1*n2*n3
원뿔 3.14/3*r**2 *n2 '''

def cm3(s=0,w=0,h=0,l=0,r=0):
    if s>0:
        print (s**3)
    elif l>0 and w>0 and h>0 :
        print (w*h*l)
    elif r>0 and h>0 :
        answer = input('원뿔인가요[1] , 원기둥인가요[2] ? >')
        if answer =='1':
            print(3.14/3*r**2*h)
        else :
            print(3.14*r**2*h)
    elif r>0 :
        print(3.14*4/3*r**3)
    
cm3(s=12)
cm3(s=20)
cm3(w=3,h=5,l=6)
cm3(r=20,h=10)
cm3(r=15)
cm3(r=20,h=10)