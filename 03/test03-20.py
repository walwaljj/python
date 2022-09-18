#3-29 초기연료 500인 자동차연료 . 주행하면 연료가 줄어들고 충전하면증가.
#       반복문을 이용해 총전, 사용연료를 입력받아 남은양을 계속출력, 연료가 10%미만이면 경고출력

full = 500

ttl_full=full

while True :
    n = int(input("충전 또는 사용한 연료를 +/- 기호와 함께 입력하시오: >"))
    
    if full > n :
        ttl_full = ttl_full+n
        print( f'현재 탱크 양은 {ttl_full}입니다.' )
        if full*0.1 > ttl_full :
            print("경고 : 연료가 10% 미만이니 충전하세요!")
            break

