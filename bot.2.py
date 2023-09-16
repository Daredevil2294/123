import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def text_write(ctx):
    with open('text.txt', 'r', encoding='utf-8') as f:
        print(f.read())

@bot.command()
async def text_read(ctx):
    f = open('text.txt', 'r', encoding='utf-8')
    text = f.read()
    print(text)
    f.close()

@bot.command()
async def meme(ctx):
    with open('dosya\images\mem1.png' , 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)

meme_probabilities = {
    'dosya\images\mem1.png': 0.2,  
    'dosya\images\mem2.jpg': 0.5,  
    'dosya\images\mem3.jpg': 0.8,
    'dosya\images\mem4.jpg': 0.8
    }
@bot.command()
async def memrandom(ctx):
    meme_list = []
    for meme, probability in meme_probabilities.items():
        if random.random() < probability:
            meme_list.append(meme)

    if meme_list:
        img_name = random.choice(meme_list)

    print(os.listdir('dosya\images'))
    img_name = random.choice(os.listdir('dosya\images'))
    with open(f'dosya\images/{img_name}', 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)

bot.run("TOKEN")
