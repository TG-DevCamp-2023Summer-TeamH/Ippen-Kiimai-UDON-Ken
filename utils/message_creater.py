from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json          #json形式の読み込み
import csv          #csvの読み込み
import requests      #気象庁API読み込みに使用


def create_single_text_message(message):
    if message[0] == '1':
        json_data = json.load(open('templates/json/udon_search_pref.json', 'r'))
        message = [json_data]
        return message
    elif message[0] == '2':
        return
    elif message == '観光地を調べる':
        sightseeing_message = [
            {
                "type": "text",
                "text": "現在地を以下のクイックリプライから選択するか送信してください。"
                "quickReply": {
                    "items":[
                        {
                            "type": "action",
                            "action": {
                                "type": "message",
                                "label": "高松市",
                                "text": "0",
                            }
                        },
                        {
                            "type": "action",
                            "action": {
                                "type": "message",
                                "label": "中讃",
                                "text": "1",
                            }
                        },
                        {
                            "type": "action",
                            "action": {
                                "type": "message",
                                "label": "西讃",
                                "text": "2",
                            }
                        },
                        {
                            "type": "action",
                            "action": {
                                "type": "message",
                                "label": "東讃",
                                "text": "3",
                            }
                        },
                        {
                            "type": "action",
                            "action": {
                                "type": "message",
                                "label": "島しょ部",
                                "text": "4",
                            }
                        },
                    ]
                }
            }
        ]
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
        if res in weathercode:
            print()
        else:
            print()
            
    elif message == 'お土産を見つける':
        return