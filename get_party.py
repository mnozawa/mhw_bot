import json
import requests
import configparser

config = configparser.ConfigParser()
config.read('conf.ini')
baseurl = config["DEFAULT"]["Baseurl"]

def get_party(message):
    url = "{}/mhw_api/api/v1/party".format(baseurl)
    response = requests.get(url).text
    res_dict = json.loads(response)
    m = "\n".join(["```{}\n・{}```".format(i["name"], 
        "\n・".join(i["members"])) for i in res_dict])
    return m

if __name__ == '__main__':
    get_party("test")