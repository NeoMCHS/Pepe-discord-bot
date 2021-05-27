import discord
import random
from discord.ext import commands
intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix = '+', intents=intents)
role = discord.Role
TOKEN = 'Nzk0MjAyNjgyMjA5ODYxNjQz.X-3Y4w.LHW2EjWabdjQTtxo-GaQCxZo82g'
@bot.command()
async def giveaway(ctx, role: discord.Role = None):
    if role == None:
        users = ctx.guild.members
        user1 = random.choice(users)
        await ctx.channel.send(f'{user1.mention} победил.')
    else:
        members = role.members
        mem = random.choice(members)
        await ctx.channel.send(f'{mem.mention} победитель.')

bot.run(TOKEN)