# test 
def generateResponse(message, personEmail, bot_email)
	spark.messages.create(toPersonEmail=message, text="processing...")