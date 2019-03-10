import json
import requests
import configparser

config = configparser.ConfigParser()
config.read('conf.ini')
baseurl = config["DEFAULT"]["Baseurl"]

weapon_map_table = {
    1: "大剣",
    2: "太刀",
    3: "片手",
    4: "双剣",
    5: "槌",
    6: "笛",
    7: "槍",
    8: "銃槍",
    9: "剣斧",
    10: "盾斧",
    11: "棒",
    12: "軽",
    13: "重",
    14: "弓"
}

def use_weapon(message, isUse):
    author_id = message.author.id
    weapon_id = message.content.split(" ")[2]
    request_dict = {
        "weaponId": int(weapon_id),
        "isUse": isUse
    }
    print(json.dumps(request_dict))
    url = "{}/mhw_api/api/v1/weapon/isUse/{}".format(baseurl, author_id)
    response = requests.put(url, json.dumps(request_dict), headers={'Content-Type': 'application/json'}).text
    weapon_name = weapon_map_table.get(int(weapon_id), "無")
    if isUse:
        m = "{}を選択肢に追加しました。".format(weapon_name)
    else:
        m = "{}を選択肢から除外しました".format(weapon_name)
    return m

if __name__ == '__main__':
    use_weapon("test", True)