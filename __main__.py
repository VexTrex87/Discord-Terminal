import discord
from discord.ext import commands
import shlex
import requests
import shutil
import traceback


from secrets import TOKEN
from commands.set import set_guild_name, set_guild_icon

bot = commands.Bot(command_prefix = "$")
data = {
    "selected_guild": None
}

def get_image(image_url: str):
    filename = "temp/image.png"
    r = requests.get(image_url, stream = True)
    r.raw.decode_content = True

    with open(filename, "wb") as f:
        shutil.copyfileobj(r.raw, f)

    return filename

@bot.event
async def on_ready():
    print("ready")
    while True:
        text = input("$ ")
        args = shlex.split(text, posix = True)
        try:
            if args[0] == "set":
                if args[1] == "guild":
                    guild = discord.utils.find(lambda g: g.name == args[2] or g.id == int(args[2]), bot.guilds)
                    if guild:
                        data["selected_guild"] = guild
                        print(f"selected guild changed to {guild}")
                    else:
                        print("could not find guild {}".format(args[2]))
                elif args[1] == "guildname":
                    await set_guild_name(data["selected_guild"], args[2])
                elif args[1] == "guildicon":
                    guild_icon = get_image(args[2])
                    await set_guild_icon(data["selected_guild"], guild_icon)
                else:
                    print("{} is an invalid argument".format(args[1]))
            elif args[0] == "get":
                if args[1] == "guild":
                    guild = data["selected_guild"]
                    print(f"selected guild is {guild}")
                elif args[1] == "guilds":
                    guilds = []
                    for guild in bot.guilds:
                        guilds.append(guild.name)
                    print(guilds)
                else:
                    print("{} is an invalid argument".format(args[1]))
            else:
                print("{} is an invalid argument".format(args[0]))
        except Exception:
            traceback.print_exc()

bot.run(TOKEN)