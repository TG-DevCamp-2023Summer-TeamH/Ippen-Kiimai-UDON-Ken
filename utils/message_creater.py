from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json          #json形式の読み込み
import csv          #csvの読み込み
import requests      #気象庁API読み込みに使用
from .templates.search_templates import pref, tak, chu

def create_message(message):
    if message[0] == '1':
        if message[4].isdecimal():
            with open('templates/line_bot/udon-shop.csv') as file:
                
        else:
            if message[2] == '0':
                data = tak()
            elif message[2] == '1':
                data = chu()
            else:
                data = pref()
        return data
    elif message == '2':
        return
    elif message == '3':
        print('Google Mapから現在地を送信してください。')
        @handler.add(MessageEvent, message=LocationMessage)
        def handler_location(event):
            user_address = event.message.address
            user_latitube = event.message.latitude
            user_longittube = event.message.longitude

            filed_name = find_near_filed(user_latitube)
        url = 'https://www.jma.go.jp/bosai/forecast/data/overview_forecast/370000.json'     #気象庁API（天気概要）
        res = requests.get(url)

        print(res.text)     #天気概要の表示

        #csvを読み込んで一旦全ての観光地を表示。
        filename = 'tourist-attraction.csv'
        with open(filename, encoding='utf-8', newline='') as f:
            csvreader = csv.reader(f, quotechar="'", quoting=csv.QUOTE_NONNUMERIC)
            for row in csvreader:
                print(row)

        #weathercodeで場合分け
        weathercode = ["102", "103", "104", "105", "106", "107", "108", "112", "113", "114", "115", "116", "117", "118", "119", "123", "124", "125", "126", "140", "160", "170", "181", "202", "203", "204", "205", "206", "207", "208", "212", "213", "214", "215", "216", "217", "218", "219", "224", "228", "240", "250", "260", "270", "281", "300", "301", "302", "303", "304", "306", "308", "309", "311", "313", "314", "315", "316", "317", "322", "328", "329", "340", "350", "371", "400", "401", "402", "403", "405", "406", "407", "409", "413", "414", "422", "423", "425", "426", "427", "450"]
        for rain in weathercode:
            if rain == weathercode:
                if row == '屋内':
                    print(row) 
            else:
                print(row)
    elif message == '4':
        return
    else:
        return {"type": "message", "text": "Error Message."}