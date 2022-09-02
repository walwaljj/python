#id /password 여러개 .. 무엇으로 보관할까?

'''
리스트로 저장한다면
[[id1, password1],[[id2,password2],...]
튜플로 한다면
((id1,password1),(id2,password2)...)
사전으로 한다면
{id1 : password1 , id2 : password2, ...}
'''


#로그인을 위해 아이디와 비밀번호 입력받기

from pickle import NONE




#=============================================
 #입력한 id에 대응하는 password?

'''리스트와 튜플이 라면 루프로 찾아야함.
사전은 바로 찾을 수 있다.'''



users={
    'hong' : '1234',
    'kim' : '2345',
    'lee' : 'abcd',
    'park' : 'ABCD'
}

#password = users[id] #id는 변수다 . id가 가지고 있는 값을 key로 하고 값을 password에 저장.
                      #그러나 없는 값에대해 err를 내기때문에 get을 사용하는게 더 좋다.

i = 0

for i in range(3):
    id = input('ID입력')
    user_password = input("비밀번호 : ")

    password = users.get(id)

    if not password: #id 유효성 검사 
        print('id가 존재하지 않습니다.')
    else :
        if user_password == password : #password값이랑 input으로 입력받을 비밀번호값이 맞는지 확인
            print('로그인 성공')
            break
        else :  
            print('로그인 실패')

    
          
        

