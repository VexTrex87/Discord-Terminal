import discord
from discord.ext import commands
from ast import literal_eval

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

async def set_notifications(value):
    guild = data.data["selected_guild"]
    if not guild:
        print("no guild selected")
        return

    if value == "allmessages":
        await guild.edit(default_notifications = discord.NotificationLevel.all_messages)
        print("default notifications set to all messages")
    elif value == "onlymentions":
        await guild.edit(default_notifications = discord.NotificationLevel.only_mentions)
        print("default notifications set to only mentions")
    else:
        print(f"{value} is not a valid notification level")

async def set_role_name(role, new_name):
    guild = data.data["selected_guild"]
    if not guild:
        print("no guild selected")
        return

    role = get_object(guild.roles, role)
    if not role:
        print(f"cannot find role {role}")
        return

    old_role_name = role.name
    await role.edit(name = new_name)
    print(f"set role {old_role_name}'s name to {new_name}")

async def set_role_permission(role, permission, value):
    guild = data.data["selected_guild"]
    if not guild:
        print("no guild selected")
        return

    role = get_object(guild.roles, role)
    if not role:
        print(f"could not find role {role}")
        return

    if value == "true":
        value = True
    elif value == "false":
        value = False
    else:
        print(f"{value} is not a valid value")
        return

    permissions = discord.Permissions()
    permissions.update(**{permission: value})

    await role.edit(permissions = permissions)
    print(f"set permission {permission} to {value} for role {role}")

async def set_role_color(role, color: int):
    guild = data.data["selected_guild"]
    if not guild:
        print("no guild selected")
        return

    role = get_object(guild.roles, role)
    if not role:
        print(f"could not find role {role}")
        return

    color = int(color, 16)
    await role.edit(color = discord.Color(color))
    print(f"set role {role}'s color to {color}")

async def set_role_mentionable(role, value):
    guild = data.data["selected_guild"]
    if not guild:
        print("no guild selected")
        return

    role = get_object(guild.roles, role)
    if not role:
        print(f"could not find role {role}")
        return

    if value == "true":
        value = True
    elif value == "false":
        value = False
    else:
        print(f"{value} is not a valid value")
        return

    await role.edit(mentionable = value)
    print(f"set role {role}'s mentionable value to {value}")

async def set_role_position(role, value):
    guild = data.data["selected_guild"]
    if not guild:
        print("no guild selected")
        return

    role = get_object(guild.roles, role)
    if not role:
        print(f"could not find role {role}")
        return

    value = int(value)
    await role.edit(position = value)
    print(f"set role {role}'s position to {value}")
