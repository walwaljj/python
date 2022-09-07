def greet(*names):
    print(type(names),len(names))
    for name in names:
        print("안녕하세요",name,"씨")

greet('홍길동,','양만춘','이순신')
greet()
greet('kim')
