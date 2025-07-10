from dotenv import load_dotenv
import discord, os, asyncio
from discord.ext import commands
from scraping import search, selected

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

    message = f"Hello everyone! \nI'm online and ready to help.\nYou can use me to search for aircraft information. Just type `$plane <aircraft_name>` and I'll provide you with the details.\nHave a great day!. For more commands type `$Help`"
    
    try:
        channel = bot.get_channel(int(channel_id)) or await bot.fetch_channel(int(channel_id))
        await channel.send(message)
    except Exception as e:
        print(f"Failed to send message: {e}")
    

@bot.command(name="Help")
async def Help(ctx):
    await ctx.send("""
    $Help - Show this message.
    $plane <aircraft_name> - Search for aircraft information.
    $delete-chat / $clear - Delete the chat.
    """)

@bot.command(name="delete-chat", aliases=["clear"])
async def delete_chat(ctx):
    if str(ctx.author.id) != os.getenv("DISCORD_USER_ID"):
        return await ctx.send("You are not authorized to use this command.")
    
    await ctx.send("How many messages do you want to delete?\nType 'all' to delete all messages.")
    
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    try:
        msg = await bot.wait_for("message", check=check, timeout=9.0)
        content = msg.content.lower()
        
        if content == "all":
            await ctx.channel.purge()
            await ctx.send("Successfully deleted all messages.")
        else:
            try:
                num_messages = int(content)
                if num_messages <= 0:
                    await ctx.send("Please enter a positive number.")
                    return
                
                await ctx.channel.purge(limit=num_messages + 3)
                await ctx.send(f"Successfully deleted {num_messages} messages.")
            except ValueError:
                await ctx.send("Please enter a valid number or 'all'.")

    except asyncio.TimeoutError:
        await ctx.send("You took too long to respond.")

@bot.command(name="plane")
async def plane_info(ctx, arg: str = None):
    try:
        if arg is None:
            return await ctx.send(f"Please provide an aircraft name.\nExample: `$plane p-47d`."),

        data = search(arg)
        
        if isinstance(data, str):
            return await ctx.send(data)
            
        if isinstance(data, dict) and "Plane:" in data:
            embed = discord.Embed(title=data["Plane:"], color=0x1E90FF)
            embed.set_image(url=data["Image:"])
            
            for key, value in data.items():
                if key != "Plane:" and key != "Image:":
                    embed.add_field(name=key, value=value, inline=True)
            return await ctx.send(embed=embed)
            
        if not isinstance(data, dict) or "options" not in data:
            return await ctx.send("Invalid choice number.")
        # Send the options to the user
        await ctx.send(f"Found multiple matches:\n{data['message']}\nPlease select a number:")

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        try:
            msg = await bot.wait_for("message", check=check, timeout=15)
            choice = int(msg.content) - 1

            if not (0 <= choice < len(data["options"])):
                return await ctx.send("Invalid choice number.")

            selected_plane = data["options"][choice]
            data = selected(selected_plane)
            
            if not isinstance(data, dict) or "Plane:" not in data:
                return await ctx.send("Plane not found.")

            embed = discord.Embed(title=data["Plane:"], color=0x1E90FF)
            embed.set_image(url=data["Image:"])
            
            for key, value in data.items():
                if key != "Plane:" and key != "Image:":
                    embed.add_field(name=key, value=value, inline=True)
            await ctx.send(embed=embed)

        except asyncio.TimeoutError:
            await ctx.send("Selection timed out.")
        except ValueError:
            await ctx.send("Please enter a valid number.")

    except Exception as e:
        print(f"Error: {e}")
        await ctx.send("Error, try again later.")

TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)
