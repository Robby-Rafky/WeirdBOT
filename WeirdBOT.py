import discord
from BOTrequiredDataPrivate import *

client = discord.Client()
pogD_token = True


@client.event
async def on_ready():
    print("Started Successfully")


@client.event
async def on_message(message):
    if message.author != client.user:
        global pogD_token

        if str(message.author) == weird_recipient:
            await message.add_reaction(emote_weird)

        if message.content == emote_pogD:
            if pogD_token:
                pogD_token = False
                await message.channel.send("<:botPogD:937903199698952233>")
        else:
            pogD_token = True

client.run(bot_key)
