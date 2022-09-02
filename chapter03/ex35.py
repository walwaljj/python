import numbers


numbers = [11, 22, 33, 44, 55, 66]
print(type(numbers))
for n in numbers :
    print (n , end = ' ')

print()

fruits = ['수박', '참외', '체리', '포도']
for fruit in fruits:
    print(fruit,end = ' ')  
print()
print(fruits)

for ix,fruit in enumerate(fruits) :
    print(ix,fruit,end = ' ')  