from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .models import LINEFollower
from utils.message_creater import create_message
from utils.stamp import set_stamp
from line_bot.line_message import LineMessage
from utils.templates.search_templates import shopData
import requests

ACCESSTOKEN = 'gASBNZY+U6ZNrhCZYa3tou5dX6+Seue+Yq3QvbZ3n4Wfb1/Pc9OS9z+XJ+WFJUn3poHbntob1k2G7NAPqyqrwlVxw38DHOq2K4nRO3i2wXW0CvjBuooHNL5Qva2yPV/0bDlW4lEhqwKq8mT+icJRigdB04t89/1O/w1cDnyilFU='
headers = {
    'Authorization': 'Bearer ' + ACCESSTOKEN
}

@csrf_exempt
def index(request):
    if request.method == 'POST':
        request = json.loads(request.body.decode('utf-8'))
        data = request['events'][0]
        user_id = data["source"]["userId"]
        if data["type"] == "follow":
            response = requests.get("https://api.line.me/v2/bot/profile/" + user_id, headers=headers)
            user_data = response.json()
            print(user_data)
            nickname = user_data["displayName"]
            print(nickname)
            mode = "0-0-0"
            stamp = "00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
            LINEFollower.objects.create(user_id = user_id, nickname = nickname, mode = mode, stamp = stamp)
        elif data["type"] == "unfollow":
            users = LINEFollower.objects.all()
            for user in users:
                if user.user_id == data["source"]["userId"]:
                    id = user.id
            user = LINEFollower.objects.get(id = id)
            user.delete()
        elif data["type"] == "message":
            reply_token = data['replyToken']
            if data['message']['type'] == "location":
                reply_message = set_stamp(data['message'], user_id)
            else:
                message = data['message']
                message_detail = message['text']
                print(message_detail)
                reply_message = create_message(message_detail, user_id)
            line_message = LineMessage(reply_message)
            line_message.reply(reply_token)
    return JsonResponse({"status": "successful"})

@csrf_exempt
def stamp(request, user_id):
    if request.method == 'GET':
        users = LINEFollower.objects.all()
        for user in users:
            if user.user_id == user_id:
                id = user.id
        user = LINEFollower.objects.get(id = id)
        stamps = user.stamp
        num = 0
        for i in range(len(stamps)):
            if stamps[i] == "1":
                num += 1
        nickname = user.nickname
        shop_data = shopData()
        stamp_shop = []
        no_stamp_shop = []
        for i in range(len(shop_data)):
            if stamps[i] == "0":
                no_stamp_shop.append(shop_data[i][1])
            else:
                stamp_shop.append(shop_data[i][1])
        return render(request, "line_bot/stamp_data.html", {
            "nickname": nickname,
            "stamps": stamps,
            "num": num,
            "stamp_shop": stamp_shop,
            "no_stamp_shop": no_stamp_shop
        })