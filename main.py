from concurrent.futures import thread
import discord, os, pyautogui, requests, cv2, numpy, subprocess, threading
from config import *

client = discord.Bot(intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f" > Logged in as: {client.user.name}#{client.user.discriminator}")

@client.slash_command(name="download", guild_ids=guildid)
async def killall(ctx, url):
    embed = discord.Embed(title="Downloading Video", description=f"```Url:\n{url}```", color=0x660cf)
    await ctx.respond(embed=embed)
    

client.run(token)