import json, datetime, wikipedia, discord, asyncio, requests, random
from jokeapi import Jokes
from covid import Covid
from discord.abc import Messageable
from discord.ext.commands import Bot
from discord.ext import commands, tasks
from itertools import cycle

bot = Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('-----------------')
    await bot.change_presence(status = discord.Status.idle, activity = discord.Game('with Python'))

@bot.event
async def on_command_error(ctx, error):
    await ctx.send(error)
    #ovo moze samo zasad

@bot.command()
async def wiki(ctx, input):
    await ctx.send(wikipedia.summary(input, auto_suggest=False,redirect=True,sentences=3))

@bot.command()
async def randbroj(ctx, broj1: int, broj2: int):
    await ctx.send(random.randint(broj1, broj2))

"""
@bot.command()
async def korona(ctx):
    covid = Covid()
    status = covid.get_status_by_country_id(22)
    print(status)
    await ctx.send()
    #{'id': '22', 'name': 'Bosnia and Herzegovina'}
"""

"""
@bot.command()
async def sala(ctx):
    j = Jokes()
    joke = j.get_joke(response_format="json", amount=1)
    if joke['type'] == "single":
        await ctx.send(joke["joke"])
    else:
        await ctx.send(joke["setup"])
        await ctx.send(joke["delivery"])
"""

@bot.command()
@commands.has_permissions(manage_messages = True)
async def clear(ctx, broj):
    broj = int(broj)
    counter = 0
    async for x in Messageable.history(ctx.message.channel, limit = broj):
        if counter < broj:
            await discord.Message.delete(x)
            counter += 1

@bot.command()
@commands.has_permissions(manage_messages = True)
async def bulkclear(ctx, num):
    num = int(num)
    await ctx.channel.purge(limit=num, bulk=True)

@bot.command()
async def ping(ctx):
    await ctx.send("Bot je ziv!")

<<<<<<< HEAD
@bot.command()
@commands.has_permissions(kick_members = True)
async def whois(ctx, member: discord.Member):
    embed = discord.Embed(title = member.display_name, description = member.mention, color = discord.Color.green())
    embed.add_field(name = "ID", value = member.id, inline = True)
    embed.set_thumbnail(url = member.avatar_url)
    embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}") 
    await ctx.send(embed=embed)

@bot.command()
async def poll(ctx, text: str):
    emojis = ['👍', '👎']
    embed = discord.Embed(title = "Poll", description = text, color = discord.Color.red())
    message = await ctx.send(embed = embed)
    for i in emojis:
        await message.add_reaction(emoji=i)

"""
@tasks.loop(minutes = 1)
async def casevi():
    #nesto
"""

bot.run('token')
