

try :
    with open('sensors.csv','rt',encoding='UTF-8') as f :
        data = f.readlines()
        # data = [line.strip().split(',') for line in data]
        for row in data : 
            row = row.strip().split(',')
            print(row)
        # print(data)
except Exception as e :
    print(e)