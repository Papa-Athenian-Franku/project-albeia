import discord

def create_house_domestic_info_embed(data):
    embedded_message = discord.Embed(
                    title=data[0],
                    description="Embed for Domestic House Information.",
                    color=discord.Color.dark_green())

    embedded_message.add_field(name="`` Economic ``", value="\u200b", inline=False)
    embedded_message.add_field(name="House Bank", value=data[1], inline=False)
    embedded_message.add_field(name="House Income Incl. Tax", value=data[3], inline=False)
    embedded_message.add_field(name="House Income at War", value=data[4], inline=False)

    embedded_message.add_field(name="`` Population ``", value="\u200b", inline=False)
    embedded_message.add_field(name="Total Population", value=data[5], inline=False)
    embedded_message.add_field(name="Population Upkeep (Currency)", value=data[6], inline=False)
    embedded_message.add_field(name="Population Annual Growth", value=data[7], inline=False)
    embedded_message.add_field(name="Population Points", value=data[8], inline=False)

    embedded_message.add_field(name="`` War ``", value="\u200b", inline=False)
    embedded_message.add_field(name="War Status", value=data[9], inline=False)
    embedded_message.add_field(name="War Exhaustion", value=data[10], inline=False)

    embedded_message.add_field(name="`` Other ``", value="\u200b", inline=False)
    embedded_message.add_field(name="Tax Level", value=data[11], inline=False)
    embedded_message.add_field(name="Stability", value=data[12], inline=False)

    return embedded_message

def create_house_resource_info_embed(data):
    embedded_message = discord.Embed(
                    title=data[0],
                    description="Embed for House Resource Information.",
                    color=discord.Color.dark_green())

    embedded_message.add_field(name="`` Stockpiled ``", value="\u200b", inline=False)
    embedded_message.add_field(name="Gold", value=data[1], inline=False)
    embedded_message.add_field(name="Silver", value=data[2], inline=False)
    embedded_message.add_field(name="Copper", value=data[3], inline=False)
    embedded_message.add_field(name="Stone", value=data[4], inline=False)
    embedded_message.add_field(name="Wood", value=data[5], inline=False)
    embedded_message.add_field(name="Food", value=data[6], inline=False)


    embedded_message.add_field(name="`` Produced (Anually) ``", value="\u200b", inline=False)
    embedded_message.add_field(name="Gold", value=data[7], inline=False)
    embedded_message.add_field(name="Silver", value=data[8], inline=False)
    embedded_message.add_field(name="Copper", value=data[9], inline=False)
    embedded_message.add_field(name="Stone", value=data[10], inline=False)
    embedded_message.add_field(name="Wood", value=data[11], inline=False)
    embedded_message.add_field(name="Food", value=data[12], inline=False)

    return embedded_message

def create_house_research_info_embed(data):
    pass

def create_house_districts_info_embed(data):
    pass

def create_house_trades_info_embed(data):
    embedded_message = discord.Embed(
                    title=data[0],
                    description="Embed for House Trade Information.",
                    color=discord.Color.dark_green())

    embedded_message.add_field(name="`` Trade Partner One ``", value="\u200b", inline=False)
    embedded_message.add_field(name="House Name", value=data[0], inline=False)
    embedded_message.add_field(name="Trade Item", value=data[1], inline=False)
    embedded_message.add_field(name="Amount", value=data[2], inline=False)
    embedded_message.add_field(name="Raw Trade Value", value=data[3], inline=False)
    embedded_message.add_field(name="Trade Income", value=data[8], inline=False)


    embedded_message.add_field(name="`` Trade Partner Two ``", value="\u200b", inline=False)
    embedded_message.add_field(name="House Name", value=data[4], inline=False)
    embedded_message.add_field(name="Trade Item", value=data[5], inline=False)
    embedded_message.add_field(name="Amount", value=data[6], inline=False)
    embedded_message.add_field(name="Raw Trade Value", value=data[7], inline=False)
    embedded_message.add_field(name="Trade Income", value=data[9], inline=False)

    
    return embedded_message


def create_house_family_tree_info_embed(data):
    pass

def create_item_value_info_embed(data):
    embedded_message = discord.Embed(
                    title=data[0],
                    description="Embed for Trade Item Value Information.",
                    color=discord.Color.dark_green())

    embedded_message.add_field(name="`` Item Value ``", value=data[1], inline=False)
    
    return embedded_message


def create_house_military_info_embed(data):
    embedded_message = discord.Embed(
                    title=data[0],
                    description="Embed for House Military Information.",
                    color=discord.Color.dark_green())
    
    set_house_military_land_info(embedded_message, data)
    set_house_military_naval_info(embedded_message, data)
    set_house_military_siege_info(embedded_message, data)

    return embedded_message

def set_house_military_land_info(embedded_message, data):
    embedded_message.add_field(name="`` Land ``", value="\u200b", inline=False)
    embedded_message.add_field(name="Infantry", value=data[1], inline=False)
    embedded_message.add_field(name="Spearmen", value=data[2], inline=False)
    embedded_message.add_field(name="Archers", value=data[3], inline=False)
    embedded_message.add_field(name="Cavalry", value=data[4], inline=False)

    return embedded_message

def set_house_military_naval_info(embedded_message, data):
    embedded_message.add_field(name="`` Naval ``", value="\u200b", inline=False)
    embedded_message.add_field(name="Warships", value=data[5], inline=False)
    embedded_message.add_field(name="Transport Ships", value=data[6], inline=False)
    embedded_message.add_field(name="Longships", value=data[7], inline=False)
    embedded_message.add_field(name="Merchant Ships", value=data[8], inline=False)

    return embedded_message

def set_house_military_siege_info(embedded_message, data):
    embedded_message.add_field(name="`` Siege ``", value="\u200b", inline=False)
    embedded_message.add_field(name="Catapults", value=data[9], inline=False)
    embedded_message.add_field(name="Ballistas", value=data[10], inline=False)
    embedded_message.add_field(name="Siege Towers", value=data[11], inline=False)
    embedded_message.add_field(name="Battering Rams", value=data[12], inline=False)
    embedded_message.add_field(name="Ladders", value=data[13], inline=False)

    return embedded_message
