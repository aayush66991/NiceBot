import discord
from discord.ext import commands
import time

a = 1
b = 2

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

@bot.command()
async def get(ctx):
    while a < b:
        async def stop(ctx):
            b = b+2
        msg = "+get"
        response = msg
        await ctx.send(response)
        time.sleep(305)

bot.run("OTgwNjg4MjE5MjY1OTYyMDA0.GBnzfE.zOi9L1c-LqVG4tW7laJMIPtw0mtv2y25Hxpves", bot = False)