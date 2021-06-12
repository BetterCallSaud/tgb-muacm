import discord
import aiohttp
from random import randint
from keep_alive import keep_alive
import pandas as pd
import random
import requests
import json

client = discord.Client()

# TOKEN removed for security purposes
TOKEN = ''

trivia_api = [
              "https://opentdb.com/api.php?amount=1&category=15" # Video Games
              "https://opentdb.com/api.php?amount=1&category=18", # Science Computer
              "https://opentdb.com/api.php?amount=1&category=30" # Science & Gadgets
             ]

user_input = ["tgb hello", "tgb hii", "tgb hi", "tgb bro", "tgb yo", "tgb yoohoo", "tgb hey", "tgb ola", "tgb wassup", "tgb dude", "tgb what up dude", "tgb ciao", "tgb buddy"]

bot_reply = ["Hello", "Heya", "Ciao", "Hey", "Heya, how's it going", "Hey, wassup", "Good to see you", "Great to see you", "Glad to see you", "Look who it is! It's a bird... it's a plane... it's ", "Nice to see you again", "Hi there","Long time no see","Howdy", "Hiya", "Yoohoo", "Ola", "Bonjour","What's going on","Look who it is. It's"]


def quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.content)
    quo = "*" + json_data[0]['q'] + "*\n-**" + json_data[0]['a'] + "**"
    return quo


@client.event
async def on_ready():
    print('Ready {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower() == 'tgb help':
        embed = discord.Embed(
            title="***TGB Help/Command list***",
            description=f"{user_input}\ntgb council\ntgb core\ntgb exec\ntgb contacts\ntgb trivia\ntgb meme\ntgb quote\ntgb bio\ntgb bio:@<user>\ntgb add bio:<ADD_YOUR_BIO_TEXT>*",
            colour=discord.Colour.teal()
        )

        await message.channel.send(embed=embed)

    if message.content.lower() == 'tgb council':
        embed = discord.Embed(
            title="***Council Members***",
            description="***Nishant Gandhi*** >>> Chairman\n***Sarthak Khandelwal*** >>> Vice-Chairman\n***Hiteshi Gupta***  >>> Treasurer",
            colour=discord.Colour.red()
        )
        await message.channel.send(embed=embed)

    if message.content.lower() == 'tgb core':
        embed = discord.Embed(
            title="***Head Members***",
            description="***Saud Hashmi*** -->  Content Head\n***Riya Ahuja*** -->  Management Head\n***Ritika Maheshwari*** -->  Marketing Head\n"
                        "***Mihir Dutta*** -->  Technical Head\n***Samriddhi Kaur*** -->  Graphics Head\n***Yash Sehgal*** -->  Junior Coordinator",
            colour=discord.Colour.blue()
        )
        await message.channel.send(embed=embed)

    if message.content.lower() == 'tgb exec':
        embed = discord.Embed(
            title="***Executives Members***",
            description="*Mayank Verma\nJaspreet Singh Saini\nSamarth Sharma\nAditi Mandlik\nPrateeti Mehta Jain\n"
                        "Rajesh Nathani\nIshika Shahaney\nRaj Soni\nAnushka Jain\nTanisha Jain\nAditi Dandawate\n"
                        "Suchismita Nanda*",
            colour=discord.Colour.green()
        )
        await message.channel.send(embed=embed)

    if message.content.lower() == "tgb contacts":
        embed = discord.Embed(
            title='***Connect us on*** !',
            description='**[Instagram](https://instagram.com/mu_acm?utm_medium=copy_link)**\n\n'
                        '**[LinkedIn](https://www.linkedin.com/company/acm-student-chapter-medicaps/)**'
                        '\n\n**[Website](http://medicaps.hosting.acm.org/)**',
            colour=discord.Colour.orange()
        )
        embed.set_image(url='https://i.ibb.co/YWV5Bx0/Mu-ACMlogo.png')
        await message.channel.send(embed=embed)

    if message.content.lower() == "tgb trivia":
        res = requests.get(random.choice(trivia_api))
        data = res.json()
        val = data["results"][0]["question"] + "\n**Answer: **" + data["results"][0]["correct_answer"]
        embed = discord.Embed(colour=discord.Colour.random())
        embed.add_field(name="**Trivia**", value=val)
        await message.channel.send(embed=embed)

    if message.content.lower() == 'tgb meme':
        await message.channel.send(embed=await pyrandmeme())

    if message.content.lower() == "tgb quote":
        quo = quote()
        embed = discord.Embed(color=discord.Color.random())
        embed.add_field(name="Quote:", value=quo)
        embed.set_footer(text="Requested by {0.author.name}".format(message))
        await message.channel.send(embed=embed)

    if message.content.lower() == 'tgb bio':
        await message.channel.send(tgb_bio(message))

    if 'tgb bio: ' in message.content.lower() and message.content[9] != None:
        code = message.content[9:]
        userid = int(code[3:len(code) - 1])
        await message.channel.send(tgb_bio_with_user(message, userid))

    if ("tgb add bio: " in message.content.lower()) and (message.content[13] != None):
        await message.channel.send(add_bio(message))

    if ("tgb change bio: " in message.content.lower()) and (message.content[16] != None):
        await message.channel.send(change_bio(message))

async def pyrandmeme():
    pymeme = discord.Embed(title="Tech Meme requested", description="Here you go!", color=0x84d4f4)
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/TechMemes/new.json?sort=new') as r:
            res = await r.json()
            pymeme.set_image(url=res['data']['children'][randint(0, 25)]['data']['url'])
            return pymeme
        await pyrandmeme()

def tgb_bio(message):
    df = pd.read_csv(r'bio.csv')
    user = str(message.author)
    users = list(df['user'].values)
    userid = message.author.id
    if user in users:
        return df[df['userid'] == userid].bio.values[0]
    else:
        rtn = f"No bio found for {user}"
        return rtn

def tgb_bio_with_user(message, userid):
    df = pd.read_csv(r'bio.csv')
    user = str(message.author)
    users = list(df['user'].values)
    userid = message.author.id
    if user in users:
        return df[df['userid'] == userid].bio.values[0]
    else:
        rtn = f"No bio found for {user}"
        return rtn

def add_bio(message):
    df = pd.read_csv(r'bio.csv')
    bio = str(message.content[13:])
    user = str(message.author)
    userid = message.author.id
    users = list(df['user'].values)
    if user in users:
        return 'You already have a bio!'
    df.loc[len(df.index)] = [userid, user, bio]
    df.to_csv(r'bio.csv', index=False)
    return 'Bio added!'

def change_bio(message):
    df = pd.read_csv(r'bio.csv')
    new_bio = str(message.content[16:])
    user = str(message.author)
    userid = str(message.author.id)
    users = list(df['user'].values)
    if user in users:
        df.loc[df.userid == userid, 'bio'] = new_bio
        df.to_csv(r'bio.csv', index=False)
        return 'Bio changed!'
    else:
        rtn = f"No bio found for {user}"
        return rtn

keep_alive()
client.run(TOKEN)
