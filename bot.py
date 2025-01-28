from discord.ext import commands
import discord

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command(name="funciones")
async def funciones(ctx):
    await ctx.send("Tengo las siguientes funciones:")

bot.run("TOKEN")