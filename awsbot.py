from itty import *
import urllib2
import json
from ciscosparkapi import CiscoSparkAPI
import requests
import sys
import os
import warnings 


def sendSparkGET(url):
    """
    This method is used for:
        -retrieving message text, when the webhook is triggered with a message
        -Getting the username of the person who posted the message if a command is recognized
    """
    request = urllib2.Request(url,
                            headers={"Accept" : "application/json",
                                     "Content-Type":"application/json"})
    request.add_header("Authorization", "Bearer "+bearer)
    contents = urllib2.urlopen(request).read()
    return contents
   
def sendSparkPOST(url, data):
    """
    This method is used for:
        -posting a message to the Spark room to confirm that a command was received and processed
    """
    request = urllib2.Request(url, json.dumps(data),
                            headers={"Accept" : "application/json",
                                     "Content-Type":"application/json"})
    request.add_header("Authorization", "Bearer "+bearer)
    contents = urllib2.urlopen(request).read()
    return contents
   


@post('')
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
    result = spark.messages.get(message_id)
    msg = None
    if webhook['data']['personEmail'] != bot_email:
        in_message = result.text
        # in_message = result.get('text', '').lower()
        in_message = in_message.replace(bot_name, '')
        memberList = spark.memberships.list(roomId=room_id)
        if 'start' in in_message:
            msg = "Test will initiate"
            spark.messages.create(roomId=room_id, text= msg)
            for Membership in memberList: 
                if Membership.personEmail != bot_email or Membership.personEmail != security_email:
                    spark.messages.create(toPersonEmail=Membership.personEmail, text="how can I help")
    return "true"


####CHANGE THESE VALUES#####
bot_email = "awstest1@sparkbot.io"
security_email = "spark-cisco-it-admin-bot@cisco.com"
bot_name = "awstest1"
bearer = "MjViMjgwMzQtMGY5MC00MGYwLTk2YmUtNGQwOTc5OTVkODc4ODc3ZDRkY2MtZDA3"
run_itty(server='wsgiref', host='0.0.0.0', port=10010)
