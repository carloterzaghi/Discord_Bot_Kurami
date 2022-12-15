# LV Artefato
def lv_artefato(nome):
    if nome == "Vazio":
        return ""
    lv = ''
    pegar = 'nao'
    for i in nome:
        if i == "V":
            pegar = 'sim'
        elif i.isnumeric() == False:
            pegar = 'nao'
        elif pegar == 'sim':
            lv = lv + i
    return lv