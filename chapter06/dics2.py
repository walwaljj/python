#무한루프를 돌면서 검색어를 입력
#검색어로 exit를 입력하면 루프종료

#검색어의 검색 회수 관리 :어떤 검색어가 있는가 = 리스트
                    #    + 검색어의 횟수까지 관리 = 사전 key : 검색어 , value : count 

keywords = {}

count = 0
while True :
    keyword = input('검색어를 입력하세요 : ')#key값을 입력받는다.
    if keyword == 'exit' :#key가 exit면
        
        break               # 루프종료
    
    keywords[keyword] = keywords.get(keyword,0) +1 # 
   #dict[key]=value : 해당 키에 값을 입력, 수정한다. 
    #.get(key)는 해당 키의 값을 반환한다. 해당 key가 없으면 0을 반환하라는 뜻
    # +1은 dict[key]= 1..+1..+1.. 등 입력했었던 key에 대해 루프문을 돌며 값을 +1시키라는 뜻
    
    #정렬 , 상위 10개 추출 : 실시간 인기검색어
    


for keyword, count in keywords.items():#.items는 키 : 값 을 반환.. 언패킹을 이용해서 keyword : count순으로 저장
    print(f'{keyword} : {count}')