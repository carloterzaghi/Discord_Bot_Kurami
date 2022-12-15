# Estrelas do Artefato
# !=1 @=2 #=3 $=4 %=5 - Estrelas
def estrelas_artefato(nome):
    if "!" in nome:
        return '⭐'
    elif "@" in nome:
        return '⭐⭐'
    elif "#" in nome:
        return '⭐⭐⭐'
    elif "$" in nome:
        return '⭐⭐⭐⭐'
    elif "%" in nome:
        return '⭐⭐⭐⭐⭐'