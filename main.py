import discord, os, pytube
from config import *

token = token
guildid = guildid
client = discord.Bot(intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f" > Logged in as: {client.user.name}#{client.user.discriminator}")

@client.slash_command(name="download", guild_ids=guildid)
async def download(ctx, link):
    embed = discord.Embed(title="Downloading Video", description=f"```{link}```", color=0x660cf)
    await ctx.respond(embed=embed)
    url = pytube.YouTube(str(link))
    video = url.streams.get_highest_resolution()
    video.download(os.getenv('TEMP'), filename="video.mp4")
    try:
        await ctx.respond(file=discord.File(f"{os.getenv('TEMP')}\\video.mp4"))
    except Exception as error:
        embed = discord.Embed(title="Error sending video", description=f"```{error}```", color=0x660cf)

client.run(token)