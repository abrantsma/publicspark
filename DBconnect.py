import mysql.connector

def createDatabase(personName):
	conn = mysql.connector.connect(user='brainspark', password='C!sco123',
                              host='brainspark.cptvcix7ijfy.us-west-2.rds.amazonaws.com',
                              database='brainspark')
	mycursor=conn.cursor()
	mycursor.execute("CREATE TABLE %s (Question INT PRIMARY KEY AUTO_INCREMENT, Answer TEXT)" % (personName))
	conn.commit()
	return "true"







def sendToDatabase(personName,answer):
	conn = mysql.connector.connect(user='brainspark', password='C!sco123',
                              host='brainspark.cptvcix7ijfy.us-west-2.rds.amazonaws.com',
                              database='brainspark')
	mycursor=conn.cursor()
	mycursor.execute("INSERT INTO %s VALUES ('%s')", (personName,answer))
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

# createDatabase("chris")
sendToDatabase("chris","bla bla bla")
# pullFromDatabase("message", "personEmail")