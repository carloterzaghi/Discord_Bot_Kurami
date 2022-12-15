from discord.ext import commands
import discord
from decouple import config
from discord.ext.commands import context
from discord.ext.commands.core import check, command
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from infos_ficha_heroi.fichagenshin import arma_ficha, nome_ficha, lv_ficha, url_ficha, elemento_ficha, ascensao_ficha, raridade_ficha, constelacao_ficha
from infos_ficha_heroi.hp_personagens import vida_ficha
from infos_ficha_heroi.atq_personagens import atq_ficha
from infos_ficha_heroi.def_personagens import def_ficha
from infos_ficha_heroi.heroes_list import heroes_list
from infos_ficha_heroi.destino_heroes import destino_heroes
from discord_buttons_plugin import *
from constelacao_genshin.imagens_constelacao import imagem_constelacao
from constelacao_genshin.dados_constelacao import info_constelacao
from armas_genshin.arma_list import arma_list, separacao_arma, status_arma
from armas_genshin.info_arma_atq import atq_arma
from armas_genshin.info_arma_nome import nome_arma
from armas_genshin.info_estrelas_arma import raridade_arma
from armas_genshin.info_lv_arma import lv_arma
from armas_genshin.info_tipo_arma import tipo_arma
from armas_genshin.url_arma import url_arma
from armas_genshin.info_abilit_arma import abilit_arma

class GenshinArmas(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Mostrar a lista de Armas que tem no Arsenal
    @commands.command()
    async def arsenal(self, ctx,tipo = '', numero = ''):
        user = ctx.message.author.id
        data = db.reference(f"/{user}")
        comeco = data.child("Começou").get()
        if "Sim" == comeco:
            res = data.child(f"Armas").get()
            List = []
            for i in res:
                List.append(i)
            if numero == "" and tipo == '':
                embed = discord.Embed(
                    title = 'Suas Armas',
                    description = '*Para equipar alguma arma no herói que deseja use `k!equipar <N° da Arma do Tipo do Herói> <N° do Herói>`* \n\n' + separacao_arma(List),
                    color = 0x97CBFF
                )
                embed.set_author(name=ctx.author.display_name, url=ctx.message.author.avatar_url, icon_url=ctx.author.avatar_url)
                await ctx.send(embed = embed)
            else:
                try:
                    embed = discord.Embed(
                        title = nome_arma(status_arma(List, tipo, numero)) + ' '+ lv_arma(status_arma(List, tipo, numero)),
                        description = 
                        f"**Raridade:** {raridade_arma(status_arma(List, tipo, numero))}\n" + "**Tipo:** " + tipo_arma(status_arma(List, tipo, numero)),
                        color = 0x97CBFF
                    )
                    embed.add_field(name =
                            "__Stats__", value = "**ATQ**: " + atq_arma(status_arma(List, tipo, numero)) + "\n" + 
                            f"**Abilidade:** {abilit_arma(status_arma(List, tipo, numero))}\n")   
                    embed.set_author(name=ctx.author.display_name, url=ctx.message.author.avatar_url, icon_url=ctx.author.avatar_url)
                    embed.set_image(url =url_arma(status_arma(List, tipo, numero)))
                    await ctx.send(embed = embed)
                except:
                    await ctx.send("Erro no comando, veja em como se manda ele em `k!comandos`.")
        else:
            await ctx.send("Você ainda não iniciou a sua aventura, de `k!start` para iniciar.")
    
    # Equipa a Arma no Heroi
    @commands.command()
    async def equipar(self, ctx, arma = '',heroi = ''):
        user = ctx.message.author.id
        data = db.reference(f"/{user}")
        comeco = data.child("Começou").get()
        if "Sim" == comeco:
            if heroi == '' and arma == '':
                await ctx.send('Para equipar uma arma em um herói use `k!equipar <N° da Arma do Tipo do Herói> <N° do Herói>`.')
            else:
                try:
                    resultHero = data.child(f"Personagens/{str(int(heroi) - 1)}").get()
                    resArma = data.child(f"Armas").get()
                    List = []
                    for i in resArma:
                        List.append(i)
                    armaASerPega = status_arma(List, arma_ficha(resultHero), arma)
                    usandoArma = data.child(f"UsandoArma").get()
                    usandoHeroi = data.child(f"UsandoHeroi").get()
                    # Se o Heroi a se dado for igual ao que está armazenado
                    if resultHero in usandoHeroi:
                        ListArma = []
                        numerar = 0
                        ListHeroi = []
                        for i in usandoHeroi:
                            if resultHero == i:
                                sair = numerar
                            ListHeroi.append(i)
                            numerar = numerar + 1
                        for i in usandoArma:
                            ListArma.append(i)
                        ListArma.remove(ListArma[sair])
                        ListHeroi.remove(ListHeroi[sair])
                        ListArma.append(armaASerPega)
                        ListHeroi.append(resultHero)
                        data.update({          
                            "UsandoArma" : ListArma,
                            "UsandoHeroi" : ListHeroi  
                        })
                        await ctx.send(f"A arma **{nome_arma(armaASerPega)} {lv_arma(armaASerPega)}** foi equipada no herói **{nome_ficha(resultHero)} {lv_ficha(resultHero)}**.")
                    # Se a Arma a se dado for igual ao que está armazenado
                    elif armaASerPega in usandoArma:
                        ListArma = []
                        numerar = 0
                        ListHeroi = []
                        for i in usandoArma:
                            if armaASerPega == i:
                                sair = numerar
                            ListArma.append(i)
                            numerar = numerar + 1
                        for i in usandoHeroi:
                            ListHeroi.append(i)
                        ListArma.remove(ListArma[sair])
                        ListHeroi.remove(ListHeroi[sair])
                        ListArma.append(armaASerPega)
                        ListHeroi.append(resultHero)
                        data.update({          
                            "UsandoArma" : ListArma,
                            "UsandoHeroi" : ListHeroi  
                        })
                        await ctx.send(f"A arma **{nome_arma(armaASerPega)} {lv_arma(armaASerPega)}** foi equipada no herói **{nome_ficha(resultHero)} {lv_ficha(resultHero)}**.")
                    else:
                        ListArma = []
                        for i in usandoArma:
                            ListArma.append(i)
                        ListArma.append(armaASerPega)
                        ListHeroi = []
                        for i in usandoHeroi:
                            ListHeroi.append(i)
                        ListHeroi.append(resultHero)
                        data.update({          
                            "UsandoArma" : ListArma,
                            "UsandoHeroi" : ListHeroi  
                        })
                        await ctx.send(f"A arma **{nome_arma(armaASerPega)} {lv_arma(armaASerPega)}** foi equipada no herói **{nome_ficha(resultHero)} {lv_ficha(resultHero)}**.")
                except:
                    await ctx.send("Erro no comando, veja em como se manda ele em `k!comandos`.")
        else:
            await ctx.send("Você ainda não iniciou a sua aventura, de `k!start` para iniciar.")

def setup(bot):
    bot.add_cog(GenshinArmas(bot))