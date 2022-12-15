# Nivel da Arma
def lv_arma(nome):
    if nome == "Vazio":
        return ""
    result = ''
    Lista = []
    for i in nome:
        if i in "0123456789":
            Lista.append(i)
    for i in Lista:        
        result = result + i
    return "Lv. " + result