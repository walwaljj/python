#4-10 두 점을 입력받아 거리를 구하는 distance(x1,y1,x2,y2)함수 구현

x1=int(input("x1 좌표를 입력하시오 : "))
y1=int(input("y1 좌표를 입력하시오 : "))
x2=int(input("x2 좌표를 입력하시오 : "))
y2=int(input("y2 좌표를 입력하시오 : "))
def distance(x1,y1,x2,y2):
    return print((((x1-x2)**2)+((y1-y2)**2))**0.5)

distance(x1,y1,x2,y2)

def area(x1,y1,x2,y2):
    # print((((x1-x2)**2)+((y1-y2)**2))**0.5)
    wi= x1-x2
    hi= y1-y2
    trag = (wi*hi)/2
    return print(trag)
area(x1,y1,x2,y2)