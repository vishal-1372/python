#import mysql.connector
#mydb=mysql.connector.connect(host='localhost',user='root',password='')
#print(mydb)


# import mysql.connector
# mydb=mysql.connector.connect(host='localhost',user='root',password='')
# mycursor=mydb.cursor()
# mycursor.execute('CREATE DATABASE mypy')

# import mysql.connector
# mydb=mysql.connector.connect(host='localhost',user='root',password='',database='mypy')
# mycursor=mydb.cursor()
# mycursor.execute('SHOW DATABASEs')
# for i in mycursor:
#     print(i)


# import mysql.connector
# mydb=mysql.connector.connect(host='localhost',user='root',password='',database='mypy')
# mycursor=mydb.cursor()
# mycursor.execute('CREATE TABLE stud_data(roll int,name varchar(25))')

# import mysql.connector
# try:
#     mydb=mysql.connector.connect(host='localhost',user='root',password='',database='mypy')
#     my_insert_query='INSERT INTO stud_data(roll ,name) VALUES(%s,%s)'
#     records_to_insert=[(1,'vishal'),(2,'milan'),(3,'khan')]
#     cursor=mydb.cursor()
#     cursor.executemany(my_insert_query,records_to_insert)
#     mydb.commit()
#     print('record inserted')
# except mysql.connector.Error as error:
#     print('not connecte')
# finally:
#     if mydb.is_connected():
#         cursor.close()
#         mydb.close()
#         print('Mysql is close')    
        
        
# import mysql.connector
# mydb=mysql.connector.connect(host='localhost',user='root',password='',database='mypy')
# mycursor=mydb.cursor()
# mycursor.execute('SELECT * FROM stud__data')
# myresult=mycursor.fetchall()
# for i in myresult:
#     print(i)
            
            
            
# import mysql.connector
# mydb=mysql.connector.connect(host='localhost',user='root',password='',database='mypy')
# mycursor=mydb.cursor()
# mycursor.execute('UPDATE stud_data SET name ="mehul" WHERE ROLL = 1')
# mydb.commit()



            
# import mysql.connector
# mydb=mysql.connector.connect(host='localhost',user='root',password='',database='mypy')
# mycursor=mydb.cursor()
# mycursor.execute('DELETE FROM stud_data WHERE ROLL = 1')
# mydb.commit()
# mydb.close()






###### SQL LITE ######
import sqlite3
cnt = sqlite3.connect('mydb.dp')
# # cnt.execute('create table stud_data (roll integer,name varchar)')

# cnt.execute(""" 
#                INSERT INTO stud_data VALUES
#                 (1,'SUNDAY'),
#                 (2,'MONDAY'),
#                 (3,'TUESDAY')
#                                 """)
# print('record inserted')
# cnt.commit()


# cursor = cnt.execute('select * from stud_data')
# for i in cursor:
#     print(i)


# sql_upd=""" UPDATE stud_data SET name = 'Friday' WHERE roll = 1"""
# cnt.execute(sql_upd)
# cursor = cnt.execute('select * from stud_data')
# for i in cursor:
#      print(i)

sql_del=""" DELETE FROM stud_data WHERE roll = 1"""
cnt.execute(sql_del)
cursor = cnt.execute('select * from stud_data')
for i in cursor:
     print(i)



#commit


