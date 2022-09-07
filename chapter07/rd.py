import random
#파일명이 random일때 시스템적으로 자기자신을 먼저 경로에서 찾기때문에 에러남
#import시 자기자신을 import하지않고 내장함수를 쓰게 이름을 다르게해줘야함.

print(random.randrange(1,10))