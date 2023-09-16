import discord
import requests
from discord.ext import commands
import random
import os

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')
@bot.command()
async def hello(ctx):
    await ctx.send('hi')
    await ctx.send('geri_dönüşüm = geri dömüşümü önemi ile ilgili bilgiler')
    await ctx.send('kirlilik = dikkatli olmazsak kirliliğin gelebileceği durum')
    await ctx.send('öneri = çevreyi koruma adına yapılabilecek öneriler')

@bot.command()
async def neleryaparım(ctx):
    await ctx.send('Peki siz neler yapıyorsunuz çevremizi temiz tutmak için? buraya yazabilirsiniz.')
    with open('text.txt', 'r', encoding='utf-8') as f:
        print(f.read())
     
@bot.command()
async def geri_dönüşüm(ctx):
    a = ['Doğal kaynakların azalmasını ciddi oranda önler','Enerji tasarrufu sağlar','Çöp miktarı azalır, böylece daha temiz bir doğa olur','Ekonomiye katkı sağlar, yukarıda sözünü ettiğimiz hurda malzemelerde olduğu gibi.','Toprağın verimi arttırır. Böylece hem organik hem de besin değeri yüksek ürünler soframızla buluşur. Her şeyin doğalının, doğadan geldiğini düşünürsek doğa için atacağımız her adım bize sağlık ve iyi yaşam olarak geri dönecektir.' ]
    b = random.choice(a)

@bot.command()
async def kirlilik(ctx):
    print(os.listdir('__pycache__\dosya 2\çevrebotum\img'))
    c = random.choice(os.listdir('__pycache__\dosya 2\çevrebotum\img'))
    with open(f'__pycache__\dosya 2\çevrebotum\img/{c}', 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture)

@bot.command()
async def öneri(ctx):
    x = ['Atıklarınızı ayrıştırın, geri dönüşüme katkı sağlayın.','Naylon poşet kullanımını azaltın.','Kâğıt havlu kullanımını azaltın.','Dişinizi fırçalarken, banyo yaparken ve mutfakta çeşmeyi açık bırakmayın.','Enerji tasarruflu ampuller kullanın.']
    y = random.choice(x)

bot.run('Token')
