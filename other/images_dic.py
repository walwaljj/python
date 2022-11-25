import imp


import os 
from os import path

base = 'images'

'''

1. base 디렉토리의 내용 추출

2. value 내용추출 '''

images = {}

for dir in os.listdir(base):
    dir_path = path.join(base,dir)
    # print(dir,dir_path) # join 으로 images\cat images\dog 만들어냄.
    
    images[dir]=os.listdir(dir_path)# images\cat images\dog 의 listdir = 디렉토리의 리스트, xx.png

print(images)