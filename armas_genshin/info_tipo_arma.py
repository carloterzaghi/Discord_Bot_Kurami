# Tipo da arma
# S = Sword, C = Catalysts, P = Polearms, E = Claymores, B = Bows
def tipo_arma(nome):
    if "S" in nome:
        return "Sword"
    elif "C" in nome:
        return "Catalysts"
    elif "P" in nome:
        return "Polearms"
    elif "E" in nome:
        return "Claymores"
    elif "B" in nome:
        return "Bows"