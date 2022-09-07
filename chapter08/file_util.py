def read_file_lines(fname):
    try :
        with open(fname,'r',encoding='UTF-8') as f:
            data = f.readlines() # 반복문을 대신해 문서가 끝날때 까지 한줄씩 읽음.==> 리스트형
            data = [line.strip() for line in data] #한줄씩 읽은 문장 반복문을 돌며 공백제거 후 다시저장
        return data
    except Exception as e:
        print('err :', e)

if __name__ == '__main__':
    data= read_file_lines('foo.txt')
    print(data)