from file_util import read_file_lines

data = read_file_lines('data5.txt')
data =[int (n) for n in data]
total = sum(data)
average = total / len (data)
print (f'합 : {total}, 평균: {average}')