from armas_genshin.info_arma_atq import atq_arma
from armas_genshin.info_arma_nome import nome_arma
from armas_genshin.info_estrelas_arma import raridade_arma
from armas_genshin.info_lv_arma import lv_arma
from armas_genshin.info_tipo_arma import tipo_arma

# Retorna uma lista de armas 
def arma_list(List):
    numero = 0
    retornar = ''
    for i in List:
        numero = numero + 1
        retornar = retornar + f'{str(numero)}. **{nome_arma(i)}** • {lv_arma(i)} • **ATQ**: {atq_arma(i)} • {raridade_arma(i)}\n'
    return retornar

# Separa as Armas Por tipo
def separacao_arma(List):
    ListS = []
    ListC = []
    ListP = []
    ListE = []
    ListB = []
    for i in List:
        if "S" in i:
            ListS.append(i)
        elif "C" in i:
            ListC.append(i)
        elif "P" in i:
            ListP.append(i)
        elif "E" in i:
            ListE.append(i)
        elif "B" in i:
            ListB.append(i)
    return (
        f"__**Sword**__\n {arma_list(ListS)} \n" + f"__**Catalyst**__\n {arma_list(ListC)} \n" + 
        f"__**Polearm**__\n {arma_list(ListP)} \n" + f"__**Claymore**__\n {arma_list(ListE)} \n" +
        f"__**Bow**__\n {arma_list(ListB)} \n"
        )

# Separa por Tipo e pega 1
def status_arma(List, Tipo, Numero):
    ListS = []
    ListC = []
    ListP = []
    ListE = []
    ListB = []
    for i in List:
        if "S" in i:
            ListS.append(i)
        elif "C" in i:
            ListC.append(i)
        elif "P" in i:
            ListP.append(i)
        elif "E" in i:
            ListE.append(i)
        elif "B" in i:
            ListB.append(i)
    if Tipo == "Sword":
        return ListS[int(Numero) - 1]
    elif Tipo == "Catalyst":
        return ListC[int(Numero) - 1]
    elif Tipo == "Polearm":
        return ListP[int(Numero) - 1]
    elif Tipo == "Claymore":
        return ListE[int(Numero) - 1]
    elif Tipo == "Bow":
        return ListB[int(Numero) - 1]