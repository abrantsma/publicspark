from itty import *
import json
from ciscosparkapi import CiscoSparkAPI
import requests
import sys
import os
from generateResponse import generateResponse
from DBconnect import sendToDatabase, pullFromDatabase, createDatabase, deleteDatabase

@post('/')
def index(request):
    spark = CiscoSparkAPI(access_token=bearer) # spark apis
    webhook = json.loads(request.body) # get payload from webhook
    room_id = webhook['data']['roomId'] # get room id from message
    message_id = webhook['data']['id'] # get message id
    message = spark.messages.get(message_id) # retrieve message using message id
    room_name = spark.rooms.get(room_id) # retrieve room information to get the room name
    personName = spark.people.list()

    # Code for the bot to speak. First we make sure that it only responds to messages NOT from the bot itself
    if webhook['data']['personEmail'] != bot_email:
        # parse the initiation message to remove the bot tag
        in_message = message.text.replace(bot_name, '')
        # conditional for the initiation of the test. 
        # here we filter for a message from a "group" room and for the message "start"
        # If it matches then send a message to the group room, and also send a message to each person individually
        if message.roomType == "group" and 'start' in in_message:
            memberList = spark.memberships.list(roomId=room_id)
            GROUP_MESSAGE = "Brainstorming session for '%s' is starting." % (room_name.title)
            spark.messages.create(roomId=room_id, text=GROUP_MESSAGE) # Message the room.
            for Membership in memberList: # Message each member in the room individually.
                if Membership.personEmail != bot_email and Membership.personEmail != security_email: # filter out the bot and cisco security bot, we dont want to send them a message!
                    INTRO_MESSAGE = "You have been invited to brainstorming session '%s'. Type 'help' for a brief introduction on how I work! What is your idea?" % (room_name.title)
                    spark.messages.create(toPersonEmail=Membership.personEmail, text=INTRO_MESSAGE)
                    createDatabase(Membership.personEmail.replace('@cisco.com', '').replace('@gmail.com',''))
                    #TODO: Save list of people involved in this brainstorm & group roomId.
                    # Likely another database. This one is roomId, memberList.
        # conditional to end the test
        # same idea as above but then for the word end
        # should also post the final idea into the group room
        elif message.roomType == "group" and "end" in in_message:
            memberList = spark.memberships.list(roomId=room_id)
            GROUP_MESSAGE = "Brainstorming session for '%s' is ending." % (room_name.title)
            spark.messages.create(roomId=room_id, text=GROUP_MESSAGE) # Message the room.
            for Membership in memberList: # Message each member in the room individually.
                if Membership.personEmail != bot_email and Membership.personEmail != security_email:
                    END_MESSAGE = "Brainstorming session '%s' is ending." % (room_name.title)
                    spark.messages.create(toPersonEmail=Membership.personEmail, text=END_MESSAGE)
                    deleteDatabase(Membership.personEmail.replace('@cisco.com', '').replace('@gmail.com',''))
            #TODO: Send the best idea to the group chat.
            BEST_IDEA = "The best idea." #getBestIdea(room_id)
            spark.messages.create(roomId=room_id, text=BEST_IDEA)
        # looks for personal messages in 1:1 conversations. These messages need to be saved to our database
        else:
            if message.roomType == "direct":
                if in_message == "help":
                    spark.messages.create(toPersonEmail=message.personEmail, text="explanation of how this works, what is your idea")
                    return "true"
                #Temp making sure it tries to do this:
                spark.messages.create(toPersonEmail=message.personEmail, text="processing...")
                # TODO: Save message. Generate response. Save response. Send response.
                sendToDatabase(message.personEmail.replace('@cisco.com','').replace('@gmail.com',''), message.text)
                # Database definition: Message, From, To.
                response = generateResponse(message.text, message.personEmail)
                #sendToDatabase(response, bot_email, message.personEmail)
                spark.messages.create(toPersonEmail=message.personEmail, text=response)
            else:
                # So not a group message invoking the bot.
                # And not a direct message.
                # So they aren't talking to us. Don't respond.
                return "false"
    return "true"

#TODO: sendToDatabase(), generateResponse().


bot_email = "awstest1@sparkbot.io"
security_email = "spark-cisco-it-admin-bot@cisco.com"
bot_name = "awstest1"
bearer = "MjViMjgwMzQtMGY5MC00MGYwLTk2YmUtNGQwOTc5OTVkODc4ODc3ZDRkY2MtZDA3"
run_itty(server='wsgiref', host='0.0.0.0', port=10010)
