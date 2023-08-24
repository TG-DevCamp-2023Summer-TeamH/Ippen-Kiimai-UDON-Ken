def stamp_call(user_id):
    data = [
        {
            "type": "text", 
            "text": "うどんスタンプラリーへようこそ！\n現在地を送信することでスタンプを押せます。\n\nこのアカウントをブロックすると、スタンプの獲得情報がすべて消去されますのでご注意ください。", 
            "quickReply": {
                "items": [
                    {
                        "type": "action", 
                        "action": {
                            "type": "location", 
                            "label": "スタンプを押す"
                        }
                    },
                    {
                        "type": "action",
                        "action": {
                            "type": "uri",
                            "label": "スタンプを確認する",
                            "uri": "https://161e-2400-2653-4983-b700-7da1-1b56-4cf8-5dfe.ngrok-free.app/line_bot/stamp/" + user_id,
                        }
                    }
                ]
            }
        }
    ]
    return data

def callAgain(user_id):
    data = [
        {
            "type": "text", 
            "text": "スタンプ登録に失敗しました。\nもう少し店舗に近づいてお試しください。\nまた、営業時間内のみスタンプを獲得できます。", 
            "quickReply": {
                "items": [
                    {
                        "type": "action", 
                        "action": {
                            "type": "location", 
                            "label": "もう一度スタンプを押す"
                        }
                    },
                    {
                        "type": "action",
                        "action": {
                            "type": "uri",
                            "label": "スタンプを確認する",
                            "uri": "https://161e-2400-2653-4983-b700-7da1-1b56-4cf8-5dfe.ngrok-free.app/line_bot/stamp/" + user_id,
                        }
                    }
                ]
            }
        }
    ]
    return data

def successStamp(user_id, shop_name):
    data = [
        {
            "type": "text", 
            "text": shop_name + " のスタンプを獲得しました！\n以下ボタンより今までに獲得したスタンプを確認できます。", 
            "quickReply": {
                "items": [
                    {
                        "type": "action",
                        "action": {
                            "type": "uri",
                            "label": "スタンプを確認する",
                            "uri": "https://161e-2400-2653-4983-b700-7da1-1b56-4cf8-5dfe.ngrok-free.app/line_bot/stamp/" + user_id,
                        }
                    }
                ]
            }
        }
    ]
    return data

def doubleStamp(user_id, shop_name):
    data = [
        {
            "type": "text", 
            "text": shop_name + " のスタンプは既に登録されています。\n以下ボタンより今までに獲得したスタンプを確認できます。", 
            "quickReply": {
                "items": [
                    {
                        "type": "action",
                        "action": {
                            "type": "uri",
                            "label": "スタンプを確認する",
                            "uri": "https://161e-2400-2653-4983-b700-7da1-1b56-4cf8-5dfe.ngrok-free.app/line_bot/stamp/" + user_id,
                        }
                    }
                ]
            }
        }
    ]
    return data