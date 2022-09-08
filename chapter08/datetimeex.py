from datetime import datetime

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

now = datetime.now()

now_str = datetime.strftime(now,DATE_FORMAT)
print(now_str)

str_date = "2022-09-08 12:11:44"
s_date = datetime.strptime(str_date,DATE_FORMAT)
print(type(s_date),s_date)
print(s_date)