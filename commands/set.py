import discord
from discord.ext import commands

import data
from helper import parse_time, get_object

async def set_guild(guild_name: str):
    guild = get_object(data.bot.guilds, guild_name)
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
        channel = get_object(guild.voice_channels, vc_name)
        if channel:
            await guild.edit(afk_channel = channel)
            print(f"changed afk channel to {vc_name}")
        else:
            print(f"cannot find voice channel {vc_name}")

async def set_afk_timeout(timeout: int):
    timeout_seconds = parse_time(timeout)

    guild = data.data["selected_guild"]
    if not guild:
        print(f"no guild selected")
        return

    await guild.edit(afk_timeout = timeout_seconds)
    print(f"changed afk timeout to {timeout_seconds} seconds")
