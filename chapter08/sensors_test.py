

from datetime import date, datetime
from time import strptime
from unittest import result

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

try :
    with open('sensors.csv','rt',encoding='UTF-8') as f :#현재 파일이 프로젝트에 있음, chapter08로 변경해 넣으면 cd chaoter08로 경로 이동도 해줘야함.
        
        ##################################################################################여기서부터
        data = f.readlines()
        
        result = []
        for row in data[1:] : 
            row = row.strip().split(',')#row의 참조가 변경됨.
            #####################################################################여기까지 해주는 csv모듈이 있음
            row[0]=int(row[0])
            row[3]=float(row[3])
            row[4]=datetime.strptime(row[4],DATE_FORMAT)
            result.append(row)
            # print(row)
        #*******************************여기까지 pandas라는 형변환까지 해주는 툴이 있다.
        
        #---------------------------------------------------------------------
        # header, data = data[0], data[1:]
        # print(header)#현재 header는 문자열
        # print(data) # =(data)
        #---------------------------------------------------------------------
        # print(result)
        header, data = data[0].strip().split(','), result
        print(header)
        print("="*50)
        for row in data : 
            print(row)
except Exception as e :
    print(e)