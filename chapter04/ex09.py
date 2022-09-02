from unittest import result


def print_sum():
    result = a+b
    print('print_sum() 내부 : ',a, '과',b,'의 합은',result,'입니다.')

a=10
b=20
print_sum()
print_sum(result)
result = a+b
print('print_sum() 외부 :', a, '과', b, '의 합은', result, '입니다.')
