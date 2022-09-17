#3-26 뱀행렬 : n을 입력받고 n**2수까지 뱀행렬형태로 출력
nlist=[]
n = int(input("n을 입력하세요 :"))

# for i in range((n**2)) :
#     nlist.append(i+1)
#     for j in nlist :
#         if j%n == 0 :
#             print()
#         else 

for i in range(1,n**2+1) :
    # nlist.append(i+1)
    print(f'{i:3d}',end='')
    # for j in range(i) :
    if i%n != 0 :
        add = n*i+(i-1)
    if i%n == 0 :
         print()
           
        
    # nlist.append(add)
    # print(nlist,end='')

