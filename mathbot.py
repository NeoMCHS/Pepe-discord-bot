import discord
from discord.ext import commands
import wolframalpha
client = wolframalpha.Client('G552V3-EQTATWL5LH')
bot = commands.Bot(command_prefix = '+')
TOKEN = 'Nzk0MjAyNjgyMjA5ODYxNjQz.X-3Y4w.LHW2EjWabdjQTtxo-GaQCxZo82g'

@bot.command(name='разделить', aliases=['/'])
async def разделить(ctx, num1, num2):
    answer = int(num1) / int(num2)
    await ctx.channel.send(f'Результат деления {num1} и {num2} - {answer}')

@bot.command(name='умножить', aliases=['*'])
async def умножить(ctx, num1, num2):
    answer = int(num1) * int(num2)
    await ctx.channel.send(f'Результат умножения {num1} и {num2} - {answer}')

@bot.command(name='квадрат', aliases=['^'])
async def квадрат(ctx, num1, num2):
    answer = int(num1) ** int(num2)
    await ctx.channel.send(f'{num1} в степени {num2} - {answer}')

@bot.command()
async def wa(ctx, *questions):
    question = " ".join(questions)
    response = client.query(question)
    result = None
    for result in response.results:
        pass
    if result is not None:
        await ctx.channel.send(f"The answer is {result.text}".format(result.text))

bot.run(TOKEN)