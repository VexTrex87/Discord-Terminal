import discord
from discord.ext import commands

import data
from helper import parse_time

async def set_guild(guild_name: str):
    guild = discord.utils.find(lambda g: g.name == guild_name or g.id == int(guild_name), data.bot.guilds)
    if guild:
        data.data["selected_guild"] = guild
        print(f"set selected guild to {guild}")
    else:
        print("could not find guild {}".format(guild_name))

async def set_guild_name(name: str):
    guild = data.data["selected_guild"]
    if not guild:
        print(f"no guild selected")
        return

    await guild.edit(name = name)
    print(f"set guild name to {name}")

async def set_guild_icon(icon_url):
    guild = data.data["selected_guild"]
    if not guild:
        print(f"no guild selected")
        return

    with open(icon_url, "rb") as f:
        icon = f.read()
        await guild.edit(icon = icon)
        print(f"set guild icon to {icon_url}")

async def set_afk_channel(vc_name):
    guild = data.data["selected_guild"]
    if not guild:
        print(f"no guild selected")
        return

    if vc_name == "none":
        await guild.edit(afk_channel = None)
        print("removed afk channel")
    else:
        channel = discord.utils.find(lambda v: v.name == vc_name or v.id == int(vc_name), guild.voice_channels)
        if channel:
            await guild.edit(afk_channel = channel)
            print(f"changed afk channel to {vc_name}")
        else:
            print(f"cannot find voice channel{vc_name}")

async def set_afk_timeout(timeout: int):
    timeout_seconds = parse_time(timeout)

    guild = data.data["selected_guild"]
    if not guild:
        print(f"no guild selected")
        return

    await guild.edit(afk_timeout = timeout_seconds)
    print(f"changed afk timeout to {timeout_seconds} seconds")