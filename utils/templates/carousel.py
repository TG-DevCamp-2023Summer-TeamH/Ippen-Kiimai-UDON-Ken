def carousel(altText, getData, label_name):
    data = [
        {
            "type": "template",
            "altText": altText,
            "template": {
                "type": "carousel",
                "columns": []
            }
        }
    ]
    for i in range(len(getData)):
        pushData = [
            {
                "title": getData[i][0],
                "text": getData[i][1],
                "actions": [
                    {
                        "type": "uri",
                        "label": label_name,
                        "uri": getData[i][2]
                    }
                ]
            },]
        data[0]["template"]["columns"].extend(pushData)
    return data