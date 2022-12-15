from typing import List
from discord import raw_models
from discord.ext import commands
import random

def monkey(nick):
    List = ["Por favor, " + nick + ", não seja monkey!", nick + ", você é um monkey", "Pare de ser monkey " + nick, "Meu deus " +nick+ ", você é monkey de mais"]
    return random.choice(List)