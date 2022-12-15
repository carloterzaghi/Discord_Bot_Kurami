import random
from artefatos_genshin.substats_artefatos import substats_artefatoTresEstrelas, substats_artefatoQuatroEstrelas, substats_artefatoCincoEstrelas

# Tipo do Artefato 
Tipo = 'coroa'

# Coroa de 1 - 3 estrelas
# !=1 @=2 #=3 $=4 %=5 - Estrelas
# P - HP, K - ATK, F - DEF, H - HP%, T - ATK%, D - DEF%, M - EM, C - CritRate, R - CRITDMG
def umAtresCoroa():
    ListSet = [
        'adventurer', 'luckydog', 'travelingdoctor'
        ]
    ListStar = ['!', '@', '#']
    retornarBonus = ''
    subStats = ''
    Set = random.choice(ListSet)
    Star = random.choice(ListStar)
    List = [
          'H', 'T', 'D', 'M'
        ]
    statusInicial = random.choice(List)
    if Star == '!':
        if 'H' == statusInicial:
            retornar = str(random.uniform(1.032, 1.102))
            retornarBonus = retornar[0:6]
        elif 'T' == statusInicial:
            retornar = str(random.uniform(1.032, 1.102))
            retornarBonus = retornar[0:6]
        elif 'D' == statusInicial:
            retornar = str(random.uniform(1.038, 1.09))
            retornarBonus = retornar[0:6]
        elif 'M' == statusInicial:
            retornarBonus = str(random.uniform(12, 65))
        elif 'C' == statusInicial: 
            retornar = str(random.uniform(1.015, 1.05))
            retornarBonus = retornar[0:6]
        elif 'R' == statusInicial:
            retornar = str(random.uniform(1.03, 1.17))
            retornarBonus = retornar[0:6]
    elif Star == '@':
        if 'H' == statusInicial:
            retornar = str(random.randrange(1.042, 1.132))
            retornarBonus = retornar[0:6]
        elif 'T' == statusInicial:
            retornar = str(random.uniform(1.042, 1.132))
            retornarBonus = retornar[0:6]
        elif 'D' == statusInicial:
            retornar = str(random.uniform(1.048, 1.10))
            retornarBonus = retornar[0:6]
        elif 'M' == statusInicial:
            retornarBonus = str(random.randrange(18, 75))
        elif 'C' == statusInicial: 
            retornar = str(random.uniform(1.025, 1.10))
            retornarBonus = retornar[0:6]
        elif 'R' == statusInicial:
            retornar = str(random.uniform(1.05, 1.21))
            retornarBonus = retornar[0:6]
    elif Star == "#":
        if 'H' == statusInicial:
            retornar = str(random.uniform(1.052, 1.231))
            retornarBonus = retornar[0:6]
        elif 'T' == statusInicial:
            retornar = str(random.uniform(1.052, 1.231))
            retornarBonus = retornar[0:6]
        elif 'D' == statusInicial:
            retornar = str(random.uniform(1.066, 1.29))
            retornarBonus = retornar[0:6]
        elif 'M' == statusInicial:
            retornarBonus = str(random.randrange(21, 95))
        elif 'C' == statusInicial: 
            retornar = str(random.uniform(1.035, 1.16))
            retornarBonus = retornar[0:6]
        elif 'R' == statusInicial:
            retornar = str(random.uniform(1.07, 1.31))
            retornarBonus = retornar[0:6]
        subStats = f' {substats_artefatoTresEstrelas(Tipo +" "+ Set +" LV1 "+ Star +f" {statusInicial}"+ retornarBonus)}'
    return Tipo +" "+ Set +" LV1 "+ Star +f" {statusInicial}"+ retornarBonus + subStats

# Coroa de 3 - 4 estrelas
def tresAquatroCoroa():
    ListSet = [
        'resolutionofsojourner', 'tinymiracle', 'berserker', 'instructor', 'theexile', 'defenderwill', 'braveheart', 'martialartist', 'gambler', 
        'scholar'
        ]
    ListStar = ['#', '$']
    retornarBonus = ''
    subStats = ''
    subStatsSegundo = ''
    Set = random.choice(ListSet)
    Star = random.choice(ListStar)
    List = [
          'H', 'T', 'D', 'M'
        ]
    statusInicial = random.choice(List)
    if Star == '#':
        if 'H' == statusInicial:
            retornar = str(random.uniform(1.052, 1.231))
            retornarBonus = retornar[0:6]
        elif 'T' == statusInicial:
            retornar = str(random.uniform(1.052, 1.231))
            retornarBonus = retornar[0:6]
        elif 'D' == statusInicial:
            retornar = str(random.uniform(1.066, 1.29))
            retornarBonus = retornar[0:6]
        elif 'M' == statusInicial:
            retornarBonus = str(random.randrange(21, 95))
        elif 'C' == statusInicial: 
            retornar = str(random.uniform(1.035, 1.16))
            retornarBonus = retornar[0:6]
        elif 'R' == statusInicial:
            retornar = str(random.uniform(1.07, 1.31))
            retornarBonus = retornar[0:6]
        subStats = f' {substats_artefatoTresEstrelas(Tipo +" "+ Set +" LV1 "+ Star +f" {statusInicial}"+ retornarBonus)}'
    elif Star == '$':
        if 'H' == statusInicial:
            retornar = str(random.uniform(1.063, 1.35))
            retornarBonus = retornar[0:6]
        elif 'T' == statusInicial:
            retornar = str(random.uniform(1.063, 1.35))
            retornarBonus = retornar[0:6]
        elif 'D' == statusInicial:
            retornar = str(random.uniform(1.079, 1.44))
            retornarBonus = retornar[0:6]
        elif 'M' == statusInicial:
            retornarBonus = str(random.randrange(25, 140))
        elif 'C' == statusInicial: 
            retornar = str(random.uniform(1.042, 1.24))
            retornarBonus = retornar[0:6]
        elif 'R' == statusInicial:
            retornar = str(random.uniform(1.084, 1.47))
            retornarBonus = retornar[0:6]
        subStats = f' {substats_artefatoTresEstrelas(Tipo +" "+ Set +" LV1 "+ Star +f" {statusInicial}"+ retornarBonus)}'
        subStatsSegundo = f' {substats_artefatoQuatroEstrelas(Tipo +" "+ Set +" LV1 "+ Star +f" {statusInicial}"+ retornarBonus + subStats)}'
    return Tipo +" "+ Set +" LV1 "+ Star +f" {statusInicial}"+ retornarBonus + subStats + subStatsSegundo

# Coroa de 4 - 5 estrelas
def quatroAcincoCoroa():
    ListSet = [
        "gladiatorfinale", 'wanderertroupe', 'thundersoother', 'thunderingfury', 'maidenbeloved', 'viridescentvenerer', 'crimsonwitchofflames', 'lavawalker', 'noblesseoblige', 
        'bloodstainedchivalry', 'archaicpetra', 'retracingbolide', 'blizzardstrayer', 'heartofdepth', 'tenacityofthemillelith', 'paleflame', 'emblemofseveredfate',
        'shimenawareminiscence'
        ]
    ListStar = ['$', '%']
    retornarBonus = ''
    subStats = ''
    subStatsSegundo = ''
    subStatsTerceiro = ''
    Set = random.choice(ListSet)
    Star = random.choice(ListStar)
    List = [
          'H', 'T', 'D', 'M'
        ]
    statusInicial = random.choice(List)
    if Star == '$':
        if 'H' == statusInicial:
            retornar = str(random.uniform(1.063, 1.35))
            retornarBonus = retornar[0:6]
        elif 'T' == statusInicial:
            retornar = str(random.uniform(1.063, 1.35))
            retornarBonus = retornar[0:6]
        elif 'D' == statusInicial:
            retornar = str(random.uniform(1.079, 1.44))
            retornarBonus = retornar[0:6]
        elif 'M' == statusInicial:
            retornarBonus = str(random.randrange(25, 140))
        elif 'C' == statusInicial: 
            retornar = str(random.uniform(1.042, 1.24))
            retornarBonus = retornar[0:6]
        elif 'R' == statusInicial:
            retornar = str(random.uniform(1.084, 1.47))
            retornarBonus = retornar[0:6]
        subStats = f' {substats_artefatoTresEstrelas(Tipo +" "+ Set +" LV1 "+ Star +f" {statusInicial}"+ retornarBonus)}'
        subStatsSegundo = f' {substats_artefatoQuatroEstrelas(Tipo +" "+ Set +" LV1 "+ Star +f" {statusInicial}"+ retornarBonus + subStats)}'
    elif Star == '%':
        if 'H' == statusInicial:
            retornar = str(random.uniform(1.07, 1.47))
            retornarBonus = retornar[0:6]
        elif 'T' == statusInicial:
            retornar = str(random.uniform(1.07, 1.47))
            retornarBonus = retornar[0:6]
        elif 'D' == statusInicial:
            retornar = str(random.uniform(1.087, 1.59))
            retornarBonus = retornar[0:6]
        elif 'M' == statusInicial:
            retornarBonus = str(random.randrange(28, 187))
        elif 'C' == statusInicial: 
            retornar = str(random.uniform(1.047, 1.31))
            retornarBonus = retornar[0:6]
        elif 'R' == statusInicial:
            retornar = str(random.uniform(1.093, 1.63))
            retornarBonus = retornar[0:6]
        subStats = f' {substats_artefatoTresEstrelas(Tipo +" "+ Set +" LV1 "+ Star +f" {statusInicial}"+ retornarBonus)}'
        subStatsSegundo = f' {substats_artefatoQuatroEstrelas(Tipo +" "+ Set +" LV1 "+ Star +f" {statusInicial}"+ retornarBonus + subStats)}'
        subStatsTerceiro = f' {substats_artefatoCincoEstrelas(Tipo +" "+ Set +" LV1 "+ Star +f" {statusInicial}"+ retornarBonus + subStats + subStatsSegundo)}'
    return Tipo +" "+ Set +" LV1 "+ Star +f" {statusInicial}"+ retornarBonus + subStats + subStatsSegundo + subStatsTerceiro