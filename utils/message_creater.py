from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .templates.tourist_attractiondata import takamatuCity, chusan, seisan, tousan, shima, spotData
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
    if message[0] == '1':
        if message[4].isdecimal() or message[4] == 'a':
            today_row = day[now.weekday()]
            now_time = str('{:02}'.format(now.hour)) + str('{:02}'.format(now.minute))
            now_time = int(now_time)
            text = "エリア内現在営業中店舗のトップ5に絞って出力しています。"
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
                data = [{"type": "text", "text": text, "quickReply": today_tomorrow(message[2], message[4])}]
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
        current_day = int(datetime.datetime.now().strftime("%A"))
        url = 'https://www.jma.go.jp/bosai/forecast/data/overview_forecast/370000.json'     #気象庁API（天気概要）
        response = requests.get(url)
        weather_data = response.json()
            #weathercodeで場合分け
        weathercode_list = ["102", "103", "104", "105", "106", "107", "108", "112", "113", "114", "115", "116", "117", "118", "119", "123", "124", "125", "126", "140", "160", "170", "181", "202", "203", "204", "205", "206", "207", "208", "212", "213", "214", "215", "216", "217", "218", "219", "224", "228", "240", "250", "260", "270", "281", "300", "301", "302", "303", "304", "306", "308", "309", "311", "313", "314", "315", "316", "317", "322", "328", "329", "340", "350", "371", "400", "401", "402", "403", "405", "406", "407", "409", "413", "414", "422", "423", "425", "426", "427", "450"]
        weathercode = int(weather_data.get("timeSeries")[0].get("areas")[0].get("wheatherCodes")[0])
        if message[4].isdecimal() or message[4] == 'a':
                pickedata = []
                text = "エリア内には以下のスポットがあります。"
                if message[4] == 'a':
                    for i in filedata:
                        if message[2] == i[5]:
                            pickedata.append(i)
                else:
                    for i in filedata:
                        if message[2] == i[5] and message[4] == i[8]:
                            pickedata.append(i)
                for i in range(len(pickedata)):
                    for l in range(i, len(pickedata)):
                        index = i
                        if pickedata[15] < pickedata[i][15]: 

                            for i in pickedata:
                                text += "\n" + i[1]
                        data = [{"type": "text", "text": text}]
                        return data
                else:
                    if message[2] == '0':
                        data = takamatuCity()
                    elif message[2] == '1':
                        data =  chusan()
                    elif message[2] == '2':
                        data = seisan()
                    elif message[2] == '3':
                        data = tousan()
                    else:
                        data = shima()
                    return data

        def parse_hours(hours_str):
                parsed_hours = []
                for time_range in hours_str.split():
                    start_time, end_time = time_range.split("-")
                    start_hour, start_minute = map(int, end_time.split(":"))
                    end_hour, end_minute = map(int, end_time.split(":"))
                    parsed_hours.append((start_hour, start_minute, end_hour, end_minute))
                return parsed_hours
            
        def is_shop_open(opening_hours, current_time):
                for start_hour, start_minute, end_hour, end_minute in opening_hours:
                    start_time = datetime.strptime(f"{start_hour:02d}:{start_minute:02d}", "%H:%M").time()
                    end_time = datetime.strptime(f"{end_hour:02d}:{end_minute:02d}", "%H:%M").time()

                    if start_time <= current_time <= end_time:
                        return True
                    
                return False
            
        data = spotData()
        for line in data:
                    if day == current_day:
                        if now_time:
                            opening_hours = parse_hours(now_time)
                            if is_shop_open(opening_hours, now_time):
                                print(f"観光スポットは{current_day}に現在営業しています。")
                            else:
                                print(f"観光スポットは{current_day}に現在営業していません。")
                        else:
                            print("観光スポットは定休日です。")
                        break

        if weathercode in weathercode_list:
                print('屋外の観光スポットは以下の通りです。\n')
                data = [{"type": "text", "text": text, "quickReply": today_tomorrow(message[2], message[4])}]
                print(data)
                return data
        else:
                print('屋内の観光スポットは以下の通りです。\n')
                data = [{"type": "text", "text": text, "quickReply": today_tomorrow(message[2], message[4])}]
                print(data)
                return data

    elif message[0] == '4':
        def load_data():
            data = souvenir()
            for product in data:
                    data.append({
                        "商品の名前": souvenir[0],
                        "カテゴリID": souvenir[1],
                        "カテゴリ名": souvenir[2],
                        "金額": souvenir[3],
                        "ECサイト": souvenir[4]
                        })
                    data.append(product)
            return data

    def display_products_by_category(category_id):
        products = []
        for product in data:
            if product["カテゴリID"] == category_id:
                products.append(product)
        return products
    
    def handle_message(event):
        user_input = event.message.text

        found_products = display_products_by_category(user_input)

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

    if __name__ == '__main__':
        data = load_data()
        return data