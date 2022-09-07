import sys
fname = input('입력할 파일 이름 : ')
try : 
    f= open (fname,'r', encoding='UTF-8')
except IOError :
    print('not read file :',fname)
    sys.exit() #강제종료
except :
    print("err ", sys.exc_info()[0])
    sys.exit()
