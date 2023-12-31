import discord
import turtle
import random
import string
from botpass import *
from random import randint
import math
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):

    content = message.content.lower()
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send('\U0001f642')
    elif message.content.startswith('roll'):
        result = str(random.randint(1, 6))
        await message.channel.send(result)
    elif message.content.startswith('password'):
        await message.channel.send(gen_pass(12))
    elif message.content.startswith('şifre'):
        parts = message.content.split()
        if len(parts) == 2 and parts[1].isdigit():
            pass_length = parts[1]
            if pass_length > 0:
                b = '+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
                await message.channel.send('I have 4 different password options for your choice:')
                for i in range(4):
                    c = ''
                    for j in range(pass_length):
                        y = random.choice(b)
                        c += y
                await message.channel.send(c)
            else:
                await message.channel.send('Password length must be a positive integer')
    elif message.content.startswith('/emoji'):
        await message.channel.send(emoji_olusturucu())
    elif message.content.startswith('heads/tails'):
        await message.channel.send(yazi_tura())
    elif message.content.startswith('turtledraw'):
        a= turtle.Turtle()
        parts = message.content.split()
        if len(parts) == 2:
            if parts[1] == 'dikdörtgen':
                await message.channel.send(turtledraw_dikdörtgen())
            elif parts[1] == 'kare':
                await message.channel.send(turtledraw_kare())
            elif parts[1] =='yuvarlak':
                await message.channel.send(turtledraw_yuvarlak())
            elif parts[1] == 'üçgen':
                await message.channel.send(turtledraw_üçgen())     
    elif message.content.startswith('rps'):
        parts = message.content.split()
        if len(parts) == 2:
            await message.channel.send(parts[1], 'vs', end=' ')

            chosen = randint(1,3)
            if chosen == 1:
                computer= 'r'
            elif chosen == 2:
                computer= 'p'
            elif chosen == 3:
                computer= 's'
            await message.channel.send(computer)

            if parts[1].content == computer:
                await message.channel.send('DRAW!')
            elif parts[1].content=='r' and computer=='s':
                await message.channel.send('PLAYER WON!')
            elif parts[1].content=='r' and computer=='p':
                await message.channel.send("YOU'VE LOST")
            elif parts[1].content=='s' and computer=='r':
                await message.channel.send("YOU'VE LOST")
            elif parts[1].content=='s' and computer=='p':
                await message.channel.send('PLAYER WON!')
            elif parts[1].content=='p' and computer=='s':
                await message.channel.send("YOU'VE LOST")
            elif parts[1].content=='p' and computer=='r':
                await message.channel.send('PLAYER WON!')

    elif message.content.startswith('check_prime'):
        parts = message.content.split()
        if len(parts) == 2 and parts[1].isdigit():
            a = parts[1]
            if a == 2:
                await message.channel.send("Prime number ")
            elif a == 1:
                await message.channel.send("not a prime number.")
                o=True
            else:
                f = math.sqrt(a)
                if f == int:
                    for i in range(2, f+1):
                        d = a%i
                        if d == 0:
                            await message.channel.send("not a prime number.")
                            o= True
                            break
                elif f!= int:
                    c = round(f)
                    if f<c:
                        g = c-2
                    else:
                        g = c+1
                    for i in range(2, g+2):
                        y = a%i
                        if y == 0:
                            await message.channel.send("not a prime number.")
                            a= True
                            break
            if o!= True:
                await message.channel.send("Prime number")
    else:
        await message.channel.send(message.content)
client.run("MTE0NzE3MzEzNDE2OTAxNDM5NQ.GeFs72.Gf72JvqZ0HVoIEERi-7va0yqp4N6PdTiDbFDPM")
