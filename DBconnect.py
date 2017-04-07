import mysql.connector

def createDatabase(personName):
	conn = mysql.connector.connect(user='brainspark', password='C!sco123',
                              host='brainspark.cptvcix7ijfy.us-west-2.rds.amazonaws.com',
                              database='brainspark')
	mycursor=conn.cursor()
	ID_NUMBER = 2568
	mycursor.execute("CREATE TABLE %s (QUESTION INT PRIMARY KEY AUTO_INCREMENT)" % (personName))
	conn.commit()
	return "true"







def sendToDatabase(message, personEmail, bot):
	conn = mysql.connector.connect(user='brainspark', password='C!sco123',
                              host='brainspark.cptvcix7ijfy.us-west-2.rds.amazonaws.com',
                              database='brainspark')
	mycursor=conn.cursor()
	ID_NUMBER = 2568
	mycursor.execute("INSERT INTO ideas (userID,q1,q2) VALUES (%s,%s,%s)", (ID_NUMBER,message,bot))
	conn.commit()
	return "true"
# print(mycursor.fetchall())

def pullFromDatabase(message, personEmail):
	conn = mysql.connector.connect(user='brainspark', password='C!sco123',
                              host='brainspark.cptvcix7ijfy.us-west-2.rds.amazonaws.com',
                              database='brainspark')
	mycursor=conn.cursor()
	sql = "SELECT * FROM ideas WHERE q2 = '%s'" % ("test@cisco.com")
	try:
		mycursor.execute(sql)
		results = mycursor.fetchall()
		print (results)
	except:
		print "Nothing found"
	conn.commit()
	return "true"

createDatabase("chris")
# sendToDatabase("hallo", 65745, "test@cisco.com")
# pullFromDatabase("message", "personEmail")