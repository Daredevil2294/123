import discord
import turtle
import random
import string
from botpass import *
from random import randint
import math
import io
from PIL import Image
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
            pass_length = int(parts[1])
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
            shape = parts[1]
            if shape == 'dikdörtgen':
                await message.channel.send(turtledraw_dikdörtgen())
            elif shape == 'kare':
                await message.channel.send(turtledraw_kare())
            elif shape =='yuvarlak':
                await message.channel.send(turtledraw_yuvarlak())
            elif shape == 'üçgen':
                await message.channel.send(turtledraw_üçgen())    

    elif message.content.startswith('rps'):
        parts = message.content.split()
        if len(parts) == 2:

            b = f"{parts[1]} vs "

            chosen = randint(1,3)
            if chosen == 1:
                computer= 'r'
            elif chosen == 2:
                computer= 'p'
            elif chosen == 3:
                computer= 's'

            b += computer
            await message.channel.send(b)

            if parts[1] == computer:
                await message.channel.send('DRAW!')
            elif parts[1]=='r' and computer=='s':
                await message.channel.send('PLAYER WON!')
            elif parts[1]=='r' and computer=='p':
                await message.channel.send("YOU'VE LOST")
            elif parts[1]=='s' and computer=='r':
                await message.channel.send("YOU'VE LOST")
            elif parts[1]=='s' and computer=='p':
                await message.channel.send('PLAYER WON!')
            elif parts[1]=='p' and computer=='s':
                await message.channel.send("YOU'VE LOST")
            elif parts[1]=='p' and computer=='r':
                await message.channel.send('PLAYER WON!')
    elif message.content.startswith('check_prime'):
        o = False
        parts = message.content.split()
        if len(parts) == 2 and parts[1].isdigit():
            a = int(parts[1])
            if a == 2:
                o=True
            elif a == 1:
                o=False
            else:
                f = math.sqrt(a)
                if f == int:
                    for i in range(2, f+1):
                        d = a%i
                        if d == 0:
                            o= False
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
                            o= False
                            break
            if o:
                await message.channel.send("Prime number")
            else:
                await message.channel.send("Not a prime number")

    else:
        await message.channel.send(message.content)
client.run("TOKEN")
