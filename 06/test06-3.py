day_c = (100,121,120,130,140,120,122,123,190,125)


for ix , i in enumerate(day_c,1):

    if i > day_c[ix] :
        print(f'지난 10일간 매출이 감소한날은 {ix+1}')  
        break

    

