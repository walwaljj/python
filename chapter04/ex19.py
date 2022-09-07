def calcstep(**args):
    print(args)
    begin = args.get('begin',0)#없는인자 에러방지차 디폴트값을 전달함.
    end = args['end']
    step = args['step']

    total = 0
    for num in range(begin, end+1, step):
        total+=num
    
    return total
print (calcstep(begin=3, end = 5, step=1))
print(calcstep(step=1,end=5,begin=3))
print(calcstep(step=1,end=5,begin=5,END=4))#몇개가 오든 사전에 담김, 함수에서는 필요한 키만 사용한다.
print(calcstep(step=1,end=5))# begin = args['begin']여기서 해당키가 전달되지 않아 에러남

even = {
    'begin' : 0,
    'end' : 100,
    'step' : 2
}

print(calcstep(**even))#사전에 대한 펼침연산자. **두개를 사용함.

odd = {
    **even,
    'begin' : 1
}

print('odd : ',odd)