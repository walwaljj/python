#3-14 알파벳 입력받고 a,e,i,o,u일때 모음 아니면 자음

arr = list('aeiou')
print(arr)
al = input("알파벳을 입력하세요 : ")
for a in arr :
    if a==al :
        str = "모음입니다."
        break
    else :
        str = "자음입니다."
print(str)
