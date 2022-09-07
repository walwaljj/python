import datetime as dt
print('오늘 =', dt.datetime.now()) # 현재시간을 구한다
hundred = dt.timedelta(days = 100) # 100일 경과시간
plus100day = dt.datetime.now() + hundred # 현재 시간에서 100일 경과시간을 더함
print('100일 후 =', plus100day)


today = dt.date.today()
print(f'오늘은 {today.year}년 {today.month}월 {today.day}입니다.')
xMas = dt.datetime(2022,12,25)

time_gap = xMas - dt.datetime.now()
print(f'다음 크리스마스까지 {time_gap.days}일 {time_gap.seconds//3600}시간 남았습니다.')

import time as t

unix_timestamp = t.time()
print(unix_timestamp)
lc = t.localtime(unix_timestamp)
print(t.strftime('%y-%m-%d %H:%M:%S',lc))