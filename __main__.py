import discord
from discord.ext import commands
import shlex
import requests
import shutil
import traceback
import sys
import os
import traceback

from commands.set import *
from commands.get import *
from commands.new import *
from secrets import TOKEN
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
                elif args[1] == "notifications":
                    await set_notifications(args[2])
                elif args[1] == "rolename":
                    await set_role_name(args[2], args[3])
                elif args[1] == "rolepermission":
                    await set_role_permission(args[2], args[3], args[4])
                elif args[1] == "rolecolor":
                    await set_role_color(args[2], args[3])
                elif args[1] == "rolementionable":
                    await set_role_mentionable(args[2], args[3])
                elif args[1] == "roleposition":
                    await set_role_position(args[2], args[3]) 
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
                elif args[1] == "set_notifications":
                    await get_notifications()
                elif args[1] == "roles":
                    await get_roles()
                elif args[1] == "rolepermissions":
                    await get_role_permissions(args[2])
                elif args[1] == "rolecolor":
                    await get_role_color(args[2])
                elif args[1] == "rolementionable":
                    await get_role_mentionable(args[2])
                elif args[1] == "roleposition":
                    await get_role_position(args[2]) 
                else:
                    print("{} is an invalid argument".format(args[1]))
            elif args[0] == "new":
                if args[1] == "role":
                    await new_role(args[2])
                else:
                    print("{} is an invalid argument".format(args[1]))
            elif args[0] == "exit":
                sys.exit()
            elif args[0] == "cls":
                os.system("cls" if os.name == "nt" else "clear")
            else:
                print("{} is an invalid argument".format(args[0]))
        except Exception as error_message:
            traceback.print_exception(type(error_message), error_message, error_message.__traceback__)

if __name__ == "__main__":
    data.bot.run(TOKEN)
