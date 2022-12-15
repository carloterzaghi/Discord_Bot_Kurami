from discord.ext import commands
import discord
from decouple import config
from discord.ext.commands import context
from discord.ext.commands.core import check, command
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from infos_ficha_heroi.fichagenshin import nome_ficha, lv_ficha, url_ficha, elemento_ficha, ascensao_ficha, raridade_ficha, constelacao_ficha
from infos_ficha_heroi.hp_personagens import vida_ficha
from infos_ficha_heroi.atq_personagens import atq_ficha
from infos_ficha_heroi.def_personagens import def_ficha
from infos_ficha_heroi.heroes_list import heroes_list
from infos_ficha_heroi.destino_heroes import destino_heroes
from discord_buttons_plugin import *
from constelacao_genshin.imagens_constelacao import imagem_constelacao
from constelacao_genshin.dados_constelacao import info_constelacao

class GenshinConstelacao(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    # Mostrar a Contelação
    @commands.command()
    async def constelacao(self, ctx, heroi = ''):
        user = ctx.message.author.id
        data = db.reference(f"/{user}")
        comeco = data.child("Começou").get()
        if "Sim" == comeco:
            res = data.child(f"Personagens").get()
            List = []
            for i in res:
                List.append(i)
            if heroi == '':
                await ctx.send('Para mostrar a Constelação de um herói use `k!constelacao <Número do Herói>`.')
            else:
                try:
                    result = data.child(f"Personagens/{str(int(heroi) - 1)}").get()
                    if 'Aether' in result or 'Lumine' in result:
                        embed = discord.Embed(
                            title = f'__Constelação {constelacao_ficha(result)} de {nome_ficha(result)}__',
                            description = '*Para aumentar o Lv da Constelação deste heroi, complete as missões destinadas ao Traveler*',
                            color = 0x97CBFF
                        )
                        embed.set_author(name=ctx.author.display_name, url=ctx.message.author.avatar_url, icon_url=ctx.author.avatar_url)
                        embed.add_field(name= '⠀', value= info_constelacao(result), inline=False)
                        embed.set_image(url = imagem_constelacao(result))
                    else:
                        embed = discord.Embed(
                            title = f'__Constelação {constelacao_ficha(result)} de {nome_ficha(result)}__',
                            description = '*Para aumentar o Lv da Constelação deste heroi, combine copias deste mesmo herói usando `k!fundir <N° do herói que deseja receber o bônus> <N° do herói que ira se fundir>`*',
                            color = 0x97CBFF
                        )
                        embed.set_author(name=ctx.author.display_name, url=ctx.message.author.avatar_url, icon_url=ctx.author.avatar_url)
                        embed.add_field(name= '⠀', value= info_constelacao(result), inline=False)
                        embed.set_image(url = imagem_constelacao(result))
                    await ctx.send(embed = embed)
                except:
                    await ctx.send("Erro no comando, veja em como se manda ele em `k!comandos`.")
        else:
            await ctx.send("Você ainda não iniciou a sua aventura, de `k!start` para iniciar.")
    
    # Comando para Fundir personagens para aumentar a Constelação
    @commands.command()
    async def fundir(self, ctx, heroiBonus = '', heroiFundir = ''):
        user = ctx.message.author.id
        data = db.reference(f"/{user}")
        comeco = data.child("Começou").get()
        if "Sim" == comeco:
            res = data.child(f"Personagens").get()
            repetido = data.child("RepetidoPersonagens").get()
            List = []
            for i in res:
                List.append(i)
            ListRepetido = []
            for j in repetido:
                ListRepetido.append(j)
            if heroiBonus == '' or heroiFundir == '':
                await ctx.send('Para fundir um herói use `k!fundir <N° do herói> <N° do herói repetido>`.')
            try:
                conferirBonus = data.child(f"Personagens/{str(int(heroiBonus) - 1)}").get()
                conferirFundir = data.child(f"RepetidoPersonagens/{str(int(heroiFundir) - 1)}").get()
                if nome_ficha(conferirBonus) == nome_ficha(conferirFundir):  
                    iraBonus = List[int(heroiBonus) - 1]
                    retornar = ''
                    naoIr = ''
                    if "{" in iraBonus:
                        for i in iraBonus:
                            if i == '{':
                                retornar = retornar + '}'
                            else:
                                retornar = retornar + i
                    elif "}" in iraBonus:
                        for i in iraBonus:
                            if i == '}':
                                retornar = retornar + '['
                            else:
                                retornar = retornar + i
                    elif "[" in iraBonus:
                        for i in iraBonus:
                            if i == '[':
                                retornar = retornar + ']'
                            else:
                                retornar = retornar + i
                    elif "]" in iraBonus:
                        for i in iraBonus:
                            if i == ']':
                                retornar = retornar + ';'
                            else:
                                retornar = retornar + i
                    elif ";" in iraBonus:
                        for i in iraBonus:
                            if i == ';':
                                retornar = retornar + '<'
                            else:
                                retornar = retornar + i
                    elif "<" in iraBonus:
                        for i in iraBonus:
                            if i == '<':
                                retornar = retornar + '>'
                            else:
                                retornar = retornar + i
                    elif ">" in iraBonus:
                        naoIr = 'Sim'
                    if naoIr == 'Sim':
                        await ctx.send(f'O seu {nome_ficha(iraBonus)} já está no Lv máximo da Constelação {constelacao_ficha(iraBonus)}')
                    else:
                        ListFinal = []
                        remover = List[int(heroiBonus) - 1]
                        if len(ListRepetido) == 1:
                            ListRepetido = ["Vazio"]
                        else:
                            ListRepetido.remove(ListRepetido[int(heroiFundir) - 1])
                        for r in List:
                            if remover == r:
                                ListFinal.append(retornar)
                            else:
                                ListFinal.append(r)
                        data.update({
                                "Personagens" : ListFinal,
                                "RepetidoPersonagens" : ListRepetido
                        })
                        await ctx.send(f'Agora o seu {nome_ficha(retornar)} tem a Constelação {constelacao_ficha(retornar)}')
                else:
                    await ctx.send('Não pode fundir um herói com outro diferente.')
            except:
                await ctx.send("Erro no comando, veja em como se manda ele em `!kcomandos`.")
        else:
            await ctx.send("Você ainda não iniciou a sua aventura, de `k!start` para iniciar.")

    # Mostra os Personagens Repitidos
    @commands.command()
    async def repetidos(self, ctx, msg = ''):
        user = ctx.message.author.id
        data = db.reference(f"/{user}")
        comeco = data.child("Começou").get()
        if "Sim" == comeco:
            repetidos = data.child("RepetidoPersonagens").get()
            List = []
            for i in repetidos:
                List.append(i)
            max = len(List)
            if msg == '':
                if data.child(f"RepetidoPersonagens/0").get() == "Vazio":
                        embed = discord.Embed(
                        title = 'Seus Heróis Repetidos',
                        description = "**Vazio**",
                        color = 0x97CBFF
                    )
                else:
                    embed = discord.Embed(
                        title = 'Seus Heróis Repetidos',
                        description = heroes_list(List),
                        color = 0x97CBFF
                    )
                embed.set_author(name=ctx.author.display_name, url=ctx.message.author.avatar_url, icon_url=ctx.author.avatar_url)
                await ctx.send(embed = embed)
            else:
                try:
                    result = data.child(f"RepetidoPersonagens/{str(int(msg) - 1)}").get()
                    embed = discord.Embed(
                        title = nome_ficha(result)+ " " + lv_ficha(result),
                        description = 
                        f"**Raridade:** {raridade_ficha(result)}\n" + "**Ascensão:** " + ascensao_ficha(result) + 
                        "⠀⠀⠀⠀\n" + f"**Constelação:** {constelacao_ficha(result)} \n" + "**Elemento:** " + elemento_ficha(result),
                        color = 0x97CBFF
                    )
                    embed.set_thumbnail(url = ctx.message.author.avatar_url)
                    embed.add_field(name =
                    "__Stats__", value = "**HP:** " + vida_ficha(result) + "\n" + "**ATQ:** " + atq_ficha(result) + "\n" + 
                    "**DEF:** " + def_ficha(result) + "\n\n\n" "**Slot:** "+ str(msg) + " / " + str(max))                            
                    embed.set_image(url = url_ficha(result))
                    await ctx.send(embed = embed)
                except:
                    await ctx.send("Erro no comando, veja em como se manda ele em `!kcomandos`.")
        else:
            await ctx.send("Você ainda não iniciou a sua aventura, de `k!start` para iniciar.")

def setup(bot):
    bot.add_cog(GenshinConstelacao(bot))