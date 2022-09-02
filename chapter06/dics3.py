article = ''' Most of us have experienced turbulence while traveling: when your plane flies through clashing bodies of air moving at widely different speeds.
Severe turbulence can put even the most seasoned flier on edge and make five minutes seem like an eternity. Usually it results in nothing more than a bumpy ride, but in the worst cases it can cause damages and injuries.'''

#문자열에 나오는 글자의 출현 횟수 계산하기

spel_count = {}#빈 딕셔너리 생성

for ch in article :#문자열은 리스트로 사용가능, ch에 요소를 하나씩담는다.
    # print(ch)
    spel_count[ch] =spel_count.get(ch, 0)+1 #ch값이 없으면 0 을 가져온다. 딕셔너리에서 dics[키] = 값 ..> 키가 존재하면 수정을 하고 없으면 추가한다.

# for i in range(10): #변수 i는 데이터의 성격을 담는다.

# for x in spel_count : 
#     print (x)# 키값=스펠링 을 반환한다.--> key와 value를 얻기위해 x[0],x[1]해야함 불편

#print(spel_count.items()) 

'''결과 : dict_items([(' ', 61), ('M', 1), ('o', 13), ('s', 21), ('t', 21), ('f', 7),
 ('u', 15), ('h', 10), ('a', 20), ('v', 6), ('e', 47), ('x', 1), ('p', 5), ('r', 16), 
 ('i', 23), ('n', 25), ('c', 8), ('d', 11), ('b', 5), ('l', 13), ('w', 4), ('g', 7), 
 (':', 1), ('y', 5), ('m', 8), ('.', 3), ('\n', 1), ('S', 1), ('k', 2), ('U', 1), (',', 1),
  ('j', 1)])'''#items는 키와 velue를 각각 튜플로 담는다.

for ch, count in spel_count.items():
    print(f'{ch} : {count}')

#정렬하기 
#1- 먼저 list로 형변환
ch_list = list (spel_count) #==ch_list = list (spel_count.keys()) -> 사전을 list로 형변환하면 키값이 담긴다
print(ch_list) 
'''결과 :[' ', 'M', 'o', 's', 't', 'f', 'u', 'h', 'a', 'v', 'e',
 'x', 'p', 'r', 'i', 'n', 'c', 'd', 'b', 'l', 'w', 'g', ':'
 , 'y', 'm', '.', '\n', 'S', 'k', 'U', ',', 'j']'''

ch_list.sort()#리스트를 정렬하는 메소드
'''sort(*, key: None = ..., reverse: bool = ...) -> None

sort(*, key: (Any) -> SupportsRichComparison, reverse: bool = ...) -> None'''


for key in ch_list:
    print(f'{key} : {spel_count[key]}')

#list(spel_count.values()) 벨류값뽑고 정렬가능 , 그러나 벨류에 대응하는 키값을 알 수 없다.
#  print(f'{key} : {spel_count[key]}')불가능.

items = list(spel_count.values())# 키와 values가 튜플로 들어있음.
print(items)

def what(x):
    # pass #정의 하지 않았지만 문법에러를 pass시키게 하는 키워드.
    # print(x)
    return x[1]# 두번째 요소로 정렬하겠다는 뜻 [0]이면 첫번쨰 ,즉 key값

items.sort(key=what, reverse=True)#매개변수=함수// list 에 담겨있는 값이 x에 전달됨. 함수가 리턴하는 값을 기준으로 엘리먼트를 정렬해준다.

# 단일데이터는 상관없지만 리스트 [안에 컬렉션이 들어있다.] 라면 첫번째 키값 기준으로 정렬이 된다 . 벨류값으로 정렬을 하고 싶다면

#items의 count가 값으로 정렬된다.
for ch, count in items:
    print(f'{ch} : {count}')

#[' ', '\n', '\'','\"', '.'] 이 문자열을 제외 하고 정렬하기
article = [ch for ch in article if ch not in [' ', '\n', '\'','\"', '.']]

#빈도수가 높은 앞 5개만 출력하고 싶을때 
for ch, count in items[:5]: # Top-N 문자 상위 N개만 추출함.
    print(f'{ch} : {count}')