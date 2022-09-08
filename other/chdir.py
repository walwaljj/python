import os

os.chdir('.')#한다해도 터미널의 경로가 바뀌지않음. 원래 python ->chdir 후-> python 
wd = os.getcwd()
print(wd)