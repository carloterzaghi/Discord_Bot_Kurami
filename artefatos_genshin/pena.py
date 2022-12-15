import random
from artefatos_genshin.substats_artefatos import substats_artefatoTresEstrelas, substats_artefatoQuatroEstrelas, substats_artefatoCincoEstrelas

# Tipo do Artefato
Tipo = 'pena'

# Pena de 1 - 3 estrelas
# !=1 @=2 #=3 $=4 %=5 - Estrelas
# P - HP, K - ATK, F - DEF, H - HP%, T - ATK%, D - DEF%, M - EM, C - CritRate, R - CRITDMG
def umAtresPena():
    ListSet = [
        'initiate', 'adventurer', 'luckydog', 'travelingdoctor'
        ]
    ListStar = ['!', '@', '#']
    retornarBonus = ''
    subStats = ''
    Set = random.choice(ListSet)
    Star = random.choice(ListStar)
    if Star == '!':
        retornarBonus = str(random.randrange(14, 96))
    elif Star == '@':
        retornarBonus = str(random.randrange(20, 101))
    elif Star == "#":
        retornarBonus = str(random.randrange(28, 124))
        subStats = f' {substats_artefatoTresEstrelas(Tipo +" "+ Set +" LV1 "+ Star +" K"+ retornarBonus)}'
    return Tipo +" "+ Set +" LV1 "+ Star +" K"+ retornarBonus + subStats

# Pena de 3 - 4 estrelas
def tresAquatroPena():
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
    if Star == '#':
        retornarBonus = str(random.randrange(28, 124))
        subStats = f' {substats_artefatoTresEstrelas(Tipo +" "+ Set +" LV1 "+ Star +" K"+ retornarBonus)}'
    elif Star == '$':
        retornarBonus = str(random.randrange(42, 233))
        subStats = f' {substats_artefatoTresEstrelas(Tipo +" "+ Set +" LV1 "+ Star +" K"+ retornarBonus)}'
        subStatsSegundo = f' {substats_artefatoQuatroEstrelas(Tipo +" "+ Set +" LV1 "+ Star +" K"+ retornarBonus + subStats)}'
    return Tipo +" "+ Set +" LV1 "+ Star +" K"+ retornarBonus + subStats + subStatsSegundo

# Pena de 4 - 5 estrelas
def quatroAcincoPena():
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
        retornarBonus = str(random.randrange(42, 233))
        subStats = f' {substats_artefatoTresEstrelas(Tipo +" "+ Set +" LV1 "+ Star +" K"+ retornarBonus)}'
        subStatsSegundo = f' {substats_artefatoQuatroEstrelas(Tipo +" "+ Set +" LV1 "+ Star +" K"+ retornarBonus + subStats)}'
    elif Star == '%':
        retornarBonus = str(random.randrange(47, 312))
        subStats = f' {substats_artefatoTresEstrelas(Tipo +" "+ Set +" LV1 "+ Star +" K"+ retornarBonus)}'
        subStatsSegundo = f' {substats_artefatoQuatroEstrelas(Tipo +" "+ Set +" LV1 "+ Star +" K"+ retornarBonus + subStats)}'
        subStatsTerceiro = f' {substats_artefatoCincoEstrelas(Tipo +" "+ Set +" LV1 "+ Star +" K"+ retornarBonus + subStats + subStatsSegundo)}'
    return Tipo +" "+ Set +" LV1 "+ Star +" K"+ retornarBonus + subStats + subStatsSegundo + subStatsTerceiro
