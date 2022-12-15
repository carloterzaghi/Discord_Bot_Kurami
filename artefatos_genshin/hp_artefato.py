# HP Artefato
def hp_artefato(nome):
    if nome == "Vazio":
        return ""
    elif nome == "Flor":
        return "0"
    hp = ''
    pegar = 'nao'
    for i in nome:
        if i == "P":
            pegar = 'sim'
        elif i.isnumeric() == False:
            pegar = 'nao'
        elif pegar == 'sim':
            hp = hp + i
    if hp == '':
        hp = '0'
    return hp

# HP% Artefato
def hpPorcento_artefato(nome):
    if nome == "Vazio":
        return ""
    hp = ''
    pegar = 'nao'
    for i in nome:
        if i == "H":
            pegar = 'sim'
        elif i == '.' and pegar == 'sim':
            pegar = 'sim'
        elif i.isnumeric() == False:
            pegar = 'nao'
        elif pegar == 'sim':
            hp = hp + i
    retornar = str((int(hp[0:5])- 10000)/100)+'%'
    return retornar

# HP% Artefato para o k!heroes
def hpPorcentoHeroes_artefato(nome):
    if nome == "Vazio":
        return ""
    hp = ''
    pegar = 'nao'
    for i in nome:
        if i == "H":
            pegar = 'sim'
        elif i == '.' and pegar == 'sim':
            hp = hp + i
        elif i.isnumeric() == False:
            pegar = 'nao'
        elif pegar == 'sim':
            hp = hp + i
    if hp == '':
        hp = '0'
    return hp