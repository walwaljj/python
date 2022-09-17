#6-11 빈튜플 빈문자열 빈리스트를 제거하기

from os import remove


nlist = [(),1,(),(),(1,),('a',),('a','b'),((),),('a','b'),'']

nlist=[n for n in nlist if n!= '' and n!=()]

print(nlist)

tlist = [5,6,3,9,2,12,3,8,7]

for i in range(len(tlist)) :
    z
    if len(tlist)<i :
        break
    if tlist[i]>tlist[len(tlist)-1] :
        tlist[len(tlist)-1],tlist[i]=tlist[i],tlist[len(tlist)-1]
        
print(tlist)