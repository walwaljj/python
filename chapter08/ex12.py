f = open('foo.txt','r')
data = []

s=f.readline()
while s : 
    data.append(s.strip())
    s=f.readline()
f.close()
print(data)