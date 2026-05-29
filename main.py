import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.file_name
            file_url = attachment.file_url
            await attachment.save(f"./{file_name}")
            await ctx.send(f"Menguggah gambar ke ./{file_name}")
    else:
        await ctx.send("Maaf anda belum menguggah gambar..")

bot.run("MTQzNjMzNDc1OTMzOTg4NDY5Ng.G467V8.xdpt2yFIVdL6H6ST_egqKrN72hAouBoS3aXzz8")