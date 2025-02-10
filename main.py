from discord.ext import commands
import discord, os, webserver
from bot_logic import encontrar

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command(name="comandos")
async def funciones(ctx):
    await ctx.send("Tengo la siguiente funcion: $avion <nombre del avión>")

@bot.command(name="avion")
async def nombre(ctx, arg):
    avion_info = encontrar(arg)
    await ctx.send(avion_info)

webserver.keep_alive()
TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)