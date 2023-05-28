#4-4 km를 mile로 바꾸는 함수 , 1마일은 1.61

mile = 1.61

def cng_km(km):
   
    for n in range(1,km+1):
        print(f'{n} 마일 = {mile*n} 킬로미터')

cng_km(6)

#4-5 cm를 인치로 바꾸는 함수 , 1인치은 2.54cm
inch = 2.54

def cng_cm(cm):
    for n2 in range(1,cm+1):
        print(f'{n2} 인치 = {inch*n2} 센티미터')

cng_cm(5)