import discord
from discord.ext import commands
import time

bot = commands.Bot(command_prefix="+", self_bot=True)
@bot.event
async def on_ready():
    print(f"Self-Bot is Logged in as {bot.user}")
    print("Self-Bot is now ready to do Tasks...")

@bot.command()
async def ping(ctx):
    ping = round(bot.latency * 1000)
    response = f"Pong! {ping}ms"
    await ctx.send(response)

TOKEN = "YOUR_TOKEN_HERE"
bot.run(TOKEN, bot = False)
