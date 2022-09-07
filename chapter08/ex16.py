fname = input('입력할 파일의 이름: ')
f= open(fname,'r')#입력받은 파일을 'r' 읽기모드로 f에저장
n = 1               #라인출력을 위해 변수 선언
l = f.readline()    #파일 한줄씩 읽을 변수l선언
while l :           #읽을 줄이없다면 공백을 반환 : 공백은 false, 반대는 true로 while적용가능
    print (f'{n:3d}:{l}') #라인번호 (숫자를 위해 3칸을 비움. n이출력되고 남는자리는 공백으로 채움)
                            #입력받은 l을 출력
    n+=1                #라인번호를 1씩증가시킴
    l=f.readline()      #다음 라인을 읽음

f.close()