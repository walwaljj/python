name = input('이름입력 :')
print('이름 :',name)

age = int(input('나이 입력 :'))# 형변환 안하면TypeError: can only concatenate str (not "int") to str : 문자열만 결합할수있다. 구말
print('10년 후 나이 :', age + 10)

a=15
print(10<a<40)
