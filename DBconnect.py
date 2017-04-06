import mysql.connector


conn = mysql.connector.connect(user='brainspark', password='C!sco123',
                              host='brainspark.cptvcix7ijfy.us-west-2.rds.amazonaws.com',
                              database='brainspark')
mycursor=conn.cursor()
mycursor.execute("SHOW TABLES")
print(mycursor.fetchall())
