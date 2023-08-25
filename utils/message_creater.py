from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .templates.tourist_attractiondata import takamatuCity, chusan, seisan, tousan, shima, spotData, kagawa, weather, noweather
from .templates.souvenir_templates import category, souvenir
import json          #json形式の読み込み
import csv          #csvの読み込み
import requests      #気象庁API読み込みに使用
from .templates.search_templates import u_pref, u_tak, u_chu, u_nis, u_hig, shopData, today_tomorrow
from .templates.stamp_templates import stamp_call
import datetime
from geopy.distance import geodesic

def create_message(message, user_id):
    now = datetime.datetime.now()
    now_time = str('{:02}'.format(now.hour)) + str('{:02}'.format(now.minute))
    now_time = int(now_time)
    day = {0: 21, 1: 25, 2: 29, 3: 33, 4: 37, 5: 41, 6: 17}
    today_row = day[now.weekday()]
    if message[0] == '1':
        if message[4].isdecimal() or message[4] == 'a':
            now_time = str('{:02}'.format(now.hour)) + str('{:02}'.format(now.minute))
            now_time = int(now_time)
            text = "エリア内現在営業中店舗のトップ5を出力しています。"
            if message[5] == 'm':
                text = "前回使用条件の営業日を明日に変えて再検索したものを出力しています。"
                if now.weekday() == 6:
                    today_row -= 24
                else:
                    today_row += 4
                now_time = 1200
            elif message[5] == 'd':
                text = "前回使用条件の営業日を本日に変えて再検索したものを出力しています。"
                now_time = 1200
            print(now_time)
            filedata = shopData()
            pickdata = []
            text += "\n\n香川県のうどん屋は玉数がなくなり次第終了という店舗が多いため、営業中と書かれていてもすでに営業が終了している場合がございます。\n予めご了承ください。\n"
            if message[4] == 'a':
                if message[2] == 'a':
                    for i in filedata:
                        if i[today_row] != "定休日" and i[today_row] != "営業時間情報無し":
                            if message[5] == "d" or message[5] == "m" or int(str(i[today_row]) + '{:02}'.format(i[today_row + 1])) <= now_time and int(str(i[today_row + 2]) + '{:02}'.format(i[today_row + 3])) >= now_time:
                                pickdata.append(i)
                else:
                    for i in filedata:
                        if message[2] == i[5] and i[today_row] != "定休日" and i[today_row] != "営業時間情報無し":
                            if message[5] == "d" or message[5] == "m" or int(str(i[today_row]) + '{:02}'.format(i[today_row + 1])) <= now_time and int(str(i[today_row + 2]) + '{:02}'.format(i[today_row + 3])) >= now_time:
                                pickdata.append(i)
            else:
                for i in filedata:
                    if message[2] == i[5] and message[4] == i[8] and i[today_row] != "定休日" and i[today_row] != "営業時間情報無し":
                        if message[5] == "d" or message[5] == "m" or int(str(i[today_row]) + '{:02}'.format(i[today_row + 1])) <= now_time and int(str(i[today_row + 2]) + '{:02}'.format(i[today_row + 3])) >= now_time:
                            pickdata.append(i)
            if len(pickdata) != 0:
                for i in range(len(pickdata)):
                    index = i
                    for l in range(i, len(pickdata)):
                        if pickdata[index][15] < pickdata[l][15]:
                            index = l
                    tmp = pickdata[i]
                    pickdata[i] = pickdata[index]
                    pickdata[index] = tmp
                for i in range(len(pickdata)):
                    if i >= 5:
                        break
                    text += "\n\n" + str(i + 1) + "位 " + pickdata[i][1] + "\n" + pickdata[i][13] + "\n☆" + pickdata[i][15] + " (" + pickdata[i][16] + "件の口コミ)\n" + pickdata[i][today_row] + ":{:02}".format(pickdata[i][today_row + 1]) + " ～ " + pickdata[i][today_row + 2] + ":{:02}\n".format(pickdata[i][today_row + 3]) + pickdata[i][14]
                print(text)
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
    
    elif message[0] == '2':
        data = stamp_call(user_id)
        return data
    
    elif message[0] == '3':
        current_day = now.weekday()
        if message[4].isdecimal() or message[4] == 'a':
            text = "エリア内の観光スポットトップ5を出力しています。\n\n"
            if message[5] != "w":
                url = 'https://www.jma.go.jp/bosai/forecast/data/forecast/370000.json'     #気象庁API（天気概要）
                response = requests.get(url).json()
                weathercode_list = ["102", "103", "104", "105", "106", "107", "108", "112", "113", "114", "115", "116", "117", "118", "119", "123", "124", "125", "126", "140", "160", "170", "181", "202", "203", "204", "205", "206", "207", "208", "212", "213", "214", "215", "216", "217", "218", "219", "224", "228", "240", "250", "260", "270", "281", "300", "301", "302", "303", "304", "306", "308", "309", "311", "313", "314", "315", "316", "317", "322", "328", "329", "340", "350", "371", "400", "401", "402", "403", "405", "406", "407", "409", "413", "414", "422", "423", "425", "426", "427", "450"]
                weathercode = response[0]["timeSeries"][0]["areas"][0]["weatherCodes"][0]
                reply = noweather(message[2], message[4])
                if weathercode in weathercode_list:
                    text += "本日の天気は雨または雪予報ですので、屋内の観光スポットに絞っています。\n"
                    allplacedata = spotData()
                    placedata = []
                    for place in allplacedata:
                        if place[17] == "屋内":
                            placedata.append(place)
                else:
                    text += "屋内外の観光スポットを表示しています。\n"
                    placedata = spotData()
            else:
                text += "屋内外の観光スポットを表示しています。\n"
                placedata = spotData()
                reply = weather(message[2], message[4])
            for i in range(len(placedata)):
                index = i
                for l in range(i, len(placedata)):
                    if placedata[index][15] < placedata[l][15]:
                        index = l
                tmp = placedata[i]
                placedata[i] = placedata[index]
                placedata[index] = tmp
            pickdata = []
            if message[4] == 'a':
                if message[2] == 'a':
                    pickdata = placedata
                else:
                    for i in placedata:
                        if i[5] == message[2]:
                            pickdata.append(i)
            else:
                for i in placedata:
                    if i[5] == message[2] and i[8] == message[4]:
                        pickdata.append(i)
            if len(pickdata) != 0:
                for i in range(len(pickdata)):
                    if i >= 5:
                        break
                    text += "\n\n" + str(i + 1) + "位 " + pickdata[i][1] + "\n" + pickdata[i][13] + "\n☆" + pickdata[i][15] + " (" + pickdata[i][16] + "件の口コミ)\n" + pickdata[i][today_row + 2] + ":{:02}".format(pickdata[i][today_row + 3]) + " ～ " + pickdata[i][today_row + 4] + ":{:02}\n".format(pickdata[i][today_row + 5]) + pickdata[i][14]
            else:
                text += "\n\n該当する施設が見つかりませんでした。"
            data = [{"type": "text", "text": text, "quickReply": reply}]
        else:
            if message[2] == '0':
                data = takamatuCity()
            elif message[2] == '1':
                data =  chusan()
            elif message[2] == '2':
                data = seisan()
            elif message[2] == '3':
                data = tousan()
            elif message[2] == '4':
                data = shima()
            else:
                data = kagawa()
        return data

    elif message[0] == '4':
        products = souvenir()
        category_id = products[2]
        
        text = "お土産リスト\n※価格は作成時にECサイトで表示されている最安値価格を使用しております。値上げなどがされている場合はご容赦ください。"
        print(products)
        for i in products:
            if category_id[2] == '1':
                text = '焼き菓子のお土産一覧です。'
                text += "\n\n" + i[1] + "\n" + i[2] + "\n" + i[3] + "\n" + i[4] + "\n" + i[5]
                data = [{"type": "text", "text": text, "type": text, "type": text, "type": text, "type": text, "quickReply": reply}]
            elif category_id[2] == '2':
                text = "和菓子のお土産一覧です。"
                text += "\n\n" + i[1] + "\n" + i[2] + "\n" + i[3] + "\n" + i[4] + "\n" + i[5]
                data = [{"type": "text", "text": text, "type": text, "type": text, "type": text, "type": text, "quickReply": reply}]
            elif category_id[2] == '3':
                text = "麵類のお土産一覧です。"
                text += "\n\n" + i[1] + "\n" + i[2] + "\n" + i[3] + "\n" + i[4] + "\n" + i[5]
                data = [{"type": "text", "text": text, "type": text, "type": text, "type": text, "type": text, "quickReply": reply}]
            elif category_id[2] == '4':
                text = "飲み物のお土産一覧です。"
                text += "\n\n" + i[1] + "\n" + i[2] + "\n" + i[3] + "\n" + i[4] + "\n" + i[5]
                data = [{"type": "text", "text": text, "type": text, "type": text, "type": text, "type": text, "quickReply": reply}]
            elif category_id[2] == '5':
                text = "調味料・食品のお土産一覧です。"
                text += "\n\n" + i[1] + "\n" + i[2] + "\n" + i[3] + "\n" + i[4] + "\n" + i[5]
                data = [{"type": "text", "text": text, "type": text, "type": text, "type": text, "type": text, "quickReply": reply}]
            elif category_id[2] == '6':
                text = "骨付きどりのお土産一覧です。"
                text += "\n\n" + i[1] + "\n" + i[2] + "\n" + i[3] + "\n" + i[4] + "\n" + i[5]
                data = [{"type": "text", "text": text, "type": text, "type": text, "type": text, "type": text, "quickReply": reply}]
            else:
                text = "スナック菓子お土産一覧です。"
                text += "\n\n" + i[1] + "\n" + i[2] + "\n" + i[3] + "\n" + i[4] + "\n" + i[5]
                data = [{"type": "text", "text": text, "type": text, "type": text, "type": text, "type": text, "quickReply": reply}]
            print(i)
            text += "\n\n" + i[1] + "\n" + i[2] + "\n" + i[3] + "\n" + i[4] + "\n" + i[5]
        data = [{"type": "text", "text": text, "type": text, "type": text, "type": text, "type": text, "quickReply": reply}]
        return data

    def display_products_by_category(category_id, data):
        products = []
        for product in data:
            if product["カテゴリID"] == category_id:
                products.append(product)
        return products
    
    def handle_message(event):
        user_input = event.message.text

        found_products = display_products_by_category(user_input, data)

        if found_products:
            reply_message = ''
            for product in found_products:
                reply_message += f"商品名: {product['商品の名前']}, 金額: {product['金額']}円, ECサイトリンク: {product['ECサイト']}\n\n"
                
            category(
                event.reply_token,
                text = reply_message
            )
        
        else:
            category(
                event.reply_token,
                text = "該当する商品はありません。"
            )