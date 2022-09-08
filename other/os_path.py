import os

file_path = '정리.txt'

print(os.path.isabs(file_path))# 상대경로 '.' --> false
                                #절대경로 'c:/temp' --> true
print(os.path.abspath(file_path))#절대경로로 변경함 C:\python\temp(현재path 기준으로 변경. 파일존재여부 안함.)
print(file_path)
print("존재여부 : ",os.path.exists(file_path)) #path기준 파일존재안함 ==> false
print('파일여부 : ', os.path.isfile(file_path))#찾고자 하는것이 파일인지 아닌지를 확인
print('디렉토리여부 : ', os.path.isdir(file_path))#isfile과 배타적임. isdir ? <DIR> : ' ' 등 응용
print('파일 크기',os.path.getsize(file_path))

file_path= os.path.join('a','b','c','test.jpg')
print(file_path)