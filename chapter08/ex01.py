from unittest import result


try :
    a,b = input("수 입력 : >").split()
    result = int(a) / int (b)
   
except ZeroDivisionError:
    print ('분모가 0')
except TypeError :
    print("타입에러")
else :
    print("잘했어요!")
    print(f'{a}/{b}={result}')
    