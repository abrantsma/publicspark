import mysql.connector


conn = mysql.connector.connect(user='brainspark', password='C!sco123',
                              host='brainspark.cptvcix7ijfy.us-west-2.rds.amazonaws.com',
                              database='brainspark')
mycursor=conn.cursor()
mycursor.execute(""INSERT INTO ideas VALUES (1,'my idea is that Alex sucks')"")
conn.commit()
print(mycursor.fetchall())
