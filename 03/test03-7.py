#1-10사이 복권번호중 3개를 맞히면 1억
#2개를 맞히면 1천
#1개를 맞히면 1만원
#모두틀리면 다음기회를 출력하는 복권시스템

a,b,c = map(int, input("세개의 복권번호를 입력하세요 : >").split())

num = [2, 3, 9]
count = 0
for i in num :
    print(i, end=' ')
    if a == i or b == i or c == i : 
        count +=1
print()
print(f'맞는 갯수 : {count}')

str = " "
if count == 1 :
    str = "상금 : 1만원"
elif count == 2 :
    str = "상금 : 1천만원"
elif count == 3 :
    str = "상금 : 1억원"
else :
    str = "다음 기회에.."

print(f'{str}')