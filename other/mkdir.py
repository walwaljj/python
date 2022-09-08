import imp


import os,shutil

# os.mkdir('images')
# os.mkdir('images/dog')#이미있으면 err남 , 하위 폴더를 만드려면 상위폴더가 존재해야함. 동시에 만들기 불가

# os.rmdir('images/dog')#path 기준 부모폴더 / 하위폴더 로 적어야함. dog만하면 path가 파일을 못찾음(현재 wkd python임)
# os.rmdir('images')#없으면 err
# shutil.rmtree("images") #하위 폴더가 있어도 해당 디렉토리와 하위내용을 모두 삭제 할 수 있다.

files = os.listdir('.')#현재 워킹 디렉토리의 목록을 전부 받아옴 
for f in files:
    print(f)# 이름이 정렬되어 출력됨

print(files)