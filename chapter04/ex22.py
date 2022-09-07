file_names=[
    'song1,mp3 ,100',
    'image1,JPG ,20',
    'image2,JPG ,30',
    'song2,Mp3 ,200',
    'video1,mp4,500'
]

#전달된 문자열 리스트 데이터를 #place, type, value키를 가지는 사전의 리스트로 변환하는 함수 load_data()를 만들기

def load_data(file_names):
    dict_list = []
    for line in file_names : #line의 데이터를 사전으로 변환할얘정
        row = line.split(',')
        data = {
            'place':row[0].strip(),
            'type':row[1].strip(),
            'value':int(row[2])
        }
        dict_list.append(data)
    return dict_list

dict_list = load_data(file_names)

print(dict_list)

for data in dict_list:
    print(data)