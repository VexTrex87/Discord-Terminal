import discord
from discord.ext import commands
import shlex
import requests
import shutil
import traceback
import sys
import os

from secrets import TOKEN
from commands.set import *
from commands.get import *
from helper import save_image
import data
import constants

data.bot = commands.Bot(command_prefix = "$")

@data.bot.event
async def on_ready():
    print("ready")
    while True:
        text = input("$ ")
        args = shlex.split(text, posix = True)
        try:
            if args[0] == "help":
                print(constants.commands)
            elif args[0] == "set":
                if args[1] == "guild":
                    await set_guild(args[2])
                elif args[1] == "guildname":
                    await set_guild_name(args[2])
                elif args[1] == "guildicon":
                    guild_icon = get_image(args[2])
                    await set_guild_icon(guild_icon)
                elif args[1] == "afkchannel":
                    await set_afk_channel(args[2])
                elif args[1] == "afktimeout":
                    await set_afk_timeout(args[2])
                elif args[1] == "defaultnotifications":
                    await set_default_notifications(args[2])
                else:
                    print("{} is an invalid argument".format(args[1]))
            elif args[0] == "get":
                if args[1] == "guild":
                   await get_guild()
                elif args[1] == "guilds":
                   await get_guilds()
                elif args[1] == "guildname":
                   await get_guild_name()
                elif args[1] == "guildicon":
                   await get_guild_icon()
                elif args[1] == "afkchannel":
                    await get_afk_channel()
                elif args[1] == "afktimeout":
                    await get_afk_timeout()
                elif args[1] == "defaultnotifications":
                    await get_default_notifications()
                else:
                    print("{} is an invalid argument".format(args[1]))
            elif args[0] == "exit":
                sys.exit()
            elif args[0] == "cls":
                os.system("cls" if os.name == "nt" else "clear")
            else:
                print("{} is an invalid argument".format(args[0]))
        except Exception:
            traceback.print_exc()

if __name__ == "__main__":
    data.bot.run(TOKEN)
