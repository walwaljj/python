file_names=[
    'song1.mp3',
    'image1.JPG',
    'image2.JPG',
    'song2.Mp3',
    'video1.mp4'
]
#전달된 파일명 리스트에서 mp3파일만 담긴 튜플을 반환하는 함수 find_song 만들기

#튜플로 먼저변환하게 되면 튜플은 내용수정불가라 lower처리 불가함.
#먼저 lower처리를 list로 해주고 내용을 변수에담아준다.
#변수에 담은것을 tuple로 변환해주기

find_s=tuple(file_names)
print(find_s)

def find_song(names):
    songs=[]
    for name in names :
        test_name = name.lower()
        if test_name.endswith('.mp3'):#.mp3로 끝나는 것들을 추림
            songs.append(name)

    return tuple(songs)

songs = find_song(file_names)

for song in songs :
    print(song)