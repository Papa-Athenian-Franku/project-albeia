from discord.ext import commands
from utilities import sheets_utilities as sheet_utils
from utilities import embed_utilities as embed_utils

class Retrieval(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def domesticinfo(self, ctx, house_name):
        sheet_values = sheet_utils.get_sheet_by_name("House Meta Sheet")
        for row in sheet_values:
            if row[0] == house_name:
                await ctx.send(embed=embed_utils.create_house_domestic_info_embed(row))

    @commands.command()
    async def militaryinfo(self, ctx, house_name):
        sheet_values = sheet_utils.get_sheet_by_name("Military Meta Sheet")
        for row in sheet_values:
            if row[0] == house_name:
                await ctx.send(embed=embed_utils.create_house_military_info_embed(row))

    @commands.command()
    async def resourceinfo(self, ctx, house_name):
        sheet_values = sheet_utils.get_sheet_by_name("Resource Meta Sheet")
        for row in sheet_values:
            if row[0] == house_name:
                await ctx.send(embed=embed_utils.create_house_resource_info_embed(row))

    @commands.command()
    async def tradeinfo(self, ctx, house_name):
        sheet_values = sheet_utils.get_sheet_by_name("Trade Meta Sheet")
        for row in sheet_values:
            if row[0] == house_name or row[4] == house_name:
                await ctx.send(embed=embed_utils.create_house_trades_info_embed(row))

    @commands.command()
    async def tradeiteminfo(self, ctx):
        sheet_values = sheet_utils.get_sheet_by_name("Item Value Meta Sheet")
        for row in sheet_values:
            if row[0] != "Resource":
                await ctx.send(embed=embed_utils.create_item_value_info_embed(row))

    @commands.command()
    async def researchinfo(self, ctx, house_name): # TODO
        sheet_values = sheet_utils.get_sheet_by_name("Research Meta Sheet")
        for row in sheet_values:
            if row[0] == house_name:
                await ctx.send(embed=embed_utils.create_house_domestic_info_embed(row))

    @commands.command()
    async def districtinfo(self, ctx, house_name): # TODO
        sheet_values = sheet_utils.get_sheet_by_name("District Meta Sheet")
        for row in sheet_values:
            if row[0] == house_name:
                await ctx.send(embed=embed_utils.create_house_domestic_info_embed(row))


async def setup(bot):
    await bot.add_cog(Retrieval(bot))
