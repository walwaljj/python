#6-13  1.가장큰 수를 제일 마지막으로 옮기기 2.끝으로 옮겨진 요소를 제외한 리스트중 가장 큰수를 두번째위치로..

nlist = [5,6,3,9,2,12,3,8,7]

for ix,i in enumerate(nlist) :
    if nlist[ix+1] > nlist[len(nlist)-1] :
        break
        if nlist[ix+1]>i :
            nlist[len(nlist)-1]=nlist[ix]
        
print(nlist)