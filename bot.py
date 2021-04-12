import discord
import aiohttp
import time
from random import randint
from keep_alive import keep_alive
import pandas as pd

client = discord.Client()

# TOKEN removed for security purposes
TOKEN = ''

cmdlist = """
TGB Command List:
* tgb hi
* tgb help me
* tgb council
* tgb core
* tgb exec
* tgb trivia
* tgb meme
* tgb bio
* tgb bio: @<user>
* tgb add bio: <ADD_YOUR_BIO_TEXT>
* tgb change bio:<ADD_YOUR_BIO_TEXT>   
"""

council = """
**Council Members:**
Nishant Gandhi - Chairman
Sarthak Khandelwal - Vice-Chairman
Hiteshi Gupta - Treasurer
"""

heads = """
**Head Members:**
Saud Hashmi - Content Head
Riya Ahuja - Management Head
Ritika Maheshwari - Marketing Head
Mihir Dutta - Technical Head
Samriddhi Kaur - Graphics Head
Yash Sehgal - Junior Coordinator
"""

execs = """
**Executive Members:**
Mayank Verma
Jaspreet Singh Saini
Samarth Sharma
Aditi Mandlik
Prateeti mehta jain
Rajesh Nathani
Ishika Shahaney
Raj Soni
Anushka Jain
Tanisha Jain
Aditi Dandawate
Suchismita Nanda
"""

trivia = [
"The Firefox logo isn’t a fox.",
"The first Apple logo isn’t what you would think.",
"Google rents out goats",
"The name for “robot” has dark origins",
"The first-ever VCR was the size of a piano",
"Samsung is 38 years and 1 month older than Apple",
"A Petabyte is a lot of data",
"Domain name registration used to be free",
"Megabytes used to weigh hundreds of pounds",
"The Radio took 38 years to reach an audience of 50 million",
"The first camera needed an incredibly long exposure",
"Credit card chips have been around for a LONG time",
'Google rents out goats',
'The name for “robot” has dark origins',
'The first-ever VCR was the size of a piano',
'Samsung is 38 years and 1 month older than Apple',
'A Petabyte is a lot of data',
'Domain name registration used to be free',
'Megabytes used to weigh hundreds of pounds',
'The Radio took 38 years to reach an audience of 50 million',
'The first camera needed an incredibly long exposure',
'Credit card chips have been around for a LONG time',
'Alexa is always listening to your conversations',
'People read faster or slower depending on what they read from',
'GPS is free for some',
'There are Amish computers',
'Mac computers were named after the apple',
'The first computer mouse wasn’t made from plastic',
'Which came first, Spam mail or Spam meat',
'The original Xbox had sound snippets of real space missions',
'The majority of the people plug in their USB wrong',
'Steve Jobs used sleight of hand at the first iPhone presentation',
'The first alarm clock could only ring at one time',
'Computer Security Day is celebrated on November 30th',
'The government used PlayStation 3’s… but not for gaming',
'The first online gaming was before the year 2000',
'The first product scanned was a packet of chewing gum in 1974',
'You’re in good hands if your surgeon was a gamer',
'iTunes has unusual Terms & Conditions',
'Nintendo didn’t start as a video games company',
'Apollo 11 astronauts couldn’t afford insurance',
'People are still using dial-up',
"You can spell your email in Morse code",
'Yahoo’s original name was a mouthful',
'Everyone uses Google as a spellchecker',
'The first word to ever be auto-corrected was “teh"',
'The Nintendo Game Boy went to space',
'PlayStation 1 had Scratch and Sniff discs',
'“Android” is gender-specific',
'Google searches hit the billions every month',
"There’s a name for when you feel your phone vibrate… but it doesn’t",
'Smoking will void your Apple warranty',
'Technology is now influencing baby names',
'Blind people can use cell phones',
'Google’s first tweet was gibberish',
'The first cell phone call was in New York City',
'The first commercial text message was sent in 1992',
'Over 6,000 new computer viruses are created and released every month',
'There are more likes than photos on Facebook',
'iPhones were almost in the shape of an apple',
'Comic Sans is the most hated font in the world',
'NASA’s internet speed is 91 GB per second',
'Nokia is the largest company from Finland',
'More people have cell phones than toilets',
'The Apple Lisa was the first commercial computer with a Graphical User Interface (GUI) and a mouse',
'Some people are afraid of technology',
'The most expensive phone number cost millions',
'Mark Zuckerberg is color blind',
'40% of American couples meet online',
'Music content makes up 5% of YouTube',
'Finding a security bug in Facebook’s code will pay off',
'Kids that are on social media for 1 hour a day have less chance of being happy',
'MySpace lost all of its content before 2016',
'Nearly one third of divorces are because of Facebook',
'Using a thinner font can save printer ink',
'The QWERTY keyboard was originally designed to slow you down',
'The first webpage is still running',
'Some countries skipped the era of landlines,'
'The passwords for the nuclear missiles were just a string of zero’s',
'Over 90% of the world’s currency is digital',
'Millions of hours of TV and movies are watched every day on Netflix',
'Technical degrees are almost useless by the time you graduate',
'There’s a term for old people who use the internet',
'Tech companies often test their products in New Zealand',
'There are fake Apple stores in China',
'Until 2010, carrier pigeons were faster than the internet',
'The first photo ever uploaded to the internet was a comedy band',
'Every advertisement for iPhone’s have 9:41 set as the time',
'A “jiffy” is a real measurement',
'An average 21 year old has spent 5,000 hours playing video games',
'Most of today’s successful companies started in garages',
'Most internet traffic isn’t from real humans',
'CAPTCHA is a long acronym',
'The three most common passwords are also the weakest',
'There wasn’t an app store in the first iPhone',
'We only keep 1 out of every 10 apps we try',
'Digital music sales surpassed physical sales in 2014',
'The @ symbol was chosen kind of randomly',
'There is a machine that can predict heart attacks',
'There is also artificial intelligence than can predict epidemics',
'The Amazon’s robot workers skyrocketed in less than five years',
'Digital tech is good for the environment',
'The average Facebook user has less than 200 friends',
'Google uses the same amount of energy as 200,000 homes',
'The first computer virus was harmless',
'There are only 21 million Bitcoins that can be mined in total',
'Filipinos use social media more than Americans',
'Most of the purchases in China are done with mobile phones',
'Robot laws are being put into place',
'Millions of tons of technology are thrown out each year',
'People read faster or slower depending on what they read from',
'GPS is free… for some',
'There are Amish computers',
'Mac computers were named after the apple',
'The first computer mouse wasn’t made from plastic',
'Which came first, Spam mail or Spam meat?',
'The original Xbox had sound snippets of real space missions',
'The majority of the people plug in their USB wrong',
'Steve Jobs used sleight of hand at the first iPhone presentation',
'The first alarm clock could only ring at one time',
'Computer Security Day is celebrated on November 30th',
'The government used PlayStation 3’s… but not for gaming',
'The first online gaming was before the year 2000',
'The first product scanned was a packet of chewing gum in 1974',
'You’re in good hands if your surgeon was a gamer',
'iTunes has unusual Terms & Conditions',
'Nintendo didn’t start as a video games company',
'Apollo 11 astronauts couldn’t afford insurance',
'People are still using dial-up',
'You can spell your email in Morse code',
'Yahoo’s original name was a mouthful',
'Everyone uses Google as a spellchecker',
'The first word to ever be auto-corrected was “teh”',
'The Nintendo Game Boy went to space',
'PlayStation 1 had Scratch and Sniff discs',
'“Android” is gender-specific',
'Google searches hit the billions every month',
"There’s a name for when you feel your phone vibrate… but it doesn’t",
'Smoking will void your Apple warranty',
'Technology is now influencing baby names',
'Blind people can use cell phones',
'Google’s first tweet was gibberish',
'The first cell phone call was in New York City',
'The first commercial text message was sent in 1992',
'Over 6,000 new computer viruses are created and released every month',
'There are more likes than photos on Facebook',
'iPhones were almost in the shape of an apple',
'Comic Sans is the most hated font in the world',
'NASA’s internet speed is 91 GB per second',
'Nokia is the largest company from Finland',
'More people have cell phones than toilets',
'The Apple Lisa was the first commercial computer with a Graphical User Interface (GUI) and a mouse',
'Some people are afraid of technology',
'The most expensive phone number cost millions',
'Mark Zuckerberg is color blind',
'40% of American couples meet online',
'Music content makes up 5% of YouTube',
'Finding a security bug in Facebook’s code will pay off',
'Kids that are on social media for 1 hour a day have less chance of being happy',
'MySpace lost all of its content before 2016',
'Nearly one third of divorces are because of Facebook',
'Using a thinner font can save printer ink',
'The QWERTY keyboard was originally designed to slow you down',
'The first webpage is still running',
'Some countries skipped the era of landlines',
"The passwords for the nuclear missiles were just a string of zero’s",
'Over 90% of the world’s currency is digital',
'Millions of hours of TV and movies are watched every day on Netflix',
'Technical degrees are almost useless by the time you graduate',
'There’s a term for old people who use the internet',
'Tech companies often test their products in New Zealand',
'There are fake Apple stores in China',
'Until 2010, carrier pigeons were faster than the internet',
'The first photo ever uploaded to the internet was a comedy band',
'Every advertisement for iPhone’s have 9:41 set as the time',
'A “jiffy” is a real measurement',
'An average 21 year old has spent 5,000 hours playing video games',
'Most of today’s successful companies started in garages',
'Most internet traffic isn’t from real humans',
'CAPTCHA is a long acronym',
'The three most common passwords are also the weakest',
'There wasn’t an app store in the first iPhone',
'We only keep 1 out of every 10 apps we try',
'Digital music sales surpassed physical sales in 2014',
'The @ symbol was chosen kind of randomly',
'There is a machine that can predict heart attacks',
'There is also artificial intelligence than can predict epidemics',
'The Amazon’s robot workers skyrocketed in less than five years',
'Digital tech is good for the environment',
'The average Facebook user has less than 200 friends',
'Google uses the same amount of energy as 200,000 homes',
'The first computer virus was harmless',
'There are only 21 million Bitcoins that can be mined in total',
'Filipinos use social media more than Americans',
'Most of the purchases in China are done with mobile phones',
'Robot laws are being put into place',
'Millions of tons of technology are thrown out each year',
]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower() == 'tgb hi':
        name = str(message.author)
        index = name.index("#")
        await message.channel.send(f'Hey {name[:index]}!')

    if message.content.lower() == 'tgb help me':
        await message.channel.send('How can I help you?')

    if message.content.lower() == 'tgb cmdlist':
        await message.channel.send(cmdlist)

    if message.content.lower() == 'tgb council':
        await message.channel.send(council)

    if message.content.lower() == 'tgb core':
        await message.channel.send(heads)

    if message.content.lower() == 'tgb exec':
        await message.channel.send(execs)

    if message.content.lower() == 'tgb trivia':
        await message.channel.send(trivia[randint(0, len(trivia)-1)])

    if message.content.lower() == 'tgb meme':
        await message.channel.send(embed=await pyrandmeme())

    if message.content.lower() == 'tgb bio':
        await message.channel.send(tgb_bio(message))

    if 'tgb bio: ' in message.content.lower() and message.content[9] != None:
        code = message.content[9:]
        userid = int(code[3:len(code)-1])
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
    if user in users:
        return df[df['user'] == user].bio.values[0]
    else:
        rtn = f"No bio found for {user}"
        return rtn

def tgb_bio_with_user(message, userid):
    df = pd.read_csv(r'bio.csv')
    user = str(message.author)
    users = list(df['user'].values)
    if user in users:
        return df[df['userid'] == userid].bio.values[0]
    else:
        rtn = f"No bio found for {user}"
        return rtn
    
def add_bio(message):
    df = pd.read_csv(r'bio.csv')
    bio = str(message.content[13:])
    user = str(message.author)
    userid = str(message.author.id)
    df.loc[len(df.index)] = [userid, user, bio]
    df.to_csv(r'bio.csv', index=False)
    return 'Bio added!'

def change_bio(message):
    df = pd.read_csv(r'bio.csv')
    new_bio = str(message.content[16:])
    curr_user = str(message.author)
    users = list(df['user'].values)
    if curr_user in users:
        df.loc[df.user == curr_user, 'bio'] = new_bio
        df.to_csv(r'bio.csv', index=False)
        return 'Bio changed!'

keep_alive()
client.run(TOKEN)

