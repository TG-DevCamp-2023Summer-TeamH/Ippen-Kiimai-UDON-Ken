from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .models import LINEFollower
from utils.message_creater import create_message
from line_bot.line_message import LineMessage
import requests

ACCESSTOKEN = 'gASBNZY+U6ZNrhCZYa3tou5dX6+Seue+Yq3QvbZ3n4Wfb1/Pc9OS9z+XJ+WFJUn3poHbntob1k2G7NAPqyqrwlVxw38DHOq2K4nRO3i2wXW0CvjBuooHNL5Qva2yPV/0bDlW4lEhqwKq8mT+icJRigdB04t89/1O/w1cDnyilFU='
HEADER = {
    'Authorization': 'Bearer ' + ACCESSTOKEN
}

@csrf_exempt
def index(request):
    if request.method == 'POST':
        request = json.loads(request.body.decode('utf-8'))
        data = request['events'][0]
        if data["type"] == "follow":
            user_id = data["source"]["userId"]
            response = requests.get("https://api.line.me/v2/bot/profile/" + user_id, header = HEADER)
            user_data = response.json()
            print(user_data)
            nickname = user_data["displayName"]
            print(nickname)
            mode = "0-0-0"
            stamp = "0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
            LINEFollower.objects.create(user_id = user_id, nickname = nickname, mode = mode, stamp = stamp)
        elif data["type"] == "unfollow":
            users = LINEFollower.objects.all()
            for user in users:
                if user.user_id == data["source"]["userId"]:
                    id = user.id
            user = LINEFollower.objects.get(id = id)
            user.delete()
        else:
            message = data['message']
            reply_token = data['replyToken']
            message_detail = message['text']
            print(message_detail)
            reply_message = create_message(message_detail)
            line_message = LineMessage(reply_message)
            line_message.reply(reply_token)
    return JsonResponse({"status": "successful"})

@csrf_exempt
def stamp(request, user_id):
    if request.method == 'GET':
        return render(request, "line_bot/stamp_data.html", {
            "stamp": stamp
        })