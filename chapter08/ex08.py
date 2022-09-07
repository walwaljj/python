def get_ans(ans):
    if ans in ['예','아니오']:
        print('정상적인 입력입니다.')
    else :
        raise ValueError("입력확인 필요")#예외를 발생시키고 try문을 벗어남. -> while이라 반복

while True:
    try:
        ans = input("예 / 아니오 ")
        get_ans(ans)
        break
    except Exception as e:
        print(e)