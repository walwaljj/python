import imp,pickle


import os 
from os import path

base = 'images'

'''

1. base 디렉토리의 내용 추출

2. value 내용추출 '''

def get_category_images(base):
    images = {}

    for dir in os.listdir(base):
        dir_path = path.join(base,dir)
        # print(dir,dir_path) # join 으로 images\cat images\dog 만들어냄.
        images[dir]=os.listdir(dir_path)
    return images

def save (fpath,data) :
    #save('category.dat',category_images)매개변수로 파일명,위 함수로 인해 파일명이 담긴 객체
    try :
        with open(fpath,'wb') as file :#첫 인자인 파일을 w로 오픈, 별칭을 file로 줌.
            pickle.dump(data,file)#피클.dump로 두번쨰 인자data내용을 첫 인자로 받은 파일객체fpath에 저장?
    except Exception as e:
        print(f"{fpath} 파일쓰기 실패")
        print(e)

def load(fpath):#파일을매개변수로받음
    try :
        with open(fpath, 'rb')as file :#읽을 파일을 오픈하고 별칭을 file로 줌
            data = pickle.load(file)#pickle.load의 매개변수로 파일
            return data
    except :
        print(f"{fpath}파일 읽기에 실패했습니다.")

# category_images = get_category_images(base)#함수에서 사전을 리턴받아 category_images에 저장.

# for dir, fnames in category_images.items():#저장한 사전에서 키와 값을 얻기위해 반복문
#                                             #.items는 키,값을 준다.
#     for fname in fnames : #키값이 fname에 리스트로 저장되어 fname요소들을 하나씩 출력할예정
#         print(dir,fname) #위에서 받은 키값과 fname을 출력해봄cat cat1.png cat cat2.png...
#         file_path = path.join(base,dir,fname)#join으로 파일 디렉토리/디렉토리/파일 순으로 합치고 변수에 담음.
#         print(file_path)#파일의 경로를 만들어냄. images\cat\cat1.png 
# 
category_images = get_category_images(base) #cat1.png...
save('category.dat',category_images)

data = load('category.dat')
print(type(data))#dict
print(data)

