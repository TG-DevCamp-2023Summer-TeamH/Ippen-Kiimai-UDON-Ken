def kagawa():
       data = [
            {
                "type": "text",
                "text": "現在地を以下のクイックリプライから選択してください。",
                "quickReply": {
                    "items":[
                        {
                            "type": "action",
                            "action": {
                                "type": "message",
                                "label": "高松市",
                                "text": "1-0高松市内の観光地",
                            }
                            
                        },
                        {
                            "type": "action",
                            "action": {
                                "type": "message",
                                "label": "中讃",
                                "text": "1-1中讃地域の観光地",
                            }
                        },
                        {
                            "type": "action",
                            "action": {
                                "type": "message",
                                "label": "西讃",
                                "text": "1-2西讃地域の観光地",
                            }
                        },
                        {
                            "type": "action",
                            "action": {
                                "type": "message",
                                "label": "東讃",
                                "text": "1-3東讃地域の観光地",
                            }
                        },
                        {
                            "type": "action",
                            "action": {
                                "type": "message",
                                "label": "島しょ部",
                                "text": "1-4島しょ部の観光地",
                            }
                        },
                    ]
                }
            }
        ]
       return data

def takamatuCity():
       data = [ 
       {
                "type": "text",
                "text": "以下よりエリア名を選択してください。",
                "quickReply": {
                    "items":[
                        {
                            "type": "action",
                            "action": {
                                "type": "message",
                                "label": "市街地・北部（サンポート・高松駅周辺・栗林）",
                                "text": "1-0-0市街地・北部（サンポート・高松駅周辺・栗林）の観光地",
                            }
                            
                        },
                        {
                            "type": "action",
                            "action": {
                                "type": "message",
                                "label": "中央部（仏生山・太田）",
                                "text": "1-0-1中央部（仏生山・太田）の観光地",
                            }
                        },
                        {
                            "type": "action",
                            "action": {
                                "type": "message",
                                "label": "北東部（屋島・牟礼）",
                                "text": "1-0-2北東部（屋島・牟礼）の観光地",
                            }
                        },
                        {
                            "type": "action",
                            "action": {
                                "type": "message",
                                "label": "東部（十河・植田）",
                                "text": "1-0-3東部（十河・植田）の観光地",
                            }
                        },
                        {
                            "type": "action",
                            "action": {
                                "type": "message",
                                "label": "南部（香南・塩江）",
                                "text": "1-0-4南部（香南・塩江）の観光地",
                            }
                        },
                        {
                            "type": "action",
                            "action": {
                                "type": "message",
                                "label": "西部（国分寺・円座）",
                                "text": "1-0-5西部（国分寺・円座）の観光地",
                            }
                        },
                        {
                            "type": "action",
                            "action": {
                                "type": "message",
                                "label": "北西部（下笠居・香西）",
                                "text": "1-0-6北西部（下笠居・香西）の観光地",
                            }
                        },
                    ]
                }
            }
        ]
       return data

def chusan():
        data = [ 
       {
                "type": "text",
                "text": "以下よりエリア名を選択してください。",
                "quickReply": {
                    "items":[
                        {
                            "type": "action",
                            "action": {
                                "type": "message",
                                "label": "丸亀市",
                                "text": "1-1-0丸亀市の観光地",
                            }
                            
                        },
                        {
                            "type": "action",
                            "action": {
                                "type": "message",
                                "label": "坂出市",
                                "text": "1-1-1坂出市の観光地",
                            }
                        },
                        {
                            "type": "action",
                            "action": {
                                "type": "message",
                                "label": "善通寺市",
                                "text": "1-1-2善通寺市の観光地",
                            }
                        },
                        {
                            "type": "action",
                            "action": {
                                "type": "message",
                                "label": "綾歌郡綾川町",
                                "text": "1-1-3綾歌郡綾川町の観光地",
                            }
                        },
                        {
                            "type": "action",
                            "action": {
                                "type": "message",
                                "label": "仲多度郡多度津町",
                                "text": "1-1-4仲多度郡多度津町の観光地",
                            }
                        },
                        {
                            "type": "action",
                            "action": {
                                "type": "message",
                                "label": "綾歌郡宇多津町",
                                "text": "1-1-5綾歌郡宇多津町の観光地",
                            }
                        },
                        {
                            "type": "action",
                            "action": {
                                "type": "message",
                                "label": "仲多度郡まんのう町",
                                "text": "1-1-6仲多度郡まんのう町の観光地",
                            }
                        },
                        {
                            "type": "action",
                            "action": {
                                "type": "message",
                                "label": "仲多度郡琴平町",
                                "text": "1-1-7仲多度郡琴平町の観光地",
                            }
                        },
                    ]
                }
            }
        ]
        return data

def seisan():
       data = [ 
       {
                "type": "text",
                "text": "以下よりエリア名を選択してください。",
                "quickReply": {
                    "items":[
                        {
                            "type": "action",
                            "action": {
                                "type": "message",
                                "label": "三豊市",
                                "text": "1-2-0三豊市の観光地",
                            }
                            
                        },
                        {
                            "type": "action",
                            "action": {
                                "type": "message",
                                "label": "観音寺市",
                                "text": "1-2-1観音寺市の観光地",
                            }
                        },
                    ]
                }
            }
        ]
       return data

def tousan():
       data = [ 
       {
                "type": "text",
                "text": "以下よりエリア名を選択してください。",
                "quickReply": {
                    "items":[
                        {
                            "type": "action",
                            "action": {
                                "type": "message",
                                "label": "さぬき市",
                                "text": "1-3-0さぬき市の観光地",
                            }
                            
                        },
                        {
                            "type": "action",
                            "action": {
                                "type": "message",
                                "label": "東かがわ市",
                                "text": "1-3-1東かがわ市の観光地",
                            }
                        },
                        {
                            "type": "action",
                            "action": {
                                "type": "message",
                                "label": "木田郡三木町",
                                "text": "1-3-2木田郡三木町の観光地",
                            }
                        },
                    ]
                }
            }
        ]
       return data

def shima():
       data = [ 
       {
                "type": "text",
                "text": "以下よりエリア名を選択してください。",
                "quickReply": {
                    "items":[
                        {
                            "type": "action",
                            "action": {
                                "type": "message",
                                "label": "小豆島",
                                "text": "1-4-0小豆島の観光地",
                            }
                            
                        },
                        {
                            "type": "action",
                            "action": {
                                "type": "message",
                                "label": "直島",
                                "text": "1-4-1直島の観光地",
                            }
                        },
                        {
                            "type": "action",
                            "action": {
                                "type": "message",
                                "label": "豊島",
                                "text": "1-4-2豊島の観光地",
                            }
                        },
                    ]
                }
            }
        ]
       return data

       
        
       
      
