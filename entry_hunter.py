import json
import requests
import configparser

config = configparser.ConfigParser()
config.read('conf.ini')
baseurl = config["DEFAULT"]["Baseurl"]


def entry_hunter(message, isEntry):
    hunter_name = message.content.split(" ")[2]
    request_dict = {
        "userName": hunter_name
    }
    url = "{}/mhw_api/api/v1/party".format(baseurl)
    if isEntry:
        requests.post(url, json.dumps(request_dict), headers={'Content-Type': 'application/json'})
        m = "{}が加わりました".format(hunter_name)
    else:
        requests.delete(url, data=json.dumps(request_dict), headers={'Content-Type': 'application/json'})
        m = "{}が離脱しました".format(hunter_name)
    return m

if __name__ == '__main__':
    entry_hunter("test_hunter", True)