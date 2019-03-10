import json
import requests
import configparser

config = configparser.ConfigParser()
config.read('conf.ini')
baseurl = config["DEFAULT"]["Baseurl"]

def get_list(message):
    author_id = message.author.id
    url = "{}/mhw_api/api/v1/weapon/list/{}".format(baseurl, author_id)
    response = requests.get(url).text.encode("utf-8")
    res_dict = json.loads(response)
    m = "\n".join(["{}. {}".format(i["id"], i["name"]) for i in res_dict])
    return m

if __name__ == '__main__':
    get_list("test")