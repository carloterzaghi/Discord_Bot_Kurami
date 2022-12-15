# ATQ Artefato
def atq_artefato(nome):
    if nome == "Vazio":
        return ""
    atq = ''
    pegar = 'nao'
    for i in nome:
        if i == "K":
            pegar = 'sim'
        elif i.isnumeric() == False:
            pegar = 'nao'
        elif pegar == 'sim':
            atq = atq + i
    if atq == '':
        atq = '0'
    return atq

# ATQ% Artefato
def atqPorcento_artefato(nome):
    if nome == "Vazio":
        return ""
    atq = ''
    pegar = 'nao'
    for i in nome:
        if i == "T":
            pegar = 'sim'
        elif i == '.' and pegar == 'sim':
            pegar = 'sim'
        elif i.isnumeric() == False:
            pegar = 'nao'
        elif pegar == 'sim':
            atq = atq + i
    retornar = str((int(atq[0:5])- 10000)/100)+'%'
    return retornar

# ATQ% Artefato para o k!heroes
def atqPorcentoHeroes_artefato(nome):
    if nome == "Vazio":
        return ""
    atq = ''
    pegar = 'nao'
    for i in nome:
        if i == "T":
            pegar = 'sim'
        elif i == '.' and pegar == 'sim':
            atq = atq + i
        elif i.isnumeric() == False:
            pegar = 'nao'
        elif pegar == 'sim':
            atq = atq + i
    if atq == '':
        atq = '0'
    return atq

# Elemental Mastery Artefato
def em_artefato(nome):
    if nome == "Vazio":
        return ""
    atq = ''
    pegar = 'nao'
    for i in nome:
        if i == "M":
            pegar = 'sim'
        elif i.isnumeric() == False:
            pegar = 'nao'
        elif pegar == 'sim':
            atq = atq + i
    return atq

# Elemental Mastery Artefato para k!heroes
def emHeroes_artefato(nome):
    if nome == "Vazio":
        return ""
    atq = ''
    pegar = 'nao'
    for i in nome:
        if i == "M":
            pegar = 'sim'
        elif i.isnumeric() == False:
            pegar = 'nao'
        elif pegar == 'sim':
            atq = atq + i
    if atq == '':
        atq = '0'
    return atq

# CRIT Rate% Artefato
def critRate_artefato(nome):
    if nome == "Vazio":
        return ""
    atq = ''
    pegar = 'nao'
    for i in nome:
        if i == "C":
            pegar = 'sim'
        elif i == '.' and pegar == 'sim':
            pegar = 'sim'
        elif i.isnumeric() == False:
            pegar = 'nao'
        elif pegar == 'sim':
            atq = atq + i
    retornar = str((int(atq[0:5])- 10000)/100)+'%'
    return retornar

# CRIT Rate% Artefato para o k!heroes
def critRateHeroes_artefato(nome):
    if nome == "Vazio":
        return ""
    atq = ''
    pegar = 'nao'
    for i in nome:
        if i == "C":
            pegar = 'sim'
        elif i == '.' and pegar == 'sim':
            pegar = 'sim'
        elif i.isnumeric() == False:
            pegar = 'nao'
        elif pegar == 'sim':
            atq = atq + i
    if atq == '':
        retornar = '0'
    else:
        retornar = str((int(atq[0:5])- 10000)/100)
    return retornar

# CRIT DMG%	 Artefato
def critDMG_artefato(nome):
    if nome == "Vazio":
        return ""
    atq = ''
    pegar = 'nao'
    for i in nome:
        if i == "R":
            pegar = 'sim'
        elif i == '.' and pegar == 'sim':
            pegar = 'sim'
        elif i.isnumeric() == False:
            pegar = 'nao'
        elif pegar == 'sim':
            atq = atq + i
    retornar = str((int(atq[0:5])- 10000)/100)+'%'
    return retornar

# CRIT DMG%	 Artefato para k!heroes
def critDMGHeroes_artefato(nome):
    if nome == "Vazio":
        return ""
    atq = ''
    pegar = 'nao'
    for i in nome:
        if i == "R":
            pegar = 'sim'
        elif i == '.' and pegar == 'sim':
            pegar = 'sim'
        elif i.isnumeric() == False:
            pegar = 'nao'
        elif pegar == 'sim':
            atq = atq + i
    if atq == '':
        retornar = '0'
    else:
        retornar = str((int(atq[0:5])- 10000)/100)
    return retornar