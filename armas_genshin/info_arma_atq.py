
# Dano da Arma
def atq_arma(nome):
    if "lâmina maçante" in nome:
        return "23"
    elif "notas do aprendiz" in nome:
        return "23"
    elif "protetor de iniciantes" in nome:
        return "23"
    elif "espada larga waster" in nome:
        return "23"
    elif "arco de caça" in nome:
        return "23"

# Ver o LV
def lv(nome):
    result = ''
    Lista = []
    for i in nome:
        if i in "0123456789":
            Lista.append(i)
    for i in Lista:        
        result = result + i
    return result