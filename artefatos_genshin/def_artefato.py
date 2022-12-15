# DEF Artefato
def defe_artefato(nome):
    if nome == "Vazio":
        return ""
    defe = ''
    pegar = 'nao'
    for i in nome:
        if i == "F":
            pegar = 'sim'
        elif i.isnumeric() == False:
            pegar = 'nao'
        elif pegar == 'sim':
            defe = defe + i
    if defe == '':
        defe = '0'
    return defe

# DEF% Artefato
def defePorcento_artefato(nome):
    if nome == "Vazio":
        return ""
    defe = ''
    pegar = 'nao'
    for i in nome:
        if i == "D":
            pegar = 'sim'
        elif i == '.' and pegar == 'sim':
            pegar = 'sim'
        elif i.isnumeric() == False:
            pegar = 'nao'
        elif pegar == 'sim':
            defe = defe + i
    retornar = str((int(defe[0:5])- 10000)/100)+'%'
    return retornar

# DEF% Artefato para o k!heroes
def defePorcentoHeroes_artefato(nome):
    if nome == "Vazio":
        return ""
    defe = ''
    pegar = 'nao'
    for i in nome:
        if i == "D":
            pegar = 'sim'
        elif i == '.' and pegar == 'sim':
            defe = defe + i
        elif i.isnumeric() == False:
            pegar = 'nao'
        elif pegar == 'sim':
            defe = defe + i
    if defe == '':
        defe = '0'
    return defe