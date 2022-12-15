from artefatos_genshin.set_artefatos import set_artefato
from artefatos_genshin.estrelas_artefato import estrelas_artefato
from artefatos_genshin.url_artefato import url_artefato
from artefatos_genshin.lv_artefato import lv_artefato
from artefatos_genshin.nome_artefato import nome_artefato
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
from artefatos_genshin.artefatos_list import artefatos_list, separacao_artefatos, status_artefatos
from artefatos_genshin.flor import umAtresFlor, tresAquatroFlor, quatroAcincoFlor
from armas_genshin.info_arma_atq import atq_arma
from armas_genshin.info_arma_nome import nome_arma
from armas_genshin.info_estrelas_arma import raridade_arma
from armas_genshin.info_lv_arma import lv_arma
from armas_genshin.info_tipo_arma import tipo_arma
from artefatos_genshin.tipo_artefatos import tipo_artefato
from artefatos_genshin.stats_artefatos import stats_artefatos
from artefatos_genshin.ampulheta import umAtresAmpulheta, tresAquatroAmpulheta, quatroAcincoAmpulheta
from artefatos_genshin.calice import umAtresCalice, tresAquatroCalice, quatroAcincoCalice
from artefatos_genshin.pena import umAtresPena, tresAquatroPena, quatroAcincoPena
from artefatos_genshin.coroa import umAtresCoroa, tresAquatroCoroa, quatroAcincoCoroa

class GenshinArtefatos(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # P - HP, K - ATK, F - DEF, H - HP%, T - ATK%, D - DEF%, M - EM, C - CritRate, R - CRITDMG
    # Mostrar a lista de Artefatos
    @commands.command()
    async def artefatos(self, ctx, tipo = '', numero = ''):
        user = ctx.message.author.id
        data = db.reference(f"/{user}")
        comeco = data.child("Começou").get()
        if "Sim" == comeco:
            artefatos = data.child("Artefatos").get()
            List = []
            for i in artefatos:
                List.append(i)
            if numero == '' and tipo == '':
                if data.child(f"Artefatos/0").get() == "Vazio":
                        embed = discord.Embed(
                        title = 'Seus Artefatos',
                        description = "**Vazio**",
                        color = 0x97CBFF
                    )
                else:
                    embed = discord.Embed(
                        title = 'Seus Artefatos',
                        description = separacao_artefatos(List),
                        color = 0x97CBFF
                    )
                embed.set_author(name=ctx.author.display_name, url=ctx.message.author.avatar_url, icon_url=ctx.author.avatar_url)
                await ctx.send(embed = embed)
            else:
                try:
                    embed = discord.Embed(
                        title = set_artefato(status_artefatos(List, tipo, numero)) + ' Lv.'+ lv_artefato(status_artefatos(List, tipo, numero)),
                        description = 
                        f"**Raridade:** {estrelas_artefato(status_artefatos(List, tipo, numero))}\n" + "**Tipo:** " + tipo_artefato(status_artefatos(List, tipo, numero)),
                        color = 0x97CBFF
                    )
                    embed.add_field(name =
                            "__Stats__", value = stats_artefatos(status_artefatos(List, tipo, numero)))
                    embed.set_author(name=ctx.author.display_name, url=ctx.message.author.avatar_url, icon_url=ctx.author.avatar_url)
                    embed.set_image(url =url_artefato(status_artefatos(List, tipo, numero)))
                    await ctx.send(embed = embed)
                except:
                    await ctx.send("Erro no comando, veja em como se manda ele em `!kcomandos`.")
        else:
            await ctx.send("Você ainda não iniciou a sua aventura, de `k!start` para iniciar.")

    # Equipa o Artefato
    @commands.command() 
    async def gerenciar(self, ctx, tipo = '', artefato = '', heroi = ''):
        user = ctx.message.author.id
        data = db.reference(f"/{user}")
        comeco = data.child("Começou").get()
        if "Sim" == comeco:
            if heroi == '' and tipo == '' and artefato == '':
                await ctx.send('Para equipar um artefato em um herói use `k!gerenciar <Tipo do Artefato> <N° do Artefato> <N° do Herói>`.')
            elif heroi == '' or tipo == '' or artefato == '':
                await ctx.send('Para equipar um artefato em um herói use `k!gerenciar <Tipo do Artefato> <N° do Artefato> <N° do Herói>`.')
            else:
                try:
                    resultHero = data.child(f"Personagens/{str(int(heroi) - 1)}").get()
                    resArtefatos = data.child(f"Artefatos").get()
                    List = []
                    for i in resArtefatos:
                        List.append(i)
                    artefatosASerPega = status_artefatos(List, tipo, artefato)
                    usandoArtefatos = data.child(f"EquipaArtefato").get()
                    usandoHeroi = data.child(f"EquipaHeroi").get()
                    # Se o Heroi a se dado for igual ao que está armazenado
                    if resultHero in usandoHeroi:
                        ListArtefatos = []
                        numerar = 0
                        ListHeroi = []
                        ArtefatoHeroi = []
                        for i in usandoHeroi:
                            if resultHero == i:
                                sair = numerar
                            ListHeroi.append(i)
                            numerar = numerar + 1
                        for i in usandoArtefatos:
                            ListArtefatos.append(i)
                        ArtefatoHeroi.append(ListArtefatos[sair])
                        ListArtefatos.remove(ListArtefatos[sair])
                        ListHeroi.remove(ListHeroi[sair])
                        numero = 0
                        adicionar = []
                        if "flor" in artefatosASerPega:
                            for i in ArtefatoHeroi[0]:
                                numero = numero + 1
                                if numero == 1:
                                    adicionar.append(artefatosASerPega)
                                else:
                                    adicionar.append(i)
                        elif "calice" in artefatosASerPega:
                            for i in ArtefatoHeroi[0]:
                                numero = numero + 1
                                if numero == 4:
                                    adicionar.append(artefatosASerPega)
                                else:
                                    adicionar.append(i)
                        elif "ampulheta" in artefatosASerPega:
                            for i in ArtefatoHeroi[0]:
                                numero = numero + 1
                                if numero == 3:
                                    adicionar.append(artefatosASerPega)
                                else:
                                    adicionar.append(i)
                        elif "coroa" in artefatosASerPega:
                            for i in ArtefatoHeroi[0]:
                                numero = numero + 1
                                if numero == 5:
                                    adicionar.append(artefatosASerPega)
                                else:
                                    adicionar.append(i)
                        elif "pena" in artefatosASerPega:
                            for i in ArtefatoHeroi[0]:
                                numero = numero + 1
                                if numero == 2:
                                    adicionar.append(artefatosASerPega)
                                else:
                                    adicionar.append(i)
                        ListArtefatos.append(adicionar)
                        ListHeroi.append(resultHero)
                        data.update({          
                            "EquipaArtefato" : ListArtefatos,
                            "EquipaHeroi" : ListHeroi  
                        })
                        await ctx.send(f"O artefato **{tipo_artefato(artefatosASerPega)} {set_artefato(artefatosASerPega)} {lv_artefato(artefatosASerPega)}** foi equipada no herói **{nome_ficha(resultHero)} {lv_ficha(resultHero)}**.")
                    else:
                        ListArtefatos = []
                        for i in usandoArtefatos:
                            if i != "Vazio":
                                ListArtefatos.append(i)
                        adicionar = ['Flor', 'Pena', 'Ampulheta', 'Calice', 'Coroa']
                        if "flor" in artefatosASerPega:
                            adicionar = [artefatosASerPega, 'Pena', 'Ampulheta', 'Calice', 'Coroa']
                        elif "calice" in artefatosASerPega:
                            adicionar = ['Flor', 'Pena', 'Ampulheta', artefatosASerPega, 'Coroa']
                        elif "ampulheta" in artefatosASerPega:
                            adicionar = ['Flor', 'Pena', artefatosASerPega, 'Calice', 'Coroa']
                        elif "coroa" in artefatosASerPega:
                            adicionar = ['Flor', 'Pena', 'Ampulheta', 'Calice', artefatosASerPega]
                        elif "pena" in artefatosASerPega:
                            adicionar = ['Flor', artefatosASerPega, 'Ampulheta', 'Calice', 'Coroa']
                        ListArtefatos.append(adicionar)
                        ListHeroi = []
                        for i in usandoHeroi:
                            if i != "Vazio":
                                ListHeroi.append(i)
                        ListHeroi.append(resultHero)
                        data.update({          
                            "EquipaArtefato" : ListArtefatos,
                            "EquipaHeroi" : ListHeroi  
                        })
                        await ctx.send(f"O artefato **{tipo_artefato(artefatosASerPega)} {set_artefato(artefatosASerPega)} {lv_artefato(artefatosASerPega)}** foi equipada no herói **{nome_ficha(resultHero)} {lv_ficha(resultHero)}**.")
                except:
                    await ctx.send("Erro no comando, veja em como se manda ele em `k!comandos`.")
        else:
            await ctx.send("Você ainda não iniciou a sua aventura, de `k!start` para iniciar.")

    # Mostrar a lista de Artefatos
    @commands.command()
    async def testeartefatos(self, ctx):
        user = ctx.message.author.id
        data = db.reference(f"/{user}")
        result = data.child(f"Artefatos").get()
        List = []
        for i in result:
            if i != 'Vazio':
                List.append(i)
        List.append(umAtresCoroa())
        data.update({
            "Artefatos" : List,       
        })
        await ctx.send(
                "Adicionado"
            )
    
    @commands.command()
    async def umtesteartefatos(self, ctx):
        user = ctx.message.author.id
        data = db.reference(f"/{user}")
        result = data.child(f"Artefatos").get()
        List = []
        for i in result:
            if i != 'Vazio':
                List.append(i)
        List.append(tresAquatroCoroa())
        data.update({
            "Artefatos" : List,       
        })
        await ctx.send(
                "Adicionado"
            )
    
    @commands.command()
    async def doistesteartefatos(self, ctx):
        user = ctx.message.author.id
        data = db.reference(f"/{user}")
        result = data.child(f"Artefatos").get()
        List = []
        for i in result:
            if i != 'Vazio':
                List.append(i)
        List.append(quatroAcincoCoroa())
        data.update({
            "Artefatos" : List,       
        })
        await ctx.send(
                "Adicionado"
            )

def setup(bot):
    bot.add_cog(GenshinArtefatos(bot))