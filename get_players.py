import json
import requests
import configparser

config = configparser.ConfigParser()
config.read('conf.ini')
baseurl = config["DEFAULT"]["Baseurl"]

def get_players():
    url = "{}/mhw_api/api/v1/party/list".format(baseurl)
    response = requests.get(url).text
    players = json.loads(response)
    if players == []:
        res = "参加者がいませんニャ"
    else:
        res = "参加者は...\n"
        res += "```{}```".format("\n".join(players))
    return res

if __name__ == '__main__':
    get_players()