def read_file_lines(fname) : #매개변수로 파일이름을 받음
    try :
        f=open(fname,'r')#받은파일을 열고
        data = f.readlines()#한줄씩읽어서 data에 담는다.
        data = [line.strip() for line in data]#담은 데이터를 line변수에 한 줄 씩 담고
                                                #list에 저장하는데 , 한줄의 마지막에있는 공백문자를 제거한다.
        return data #data를 함수 호출한곳으로 리턴한다.
    except Exception as e:
        print (e) #읽기에 실패했을때 에러메세지/
    finally :
        f.close()

data1 = read_file_lines('foo.txt')
print(data1)