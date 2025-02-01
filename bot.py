from discord.ext import commands
import discord, requests

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command(name="funciones")
async def funciones(ctx):
    await ctx.send("Tengo las siguientes funciones:")

@bot.command(name="avion")
async def nombre(ctx, arg):
    enlace = f"https://wiki.warthunder.com/unit/{arg}"

    response = requests.get(enlace)
    if response.status_code == 404:
        enlace_nuevo = arg.replace("-", "_")

        response2 = requests.get(f"https://wiki.warthunder.com/unit/{enlace_nuevo}")
        if response2.status_code == 404:
            await ctx.send("El avión no existe, intente con otro nombre.")#si el avión no existe
        else:
            await ctx.send(f"enlace del avión: https://wiki.warthunder.com/unit/{enlace_nuevo}")
            
    else:
        await ctx.send(f"enlace del avión: {enlace}")

bot.run("TOKEN")