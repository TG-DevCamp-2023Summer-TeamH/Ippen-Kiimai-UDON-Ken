from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import urllib.request
import json

REPLY_ENDPOINT_URL = "https://api.line.me/v2/bot/message/reply"
ACCESSTOKEN = 'gASBNZY+U6ZNrhCZYa3tou5dX6+Seue+Yq3QvbZ3n4Wfb1/Pc9OS9z+XJ+WFJUn3poHbntob1k2G7NAPqyqrwlVxw38DHOq2K4nRO3i2wXW0CvjBuooHNL5Qva2yPV/0bDlW4lEhqwKq8mT+icJRigdB04t89/1O/w1cDnyilFU='
HEADER = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + ACCESSTOKEN
}

class LineMessage():
    def __init__(self, messages):
        self.messages = messages

    def reply(self, reply_token):
        body = {
            'replyToken': reply_token,
            'messages': self.messages
        }
        print(body)
        req = urllib.request.Request(REPLY_ENDPOINT_URL, json.dumps(body).encode(), HEADER)
        try:
            with urllib.request.urlopen(req) as res:
                body = res.read()
        except urllib.error.HTTPError as err:
            print(err)
        except urllib.error.URLError as err:
            print(err.reason)