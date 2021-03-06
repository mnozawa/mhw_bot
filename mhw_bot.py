import discord
import configparser

from get_weapon import *
from get_list import *
from use_weapon import *
from get_history import *
from reset_history import *
from get_party import *
from entry_hunter import *
from get_players import *
from refresh_party import *

config = configparser.ConfigParser()
config.read('conf.ini')
token = config["DEFAULT"]["Token"]
client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    
@client.event
async def on_message(message):
    if client.user != message.author:
        prefix_monster_hanter = "/mhw"
        if message.content.startswith(prefix_monster_hanter):
            content = message.content
            try:
                command = content.split(" ")[1]
            except:
                command = "none"
            if command == "none":
                res = get_weapon(message)
            elif command == "list":
                res = get_list(message)
            elif command == "use":
                res = use_weapon(message, True)
            elif command == "disuse":
                res = use_weapon(message, False)
            elif command == "history":
                res = get_history(message)
            elif command == "reset":
                res = reset_history(message)
            elif command == "party":
                res = get_party(message)
            elif command == "entry":
                res = entry_hunter(message, True)
            elif command == "disentry":
                res = entry_hunter(message, False)
            elif command == "players":
                res = get_players()
            elif command == "refresh":
                res = refresh_party()
            else:
                res = get_weapon(message)
            m = message.author.mention + "\n"
            m += res
            await client.send_message(message.channel, m)

client.run(token)