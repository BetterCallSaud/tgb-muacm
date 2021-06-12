import discord
import requests
import random
trivia_api = [
              "https://opentdb.com/api.php?amount=1&category=15" # Video Games
              "https://opentdb.com/api.php?amount=1&category=18", # Science Computer
              "https://opentdb.com/api.php?amount=1&category=30" # Science & Gadgets
              ]
client = discord.Client()

@client.event
async def on_message(message):
    if client.user == message.author:
        return

    if message.content.lower() == "tgb trivia":
        res = requests.get(random.choice(trivia_api))
        data = res.json()
        val = data["results"][0]["question"] + "\n**Answer :-  **" + data["results"][0]["correct_answer"]
        embed = discord.Embed(colour=discord.Colour.random())
        embed.add_field(name="**Trivia**", value=val)
        await message.channel.send(embed=embed)
