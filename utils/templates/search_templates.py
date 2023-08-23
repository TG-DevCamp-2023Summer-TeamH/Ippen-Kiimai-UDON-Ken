def pref():
    data = [
        {
            "type": "text",
            "text": "以下より現在地またはエリア名を送信してください。",
            "quickReply": {
                "items": [
                    {
                        "type": "action",
                        "action": {
                            "type": "message",
                            "label": "高松市内",
                            "text": "1-0 高松市内のうどん店を探す"
                        }
                    },
                    {
                        "type": "action",
                        "action": {
                            "type": "message",
                            "label": "中讃（丸亀）",
                            "text": "1-1 中讃のうどん店を探す"
                        }
                    },
                    {
                        "type": "action",
                        "action": {
                            "type": "message",
                            "label": "西讃（三豊）",
                            "text": "1-2 西讃のうどん店を探す"
                        }
                    },
                    {
                        "type": "action",
                        "action": {
                            "type": "message",
                            "label": "東讃（さぬき）",
                            "text": "1-3 東讃のうどん店を探す"
                        }
                    }
                ]
            }
        }
    ]
    return data

def tak():
    data = [
        {
            "type": "text",
            "text": "以下よりエリア名を送信してください。",
            "quickReply": {
                "items": [
                    {
                        "type": "action",
                        "action": {
                            "type": "message",
                            "label": "エリア全域",
                            "text": "1-0-0 市街地・北部のうどん店を探す"
                        }
                    },
                    {
                        "type": "action",
                        "action": {
                            "type": "message",
                            "label": "市街地・北部（サンポート・栗林）",
                            "text": "1-0-0 市街地・北部のうどん店を探す"
                        }
                    },
                    {
                        "type": "action",
                        "action": {
                            "type": "message",
                            "label": "中央部（仏生山・太田）",
                            "text": "1-0-1 中央部のうどん店を探す"
                        }
                    },
                    {
                        "type": "action",
                        "action": {
                            "type": "message",
                            "label": "北東部（屋島・牟礼）",
                            "text": "1-0-2 北東部のうどん店を探す"
                        }
                    },
                    {
                        "type": "action",
                        "action": {
                            "type": "message",
                            "label": "東部（十河・植田）",
                            "text": "1-0-3 東部のうどん店を探す"
                        }
                    },
                    {
                        "type": "action",
                        "action": {
                            "type": "message",
                            "label": "南部（香南・塩江）",
                            "text": "1-0-4 南部のうどん店を探す"
                        }
                    },
                    {
                        "type": "action",
                        "action": {
                            "type": "message",
                            "label": "西部（国分寺・円座）",
                            "text": "1-0-5 西部のうどん店を探す"
                        }
                    },
                    {
                        "type": "action",
                        "action": {
                            "type": "message",
                            "label": "北西部（下笠居・香西）",
                            "text": "1-0-6 北西部のうどん店を探す"
                        }
                    },
                ]
            }
        }
    ]
    return data