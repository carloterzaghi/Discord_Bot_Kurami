from discord.ext import commands
import discord
from discord.colour import Color

class Conversas(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name = "nekos", help = "Manda a imagem de uma Neko aleatória.")
    async def send_neko(self, ctx):
        await ctx.send("https://nekos.life/")

    @commands.command(name = "stats", help = "Verifica se está Online o Bot.")
    async def send_stats(self, ctx):
        await ctx.send("I'm Online")

    @commands.command(name = "comandos", help = "Manda os comandos do Bot no privado.")
    async def send_help(self, ctx):
        try:
            embed = discord.Embed(
                title = "__Informações do Bot__",
                description = "*Este bot foi feito somente para alguns servers.*",
                color = 0x97CBFF
            )   
            embed.set_author(name = self.bot.user.name, icon_url= self.bot.user.avatar_url)
            embed.add_field(name= "⠀\n__GENSHIN BÁSICO:__", value=
             '➤ **k!start**: Começa a sua aventura em Genshin Impact. \n ➤ **k!heroes**: Mostra todos os seus heróis.' +
             '\n➤ **k!heroes <N° do Slot>**: Mostra os status do herói que você tem no slot desejado. \n ➤ **k!status**: Mostra os seus status no jogo.' + 
             '\n ➤ **k!select <N° do seu herói> <N° do slot que você quer colocar o personagem>**: Você coloca o herói no slot de sua equipe. \n'
             , inline=False)
            embed.add_field(name= "⠀\n__GENSHIN SHOP:__", value= 
            '➤ **k!shop**: Loja de itens do jogo. \n ➤ **k!buy <Nome do Item>**: Compra o item que deseja. \n ➤ **k!use <Nome do Item>**: Usa o item que deseja.\n' +
            '➤ **k!repetidos**: Mostra todos os seus heróis repetidos. \n➤ **k!repetidos <N° do Slot>**: Mostra os status do herói repetido que você tem no slot desejado.'
            , inline=False)
            embed.add_field(name= "⠀\n__GENSHIN CONSTELAÇÃO:__", value= 
            "➤ **k!constelacao <Número do Herói>**: Mostra o nível de Constelação do seu Herói." + 
             "\n ➤ **k!fundir <N° do herói> <N° do herói repetido>**: Fundi um herói com outro para aumentar o seu Lv da Constelação. \n"
            , inline=False)
            embed.add_field(name= "⠀\n__GENSHIN ARMAS:__", value= 
            '➤ **k!arsenal**: Mostra todas as suas armas. \n ➤ **k!arsenal <Tipo da Arma> <N° da Arma>**: Mostra os status da arma que você tem no slot desejado.\n' +
             '➤ **k!equipar <N° da Arma do Tipo do Herói> <N° do Herói>**: Para equipar uma arma do seu arsenal no herói que deseja. \n' 
            , inline=False)
            embed.add_field(name= "⠀\n__GENSHIN ARTEFATOS:__", value= 
            '➤ **k!artefatos**: Mostra todos os seus artefatos. \n ➤ **k!artefatos <Tipo do Artefato> <N° do Artefato>**: Mostra os status do artefato que você tem no slot desejado.\n' +
            '➤ **k!gerenciar <Tipo do Artefato> <N° do Artefato> <N° do Herói>**: Para equipar um artefato do seu desejo no herói que deseja.' 
            , inline=False)
            embed.add_field(name ="⠀\n__OUTROS:__", value = "➤ **k!nekos**: Manda um link de uma imagem de neko aleatória. \n ➤ **k!tictactoe**: Inicia partida de Jogo da Velha.\n ➤ **k!place (N°)**: Coloca o seu simbolo no número da casa que deseja.", inline=False)
            await ctx.author.send(embed = embed)
            
        except discord.errors.Forbidden:
            await ctx.send(
                "Não foi possível mandar a mensagem, por favor abilitar receber mensagem de qualquer pessoa do servidor (Opções > Privacidade)"
            )
        
def setup(bot):
    bot.add_cog(Conversas(bot))