import discord, os
from discord.ext import commands
from scraping import search
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
        print(f"Failed to send message: {e}")\

@bot.command(name="plane")
async def plane_info(ctx, arg: str = None):
    if not arg or len(arg) <= 2:
        return await ctx.send("❗ Please provide a valid aircraft name (at least 3 characters).")

    data = search(arg)

    title = data["Plane:"]
    image = data["Image:"]

    # Create embed
    embed = discord.Embed(title=title, color=0x1E90FF)
    embed.set_image(url=image)
    
    for key, value in data.items():
        if key != "Plane:":
            embed.add_field(name=key, value=value, inline=True)

    await ctx.send(embed=embed)




TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)