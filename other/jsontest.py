import json

data = {'name': '홍길동','birth': '0525','age': 30
    }
with open('myinfo.json', 'w', encoding='utf-8') as f:#encoding 설정
    json.dump(data, f,indent=2,ensure_ascii=False)# indent 는 들여쓰기 , ensure_ascii=False 아스키코드가 아닐수도있다는 설정해주기

json_str = json.dumps(data,indent=10,ensure_ascii=False)
print(json_str)