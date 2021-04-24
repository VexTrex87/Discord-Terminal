import discord
from discord.ext import commands

import data
from helper import get_object

async def new_role(role_name: str):
    guild = data.data["selected_guild"]
    if not guild:
        print("no guild selected")
        return

    await guild.create_role(name = role_name)
    print(f"create role {role_name}")
