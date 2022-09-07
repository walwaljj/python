#5-3 . list 1, list 2가있을때 이중fpr루프로 각원소를 곱하고 출력
l1=[3,5,7]
l2=[2,3,4,5,6]

for n1 in l1 :
    for n2 in l2 :
        print(f'{n1} x {n2} = {n1*n2:3d}')