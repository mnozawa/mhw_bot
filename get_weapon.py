import json
import requests
import configparser

config = configparser.ConfigParser()
config.read('conf.ini')
baseurl = config["DEFAULT"]["Baseurl"]

def get_weapon(message):
    author_id = message.author.id
    url = "{}/mhw_api/api/v1/weapon/{}".format(baseurl, author_id)
    try:
        response = requests.get(url).text.encode("utf-8")
        res_dict = json.loads(response)
        m = "あなたの今日のラッキーウエポンは...{}.{}!!!".format(res_dict["id"], res_dict["weapon"])
    except:
        m = "武器選びに失敗したニャ...ちょっとだけ待ってほしいニャ..."
    return m

if __name__ == '__main__':
    get_weapon("test")