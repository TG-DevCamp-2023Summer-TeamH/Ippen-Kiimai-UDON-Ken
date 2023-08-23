def create_single_text_message(message):
    if message == 'うどんの店舗を検索する':
        test_message = [
            {
                "type": "text",
                "text": "sample quick reply!",
                "quickReply": {
                    "items": [
                        {
                            "type": "action",
                            "action": {
                                "type": "message",
                                "label": "高松市内",
                                "text": "高松市内"
                            }
                        },
                        {
                            "type": "action",
                            "action": {
                                "type": "message",
                                "label": "中讃（丸亀）",
                                "text": "中讃（丸亀）"
                            }
                        }
                    ]
                }
            }
        ]
        return test_message
    elif message == 'うどんスタンプラリーを開く':
        return
    elif message == '観光地を調べる':
        return
    elif message == 'お土産を見つける':
        return