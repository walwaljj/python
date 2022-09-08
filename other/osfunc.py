import os

def dumpdir(path):#파일을 매개변수로받아옴.
    files = os.listdir(path)#os.listdir('.')#현재 워킹 디렉토리의 목록을 전부 받아옴 
    for f in files :#받아온 파일을 for를 돌며 f에 저장
        fullpath = os.path.join(path , f)#join을 통해 매개변수로 받은 파일이름과 f의 파일이름을 구분자 / 로 합침
        if os.path.isdir(fullpath): #합쳐진 파일이름을 isdir로 디렉토리인지 검사 , 디렉토리가아니라면 else로 감.
            print(f'{fullpath}') # 디렉토리명을 출력
            dumpdir(fullpath)# 여기서 재귀호출 --> 매개변수로 디렉토리명이 들어감. 
                            #os.listdir('디렉토리명')이되어 반복문을 수행하다가 가장 마지막 하위목록이 else문의 print가 완료 되면 끝남. 
        else :
            print('\t'+f)#fullpath가 파일일때 프린트함.
dumpdir(".")