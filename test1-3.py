import pymysql

conn= pymysql.connect (host='localhost', user='root', 
password='multi123', db='car_manage', 
charset='utf8')

cursor = conn.cursor()
cursor.execute('USE car_manage;')
# cursor.execute('INSERT INTO user (last_number, car_type, car_type2, first_number, intro_time, outro_time) VALUES ("3355", "EV", "x" , "11너", "221202","221204")')

# cursor.execute('SELECT * FROM user;')
value = cursor.fetchall()
print(value)

# conn.commit()
# conn.close()