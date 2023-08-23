from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

from utils.message_creater import create_message
from line_bot.line_message import LineMessage

@csrf_exempt
def index(request):
    if request.method == 'POST':
        request = json.loads(request.body.decode('utf-8'))
        data = request['events'][0]
        message = data['message']
        reply_token = data['replyToken']
        message_detail = message['text']
        print(message_detail)
        reply_message = create_message(message_detail)
        print("Successful!")
        line_message = LineMessage(reply_message)
        line_message.reply(reply_token)
        print("Successful!")
    return HttpResponse("successful")