from discord.ext import commands
from discord.ext.commands.errors import MissingRequiredArgument

class Maneger(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Kurami Online")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, MissingRequiredArgument):
            await ctx.send("Erro no comando, verifique ele.")
        else:
            raise error

def setup(bot):
    bot.add_cog(Maneger(bot))