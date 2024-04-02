import discord
from discord.ext import commands
from utilities import embed_utilities as embed_utils

retrieval_commands_info = {
    ";domesticinfo": "Takes 'House Name' as parameter. Returns Economic, Population and Stability info.",
    ";militaryinfo": "Takes 'House Name' as parameter. Returns Land, Naval and Siege info.",
    ";resourceinfo": "Takes 'House Name' as parameter. Returns Stockpile and production.",
    ";tradeinfo": "Takes 'House Name' as parameter. Returns Trades Information.",
    ";tradeiteminfo": "Takes no parameter. Returns all items and values as embeds."
}


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        for key, value in retrieval_commands_info.items():
            await ctx.send(embed=embed_utils.set_info_embed_from_dictionary(key, value))

async def setup(bot):
    await bot.add_cog(Help(bot))