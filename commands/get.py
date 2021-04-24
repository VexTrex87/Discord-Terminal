import discord
from discord.ext import commands

import data
from helper import get_object

async def get_guild():
    selected_guild = data.data["selected_guild"]
    if selected_guild:
        print(selected_guild)
    else:
        print("no guild selected")

async def get_guilds():
    guilds = []
    for guild in data.bot.guilds:
        guilds.append(guild.name)
        
    if len(guilds) == 0:
        print("no connected guilds")
    else:
        print(guilds)

async def get_guild_name():
    selected_guild = data["selected_guild"]
    if selected_guild:
        print(selected_guild.name)
    else:
        print("no guild selected")

async def get_guild_icon():
    selected_guild = data["selected_guild"]
    if selected_guild:
        print(selected_guild.icon_url)
    else:
        print("no guild selected")

async def get_afk_channel():
    selected_guild = data.data["selected_guild"]
    if not selected_guild:
        print("no guild selected")
        return

    afk_channel = selected_guild.afk_channel
    if afk_channel:
        print(afk_channel)
    else:
        print("no afk channel")

async def get_afk_timeout():
    selected_guild = data.data["selected_guild"]
    if not selected_guild:
        print("no guild selected")
        return

    afk_timeout = selected_guild.afk_timeout
    if afk_timeout:
        print(f"{afk_timeout} seconds")
    else:
        print("no afk timeout")

async def get_notifications():
    guild = data.data["selected_guild"]
    if not guild:
        print("no guild selected")
        return

    if guild.default_notifications == discord.NotificationLevel.all_messages:
        print("all messages")
    else:
        print("only mentions")

async def get_roles():
    guild = data.data["selected_guild"]
    if not guild:
        print("no guild selected")
        return

    roles = []
    for role in guild.roles:
        roles.append(role.name)

    print(roles)

async def get_role_permissions(role):
    guild = data.data["selected_guild"]
    if not guild:
        print("no guild selected")
        return

    role = get_object(guild.roles, role)
    if not role:
        print(f"could not find role {role}")
        return

    permissions = {}
    for permission in role.permissions:
        permissions[permission[0]] = permission[1]

    print(permissions)

async def get_role_color(role):
    guild = data.data["selected_guild"]
    if not guild:
        print("no guild selected")
        return

    role = get_object(guild.roles, role)
    if not role:
        print(f"could not find role {role}")
        return

    print(role.color)

async def get_role_mentionable(role):
    guild = data.data["selected_guild"]
    if not guild:
        print("no guild selected")
        return

    role = get_object(guild.roles, role)
    if not role:
        print(f"could not find role {role}")
        return

    print(role.mentionable)

async def get_role_position(role):
    guild = data.data["selected_guild"]
    if not guild:
        print("no guild selected")
        return

    role = get_object(guild.roles, role)
    if not role:
        print(f"could not find role {role}")
        return

    print(role.position)
