from random import randint
from d20 import roll
import discord
import re

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return 

    if bool(re.fullmatch("roll (\d*)(d\d*)((?:[+*-](?:\d+|\(*\)))*)(?:\+(d\d*))?", message.content)):
        print(message.content)
        result = roll(message.content[5:])
        print(result)
        await message.channel.send('You rolled: ' + str(result))


client.run('bot-token')