import pymysql

conn= pymysql.connect (host='localhost', user='root', 
password='multi123', db='car_manage', 
charset='utf8')

#connect
conn = pymysql.connect (host='localhost', user='root', 
password='nulti123', db='car_manage', 
charset='utf8')

cursor = conn.cursor()
cursor.execute('USE car_manage;')

cursor.execute('INSERT INTO user
							(last_number, car_type, first_number, intro_time, outro_time)
					    VALUES("3333", "yellow", "16나", "221102", "221105")')
conn.commit() # 그리고 이거만 하면 db에 올라감.
conn.close()
