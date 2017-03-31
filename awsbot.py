from itty import *
from ciscosparkapi import CiscoSparkAPI
import requests
import sys
import json



@post('/')
def index(request):
    """
    When messages come in from the webhook, they are processed here.  The message text needs to be retrieved from Spark,
    using the sendSparkGet() function.  The message text is parsed.  If an expected command is found in the message,
    further actions are taken. i.e.
    /batman - replies to the room with text
    /batcave   - echoes the incoming text to the room
    /batsignal - replies to the room with an image
    """
    webhook = json.loads(request.body)
    print webhook
    room_id = webhook["data"]["roomId"]

####CHANGE THESE VALUES#####
bot_email = "jukkmoddr@sparkbot.io"
bot_name = "Test"
bearer = "ZTlkYzU2MGQtNWZlOC00MTA5LWE5MzYtMjdiYjMyNzA5NTYzNjBlYjU3NWMtYjg4"
bat_signal  = "https://upload.wikimedia.org/wikipedia/en/c/c6/Bat-signal_1989_film.jpg"
run_itty(server='wsgiref', host='0.0.0.0', port=10010)
