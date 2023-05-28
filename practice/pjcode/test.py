result_list =  ['1', '0', '7', '가', '6', '5', '4', '0']
result_list2 = [n for n in result_list if '0'<=n<='9' not in result_list]
print(result_list2)