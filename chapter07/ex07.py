# from mypck.calc import add,multi#현재 작성 폴더 기준(chapter07)으로 작성해야함. 다른챕터에 가면 폴더 못찾음.
from mypck.calc import * #==> mypck.calc에있는 모든모듈을 뜻함
# 버전상의 문제로 *사용불가 --> __init__에 __all__ = ['add','multi'] 추가해 사용할수있다.
#ㅠㅐ키지 쓸때 from
#구분은 .

#C:\ProgramData\Anaconda3\Lib 에 많은 모듈을 볼 수 있음.

#from mypack.calc.add import outadd -- 가능
add.outadd(1,2)
multi.outmulti(1,2)