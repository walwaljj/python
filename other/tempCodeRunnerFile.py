for dir, fnames in category_images.items():#저장한 사전에서 키와 값을 얻기위해 반복문
#                                             #.items는 키,값을 준다.
#     for fname in fnames : #키값이 fname에 리스트로 저장되어 fname요소들을 하나씩 출력할예정
#         print(dir,fname) #위에서 받은 키값과 fname을 출력해봄cat cat1.png cat cat2.png...
#         file_path = path.join(base,dir,fname)#join으로 파일 디렉토리/디렉토리/파일 순으로 합치고 변수에 담음.
#         print(file_path)#파일의 경로를 만들어냄. images\cat\cat1.png 
