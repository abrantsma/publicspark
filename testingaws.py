from itty import *
import urllib2
import json

def sendSparkGET(url):
    request = urllib2.Request(url,
                            headers={"Accept" : "application/json",
                                     "Content-Type":"application/json"})
    request.add_header("Authorization", "Bearer "+bearer)
    contents = urllib2.urlopen(request).read()
    return contents

@post('/')
def index(request):
    webhook = json.loads(request.body)
    print webhook['data']['id']
    result = sendSparkGET('https://api.ciscospark.com/v1/messages/{0}'.format(webhook['data']['id']))
    result = json.loads(result)
    print result
    return "true"

####CHANGE THIS VALUE#####
bearer = "ZTlkYzU2MGQtNWZlOC00MTA5LWE5MzYtMjdiYjMyNzA5NTYzNjBlYjU3NWMtYjg4"

run_itty(server='wsgiref', host='0.0.0.0', port=10010)

print result
if 'batman' in result.get('text', '').lower():
    print "I'm Batman!"
elif 'batcave' in result.get('text', '').lower():
    print "The Batcave is silent..."
elif 'batsignal' in result.get('text', '').lower():
    print "NANA NANA NANA NANA"
