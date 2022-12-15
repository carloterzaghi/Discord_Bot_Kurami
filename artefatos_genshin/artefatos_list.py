from discord.enums import Status
from artefatos_genshin.nome_artefato import nome_artefato
from artefatos_genshin.lv_artefato import lv_artefato
from artefatos_genshin.estrelas_artefato import estrelas_artefato
from artefatos_genshin.hp_artefato import hp_artefato, hpPorcento_artefato
from artefatos_genshin.atq_artefato import atq_artefato, atqPorcento_artefato, em_artefato, critDMG_artefato, critRate_artefato
from artefatos_genshin.def_artefato import defe_artefato, defePorcento_artefato
from artefatos_genshin.set_artefatos import set_artefato

# List Base Artefatos
# P - HP, K - ATK, F - DEF, H - HP%, T - ATK%, D - DEF%, M - EM, C - CritRate, R - CRITDMG
def artefatos_list(List):
    numero = 0
    retornar = ''
    status = ''
    for i in List:
        numero = numero + 1
        if 'P' in i:
            status = f' • **HP**: {hp_artefato(i)}'
        if 'K' in i:
            status = status + f' • **ATK**: {atq_artefato(i)}'
        if 'F' in i:
            status = status + f' • **DEF**: {defe_artefato(i)}'
        if 'H' in i: 
            status = status + f' • **HP%**: {hpPorcento_artefato(i)}'
        if 'T' in i:
            status = status + f' • **ATK%**: {atqPorcento_artefato(i)}'
        if 'D' in i:
            status = status + f' • **DEF%**: {defePorcento_artefato(i)}'
        if 'M' in i:
            status = status + f' • **EM**: {em_artefato(i)}'
        if 'C' in i:
            status = status + f' • **CRIT Rate%**: {critRate_artefato(i)}'
        if 'R' in i:
            status = status + f' • **CRIT DMG%**: {critDMG_artefato(i)}'
        retornar = retornar + f'{str(numero)}. **{set_artefato(i)}** • Lv. {lv_artefato(i)} {status} • {estrelas_artefato(i)}\n'
    return retornar

# Artefatos para o k!heroe
def artefatos_heroes(nome):
    retornar = ''   
    status = ''
    if nome == 'Flor' or nome == 'Pena' or nome == 'Ampulheta' or nome == 'Calice' or nome == 'Coroa':
        retornar = ' \n'
    else:
        if 'P' in nome:
                status = f' • **HP**: {hp_artefato(nome)}'
        if 'K' in nome:
                status = status + f' • **ATK**: {atq_artefato(nome)}'
        if 'F' in nome:
                status = status + f' • **DEF**: {defe_artefato(nome)}'
        if 'H' in nome: 
                status = status + f' • **HP%**: {hpPorcento_artefato(nome)}'
        if 'T' in nome:
                status = status + f' • **ATK%**: {atqPorcento_artefato(nome)}'
        if 'D' in nome:
                status = status + f' • **DEF%**: {defePorcento_artefato(nome)}'
        if 'M' in nome:
                status = status + f' • **EM**: {em_artefato(nome)}'
        if 'C' in nome:
                status = status + f' • **CRIT Rate%**: {critRate_artefato(nome)}'
        if 'R' in nome:
            status = status + f' • **CRIT DMG%**: {critDMG_artefato(nome)}'
        retornar = retornar + f'**{set_artefato(nome)}** • Lv. {lv_artefato(nome)} {status} • {estrelas_artefato(nome)}\n'
    return retornar

# Separação List Artefatos
def separacao_artefatos(List):
    ListFlor = []
    ListCalice = []
    ListAmpulheta = []
    ListCoroa = []
    ListPena = []
    for i in List:
        if "flor" in i:
            ListFlor.append(i)
        elif "calice" in i:
            ListCalice.append(i)
        elif "ampulheta" in i:
            ListAmpulheta.append(i)
        elif "coroa" in i:
            ListCoroa.append(i)
        elif "pena" in i:
            ListPena.append(i)
    return (
        f"__**Flor**__\n {artefatos_list(ListFlor)} \n" + f"__**Cálice**__\n {artefatos_list(ListCalice)} \n" + 
        f"__**Ampulheta**__\n {artefatos_list(ListAmpulheta)} \n" + f"__**Coroa**__\n {artefatos_list(ListCoroa)} \n" +
        f"__**Pena**__\n {artefatos_list(ListPena)} \n"
        )

# Separa por Tipo e pega 1
def status_artefatos(List, Tipo, Numero):
    ListFlor = []
    ListCalice = []
    ListAmpulheta = []
    ListCoroa = []
    ListPena = []
    for i in List:
        if "flor" in i or "Flor" in i:
            ListFlor.append(i)
        elif "calice" in i or "Calice" in i:
            ListCalice.append(i)
        elif "ampulheta" in i or "Ampulheta" in i:
            ListAmpulheta.append(i)
        elif "coroa" in i or "Coroa" in i:
            ListCoroa.append(i)
        elif "pena" in i or "Pena" in i:
            ListPena.append(i)
    if Tipo == "Flor":
        return ListFlor[int(Numero) - 1]
    elif Tipo == "Calice":
        return ListCalice[int(Numero) - 1]
    elif Tipo == "Ampulheta":
        return ListAmpulheta[int(Numero) - 1]
    elif Tipo == "Coroa":
        return ListCoroa[int(Numero) - 1]
    elif Tipo == "Pena":
        return ListPena[int(Numero) - 1]