#무한루프를 돌면서 검색어를 입력
#검색어로 exit를 입력하면 루프종료

#검색어의 검색 회수 관리 :어떤 검색어가 있는가 = 리스트
                    #    + 검색어의 횟수까지 관리 = 사전 key : 검색어 , value : count 

keywords = {}

count = 0
while True :
    keyword = input('검색어를 입력하세요 : ')
    if keyword == 'exit' :
        
        break
    
    keywords[keyword] = keywords.get(keyword,0) +1 #중요!
    # key가 없으면 0을 달라는 말 그리고 검색 횟수를 +1시킴
    
    #정렬 , 상위 10개 추출 : 실시간 인기검색어
    


for keyword, count in keywords.items():
    print(f'{keyword} : {count}')