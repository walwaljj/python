person = {
    '이름' : '홍길동',
    '나이 ': 26,
    '몸무게' : 82
}

print(person['이름'])
#print(person['콩'])# KeyError: '콩'

person['이름']='콩길동'
print(person['이름'])

person['지역']='붓싼'
print(person)

del person['지역']
print(person)

#del person['남자친구']#    del person['남자친구']  없으니까,, KeyError: '남자친구'
#print(person)

print(len(person))

print('이름' in person)
print('직업' in person)
print(26 in person)

print(person.keys())
print(person.values())
print(person.items())

print(person['이름'])
print(person.get('이름'))
print(person.get('이름2'))

print(person.popitem())

person.pop('나이')
print(person)

