#학점산출기

scr = int(input("내 학점은? : "))
str = ''
if((100<scr or scr<0)) :
    print('잘못된 점수')
else :
    if 90<=scr<=100 : 
        str = 'A'
    elif 80<scr<=90  :
        str = 'B'
    elif 70<scr<=80 :
        str = 'C'
    else : str="F"

    print("내 점수 : ", scr,"내 학점 : ", str)

#1에서 10까지 정수의 합 구하기

sum = 0

for i in range(11) :
    sum+=i
print(sum)
print(f'1부터 {i}까지 숫자의 합은 :{sum}')