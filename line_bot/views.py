from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

from utils.message_creater import create_single_text_message
from line_bot.line_message import LineMessage

@csrf_exempt
def index(request):
    print(request.method)
    if request.method == 'POST':
        request = json.loads(request.body.decode('utf-8'))
        try:
            data = request['events'][0]
            message = data['message']
            reply_token = data['replyToken']
            line_message = LineMessage(create_single_text_message(message['text']))
            line_message.reply(reply_token)
        except:
            pass
    return HttpResponse("successful")