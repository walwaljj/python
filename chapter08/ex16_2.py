from asyncore import read
from file_util import read_file_lines
fname = input("파일이름 >")#파일이름을 받아온다.
data = read_file_lines(fname)# 파일의 내용을 한 줄씩 읽어오는 함수에 매개변수를 전달 , data에 저장
for n , l in enumerate(data,1): #enumerate로 data의 인덱스값과 해당 인덱스의 내용을 받아옴.
                                #시작인덱스를 1로 지정해줌.
    print(f'{n:3d}:{l}')        #n에저장된 인덱스번호와 , 내용을 출력