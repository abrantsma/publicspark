
# Welcome!  Ready to get going?  You can just hit save and 
# this code should work all by itself.  

# Want to learn more?  Well, here's the first thing to know: 

# YOU MUST define a function named 'spark_handler' or nothing will
# happen.  

# currently the default libraries are enabled as well:
# - requests==2.11.1
# - Flask==0.11.1
# - ciscosparkapi==0.3.1

# we already include the ciscospark API
# https://pypi.python.org/pypi/ciscosparkapi
# and have already initialized the client for you.  You just
# need to run it now. 

# you can import another library here as well:
# we already import the following libs: 
#from flask import Flask, request
#from ciscosparkapi import CiscoSparkAPI
import flask
from flask import Flask, request
import requests
import ciscosparkapi
from ciscosparkapi import CiscoSparkAPI
import os
import sys
import json 


# Create an instance of Flask
app = Flask(__name__)

def spark_handler(post_data, message):
	# get the room id: 
	room_id = post_data["data"]["roomId"]
	# get message
	initMessage = str(message.text)
	# if message is Test start, then initiate the test
	# get all the member emails from the room and start a conversation with them
	if initMessage == "Test start":
		spark.messages.create(roomId=room_id, text= "Test will initiate")
		memberList = spark.memberships.list(roomId=room_id)
		userEmail = []
		newRoomIds = []
		for Membership in memberList:
			userEmail.append(Membership.personEmail)
			spark.messages.create(toPersonEmail=Membership.personEmail, text="how can I help")
		# 	newRooms = spark.rooms.create("BrainSpark")
		# 	# spark.messages.create(roomId=room_id, text= str(newRooms))
		# 	spark.memberships.create(newRooms.id, personEmail = Membership.personEmail)
		# 	newRoomIds.append(newRooms.id)

		# spark.messages.create(roomId=room_id, text= "RoomIds: " + str(newRoomIds))
		# spark.messages.create(roomId=room_id, text= "Useremails: " + str(userEmail))



