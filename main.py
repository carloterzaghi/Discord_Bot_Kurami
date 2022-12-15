import os
from discord.ext import commands
from decouple import config
import logging
from discord_buttons_plugin import *

logger = logging.getLogger(__name__)

bot = commands.Bot("k!")
buttons = ButtonsClient(bot)

def load_cogs(bot):
    bot.load_extension("maneger")

    for file in os.listdir("commands"):
        if file.endswith(".py"):
            cog = file[:-3]
            bot.load_extension(f"commands.{cog}")

load_cogs(bot)

TOKEN = config('TOKEN')
bot.run(TOKEN)