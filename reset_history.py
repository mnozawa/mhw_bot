import json
import requests
import configparser

config = configparser.ConfigParser()
config.read('conf.ini')
baseurl = config["DEFAULT"]["Baseurl"]

def reset_history(message):
    author_id = message.author.id
    url = "{}/mhw_api/api/v1/weapon/reset/history/{}".format(baseurl, author_id)
    print(url)
    response = requests.delete(url).text.encode("utf-8")
    print(response)
    m = "武器抽選履歴を消去するニャ！\n新しい気持ちでひと狩り行くニャ！"
    return m

if __name__ == '__main__':
    reset_history("test")