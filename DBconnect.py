import mysql.connector


cnx = mysql.connector.connect(user='brainspark', password='C!sco123',
                              host='brainspark.cptvcix7ijfy.us-west-2.rds.amazonaws.com:3306',
                              database='brainspark')
cnx.close()