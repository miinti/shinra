# shinra - a simple discord bot
# created by Miinti#5774
# some base code taken from boostlog and other sources.

try:
    import discord
    from discord.ext import commands
    import atexit
    import random
    from random import randint
except:
    print("Please install the discord.py rewrite API.")
    exit(-1)

bot = commands.Bot(command_prefix='-', description='shinra is a simple bot designed for private servers.')
client = discord.Client()

# bot logon message in console
@bot.event
async def on_ready():
    #await bot.change_presence(activity=discord.Game(name='with fire'))
    await bot.change_presence(activity=discord.Activity(name='Astroworld', type=2))
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

# static text and embedded response commands
@bot.command()
async def hi(ctx):
    await ctx.send("hey there.")

@bot.command()
async def tyler(ctx):
    await ctx.send("<3")

@bot.command()
async def rui(ctx):
    await ctx.send("nerd")

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="shinra", description="a simple bot for simple tasks. designed for private servers. this bot is a WIP.", color=0xeee657)

    embed.add_field(name="Author", value="Miinti#5774 (ty i.)")
    embed.add_field(name="Member of", value=f"{len(bot.guilds)} server(s).")
    embed.add_field(name="Interested?", value="Contact Miinti#5774 for info.")
    await ctx.send(embed=embed)

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="shinra.", description="a simple bot for simple tasks. designed for private servers.", color=0xeee657)

    embed.add_field(name="-help", value="Shows this message.", inline=False)
    embed.add_field(name="-info", value="Shows some brief information about shinra.", inline=False)
    embed.add_field(name="-ping", value="Displays the latency between the API and the client. (I need to verify this.)")
    embed.add_field(name="...", value="...", inline=False)
    embed.add_field(name="expansion coming soon.", value="this help list is a WIP and will be expanded in the future. shinra has hidden commands outside of this list.")
    await ctx.send(embed=embed)


bot.run('NDcyMjIwMjM5NDc2Njg2ODU5.DkTYGg.Zk1qIm9SRs1C5f8OskXxukFNbGw')