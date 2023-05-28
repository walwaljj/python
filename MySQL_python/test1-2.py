import pymysql

conn = pymysql.connect(host = '127.0.0.1' , user='root' , password='multi123', db='car_manage', charset='utf8')

cur = conn.cursor()

# cur.execute("INSERT INTO user values('')")

cur.execute('INSERT INTO user (last_number, car_type, car_type2, first_number, intro_time, outro_time) VALUES("3333", "yellow", "x" "16나", "2022-11-02", "2022-11-05")')
#             #
                

# conn.commit() # 그리고 이거만 하면 db에 올라감.
# conn.close()