n_list = (input("쉼표로 구분된 정수를 여러개 입력하세요 : > ").split(','))

n_list=[ int(n) for n in n_list]

print(f'입력된 정수의 리스트 : {n_list}')
n_list.sort()
print(f"정렬된 정수의 리스트 : {n_list}",end='')
