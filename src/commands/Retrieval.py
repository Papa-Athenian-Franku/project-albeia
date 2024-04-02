from discord.ext import commands
from utilities import sheets_utilities as sheet_utils
from utilities import embed_utilities as embed_utils

class Retrieval(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def domesticinfo(self, ctx, house_name):
        sheet_values = sheet_utils.get_sheet_by_name("House Meta Sheet")
        column_headings = sheet_values[0]
        for row in sheet_values:
            if row[0] == house_name:
                await ctx.send(embed=embed_utils.set_info_embed_from_list(column_headings, row))

    @commands.command()
    async def militaryinfo(self, ctx, house_name):
        sheet_values = sheet_utils.get_sheet_by_name("Military Meta Sheet")
        column_headings = sheet_values[1]
        for row in sheet_values:
            if row[0] == house_name:
                await ctx.send(embed=embed_utils.set_info_embed_from_list(column_headings, row))

    @commands.command()
    async def resourceinfo(self, ctx, house_name):
        sheet_values = sheet_utils.get_sheet_by_name("Resource Meta Sheet")
        column_headings = sheet_values[0]
        for row in sheet_values:
            if row[0] == house_name:
                await ctx.send(embed=embed_utils.set_info_embed_from_list(column_headings, row))

    @commands.command()
    async def tradeinfo(self, ctx, house_name):
        sheet_values = sheet_utils.get_sheet_by_name("Trade Meta Sheet")
        column_headings = sheet_values[0]
        for row in sheet_values:
            if row[0] == house_name or row[4] == house_name:
                await ctx.send(embed=embed_utils.set_info_embed_from_list(column_headings, row))

    @commands.command()
    async def tradeiteminfo(self, ctx):
        sheet_values = sheet_utils.get_sheet_by_name("Item Value Meta Sheet")
        column_headings = sheet_values[0]
        for row in sheet_values:
            if row[0] != "Resource":
                await ctx.send(embed=embed_utils.set_info_embed_from_list(column_headings, row))

    """
    @commands.command()
    async def districtinfo(self, ctx, house_name): # TODO
        sheet_values = sheet_utils.get_sheet_by_name("District Meta Sheet")
        column_headings = sheet_values[0]
        for row in sheet_values:
            if row[0] == house_name:
                await ctx.send(embed=embed_utils.set_info_embed_from_list(column_headings, row))
    """

async def setup(bot):
    await bot.add_cog(Retrieval(bot))
