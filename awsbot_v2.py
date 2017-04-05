from itty import *
import json
from ciscosparkapi import CiscoSparkAPI
import requests
import sys
import os

@post('/')
def index(request):
    """
    When messages come in from the webhook, they are processed here.  The message text needs to be retrieved from Spark,
    using the sendSparkGet() function.  The message text is parsed.  If an expected command is found in the message,
    further actions are taken. i.e.
    /batman    - replies to the room with text
    /batcave   - echoes the incoming text to the room
    /batsignal - replies to the room with an image
    """
    spark = CiscoSparkAPI(access_token=bearer)
    webhook = json.loads(request.body)
    room_id = webhook['data']['roomId']
    message_id = webhook['data']['id']
    print message_id
    message = spark.messages.get(message_id)
    if webhook['data']['personEmail'] != bot_email:
        in_message = message.text.replace(bot_name, '')
        if message.type == "group" and 'start' in in_message:
            memberList = spark.memberships.list(roomId=room_id)
            spark.messages.create(roomId=room_id, text="Test will initiate") # Message the room.
            for Membership in memberList: # Message each member in the room individually.
                if Membership.personEmail != bot_email or Membership.personEmail != security_email:
                    spark.messages.create(toPersonEmail=Membership.personEmail, text="how can I help")
                    #TODO: Save list of people involved in this brainstorm & group roomId.
                    # Likely another database. This one is roomId, memberList.
        else:
            if message.type == "direct":
                # TODO: Save message. Generate response. Save response. Send response.
                sendToDatabase(message.text, message.personEmail, bot_email)
                # Database definition: Message, From, To.
                response = generateResponse(message.text, message.personEmail, message.roomId)
                sendToDatabase(response, bot_email, message.personEmail)
                spark.messages.create(toPersonEmail=message.personEmail, text=response)
            else:
                # So not a group message invoking the bot.
                # And not a direct message.
                # So they aren't talking to us. Don't respond.
                return "false"
    return "true"

#TODO: sendToDatabase(), generateResponse().

####CHANGE THESE VALUES#####
bot_email = "awstest1@sparkbot.io"
security_email = "spark-cisco-it-admin-bot@cisco.com"
bot_name = "awstest1"
bearer = "MjViMjgwMzQtMGY5MC00MGYwLTk2YmUtNGQwOTc5OTVkODc4ODc3ZDRkY2MtZDA3"
run_itty(server='wsgiref', host='0.0.0.0', port=10010)
