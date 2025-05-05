import discord, os
from discord.ext import commands
from bot_logic import search
from dotenv import load_dotenv

import discord.ext


load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} has been successfully connected.")
    
    # ID of the channel where the message will be sent
    channel_id = os.getenv("DISCORD_CHANNEL_ID") # Replace with your channel ID
    print(f"Channel ID: {channel_id}")

    message = f"Hello everyone! \nI'm online and ready to help.\nYou can use me to search for aircraft information. Just type `$plane <aircraft_name>` and I'll provide you with the details.\nHave a great day!"
    
    try:
        channel = bot.get_channel(int(channel_id)) or await bot.fetch_channel(int(channel_id))
        await channel.send(message)
    except Exception as e:
        print(f"Failed to send message: {e}")

@bot.command(name="plane")
async def plane_info(ctx, arg: str = None):
    if not arg or len(arg) <= 2:
        return await ctx.send("❗ Please provide a valid aircraft name (at least 3 characters).")

    data = search(arg)

    if data.startswith("⚠") or data.startswith("❌"):
        return await ctx.send(data)

    lines = [line.strip() for line in data.splitlines() if line.strip()]

    title = lines[0]

    # Create embed
    embed = discord.Embed(title=title, color=0x1E90FF)

    # Agregate all lines into a single field
    for line in lines[1:]:
        try:
            parts = line.split(maxsplit=1)
            if len(parts) == 2:
                key, value = parts
                embed.add_field(name=key, value=value, inline=False)
            else:
                embed.add_field(name="Info", value=line, inline=False)
        except Exception as e:
            print(f"Error processing line: {line} ({e})")
            embed.add_field(name="Info", value=line, inline=False)

    await ctx.send(embed=embed)



TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)