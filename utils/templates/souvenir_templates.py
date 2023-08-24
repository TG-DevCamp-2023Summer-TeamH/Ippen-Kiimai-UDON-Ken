def category():
    data = [
        {
            "type": "text",
            "text": "気になるお土産のカテゴリーを以下のクイックリプライから選択してください。",
            "quickReply": {
                "items":[
                    {
                        "type": "action",
                        "action": {
                            "type": "message",
                            "label": "焼き菓子",
                            "text": "4-1香川県の焼き菓子のお土産"
                        }
                    },
                    {
                        "type": "action",
                        "action": {
                            "type": "message",
                            "label": "和菓子",
                            "text": "4-2香川県の和菓子のお土産"
                        }
                    },
                    {
                        "type": "action",
                        "action": {
                            "type": "message",
                            "label": "麺類",
                            "text": "4-3香川県の麺類のお土産"
                        }
                    },
                    {
                        "type": "action",
                        "action": {
                            "type": "message",
                            "label": "飲み物",
                            "text": "4-4香川県の飲み物のお土産"
                        }
                    },
                    {
                        "type": "action",
                        "action": {
                            "type": "message",
                            "label": "調味料・食品",
                            "text": "4-5香川県の調味料・食品のお土産"
                        }
                    },
                    {
                        "type": "action",
                        "action": {
                            "type": "message",
                            "label": "骨付きどり",
                            "text": "4-6香川県の骨付きどりのお土産"
                        }
                    },{
                        "type": "action",
                        "action": {
                            "type": "message",
                            "label": "スナック菓子",
                            "text": "4-7香川県のスナック菓子のお土産"
                        }
                    },
                ]
            }
        }
    ]
    return data
