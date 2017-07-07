import pymysql
import pymysql.cursors

conn = pymysql.connect(user='root', password='c22h20o13', host='localhost', database='wordpress')
cur = conn.cursor()

cur.execute("select * from wp_posts;")

for row in cur.fetchall():
    print(row[0],row[1])

cur.close
conn.close