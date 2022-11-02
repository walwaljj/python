


result = [([[18, 6], [158, 6], [158, 38], [18, 38]], '107아 6540', 0.9519319570751127)]


#-------------------------------------------------------------------------------------------
result_list = []

for i in result :
  for j in i[1] :
    if('0'<=j<='9' or '가'<=j<='힣'):

      result_list.append(j)

    else:
      continue    
    
for n in result_list :
  if '가'<=n<='힣' :
    a=result_list[:result_list.index(n)+1]
    b=result_list[result_list.index(n)+1:]
    
    if 3<=len(a)<=4 :
      a = ''.join(a)
    else :
      print('a err')
    
    if len(b) == 4 :
      b = ''.join(b)
    else :
      print('b err')

    print(a,b)

