import discord
from discord.ext import commands

import settings

intents = discord.Intents.all()

"""Each cog is a Python class that subclasses commands."""
# Commands (cogs) listen for user interaction.
cogs: list = ["commands.Retrieval", "commands.Help"]

client = commands.Bot(command_prefix=settings.Prefix, help_command=None, intents=intents)

@client.event
async def on_ready():
    print("Bot is ready!")
    await client.change_presence(status=discord.Status.online, activity=discord.Game(settings.BotStatus))
    for cog in cogs:
        try:
            print(f"Loading cog {cog}")
            await client.load_extension(cog)
            print(f"Loaded cog {cog}")
        except Exception as e:
            exc = "{}: {}".format(type(e).__name__, e)
            print("Failed to load cog {}\n{}".format(cog, exc))

client.run(settings.TOKEN)