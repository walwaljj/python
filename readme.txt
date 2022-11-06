
1. 접속 + db지정. 
conn = pymysql.connect(host = 'localhost', user = 'root' , password = 'multi123', db = 'car_manage', charset = 'utf8')

1-1 .

위에서 db지정하지 않았다면 
cursor.execute('USE car_manage;')
해주기

2. 커서생성

cur = conn.cursor()

3. 추가하기 

cur.execute('INSERT INTO user (last_number, car_type, car_type2, first_number, intro_time, outro_time) VALUES("3333", "yellow", "x" "16나", "2022-11-02", "2022-11-05")')

cur.execute('insert into user values("3345", "EV", "x" , "11너", "221202","221204")')

4. 조회하기

cur.execute('SELECT * FROM user;')

4-1. 조회한 내용 변수에 담아 출력
value = cursor.fetchall() # (결과의 모든 결과 담기)
value = cursor.fetchone() # (결과 중 한 행만 담기)
print(value)
5. 커밋하기 

cur.commit()

6. 커서닫기

cur.close()