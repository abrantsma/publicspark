# import Flask
from flask import Flask, request

# Create an instance of Flask
app = Flask(__name__)

# Index page will trigger index() function
@app.route('/')
def index():
    return 'Hello World'

# Webhook page will trigger webhooks() function
@app.route("/webhook", methods=['POST'])
def webhooks():

    # Get the json data
    json = request.json

    
    print(json)

    # # check if the message is the command to get hosts
    # if message == "GET HOSTS":
    #     # get list of hosts from APIC-EM Controller
    #     hosts = gethosts.main()
    #     # post the list of hosts into the Spark room
    #     postmessage.main(person_id, person_email, room_id, hosts)
    # else:
    #    print("do nothing")

# run the application
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10010)