# -*- coding: utf-8 -*- 
 
import MySQLdb
 
connect = MySQLdb.connect(host="localhost", port=3306, db="cake3", user="root", passwd="passwd", charset="utf8")
cursor  = connect.cursor()
 
sql = "select name from name_list"
cursor.execute(sql)
 
for row in cursor:
    exclusion_list_file = row[0]
 
cursor.close()
connect.close()
 
print exclusion_list_file