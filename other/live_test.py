import shutil,os

shutil.copy("live.txt","live2.txt")

answer = input("live2.txt를 삭제할까요 ? [Y]/N >").lower()#lower나 upper로 형변환하여 대문자나 소문자어떤값이 오던 상관없게
#input시 y 만쳐도 아래 조건문이 먹힘 --> y\n이 입력되지만 y만 리턴 않음 --> input에서 \n은 생략시켜주고 엔터만 쳤을때 공백이 반환
#print(answer.lower())--> 파이썬의 문자열은 한번 배정된 이후 변경될 수 없다. 그래서 input과 동시에 lower()
#print(answer)==> 위에서 lower 해도 여기서 출력시 Y
if answer == "y" or "" :# [Y]로 엔터만 쳐도 삭제하게 '' 공백문자를 줌. 그러나 다른 키입력이 들어가면 삭제안됨, \n은 삭제
    os.remove('live2.txt')
    print("삭제합니다.")
else :
    if answer == "n" :
        print("삭제를 취소합니다.")
    else:
         print("잘못 입력했습니다.")

