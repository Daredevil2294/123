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
    await ctx.send('prefix = !')
    await ctx.send('geri_dönüşüm = geri dömüşümü önemi ile ilgili bilgiler')
    await ctx.send('kirlilik = dikkatli olmazsak kirliliğin gelebileceği durum')
    await ctx.send('öneri = çevreyi koruma adına yapılabilecek öneriler')
    await ctx.send('önerilerim = Kendi önerilerinizi yazın böylece sonrasında eklenerek önerilerimiz artabilir')
    await ctx.send('yazılanlar = Başkalarının önerilerini görebilirsiniz')
    await ctx.send('süpriz ???')
     
@bot.command()
async def geri_dönüşüm(ctx):
    a = ['Doğal kaynakların azalmasını ciddi oranda önler','Enerji tasarrufu sağlar','Çöp miktarı azalır, böylece daha temiz bir doğa olur','Ekonomiye katkı sağlar, yukarıda sözünü ettiğimiz hurda malzemelerde olduğu gibi.','Toprağın verimi arttırır. Böylece hem organik hem de besin değeri yüksek ürünler soframızla buluşur. Her şeyin doğalının, doğadan geldiğini düşünürsek doğa için atacağımız her adım bize sağlık ve iyi yaşam olarak geri dönecektir.' ]
    b = random.choice(a)
    await ctx.send(b)

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
    await ctx.send(y)

@bot.command()
async def süpriz(ctx): 
    await ctx.send('süpriz test vakti')
    await ctx.send('Şimdi ne kadar çevreci olduğumuzu görelim böylece test sonrası kendimiz geliştirebilirz.Dikkat soruları cevaplarken başına Bir ), İki ), Üç ) gibi numara yazınız. Dikkat prefixi unutmayınız')
    await ctx.send('1)Sıkça toplu taşıma kullanır mısnız?')

@bot.command()
async def Bir(ctx):
    await ctx.send('2)Bilinçli bir tüketici misiniz?')

@bot.command()
async def İki(ctx):
    await ctx.send('3)Yerel ve mevsimlik yiyecekler mi tükettirsiniz?')

@bot.command()
async def Üç(ctx):
        await ctx.send('Eveettt, süpriz testimiz sona erdi bu soruların çoğuna evet dediyseniz çevre adına teşekkürler!!')

@bot.command()
async def önerilerim(ctx, *, suggestion):

    with open('__pycache__\dosya 2\çevrebotum\onerilerim.txt', 'a', encoding='utf-8') as f:
        f.write(suggestion + '\n')
    await ctx.send(f"Öneriniz kaydedildi: {suggestion}")


@bot.command()
async def yazılanlar(ctx):
    with open('__pycache__\dosya 2\çevrebotum\onerilerim.txt', 'r', encoding='utf-8') as f:
        text = f.read()
    await ctx.send(text)

bot.run('Token')
