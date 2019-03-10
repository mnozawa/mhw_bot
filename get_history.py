import json
import requests
import configparser

config = configparser.ConfigParser()
config.read('conf.ini')
baseurl = config["DEFAULT"]["Baseurl"]

def get_history(message):
    age = 10
    author_id = message.author.id
    url = "{}/mhw_api/api/v1/weapon/history/{}".format(baseurl, author_id)
    response = requests.get(url).text.encode("utf-8")
    res_dict = json.loads(response)
    m = "```"
    m += "\n".join(["{:>2}.{:・<9}・{}".format(i["id"], i["name"], i["selectTime"]) for i in res_dict[0:age]])
    m +="```"
    if m == "``````":
        m = "履歴がないニャ\nまずはひと狩りいってくるニャ！"
    return m

if __name__ == '__main__':
    get_history("test")