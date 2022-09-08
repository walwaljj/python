import json

with open('myinfo.json','r',encoding='utf-8') as f:#파일에 한글이 사용되어 인코딩 설정해줘야함.
    data = json.load(f)

    print(type(data))
    print(data)
with open('myinfo.json','r') as f:
    json_str = f.read()
    data = json.loads(json_str)#load의 리턴값은 사전이기 때문에 들여쓰기 필요없음. 

    print(type(data))
    print(data)