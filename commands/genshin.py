from discord.ext import commands
import discord
from decouple import config
from discord.ext.commands import context
from discord.ext.commands.core import check, command
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from infos_ficha_heroi.fichagenshin import nome_ficha, lv_ficha, url_ficha, elemento_ficha, ascensao_ficha, raridade_ficha, constelacao_ficha, arma_ficha
from infos_ficha_heroi.hp_personagens import vida_ficha
from infos_ficha_heroi.atq_personagens import atq_ficha
from infos_ficha_heroi.def_personagens import def_ficha
from infos_ficha_heroi.heroes_list import heroes_list
from infos_ficha_heroi.destino_heroes import destino_heroes
from discord_buttons_plugin import *
from armas_genshin.arma_list import arma_list, separacao_arma, status_arma
from armas_genshin.info_arma_atq import atq_arma
from armas_genshin.info_arma_nome import nome_arma
from armas_genshin.info_estrelas_arma import raridade_arma
from armas_genshin.info_lv_arma import lv_arma
from armas_genshin.info_tipo_arma import tipo_arma
from armas_genshin.url_arma import url_arma
from armas_genshin.info_abilit_arma import abilit_arma
from infos_ficha_heroi.multiplicar import atq_multiplica, def_multiplica, hp_multiplica
from artefatos_genshin.set_artefatos import set_artefato
from artefatos_genshin.estrelas_artefato import estrelas_artefato
from artefatos_genshin.url_artefato import url_artefato
from artefatos_genshin.lv_artefato import lv_artefato
from artefatos_genshin.tipo_artefatos import tipo_artefato
from artefatos_genshin.stats_artefatos import stats_artefatos
from artefatos_genshin.artefatos_list import status_artefatos, artefatos_list, artefatos_heroes
from artefatos_genshin.lv_artefato import lv_artefato
from artefatos_genshin.estrelas_artefato import estrelas_artefato
from artefatos_genshin.hp_artefato import hp_artefato, hpPorcento_artefato, hpPorcentoHeroes_artefato
from artefatos_genshin.atq_artefato import atq_artefato, atqPorcento_artefato, em_artefato, critDMG_artefato, critRate_artefato,atqPorcentoHeroes_artefato, critRateHeroes_artefato, critDMGHeroes_artefato, emHeroes_artefato
from artefatos_genshin.def_artefato import defe_artefato, defePorcento_artefato, defePorcentoHeroes_artefato
from artefatos_genshin.set_artefatos import set_artefato
import traceback
import math

class Genshin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #Teste de mandar DB
    @commands.command()
    async def write(self, ctx, mensagem):
        user = ctx.message.author.id
        ref = db.reference(f"/")
        ref.update({
            user: {
                "Color" : str(mensagem)
            }
        })
    
    # Teste de pegar DB
    @commands.command()
    async def cor(self, ctx):
        user = ctx.message.author.id
        data = db.reference(f"/{user}")
        result = data.child("Personagens").get()
        await ctx.send(result)

    # Teste mandar mesma mensagem
    @commands.command()
    async def falar(self, ctx, mensagem):
        await ctx.send(mensagem)

    # Iniciar o Genshin
    @commands.command()
    async def start(self, ctx):
        user = ctx.message.author.id
        data = db.reference(f"/{user}")
        comeco = data.child("Começou").get()
        result = data.child("Personagens").get()
        if  "Sim" == comeco:
            await ctx.send('Você já iniciou a aventura.')
        
        else:
            embed = discord.Embed(
                title = "Bem vindo ao mundo de Genshin Impact!",
                description = "Para começar, escolha um irmão para ir junto a você em sua jornada, use `k!pick <Nome do Irmão>`",
                color = 0x97CBFF
            )

            embed.add_field(name = "Lumine", value = "Irmã - Use `k!pick Lumine`")
            embed.add_field(name = "Aether", value = "Irmão - Use `k!pick Aether`")
            embed.set_image(url = 'https://progameguides.com/wp-content/uploads/2020/09/Genshin-Impact-Which-Twin-to-Choose.jpg')
            
            await ctx.send(embed = embed)

    # Escolher o seu Viajante inicial
    @commands.command()
    async def pick(self, ctx, mensagem):
        user = ctx.message.author.id
        ref = db.reference(f"/")
        data = db.reference(f"/{user}")
        result = data.child("Personagens").get()
        comeco = data.child("Começou").get()
        if  "Sim" == comeco:
            await ctx.send('Você já pegou o seu aventureiro.')
        else:
            if mensagem == "Lumine":
                ref.update({
                    user: {
                        "Começou" : "Sim",
                        "Personagens" : ["Lumine 1 ) {"],
                        "Wins" : 0,
                        "Losses" : 0,
                        "Money" : 1000,
                        "Destino" : 0,
                        "Super Destino" : 0,
                        "Destino Heroes" : 1,
                        "Select Heroes" : ["Lumine 1 ) {", "Vazio", "Vazio"],
                        "Armas" : ["lâmina maçante 1 S", "notas do aprendiz 1 C", "protetor de iniciantes 1 P", "espada larga waster 1 E", "arco de caça 1 B"],
                        "UsandoArma" : ["lâmina maçante 1 S"],
                        "UsandoHeroi" : ["Aether 1 ) {"],
                        "RepetidoPersonagens" : ["Vazio"],
                        "Artefatos" : ["Vazio"],
                        "EquipaArtefato" : ["Vazio"],
                        "EquipaHeroi" : ["Vazio"]
                    }
                })
                embed = discord.Embed(
                    title = "Você escolheu a Lumine",
                    description = "A sua aventura começa agora, caso tenha alguma duvida dos comandos digite `k!comandos`.",
                    color = 0x97CBFF
                )
                embed.set_image(url = 'https://static.wikia.nocookie.net/genshin-impact/images/0/02/Personagem_Viajante_Feminino_Cart%C3%A3o.jpg/revision/latest?cb=20210320120732&path-prefix=pt-br')
                await ctx.send(embed = embed)
            elif mensagem == "Aether":
                ref.update({
                    user: {
                        "Começou" : "Sim",
                        "Personagens" : ["Aether 1 ) {"],
                        "Wins" : 0,
                        "Losses" : 0,
                        "Money" : 1000,
                        "Destino" : 0,
                        "Super Destino" : 0,
                        "Destino Heroes" : 1,
                        "Select Heroes" : ["Aether 1 ) {", "Vazio", "Vazio"],
                        "Armas" : ["lâmina maçante 1 S", "notas do aprendiz 1 C", "protetor de iniciantes 1 P", "espada larga waster 1 E", "arco de caça 1 B"],
                        "UsandoArma" : ["lâmina maçante 1 S"],
                        "UsandoHeroi" : ["Aether 1 ) {"],
                        "RepetidoPersonagens" : ["Vazio"],
                        "Artefatos" : ["Vazio"],
                        "EquipaArtefato" : ["Vazio"],
                        "EquipaHeroi" : ["Vazio"]
                    }
                })
                embed = discord.Embed(
                    title = "Você escolheu o Aether",
                    description = "A sua aventura começa agora, caso tenha alguma duvida dos comandos digite `k!comandos`.",
                    color = 0x97CBFF
                )
                embed.set_image(url = 'https://static.wikia.nocookie.net/gensin-impact/images/1/1c/Traveler_Male_Card.jpg/revision/latest?cb=20201024043323')
                await ctx.send(embed = embed)
            elif mensagem == "":
                ctx.send("Digite o nome do irmão, assim `k!pick <Nome do Irmão>`")
            else:
                ctx.send("`Erro no comando, verifique.`")
    
    # Stats dos Personagens
    @commands.command()
    async def heroes(self, ctx, msg = ''):
        user = ctx.message.author.id
        data = db.reference(f"/{user}")
        comeco = data.child("Começou").get()
        try:
            res = data.child(f"Personagens").get()
            List = []
            for i in res:
                List.append(i)
            max = len(List)
            if  "Sim" == comeco:
                try:
                    if msg == "":
                        embed = discord.Embed(
                            title = 'Seus Heróis',
                            description = heroes_list(List),
                            color = 0x97CBFF
                        )
                        embed.set_author(name=ctx.author.display_name, url=ctx.message.author.avatar_url, icon_url=ctx.author.avatar_url)
                        await ctx.send(embed = embed)
                    else:
                        result = data.child(f"Personagens/{str(int(msg) - 1)}").get()
                        usandoHeroi = data.child(f"UsandoHeroi").get()
                        equipaHeroi = data.child(f"EquipaHeroi").get()
                        # Se Personagem tiver em Arma e Artefato
                        if result in usandoHeroi and result in equipaHeroi:
                            numero = 0
                            for i in usandoHeroi:
                                if i == result:
                                    retornar = numero
                                numero = numero + 1
                            numero = 0
                            for i in equipaHeroi:
                                if i == result:
                                    artefatoRetornar = numero
                                numero = numero + 1
                            usandoArma = data.child(f"UsandoArma/{str(int(retornar))}").get()
                            equipaArtefato = data.child(f"EquipaArtefato/{str(int(artefatoRetornar))}").get()
                            embed = discord.Embed(
                                title = nome_ficha(result)+ " " + lv_ficha(result),
                                description = 
                                f"**Raridade:** {raridade_ficha(result)}\n" + "**Ascensão:** " + ascensao_ficha(result) + 
                                "⠀⠀⠀⠀\n" + f"**Constelação:** {constelacao_ficha(result)} \n" + "**Elemento:** " + elemento_ficha(result) + 
                                "\n**Arma:** " + arma_ficha(result),
                                color = 0x97CBFF
                            )
                            flor = 'Flor'
                            calice = 'Calice'
                            ampulheta = 'Ampulheta'
                            coroa = 'Coroa'
                            pena = 'Pena'
                            embed.set_thumbnail(url = ctx.message.author.avatar_url)
                            embed.add_field(name =
                            "__Stats__", value = "**HP:** " + str(round((int(vida_ficha(result).replace(',', '')) + 
                            int(hp_multiplica(result)) + int(hp_artefato(status_artefatos(equipaArtefato, flor, 1))) + int(hp_artefato(status_artefatos(equipaArtefato, calice, 1)))  + 
                            int(hp_artefato(status_artefatos(equipaArtefato, ampulheta, 1)))  + int(hp_artefato(status_artefatos(equipaArtefato, coroa, 1)))   + 
                            int(hp_artefato(status_artefatos(equipaArtefato, pena, 1)))) * (float(hpPorcentoHeroes_artefato(status_artefatos(equipaArtefato, ampulheta, 1))) + 
                            float(hpPorcentoHeroes_artefato(status_artefatos(equipaArtefato, calice, 1))) + float(hpPorcentoHeroes_artefato(status_artefatos(equipaArtefato, flor, 1))) + 
                            float(hpPorcentoHeroes_artefato(status_artefatos(equipaArtefato, coroa, 1))) + float(hpPorcentoHeroes_artefato(status_artefatos(equipaArtefato, pena, 1))) or 1
                            ))) + "\n" +
                            "**ATQ:** " + str(round((int(atq_ficha(result))  + int(atq_arma(usandoArma)) +
                            int(atq_multiplica(result)) + int(atq_artefato(status_artefatos(equipaArtefato, flor, 1))) + int(atq_artefato(status_artefatos(equipaArtefato, calice, 1)))  + 
                            int(atq_artefato(status_artefatos(equipaArtefato, ampulheta, 1)))  + int(atq_artefato(status_artefatos(equipaArtefato, coroa, 1)))   + 
                            int(atq_artefato(status_artefatos(equipaArtefato, pena, 1)))) * (float(atqPorcentoHeroes_artefato(status_artefatos(equipaArtefato, ampulheta, 1))) + 
                            float(atqPorcentoHeroes_artefato(status_artefatos(equipaArtefato, calice, 1))) + float(atqPorcentoHeroes_artefato(status_artefatos(equipaArtefato, flor, 1))) + 
                            float(atqPorcentoHeroes_artefato(status_artefatos(equipaArtefato, coroa, 1))) + float(atqPorcentoHeroes_artefato(status_artefatos(equipaArtefato, pena, 1))) or 1
                            ))) + "\n" +
                            "**DEF:** " + str(round((int(def_ficha(result))  + 
                            int(def_multiplica(result)) + int(defe_artefato(status_artefatos(equipaArtefato, flor, 1))) + int(defe_artefato(status_artefatos(equipaArtefato, calice, 1)))  + 
                            int(defe_artefato(status_artefatos(equipaArtefato, ampulheta, 1)))  + int(defe_artefato(status_artefatos(equipaArtefato, coroa, 1)))   + 
                            int(defe_artefato(status_artefatos(equipaArtefato, pena, 1)))) * (float(defePorcentoHeroes_artefato(status_artefatos(equipaArtefato, ampulheta, 1))) + 
                            float(defePorcentoHeroes_artefato(status_artefatos(equipaArtefato, calice, 1))) + float(defePorcentoHeroes_artefato(status_artefatos(equipaArtefato, flor, 1))) + 
                            float(defePorcentoHeroes_artefato(status_artefatos(equipaArtefato, coroa, 1))) + float(defePorcentoHeroes_artefato(status_artefatos(equipaArtefato, pena, 1))) or 1
                            ))) + "\n" +
                            "**CRIT Rate%:** " + str(float(critRateHeroes_artefato(status_artefatos(equipaArtefato, flor, 1))) + float(critRateHeroes_artefato(status_artefatos(equipaArtefato, calice, 1))) +
                            float(critRateHeroes_artefato(status_artefatos(equipaArtefato, ampulheta, 1))) + float(critRateHeroes_artefato(status_artefatos(equipaArtefato, coroa, 1))) +
                            float(critRateHeroes_artefato(status_artefatos(equipaArtefato, pena, 1))) or 1.0
                            ) + '%'+ "\n" +
                            "**CRIT DMG%:** " + str(1 + float(critDMGHeroes_artefato(status_artefatos(equipaArtefato, flor, 1))) + float(critDMGHeroes_artefato(status_artefatos(equipaArtefato, calice, 1))) +
                            float(critDMGHeroes_artefato(status_artefatos(equipaArtefato, ampulheta, 1))) + float(critDMGHeroes_artefato(status_artefatos(equipaArtefato, coroa, 1))) +
                            float(critDMGHeroes_artefato(status_artefatos(equipaArtefato, pena, 1))) or 1.0
                            ) + '%' + "\n" +
                            "**Elemental Mastery:** " + str(int(emHeroes_artefato(status_artefatos(equipaArtefato, flor, 1))) + int(emHeroes_artefato(status_artefatos(equipaArtefato, calice, 1))) +
                            int(emHeroes_artefato(status_artefatos(equipaArtefato, ampulheta, 1))) + int(emHeroes_artefato(status_artefatos(equipaArtefato, coroa, 1))) +
                            int(emHeroes_artefato(status_artefatos(equipaArtefato, pena, 1)))
                            ) +
                            f'\n\n **Equipado:** {nome_arma(usandoArma)} {lv_arma(usandoArma)}' +
                            f'\n\n__**Artefatos**__\n **Flor:** {artefatos_heroes(status_artefatos(equipaArtefato, flor, 1))}' +
                            f'**Pena:** {artefatos_heroes(status_artefatos(equipaArtefato, pena, 1))}' +
                            f'**Ampulheta:** {artefatos_heroes(status_artefatos(equipaArtefato, ampulheta, 1))}' +
                            f'**Calice:** {artefatos_heroes(status_artefatos(equipaArtefato, calice, 1))}' +
                            f'**Coroa:** {artefatos_heroes(status_artefatos(equipaArtefato, coroa, 1))}' +
                            f"\n\n\n**Slot:** {str(msg)} / {str(max)}")                              
                            embed.set_image(url = url_ficha(result))
                            await ctx.send(embed = embed)
                        # Se Personagem tiver Artefato
                        elif result in equipaHeroi:
                            numero = 0
                            for i in equipaHeroi:
                                if i == result:
                                    artefatoRetornar = numero
                                numero = numero + 1
                            equipaArtefato = data.child(f"EquipaArtefato/{str(int(artefatoRetornar))}").get()
                            embed = discord.Embed(
                                title = nome_ficha(result)+ " " + lv_ficha(result),
                                description = 
                                f"**Raridade:** {raridade_ficha(result)}\n" + "**Ascensão:** " + ascensao_ficha(result) + 
                                "⠀⠀⠀⠀\n" + f"**Constelação:** {constelacao_ficha(result)} \n" + "**Elemento:** " + elemento_ficha(result) + 
                                "\n**Arma:** " + arma_ficha(result),
                                color = 0x97CBFF
                            )
                            flor = 'Flor'
                            calice = 'Calice'
                            ampulheta = 'Ampulheta'
                            coroa = 'Coroa'
                            pena = 'Pena'
                            embed.set_thumbnail(url = ctx.message.author.avatar_url)
                            embed.add_field(name =
                            "__Stats__", value = "**HP:** " + str(round((int(vida_ficha(result).replace(',', '')) + 
                            int(hp_multiplica(result)) + int(hp_artefato(status_artefatos(equipaArtefato, flor, 1))) + int(hp_artefato(status_artefatos(equipaArtefato, calice, 1)))  + 
                            int(hp_artefato(status_artefatos(equipaArtefato, ampulheta, 1)))  + int(hp_artefato(status_artefatos(equipaArtefato, coroa, 1)))   + 
                            int(hp_artefato(status_artefatos(equipaArtefato, pena, 1)))) * (float(hpPorcentoHeroes_artefato(status_artefatos(equipaArtefato, ampulheta, 1))) + 
                            float(hpPorcentoHeroes_artefato(status_artefatos(equipaArtefato, calice, 1))) + float(hpPorcentoHeroes_artefato(status_artefatos(equipaArtefato, flor, 1))) + 
                            float(hpPorcentoHeroes_artefato(status_artefatos(equipaArtefato, coroa, 1))) + float(hpPorcentoHeroes_artefato(status_artefatos(equipaArtefato, pena, 1))) or 1
                            ))) + "\n" +
                            "**ATQ:** " + str(round((int(atq_ficha(result))  + 
                            int(atq_multiplica(result)) + int(atq_artefato(status_artefatos(equipaArtefato, flor, 1))) + int(atq_artefato(status_artefatos(equipaArtefato, calice, 1)))  + 
                            int(atq_artefato(status_artefatos(equipaArtefato, ampulheta, 1)))  + int(atq_artefato(status_artefatos(equipaArtefato, coroa, 1)))   + 
                            int(atq_artefato(status_artefatos(equipaArtefato, pena, 1)))) * (float(atqPorcentoHeroes_artefato(status_artefatos(equipaArtefato, ampulheta, 1))) + 
                            float(atqPorcentoHeroes_artefato(status_artefatos(equipaArtefato, calice, 1))) + float(atqPorcentoHeroes_artefato(status_artefatos(equipaArtefato, flor, 1))) + 
                            float(atqPorcentoHeroes_artefato(status_artefatos(equipaArtefato, coroa, 1))) + float(atqPorcentoHeroes_artefato(status_artefatos(equipaArtefato, pena, 1))) or 1
                            ))) + "\n" +
                            "**DEF:** " + str(round((int(def_ficha(result))  + 
                            int(def_multiplica(result)) + int(defe_artefato(status_artefatos(equipaArtefato, flor, 1))) + int(defe_artefato(status_artefatos(equipaArtefato, calice, 1)))  + 
                            int(defe_artefato(status_artefatos(equipaArtefato, ampulheta, 1)))  + int(defe_artefato(status_artefatos(equipaArtefato, coroa, 1)))   + 
                            int(defe_artefato(status_artefatos(equipaArtefato, pena, 1)))) * (float(defePorcentoHeroes_artefato(status_artefatos(equipaArtefato, ampulheta, 1))) + 
                            float(defePorcentoHeroes_artefato(status_artefatos(equipaArtefato, calice, 1))) + float(defePorcentoHeroes_artefato(status_artefatos(equipaArtefato, flor, 1))) + 
                            float(defePorcentoHeroes_artefato(status_artefatos(equipaArtefato, coroa, 1))) + float(defePorcentoHeroes_artefato(status_artefatos(equipaArtefato, pena, 1))) or 1
                            ))) + "\n" +
                            "**CRIT Rate%:** " + str(float(critRateHeroes_artefato(status_artefatos(equipaArtefato, flor, 1))) + float(critRateHeroes_artefato(status_artefatos(equipaArtefato, calice, 1))) +
                            float(critRateHeroes_artefato(status_artefatos(equipaArtefato, ampulheta, 1))) + float(critRateHeroes_artefato(status_artefatos(equipaArtefato, coroa, 1))) +
                            float(critRateHeroes_artefato(status_artefatos(equipaArtefato, pena, 1))) or 1.0
                            ) + '%'+ "\n" +
                            "**CRIT DMG%:** " + str(1 + float(critDMGHeroes_artefato(status_artefatos(equipaArtefato, flor, 1))) + float(critDMGHeroes_artefato(status_artefatos(equipaArtefato, calice, 1))) +
                            float(critDMGHeroes_artefato(status_artefatos(equipaArtefato, ampulheta, 1))) + float(critDMGHeroes_artefato(status_artefatos(equipaArtefato, coroa, 1))) +
                            float(critDMGHeroes_artefato(status_artefatos(equipaArtefato, pena, 1))) or 1.0
                            ) + '%' + "\n" +
                            "**Elemental Mastery:** " + str(int(emHeroes_artefato(status_artefatos(equipaArtefato, flor, 1))) + int(emHeroes_artefato(status_artefatos(equipaArtefato, calice, 1))) +
                            int(emHeroes_artefato(status_artefatos(equipaArtefato, ampulheta, 1))) + int(emHeroes_artefato(status_artefatos(equipaArtefato, coroa, 1))) +
                            int(emHeroes_artefato(status_artefatos(equipaArtefato, pena, 1)))
                            ) +
                            f'\n\n **Equipado:**' +
                            f'\n\n__**Artefatos**__\n **Flor:** {artefatos_heroes(status_artefatos(equipaArtefato, flor, 1))}' +
                            f'**Pena:** {artefatos_heroes(status_artefatos(equipaArtefato, pena, 1))}' +
                            f'**Ampulheta:** {artefatos_heroes(status_artefatos(equipaArtefato, ampulheta, 1))}' +
                            f'**Calice:** {artefatos_heroes(status_artefatos(equipaArtefato, calice, 1))}' +
                            f'**Coroa:** {artefatos_heroes(status_artefatos(equipaArtefato, coroa, 1))}' +
                            f"\n\n\n**Slot:** {str(msg)} / {str(max)}")                                
                            embed.set_image(url = url_ficha(result))
                            await ctx.send(embed = embed)
                        # Se Personagem tiver em Arma 
                        elif result in usandoHeroi:
                            numero = 0
                            for i in usandoHeroi:
                                if i == result:
                                    retornar = numero
                                numero = numero + 1
                            usandoArma = data.child(f"UsandoArma/{str(int(retornar))}").get()
                            embed = discord.Embed(
                                title = nome_ficha(result)+ " " + lv_ficha(result),
                                description = 
                                f"**Raridade:** {raridade_ficha(result)}\n" + "**Ascensão:** " + ascensao_ficha(result) + 
                                "⠀⠀⠀⠀\n" + f"**Constelação:** {constelacao_ficha(result)} \n" + "**Elemento:** " + elemento_ficha(result) + 
                                "\n**Arma:** " + arma_ficha(result),
                                color = 0x97CBFF
                            )
                            embed.set_thumbnail(url = ctx.message.author.avatar_url)
                            embed.add_field(name =
                            "__Stats__", value = "**HP:** " + str(int(vida_ficha(result).replace(',', '')) + int(hp_multiplica(result))) + "\n" + 
                            "**ATQ:** " + str(int(atq_ficha(result)) + int(atq_arma(usandoArma)) + int(atq_multiplica(result))) + "\n" + 
                            "**DEF:** " + str(int(def_ficha(result)) + int(def_multiplica(result))) + "\n" + 
                            "**CRIT Rate%:** " + '1.0%' + "\n" + 
                            "**CRIT DMG%:** " + '1.0%' + "\n" + 
                            "**Elemental Mastery:** " + '0' +
                            f'\n\n **Equipado:** {nome_arma(usandoArma)} {lv_arma(usandoArma)}' +
                            f'\n\n__**Artefatos**__\n **Flor:**' +
                            f'\n**Pena:**' +
                            f'\n**Ampulheta:**' +
                            f'\n**Calice:**' +
                            f'\n**Coroa:**' +
                            f"\n\n\n**Slot:** {str(msg)} / {str(max)}")              
                            embed.set_image(url = url_ficha(result))
                            await ctx.send(embed = embed)
                        else:
                            embed = discord.Embed(
                                title = nome_ficha(result)+ " " + lv_ficha(result),
                                description = 
                                f"**Raridade:** {raridade_ficha(result)}\n" + "**Ascensão:** " + ascensao_ficha(result) + 
                                "⠀⠀⠀⠀\n" + f"**Constelação:** {constelacao_ficha(result)} \n" + "**Elemento:** " + elemento_ficha(result) + 
                                "\n**Arma:** " + arma_ficha(result),
                                color = 0x97CBFF
                            )
                            embed.set_thumbnail(url = ctx.message.author.avatar_url)
                            embed.add_field(name =
                                "__Stats__", value = "**HP:** " + str(int(vida_ficha(result).replace(',', '')) + int(hp_multiplica(result))) + "\n" +
                                "**ATQ:** " + str(int(atq_ficha(result)) + int(atq_multiplica(result))) + "\n" + 
                                "**DEF:** " + str(int(def_ficha(result)) + int(def_multiplica(result))) + "\n" + 
                                "**CRIT Rate%:** " + '1.0%' + "\n" + 
                                "**CRIT DMG%:** " + '1.0%' + "\n" + 
                                "**Elemental Mastery:** " + '0' +
                                f'\n\n **Equipado:**' +
                                f'\n\n__**Artefatos**__\n **Flor:**' +
                                f'\n**Pena:**' +
                                f'\n**Ampulheta:**' +
                                f'\n**Calice:**' +
                                f'\n**Coroa:**' +
                                f"\n\n\n**Slot:** {str(msg)} / {str(max)}")                             
                            embed.set_image(url = url_ficha(result))
                            await ctx.send(embed = embed)
                except Exception as e:
                    traceback.print_exc()
                    if int(msg) == False:
                        await ctx.send(
                            "Erro no comando, veja em como se manda ele em `!kcomandos`."
                        )
                    else:
                        print(e)
                        await ctx.send(
                            "Você não apresenta personagem neste slot."
                        )
                        
            else:
                await ctx.send("Você ainda não iniciou a sua aventura, de `k!start` para iniciar.")
        except:
            await ctx.send("Erro no comando, veja em como se manda ele em `!kcomandos`.")

    # Stats Player
    @commands.command()
    async def status(self, ctx):
        user = ctx.message.author.id
        data = db.reference(f"/{user}")
        comeco = data.child("Começou").get()
        wins = data.child("Wins").get()
        losses = data.child("Losses").get()
        money = data.child("Money").get()
        destino = data.child("Destino").get()
        sup_destino = data.child("Super Destino").get()
        destino_hero = data.child("Destino Heroes").get()
        try:
            if "Sim" == comeco:
                embed = discord.Embed(
                        title = '__STATUS__',
                        color = 0x97CBFF
                    )
                embed.set_author(name=ctx.author.display_name, url=ctx.message.author.avatar_url, icon_url=ctx.author.avatar_url)
                embed.add_field(name= 'Records⠀⠀⠀⠀', value= f"Wins: **{str(wins)}** \n Losses: **{str(losses)}**", inline=True)
                embed.add_field(name= 'Money', value= f"${str(money)}", inline=True)
                embed.add_field(name= '⠀', value= "⠀", inline=False)
                embed.add_field(name= 'Inventário', value= "*Para usar um item use `k!use <Nome do Item>`*", inline=False)
                embed.add_field(name= 'Destino', value= str(destino), inline=True)
                embed.add_field(name= 'Super Destino', value= str(sup_destino), inline=True)
                embed.add_field(name= 'Destino Heroes', value= str(destino_hero), inline=True)
                embed.add_field(name= '⠀', value= "⠀", inline=False)
                embed.add_field(name= 'Sua Equipe', value= "*Heróis selecionados na equipe*", inline=False)
                embed.add_field(name= 'Slot 1', value= nome_ficha(data.child("Select Heroes/0").get()) + " " +lv_ficha(data.child("Select Heroes/0").get()), inline=True)
                embed.add_field(name= 'Slot 2', value= nome_ficha(data.child("Select Heroes/1").get()) + " " +lv_ficha(data.child("Select Heroes/1").get()), inline=True)
                embed.add_field(name= 'Slot 3', value= nome_ficha(data.child("Select Heroes/2").get()) + " " +lv_ficha(data.child("Select Heroes/2").get()), inline=True)
                await ctx.send(embed = embed)
        except:
            await ctx.send("Você ainda não iniciou a sua aventura, de `k!start` para iniciar.")

    # Selecionar Heroi para por na Party
    @commands.command()
    async def select(self, ctx, nome = '', slot = ''):
        user = ctx.message.author.id
        data = db.reference(f"/{user}")
        comeco = data.child("Começou").get()
        try:
            select_hero = data.child(f"Personagens/{str(int(nome) - 1)}").get()
            select_slot = data.child(f"Select Heroes").get()
            if "Sim" == comeco:
                try:
                    List = []
                    sloty = 0
                    for i in select_slot:
                        sloty = sloty + 1
                        if sloty == int(slot):
                            List.append(select_hero)
                        else: 
                            List.append(i)
                    if List[0] == List[1]:
                        await ctx.send("Este herói já está em um slot.")
                    elif List[2] == List[1]:
                        await ctx.send("Este herói já está em um slot.")
                    elif List[2] == List[0]:
                        await ctx.send("Este herói já está em um slot.")
                    else:
                        data.update({
                            "Select Heroes" : List            
                        })
                        await ctx.send(f"O seu heroi {nome_ficha(select_hero)} foi colocado no Slot {slot} da sua equipe.")
                except:
                    await ctx.send("Você não apresenta personagem neste slot.")
            else:
                await ctx.send("Você ainda não iniciou a sua aventura, de `k!start` para iniciar.")
        except:
            await ctx.send("Erro no comando, veja em como se manda ele em `!kcomandos`.")

    # Shop do jogo
    @commands.command()
    async def shop(self, ctx):
        user = ctx.message.author.id
        data = db.reference(f"/{user}")
        comeco = data.child("Começou").get()
        if "Sim" == comeco:
            money = data.child(f"Money").get()
            embed = discord.Embed(
                        title = '__Genshin SHOP__',
                        description = '*Para comprar o pacote use `k!buy <Nome>`*',
                        color = 0x97CBFF
                    )
            embed.set_author(name=ctx.author.display_name, url=ctx.message.author.avatar_url, icon_url=ctx.author.avatar_url)
            embed.add_field(name= 'Destino', value= "$1500", inline=True)
            embed.add_field(name= 'Super Destino', value= "$7500", inline=True)
            embed.add_field(name= 'Destino Heroes', value= "$10000", inline=True)
            embed.add_field(
                name= '⠀\n__Infos__', value= 
                "➤ **Destino**: *Você tem probabilidade de ganhar um herói ou item.* \n"+ 
                '➤ **Super Destino**: *Você tem maior probabilidade de ganhar um herói ou item 5⭐.* \n' + 
                 '➤ **Destino Heroes**: *Você ganha somente heróis.*', 
                 inline=False)
            embed.add_field(name= '⠀', value= f"Your Money: ${money}", inline=False)
            await ctx.send(embed = embed)
        else:
            await ctx.send("Você ainda não iniciou a sua aventura, de `k!start` para iniciar.")

    # Comando para comprar as coisas
    @commands.command()
    async def buy(self, ctx, compra = '', comprar2 = ''):
        user = ctx.message.author.id
        data = db.reference(f"/{user}")
        comeco = data.child("Começou").get()
        if "Sim" == comeco:
            money = data.child(f"Money").get()
            destino = data.child("Destino").get()
            sup_destino = data.child("Super Destino").get()
            destino_heroi = data.child("Destino Heroes").get()
            if compra == '':
                await ctx.send("Para comprar o pacote use `k!buy <Nome>`.")
            elif compra == 'Destino' and comprar2 == 'Heroes':
                result = money - 10000
                if result < 0:
                    await ctx.send("Você não tem dinheiro para comprar isso.")
                else:
                    data.update({
                            "Destino Heroes" : destino_heroi + 1,
                            "Money" : result           
                        })
                    await ctx.send("Compra feita.")
            elif compra == 'Destino':
                result = money - 1500
                if result < 0:
                    await ctx.send("Você não tem dinheiro para comprar isso.")
                else:
                    data.update({
                            "Destino" : destino + 1,
                            "Money" : result           
                        })
                    await ctx.send("Compra feita.")
            elif compra == 'Super' and comprar2 =='Destino':
                result = money - 7500
                if result < 0:
                    await ctx.send("Você não tem dinheiro para comprar isso.")
                else:
                    data.update({
                            "Super Destino" : sup_destino + 1,
                            "Money" : result           
                        })
                    await ctx.send("Compra feita.")
            else:
                await ctx.send("Nome do produto incorreto.")
        else:
            await ctx.send("Você ainda não iniciou a sua aventura, de `k!start` para iniciar.")

    # Usar um item
    @commands.command()
    async def use(self, ctx, item = '', item2 = ''):
        user = ctx.message.author.id
        data = db.reference(f"/{user}")
        comeco = data.child("Começou").get()
        if "Sim" == comeco:
            destino = data.child("Destino").get()
            sup_destino = data.child("Super Destino").get()
            destino_heroi = data.child("Destino Heroes").get()
            herois = data.child("Personagens").get()
            repetidoherois = data.child("RepetidoPersonagens").get()
            List = []
            for i in herois:
                List.append(i)
            ListRepetida = []
            for i in repetidoherois:
                if i != 'Vazio':
                    ListRepetida.append(i)
            if item == '':
                await ctx.send("Para usar um item use `k!use <Nome do Item>`.")
            elif item == "Destino" and item2 == 'Heroes':
                if destino_heroi == 0:
                    await ctx.send("Você não tem Destino Heroes para usar.")
                else:
                    nome = destino_heroes()
                    pego = nome
                    if pego in herois:
                        embed = discord.Embed(
                            title = f'__Você Ganhou a(o) {nome_ficha(pego)} {lv_ficha(pego)}__',
                            description = f"**Raridade:** {raridade_ficha(pego)}\n" + "**Ascensão:** " + ascensao_ficha(pego) + "⠀⠀⠀⠀\n" + 
                            "**Elemento:** " + elemento_ficha(pego) + "\n**Arma:** " + arma_ficha(pego),
                            color = 0x97CBFF
                        )
                        embed.set_author(name=ctx.author.display_name, url=ctx.message.author.avatar_url, icon_url=ctx.author.avatar_url)
                        embed.add_field(name ="__Stats__", value = "**HP:** " + vida_ficha(pego) + "\n" + "**ATQ:** " + atq_ficha(pego) + "\n" + "**DEF:** " + def_ficha(pego))                            
                        embed.set_image(url = url_ficha(pego))
                        ListRepetida.append(pego)
                        data.update({
                            "Destino Heroes" : destino_heroi - 1,
                            "RepetidoPersonagens" : ListRepetida,       
                        })
                        await ctx.send(embed = embed)
                    else:
                        embed = discord.Embed(
                            title = f'__Você Ganhou a(o) {nome_ficha(pego)} {lv_ficha(pego)}__',
                            description = f"**Raridade:** {raridade_ficha(pego)}\n" + "**Ascensão:** " + ascensao_ficha(pego) + "⠀⠀⠀⠀\n" + 
                            "**Elemento:** " + elemento_ficha(pego) + "\n**Arma:** " + arma_ficha(pego),
                            color = 0x97CBFF
                        )
                        embed.set_author(name=ctx.author.display_name, url=ctx.message.author.avatar_url, icon_url=ctx.author.avatar_url)
                        embed.add_field(name ="__Stats__", value = "**HP:** " + vida_ficha(pego) + "\n" + "**ATQ:** " + atq_ficha(pego) + "\n" + "**DEF:** " + def_ficha(pego))                            
                        embed.set_image(url = url_ficha(pego))
                        List.append(pego)
                        data.update({
                            "Destino Heroes" : destino_heroi - 1,
                            "Personagens" : List,       
                        })
                        await ctx.send(embed = embed)        
            elif item == "Destino":
                if destino == 0:
                    await ctx.send("Você não tem Destino para usar.")
                else:
                    await ctx.send("Ainda fazendo")
            elif item == "Super" and item2 == 'Destino':
                if sup_destino == 0:
                    await ctx.send("Você não tem Super Destino para usar.")
                else:
                    await ctx.send("Ainda fazendo")
            else:
                await ctx.send("Nome do item incorreto.")
        else:
            await ctx.send("Você ainda não iniciou a sua aventura, de `k!start` para iniciar.")

    @commands.command()
    async def add(self, ctx):
        user = ctx.message.author.id
        ref = db.reference(f"/{user}")
        result = ref.child(f"Personagens").get()
        List = []
        for i in result:
            List.append(i)
        List.append('Xiao 90 &')
        ref.update({          
                            #"Personagens" : List      
                            #"Armas" : ["lâmina maçante 1 S", "notas do aprendiz 1 C", "protetor de iniciantes 1 P", "espada larga waster 1 E", "arco de caça 1 B"]    
                        #"UsandoArma" : ["lâmina maçante 1 S"],
                        #"UsandoHeroi" : ["Aether 1 ) {"]  
                        "EquipaArtefato" : ["Vazio"],
                        "EquipaHeroi" : ["Vazio"]
                })

def setup(bot):
    bot.add_cog(Genshin(bot))