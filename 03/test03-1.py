
#문제 3-2 // 키가 140cm 미만이면 탈 수 없는 놀이기구. 이름과 키를 입력받아 탈 수 있는지 없는지 출력하는 프로그램
name = input("이름을 입력하세요 : >")
hight = int(input("키를 입력하세요 (cm) : > "))
age = int(input("나이를 입력하세요 : >"))
if hight >=140 :
    str = "있습니다."
else : 
    str = "없습니다."

print(f'{name}님은 놀이기구를 탈 수 {str}')

#문제 3-3 // 나이19세, 키 150cm이상이면 탈 수 있는 성인 놀이기구 . 이름과 키를 입력받아 탈수 있는지 없는지 출력하는 프로그램
    #단, and 들어가야함


if hight>=150 and age > 19 : 
    str = "있습니다."
else :
    str = "없습니다."

print(f'{name}님은 입장 할 수{str}')

#문제 3-4 나이룰 압룍벋어 20살 이상이면 'adult' , 10-20살미만 'yoyth' , 10살 미만이면'kid'를 출력하는 프로그램
    #단, if-elif-else문 사용
if age>=20:
    str = 'Adult'
elif 10<=age<20 :
    str = "Youth"
else :
    str = "Kid"
print(f'{name}님은 {str}요금 입니다.')