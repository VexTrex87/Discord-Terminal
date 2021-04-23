import discord
from discord.ext import commands

async def set_guild_name(guild: discord.Guild, name: str):
    if not guild:
        print(f"no guild selected")
        return

    await guild.edit(name = name)
    print(f"set guild name to {name}")

async def set_guild_icon(guild: discord.Guild, icon_url):
    if not guild:
        print(f"no guild selected")
        return

    with open(icon_url, "rb") as f:
        icon = f.read()
        await guild.edit(icon = icon)
        print(f"set guild icon to {icon_url}")