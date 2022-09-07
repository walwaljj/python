#3-8 사용자로부터 x,y좌표를 가진 한 점을 입력받아서 이 점이 분명의 어디에 속하는지 알려주는 프로그램을 작성하시오 


def xy(x,y):
    if x > 0 :
        if y>0 :
            print("1사분면")
        else :
            print("4사분면")
    else :
        if y<0 :
            print("3사분면")
        else : 
            print("2사분면")
    print(f'x좌표 : {x} / y좌표 : {y}')

xy(10,20)
