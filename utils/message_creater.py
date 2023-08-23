from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json          #json形式の読み込み
import csv          #csvの読み込み
import requests      #気象庁API読み込みに使用
from .templates.search_templates import u_pref, u_tak, u_chu, u_nis, u_hig, shopData, today_tomorrow
import datetime

def create_message(message):
    if message[0] == '1':
        if message[4].isdecimal() or message[4] == 'a':
            now = datetime.datetime.now()
            day = {0: 21, 1: 25, 2: 29, 3: 33, 4: 37, 5: 41, 6: 17}
            today_row = day[now.weekday()]
            now_time = str('{:02}'.format(now.hour)) + str('{:02}'.format(now.minute))
            now_time = int(now_time)
            if message[5] == 'm':
                if now.weekday() == 6:
                    today_row -= 24
                else:
                    today_row += 4
                now_time = 1200
            elif message[5] == 'd':
                now_time = 1200
            print(now_time)
            filedata = shopData()
            pickdata = []
            text = "エリア内現在営業中店舗のトップ3に絞って出力しています。\n\n香川県のうどん屋は玉数がなくなり次第終了という店舗が多いため、営業中と書かれていてもすでに営業が終了している場合がございます。\n予めご了承ください。\n"
            if message[4] == 'a':
                if message[2] == 'a':
                    for i in filedata:
                        if i[today_row] != "定休日" and i[today_row] != "営業時間情報無し":
                            if int('{:02}'.format(i[today_row]) + '{:02}'.format(i[today_row + 1])) <= now_time and int('{:02}'.format(i[today_row + 2]) + '{:02}'.format(i[today_row + 3])) >= now_time:
                                pickdata.append(i)
                else:
                    for i in filedata:
                        if message[2] == i[5] and i[today_row] != "定休日" and i[today_row] != "営業時間情報無し":
                            if int('{:02}'.format(i[today_row]) + '{:02}'.format(i[today_row + 1])) <= now_time and int('{:02}'.format(i[today_row + 2]) + '{:02}'.format(i[today_row + 3])) >= now_time:
                                pickdata.append(i)
            else:
                for i in filedata:
                    if message[2] == i[5] and message[4] == i[8] and i[today_row] != "定休日" and i[today_row] != "営業時間情報無し":
                        if int('{:02}'.format(i[today_row]) + '{:02}'.format(i[today_row + 1])) <= now_time and int('{:02}'.format(i[today_row + 2]) + '{:02}'.format(i[today_row + 3])) >= now_time:
                            pickdata.append(i)
            if len(pickdata) != 0:
                for i in range(len(pickdata)):
                    index = i
                    for l in range(i, len(pickdata)):
                        if pickdata[index][15] < pickdata[l][15] or pickdata[index][15] == pickdata[l][15] and pickdata[index][16] < pickdata[l][16]:
                            index = l
                    tmp = pickdata[i]
                    pickdata[i] = pickdata[index]
                    pickdata[index] = tmp
                emoji = {0: '🥇', 1: '🥈', 2:'🥉'}
                for i in range(len(pickdata)):
                    if i >= 3:
                        break
                    text += "\n" + emoji[i] + pickdata[i][1]
            else:
                text += "\n該当する施設が見つかりませんでした。"
            data = [{"type": "text", "text": text, "quickReply": today_tomorrow(message[2], message[4])}]
        else:
            if message[2] == '0':
                data = u_tak()
            elif message[2] == '1':
                data = u_chu()
            elif message[2] == '2':
                data = u_nis()
            elif message[2] == '3':
                data = u_hig()
            else:
                data = u_pref()
        return data
    elif message == '2':
        return

    elif message == '観光地を調べる':
        sightseeing_message = [
            {
                "type": "text",
                "text": "現在地を以下のクイックリプライから選択するか送信してください。",
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
