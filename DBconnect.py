import mysql.connector

def sendToDatabase(message, personEmail, bot):
	conn = mysql.connector.connect(user='brainspark', password='C!sco123',
                              host='brainspark.cptvcix7ijfy.us-west-2.rds.amazonaws.com',
                              database='brainspark')
	mycursor=conn.cursor()
	mycursor.execute("INSERT INTO ideas (userID,q1) VALUES (?,?)", (personEmail,message))
	conn.commit()
# print(mycursor.fetchall())

def pullFromDatabase(message, personEmail):


sendToDatabase("hallo", "ctsioura@cisco.com", "test@cisco.com")