# shinra - a simple discord bot
# created by Miinti#5774
# some base code taken from boostlog and other sources.

import config

try:
    import discord
    from discord.ext import commands
    from discord.utils import get
    import asyncio
    import atexit
    import random
    from random import randint
except:
    print("Please install the discord.py rewrite API.")
    exit(-1)

bot = commands.Bot(command_prefix='-', description='shinra is a simple bot designed for private use.')
client = discord.Client()
#owner = [config.MSTR]

# bot logon message in console
@bot.event
async def on_ready():
    #await bot.change_presence(activity=discord.Game(name='with fire'))
    await bot.change_presence(activity=discord.Activity(name='Fetti', type=2))
    print('\nHello, logged in as:')
    print(bot.user.name)
    print(bot.user.id)
    print('---')
    print('Running until further notice...')

def closing():
    print ('\nshinra is safely shutting down.')

atexit.register(closing)
bot.remove_command('help')
# bot commands, if you couldn't tell!
# functional bot commands
@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a+b)

@bot.command()
async def multiply(ctx, a: int, b: int):
    await ctx.send(a*b)

@bot.command()
async def ping(ctx):
    return await ctx.send('Pong! {0} ms'.format(round(bot.latency, 1)))

@bot.command()
async def roll(ctx):
    return await ctx.send(randint(0, 100))

# work in progress, will pick a random multiplayer game from an array of games
@bot.command()
async def game(ctx):
    await ctx.send("still under construction :angry:")

@bot.command()
async def poll(ctx):
    await ctx.message.add_reaction(emoji="👍")
    await ctx.message.add_reaction(emoji="👎")
    await ctx.message.add_reaction(emoji="🤷")

@bot.command()
async def ask(ctx):
    await ctx.send("coming soon.")

@bot.command(pass_context = True)
async def say(ctx, *args):
    msg = ' '.join(args)
    await bot.delete_message(ctx.message)
    return await bot.say(msg)


# static text and embedded response commands
@bot.command()
async def hi(ctx):
    await ctx.send(f"hey there, {ctx.author.mention}.")

@bot.command()
async def tyler(ctx):
    await ctx.send("<3")

@bot.command()
async def rui(ctx):
    await ctx.send("https://i.imgur.com/aHfuPXJ.jpg")

@bot.command()
async def ryan(ctx):
    await ctx.send("Axicom: Dont fucking stick your pleb ass words on my screen \nhttps://i.imgur.com/yfeOGuI.jpg")

@bot.command()
async def wags(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/273527780438704129/439644280731205641/sasuke_v1.webm")

@bot.command()
async def luke(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/273527780438704129/475428109835960340/ips-78B912CF-D727-4D93-A429-4B4FF6CC16D8.mp4 \nbig booty god :ok_hand::weary:")

@bot.command()
async def mike(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/273527780438704129/490224513737293844/video.mov")

@bot.command()
async def brandon(ctx):
    await ctx.send("https://www.youtube.com/watch?v=Px5gRTDxZFE")

@bot.command()
async def neverforget(ctx):
    await ctx.send("https://i.imgur.com/HYTtziv.jpg \nwho's king drinker of the house?")    

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="shinra.", description="a simple bot for simple tasks. designed for private use. this bot is a WIP.", color=0xe91e63)

    embed.add_field(name="Author", value="Miinti#5774 (ty i.)")
    embed.add_field(name="Member of", value=f"{len(bot.guilds)} server(s).")
    embed.add_field(name="Interested?", value="Contact Miinti#5774 for info.")
    await ctx.send(embed=embed)

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="shinra.", description="a simple bot for simple tasks. designed for private use.", color=0x71368a)

    embed.add_field(name="-help", value="Shows this message.", inline=False)
    embed.add_field(name="-info", value="Shows some brief information about shinra.", inline=False)
    embed.add_field(name="-ping", value="Displays the latency between the API and the client. (I need to verify this.)")
    embed.add_field(name="-roll", value="Rolls a random whole number between 0 and 100.")
    embed.add_field(name="-game", value="Picks a random multiplayer game to play. List will be regularly updated.")
    embed.add_field(name="-poll", value="Starts a poll with three choices.")
    embed.add_field(name="...", value="...", inline=False)
    embed.add_field(name="expansion coming soon.", value="this help list is a WIP and will be expanded in the future. shinra has hidden commands outside of this list.")
    await ctx.send(embed=embed)


bot.run(config.TOKEN)