import mysql.connector


conn = mysql.connector.connect(user='brainspark', password='C!sco123',
                              host='brainspark.cptvcix7ijfy.us-west-2.rds.amazonaws.com',
                              database='brainspark')
mycursor=conn.cursor()
mycursor.execute("INSERT INTO ideas VALUES (1,'my idea is that Alex sucks')")
mycursor.execute("INSERT INTO ideas VALUES (2,'my idea is that Ali sucks')")
mycursor.execute("INSERT INTO ideas VALUES (3,'my idea is that Chris is nice')")
conn.commit()
print(mycursor.fetchall())
