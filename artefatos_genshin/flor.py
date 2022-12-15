import random
from artefatos_genshin.substats_artefatos import substats_artefatoTresEstrelas, substats_artefatoQuatroEstrelas, substats_artefatoCincoEstrelas

# Tipo do Artefato
Tipo = 'flor'

# Flor de 1 - 3 estrelas
# !=1 @=2 #=3 $=4 %=5 - Estrelas
# P - HP, K - ATK, F - DEF, H - HP%, T - ATK%, D - DEF%, M - EM, C - CritRate, R - CRITDMG
def umAtresFlor():
    ListSet = [
        'initiate', 'adventurer', 'luckydog', 'travelingdoctor'
        ]
    ListStar = ['!', '@', '#']
    retornarBonus = ''
    subStats = ''
    Set = random.choice(ListSet)
    Star = random.choice(ListStar)
    if Star == '!':
        retornarBonus = str(random.randrange(54, 131))
    elif Star == '@':
        retornarBonus = str(random.randrange(240, 351))
    elif Star == "#":
        retornarBonus = str(random.randrange(430, 1894))
        subStats = f' {substats_artefatoTresEstrelas(Tipo +" "+ Set +" LV1 "+ Star +" P"+ retornarBonus)}'
    return Tipo +" "+ Set +" LV1 "+ Star +" P"+ retornarBonus + subStats

# Flor de 3 - 4 estrelas
def tresAquatroFlor():
    ListSet = [
        'resolutionofsojourner', 'tinymiracle', 'berserker', 'instructor', 'theexile', 'defenderwill', 'braveheart', 'martialartist', 'gambler', 
        'scholar', 'prayersforillumination', 'prayersfordestiny', 'prayersforwisdom', 'prayerstospringtime'
        ]
    ListStar = ['#', '$']
    retornarBonus = ''
    subStats = ''
    subStatsSegundo = ''
    Set = random.choice(ListSet)
    Star = random.choice(ListStar)
    if Star == '#':
        retornarBonus = str(random.randrange(430, 1894))
        subStats = f' {substats_artefatoTresEstrelas(Tipo +" "+ Set +" LV1 "+ Star +" P"+ retornarBonus)}'
    elif Star == '$':
        retornarBonus = str(random.randrange(645, 3571))
        subStats = f' {substats_artefatoTresEstrelas(Tipo +" "+ Set +" LV1 "+ Star +" P"+ retornarBonus)}'
        subStatsSegundo = f' {substats_artefatoQuatroEstrelas(Tipo +" "+ Set +" LV1 "+ Star +" P"+ retornarBonus + subStats)}'
    return Tipo +" "+ Set +" LV1 "+ Star +" P"+ retornarBonus + subStats + subStatsSegundo

# Flor de 4 - 5 estrelas
def quatroAcincoFlor():
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
    if Star == '$':
        retornarBonus = str(random.randrange(645, 3571))
        subStats = f' {substats_artefatoTresEstrelas(Tipo +" "+ Set +" LV1 "+ Star +" P"+ retornarBonus)}'
        subStatsSegundo = f' {substats_artefatoQuatroEstrelas(Tipo +" "+ Set +" LV1 "+ Star +" P"+ retornarBonus + subStats)}'
    elif Star == '%':
        retornarBonus = str(random.randrange(717, 4781))
        subStats = f' {substats_artefatoTresEstrelas(Tipo +" "+ Set +" LV1 "+ Star +" P"+ retornarBonus)}'
        subStatsSegundo = f' {substats_artefatoQuatroEstrelas(Tipo +" "+ Set +" LV1 "+ Star +" P"+ retornarBonus + subStats)}'
        subStatsTerceiro = f' {substats_artefatoCincoEstrelas(Tipo +" "+ Set +" LV1 "+ Star +" P"+ retornarBonus + subStats + subStatsSegundo)}'
    return Tipo +" "+ Set +" LV1 "+ Star +" P"+ retornarBonus + subStats + subStatsSegundo + subStatsTerceiro
