from .templates.search_templates import shopData
from .templates.stamp_templates import callAgain, successStamp, doubleStamp
from line_bot.models import LINEFollower
from geopy.distance import geodesic

def set_stamp(message, user_id):
    users = LINEFollower.objects.all()
    for user in users:
        if user.user_id == user_id:
            id = user.id
    user = LINEFollower.objects.get(id = id)
    stamp_data = user.stamp
    shops = shopData()
    now_place = (message["latitude"], message["longitude"])
    print(now_place)
    index = None
    near_value = 999999
    for i in range(len(shops)):
        distance = geodesic(now_place, (float(shops[i][3]), float(shops[i][2]))).m
        print(i, shops[i][1], distance)
        if near_value > distance:
            near_value = distance
            index = i
    print(near_value)
    if near_value > 500:
        index = None
        data = callAgain(user_id)
    else:
        if stamp_data[index] == "0":
            data = successStamp(user_id, shops[index][1])
            new_stamp_data = ""
            for i in range(len(stamp_data)):
                if i == index:
                    new_stamp_data += "1"
                else:
                    new_stamp_data += stamp_data[i]
            user.stamp = new_stamp_data
            user.save()
        elif stamp_data[index] == "1":
            data = doubleStamp(user_id, shops[index][1])
    return data