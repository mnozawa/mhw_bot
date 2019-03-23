import json
import requests
import configparser

config = configparser.ConfigParser()
config.read('conf.ini')
baseurl = config["DEFAULT"]["Baseurl"]

def refresh_party():
    pl_url = "{}/mhw_api/api/v1/party/list".format(baseurl)
    response = requests.get(pl_url).text
    players = json.loads(response)

    ent_url = "{}/mhw_api/api/v1/party".format(baseurl)
    for player in players:
        request_dict = {
            "userName": player
        }
        requests.delete(ent_url, data=json.dumps(request_dict), headers={'Content-Type': 'application/json'})
    res = "今日の狩りはここまでだニャ(エントリーを取り消しました)"
    return res

if __name__ == '__main__':
    refresh_party()