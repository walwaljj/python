def area_and_circum(radius) : 
    area = 3.14 * radius**2
    circum = 2 * 3.14 * radius
    return area,circum

r = 4
a,c = area_and_circum(r)
print(f'반지름{r}인 원의 면적과 둘레 : {a}, {c}')