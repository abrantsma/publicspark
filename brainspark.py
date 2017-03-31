import json
import sys
import requests

#MISSION: FILL IN THE REQUESTED DETAILS
ACCESS_TOKEN 	= "MGI0MWMyMDktMGIyZC00MzAxLWEyYzAtN2U2ZTA5YjQ5N2RkZTE0NjZkODgtMTJh"
ROOM_NAME		= "Brainspark" #Replace None with the name of the room to be created. Shroud with quotes.
YOUR_MESSAGE 	= "TanTan" #Replace None with the message that you will post to the room. Shroud with quotes.


#sets the header to be used for authentication and data format to be sent.
def setHeaders():         
	accessToken_hdr = 'Bearer ' + ACCESS_TOKEN
	spark_header = {'Authorization': accessToken_hdr, 'Content-Type': 'application/json; charset=utf-8'}
	return (spark_header)

def getRoomId(the_header):
	uri = "https://api.ciscospark.com/v1/rooms"
	resp = requests.get(uri, headers=the_header).json()
	# print(resp)
	n = len(resp["items"])-1
	roomIds = resp["items"][n]["id"]
	return(roomIds)

def getMessages(the_header,roomId):
	uri = "https://api.ciscospark.com/v1/messages"
	# Parameter variable. The email belongs to a bot user, but we can use it for our code
	querystring = {"mentionedPeople":"me","roomId":roomId}
	resp = requests.request("GET", uri, headers=the_header, params=querystring).json()
	# print(resp)
	msg = resp["items"][0]["text"]
	return(msg)


# creates a new room and returns the room id.
def createRoom(the_header,room_name):
	roomInfo = {"title":room_name}
	uri = 'https://api.ciscospark.com/v1/rooms'
	resp = requests.post(uri, json=roomInfo, headers=the_header)
	var = resp.json()
	return(var["id"])
	
	
# adds a new member to the room.  Member e-mail is test@test.com
def addMembers(the_header,roomId,userEmail):
	member = {"roomId":roomId,"personEmail": userEmail, "isModerator": False}
	uri = 'https://api.ciscospark.com/v1/memberships'
	resp = requests.post(uri, json=member, headers=the_header)
	# print("addMembers JSON: ", resp.json())

#posts a message to the room
def postMsg(the_header,roomId,message):
	message = {"roomId":roomId,"text":message}
	uri = 'https://api.ciscospark.com/v1/messages'
	resp = requests.post(uri, json=message, headers=the_header)
	
#MISSION: WRITE CODE TO RETRIEVE AND DISPLAY DETAILS ABOUT THE ROOM.
def getRoomInfo(the_header,roomId):
	print("In function getRoomInfo")
	#MISSION: Replace None in the uri variable with the Spark REST API call	
	uri = "https://api.ciscospark.com/v1/rooms/" + roomId
	if uri == None:
		sys.exit("Please add the uri call to get room details.  See the Spark API Ref Guide")
	resp = requests.get(uri, headers=the_header)
	print("Room Info: ",resp.text)
	resp = resp.json()

def getUserIds(the_header,roomId):
	uri = "https://api.ciscospark.com/v1/memberships/"
	querystring = {"roomId":roomId}
	resp = requests.request("GET", uri, headers=the_header, params=querystring).json()
	# print(resp)
	n = len(resp["items"])-2
	# print(n)
	userEmail = {}
	for i in range(0,n):
			userEmail[i] = resp["items"][i]["personEmail"]
			# newRoomId = createRoom(the_header,ROOM_NAME)
			# addMembers(the_header,newRoomId,userEmail)
	return(userEmail)


header=setHeaders()
roomId=getRoomId(header)
# print(roomId)
initMessage = getMessages(header,roomId)
# print(initMessage)

if initMesssage == "BrainSpark start":
	postMsg(header,roomId,"poop")
	userEmail = getUserIds(header,roomId)
	newRoomId = {}
	for i in range(0,len(userEmail)-1):
		newRoomId[i] = createRoom(header,ROOM_NAME)
		addMembers(header,newRoomId[i],userEmail[i])
	print(userEmail)
	print(newRoomId)




# if __name__ == '__main__':
# 	if ACCESS_TOKEN==None or ROOM_NAME==None or YOUR_MESSAGE==None:
# 		sys.exit("Please check that variables ACCESS_TOKEN, ROOM_NAME and YOUR_MESSAGE have values assigned.")
# 	header=setHeaders()
# 	#passing the ROOM_NAME for the room to be created
# 	room_id=createRoom(header,ROOM_NAME) 
# 	if room_id == None:
# 		sys.exit("Please check that function createRoom returns the room ID value.")
# 	#passing roomId to members function here to add member to the room.
# 	addMembers(header,room_id)   
# 	#passing roomId to message function here to Post Message to a room.
# 	postMsg(header,room_id,YOUR_MESSAGE)
# 	#MISSION: ADD FUNCTION CALL getRoomInfo(header,room_id)
# 	print("MISSION: ADD FUNCTION CALL getRoomInfo(header,room_id)")
