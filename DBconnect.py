import mysql.connector

def sendToDatabase(message, personEmail, bot):
	conn = mysql.connector.connect(user='brainspark', password='C!sco123',
                              host='brainspark.cptvcix7ijfy.us-west-2.rds.amazonaws.com',
                              database='brainspark')
	mycursor=conn.cursor()
	mycursor.execute("INSERT INTO ideas (userID,q1,q2) VALUES (%s,%s,%s)", (personEmail,message,bot))
	conn.commit()
	return "true"
# print(mycursor.fetchall())

def pullFromDatabase(message, personEmail):
	return "true"


sendToDatabase("hallo", 5, "test@cisco.com")