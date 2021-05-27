import discord
from discord.ext import commands
import random
import websocket
import json
import praw
import youtube_dl

from youtube_dl import YoutubeDL
from discord import FFmpegPCMAudio
from discord.voice_client import VoiceClient
from discord.ext.commands import Cog, command
listener = Cog.listener

bot = commands.Bot(command_prefix = '+')

Messageable = discord.abc.Messageable

TextChannel = discord.TextChannel

guild = discord.Guild

user = discord.User

Role = discord.Role

member = discord.Member

client = discord.Client

embed = discord.Embed

message = discord.Message

get = discord.utils.get

voice_state = discord.VoiceState


    #voice_channel = ctx.message.author.voice.channel
    #vc = await voice_channel.connect()


reddit = praw.Reddit(client_id='BGmMkM0NUly3xw',
    client_secret='LkIvOVwuiNRupsgEs2UwTLbKxT7ofg',
    user_agent='Just a bot by kinda stupid dev')

TOKEN = 'Nzk0MjAyNjgyMjA5ODYxNjQz.X-3Y4w.LHW2EjWabdjQTtxo-GaQCxZo82g'

@bot.command()
async def ws(ctx):
    await ctx.channel.send('Да, работаю')

@bot.command()
async def монетка(ctx):
    await ctx.channel.send(f'{ctx.message.author.mention} ты проиграл!')

@bot.command(pass_context=True)
async def play(self, ctx, url):
    ydl_opts = {'format': 'bestaudio', 'noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    print(url)
    server = ctx.message.guild
    voice_channel = client.voice_clients

    async with ctx.typing():
        player = await YTDLSource.from_url(url, loop=self.bot.loop)
        ctx.voice_channel.play(player, after=lambda e: print('Player error: %s' % e) if e else None)
    await ctx.send('Now playing: {}'.format(player.title))

@bot.command(aliases = ['mute'])
async def замуть(ctx):
    vc = ctx.author.voice.channel
    for member in vc.members:
        await member.edit(mute=True)

@bot.command(aliases = ['unmute'])
async def размуть(ctx):
    vc = ctx.author.voice.channel
    for member in vc.members:
        await member.edit(mute=False)    

@bot.command(pass_context = True, aliases = ['в'])
async def выйди(ctx):
    x = client.voice_clients
    await bot.disconnect()

@bot.command()
async def тест(ctx, role_name):
    role = discord.utils.find(lambda r: r.name == role_name, ctx.guild.roles)
        
    for user in ctx.guild.members:
        if role in user.roles:
             await ctx.send(f"{user.mention} has the role {role.mention}")

#@bot.event
#async def on_voice_state_update(member, before, after):
        #vc_before = before.channel
        #vc_after = after.channel
        #path = r"/Users/fedya/Downloads/p2p.mp3"
        #channel = member.voice.channel
        #vc = await channel.connect()
        #vc.play(discord.FFmpegPCMAudio(path))
        #with audioread.audio_open(path) as f:
            #sleep(f.duration)
        #await vc.disconnect()
channelw = 1
messagew = 1


@bot.command()
async def правила(ctx):
    await ctx.channel.send()
    await send()
    await send()
    await send()

@bot.command()
async def set_welcome_channel(ctx, channelk):
    global channelw
    channelw = channelk
    embed=discord.Embed(title=f"Welcome channel set to {channelk}!".format(member, ctx.message.author), color=0xff00f6)
    await ctx.channel.send(embed=embed)

@bot.command()
async def set_welcome_message(ctx, *args):
    global messagew
    messagew = args
    embed=discord.Embed(title=f"Welcome message set to {messagew}!".format(member, ctx.message.author), color=0xff00f6)
    await ctx.channel.send(embed=embed)


@bot.command()
@commands.has_role('Модер_госта')
async def Сспам(ctx,count, *args):
    count = int(count)
    channel = ctx.channel
    sargs = ' '.join(args)
    for i in range(count):
        await channel.send(f"{sargs}")

all_subs = []

@bot.command(pass_context=True)
async def мемчик(ctx):
    if not hasattr(client, 'nextMeme'):
        client.nextMeme = getMeme()
    name, url = client.nextMeme
    embed = discord.Embed(title = name)
    embed.set_image(url=url)
    
    await ctx.send(url)
    
    client.nextMeme = getMeme()

def getMeme():
    subreddit = reddit.subreddit("HollowKnightMemes")   

    top = subreddit.top(limit=50)

    for submission in top:
        all_subs.append(submission)

    random_sub = random.choice(all_subs)

    name = random_sub.title
    url = random_sub.url

    return name, url

@bot.command()
async def balance(ctx):
    await open_account(ctx.author)

    users = await get_bank_data()


    wallet_amt = users[str(user.id)]["wallet"]
    bank_amt = users[str(user.id)]["bank"]

    embed=discord.Embed(title="{}s balance:".format(member.name), color=0xe20303)
    embed.add_field(name="Wallet:", value=wallet_amt, inline=False)
    embed.add_field(name="Bank:", value=bank_amt, inline=False)

    await ctx.send(embed=embed)

async def open_account(user):
    users = await get_bank_data()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 0
        users[str(user.id)]["bank"] = 0

    with open("Economic.json.rtf", "w") as f:
        for i in users:
            json.dump(i, f)
    return True

async def get_bank_data():
    with open("Economic.json.rtf", "r") as f:
        users = json.load(f)
    return users

@bot.command()
@commands.has_role('Модер_госта')
async def спам(ctx, count, user: discord.User, message):
    message = str(message)
    count = int(count)
    for i in range(count):
        await user.send(message)

@bot.command(pass_context=True)
async def пмемчик(ctx):
    if not hasattr(client, 'nextMeme'):
        client.nextMeme = getMeme()
    name, url = client.nextMeme
    embed = discord.Embed(title = name)
    embed.set_image(url=url)
    
    await ctx.send(url)
    
    client.nextMeme = getMeme()

def getMeme():
    subreddit = reddit.subreddit("ProgrammerHumor")   

    top = subreddit.top(limit=50)

    for submission in top:
        all_subs.append(submission)

    random_sub = random.choice(all_subs)

    name = random_sub.title
    url = random_sub.url

    return name, url

@bot.command(name = 'anag', aliases = ['анаграмма', 'ag'])
async def anag(ctx, word):
    output = list(word[1:-1])
    random.shuffle(output)
    output.append(word[-1])
    outword =  word[0] + "".join(output)
    await ctx.channel.send(outword)

@bot.command()
async def лучший(ctx, arg1, arg2):
    for n in [1]:
        gl = [arg1, arg2]
        p = random.sample(gl, k=n)
        kok = p[0] + "".join(output)
        await ctx.channel.send(f'{kok}')

#@bot.command()
#async def say(ctx, *args):

    #msg = ' '.join(args)
    #await channelj.send(msg)

@bot.command(name = 'БАН', description = 'Забань близкого своего', aliases = ['бан', 'б'])
@commands.has_role('Модер_госта')
async def БАН(ctx, member: discord.Member):
        role = discord.utils.get(member.guild.roles, name='БАН')
        await member.add_roles(role)
        url = 'https://media0.giphy.com/media/dvOwFmfbzmAsI9v2IV/giphy.gif'
        embed=discord.Embed(title="Вам БАН! **{0}** был забанен **{1}**!".format(member, ctx.message.author), color=0xff00f6)
        embed.set_image(url=url)
        await ctx.channel.send(embed=embed)

@bot.command()
async def uno(ctx, player1: discord.User, player2: discord.User):
    players = []
    players.append(player1)
    players.append(player2)
    deck = []
    colours = ['красный', 'жёлтый', 'зелёный', 'синий']
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9, '+2', 'реверс', 'пропуск хода']
    wilds = ['смена цвета', '+4 смена цвета']
    for colour in colours:
        for value in values:
            card = "{} {}".format(colour, value)
            deck.append(card)
            if value != 0:
                deck.append(card)
    for i in range(4):
        deck.append(wilds[0])
        deck.append(wilds[1])
    random.shuffle(deck)

    hand1 = []
    hand2 = []

    def draw(count):
        cardsDrawn = []
        for x in range(count):
            cardsDrawn.append(deck.pop(0))
        return cardsDrawn

    for player in range(len(players)):
        s = set(deck)
        if player1 in players:
            hand1.append(draw(5))
            players.remove(player1)
        else:
            hand2.append(draw(5))
            players.append(player1)

    discards = []
    shand1 = str(hand1)
    shand2 = str(hand2)
    k1 = shand1.replace('[', '').replace(']', '').replace("'", "")
    k2 = shand2.replace('[', '').replace(']', '').replace("'", "")
    await player2.send(f'{k2}')
    await player1.send(f'{k1}')

    splitCard = discards.split(' ',1)
    currentColour = splitCard[0]
    if currentColour != 'смена цвета':
        cardVal = splitCard[1]
    else:
        cardVal = 'Any'
    playDirection = 1
    playerTurn = 0
    playing = True
    discards.append(deck.pop(0))
    playflag = False

    def canPlay(colour, value, playerHand):
        for cards in playerHand:
            global playflag
            if 'смена цвета' in card:
                return True
            elif colour in card or value in card:
                return True
            else:
                return False


    while playing:
        await player2.send('Карта сверху - {}'.format(discards[-1]))
        await player1.send('Карта сверху - {}'.format(discards[-1]))
        await ctx.channel.send('Карта сверху - {}'.format(discards[-1]))
        if canPlay(currentColour, cardVal,players[playerTurn]):
            await ctx.channel.send('Simulation end')




@bot.command(name = 'осторожно', description = 'предостереги невнимательного друга')
async def осторожно(ctx, member: discord.Member):
        url = 'https://media0.giphy.com/media/xIytx7kHpq74c/giphy.gif?cid=ecf05e47vwnfjr4q6xjloo9at4x7nszozfra9hdfmi8ln7zr&rid=giphy.gif'
        embed=discord.Embed(title="**{1}** угрожает **{0}**!".format(member, ctx.message.author), color=0xff00f6)
        embed.set_image(url=url)
        await ctx.channel.send(embed=embed)

@bot.command(name = 'печенька', description = 'Elmo loves cookies')
async def печенька(ctx, member: discord.Member):
        url = 'https://media4.giphy.com/media/KznvKiHI5onG3XfjKt/giphy.gif?cid=ecf05e47ufdi2fv1kxxc6odjnlfqjs4ixdqr28kj2pkivqcb&rid=giphy.gif'
        embed=discord.Embed(title="Смотри чо есть **{0}**!".format(member, ctx.message.author), color=0xff00f6)
        embed.set_image(url=url)
        await ctx.channel.send(embed=embed)

@bot.command()
@commands.has_role('Модер_госта')
async def стереть(ctx, count):
    if 0 < int(count) <= 100:
        with ctx.channel.typing():
            await ctx.message.delete()
            deleted = await ctx.channel.purge(limit=int(count))
            dmessage = await ctx.channel.send(f'Стёрто {len(deleted)} сообщений')
            await dmessage.delete(delay=5)
    else:
        ctx.channel.send("Невозможно удалить указанное количество сообщений.")


@bot.command(name = 'братишка', description = 'Вырази свои братские чувства')
async def братишка(ctx, member: discord.Member):
        url = 'https://media1.giphy.com/media/YQ4l2RLuzco5IwD4dR/giphy.gif?cid=ecf05e472s8up0n90eso9smld8n8j27u58w8eyn60xhmnfmb&rid=giphy.gif'
        embed=discord.Embed(title="**{1}** стукается кулачками с **{0}**!".format(member, ctx.message.author), color=0xff00f6)
        embed.set_image(url=url)
        await ctx.channel.send(embed=embed)

@bot.command(name = 'расстрелять', description = 'Разкотячь всех')
async def расстрелять(ctx, member: discord.Member):
        url = 'https://media1.giphy.com/media/xCM0GuXe7bb7a/giphy.gif?cid=ecf05e47dgpettvlib42aiar2xhruu920i3y2orsddesija5&rid=giphy.gif'
        embed=discord.Embed(title="**{1}** приговорил к расстрелу **{0}**!".format(member, ctx.message.author), color=0xff00f6)
        embed.set_image(url=url)
        await ctx.channel.send(embed=embed)

@bot.command(name = 'нечаянно', description = 'я не нарочно')
async def нечаянно(ctx, member: discord.Member):
        url = 'https://media2.giphy.com/media/QQZgTehcKrD2w/giphy.gif?cid=ecf05e4779js5kgmic1wgql7z4f5plfrwfhuj7rkpobriyra&rid=giphy.gif'
        embed=discord.Embed(title="**{0}** Я же нечаенно!!".format(member, ctx.message.author), color=0xff00f6)
        embed.set_image(url=url)
        await ctx.channel.send(embed=embed)

@bot.command(name = 'Ау', description = 'Кто-нибудь дома?')
async def Ау(ctx, member: discord.Member):
        url = 'https://media4.giphy.com/media/CVNWEzubQAfIivcVEF/giphy.gif?cid=ecf05e474ctgmsbc6rqjhcwros46f0ral7p0gqx3ludjs4he&rid=giphy.gif'
        embed=discord.Embed(title="Есть кто-нибудь?".format(member, ctx.message.author), color=0xff00f6)
        embed.set_image(url=url)
        await ctx.channel.send(embed=embed)

@bot.command(name = 'фэйспалм', description = 'Ты что тупой?', aliases = ['фп', 'facepalm'])
async def фэйспалм(ctx, member: discord.Member):
        url = 'https://media2.giphy.com/media/AS0Tt5xDPYVZC/giphy.gif'
        embed=discord.Embed(title="**{0}** ты что делаешь?".format(member, ctx.message.author), color=0xff00f6)
        embed.set_image(url=url)
        await ctx.channel.send(embed=embed)

@bot.command(name = 'молодец', description = 'Who is good boi there?', aliases = ['мл', 'pat'])
async def молодец(ctx, member: discord.Member):
        url = 'https://media0.giphy.com/media/Rhw1pCZVrVZ3Nlljzu/giphy.gif?cid=ecf05e47rcaox8htr7aqchmyvel4y07glb83tlmbwcf35hr7&rid=giphy.gif'
        embed=discord.Embed(title="**{0}** маладец!".format(member, ctx.message.author), color=0xff00f6)
        embed.set_image(url=url)
        await ctx.channel.send(embed=embed)

@bot.command(name = 'спокойной', description = 'Have a good night!', aliases = ['сн', 'goodnight'])
async def спокойной(ctx):
        url = 'https://media2.giphy.com/media/1g1d0C8QjOyfadAaOa/giphy.gif?cid=ecf05e47q8xusoctzz0aihxopt23plq2qs9rfvl3v8q8nk68&rid=giphy.gif'
        embed=discord.Embed(title="Спокойной ночи всем!".format(member, ctx.message.author), color=0xff00f6)
        embed.set_image(url=url)
        await ctx.channel.send(embed=embed)


@bot.command(name = 'ДР', description = 'С днем рождения тебя!', aliases = ['С_Днем_Рождения', 'HB'])
async def ДР(ctx, member: discord.Member):
        url = 'https://media4.giphy.com/media/WUO8fZQmigr4aiqmgl/giphy.gif?cid=ecf05e475uey08k0tkpymrw1a2fyzw7lh7cf14t6mz2pjv2d&rid=giphy.gif'
        embed=discord.Embed(title="С Днем Рождения **{0}**!".format(member, ctx.message.author), color=0xff00f6)
        embed.set_image(url=url)
        await ctx.channel.send(embed=embed)

@bot.command(name = 'F', description = 'Press f to pay respect', aliases = ['увожение', 'Pay_respect'])
async def F(ctx, member: discord.Member):
        url = 'https://media3.giphy.com/media/WO5Q7FsxJN2pjYc424/giphy.gif?cid=ecf05e47vep7lrcqvxw4x1r8stzbp0cr3kef2h4uv7r9g57o&rid=giphy.gif'
        embed=discord.Embed(title="**{0}** увожение тебе.".format(member, ctx.message.author), color=0xff00f6)
        embed.set_image(url=url)
        await ctx.channel.send(embed=embed)

@bot.command(pass_context=True)  
async def наори(ctx, msg):
    allmembers = []
    gmembers = ctx.guild.members

reit = ['Только собери свою тиму, что бы не сгореть.', 'Не забудь огнетушитель, там сейчас очень жарко', 'Кто? Ты? Может лучшет а Brawll Stars?', 'Сыграй в КБ, там больше ботов.', 'Да прибудет с тобой сила!']
@bot.command()
async def рейтинг(ctx):
    gl = reit
    p = random.choice(gl)
    await ctx.channel.send(f"{p}")
@bot.command()
@commands.has_role('Модер_госта')
async def кик(ctx, target: discord.Member, *, reason=None):
    await target.kick(reason=reason)

    
    
#@bot.event
#async def on_command_error(ctx, error):
 #   url = 'https://media3.giphy.com/media/CCgtEDjTrowG4/giphy.gif?cid=ecf05e47y60bohaydietph1mr8ndy5zpbctjfoh5pqznbvkg&rid=giphy.gif'
  #  embed=discord.Embed(title=f"Мне очень жаль но что-то сломалось:{error}!".format(member, ctx.message.author), color=0xff00f6)
   # embed.set_image(url=url)
    #await ctx.channel.send(embed=embed)

@bot.command(pass_context = True)
async def clear(ctx, number):
    messages = [] 
    number = int(number) 
    async for x in Messageable.history(ctx.message.channel, limit = number):
        messages.append(x)
    await TextChannel.delete_messages(messages(messages))

bot.run(TOKEN)
