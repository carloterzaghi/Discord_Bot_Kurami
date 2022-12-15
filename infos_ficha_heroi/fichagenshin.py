
# Nome do Personagem
def nome_ficha(nome):
    if "Aether" in nome:
        return "Aether"
    elif "Vazio" in nome:
        return "Vazio"
    elif "Lumine" in nome:
        return "Lumine"
    elif "Xiao" in nome:
        return "Xiao"
    elif "Razor" in nome:
        return "Razor"
    elif "bennett" in nome:
        return "Bennett"
    elif "Xiangling" in nome:
        return "Xiangling"
    elif "Hu Tao" in nome:
        return "Hu Tao"
    elif "Fischl" in nome:
        return "Fischl"
    elif "Diluc" in nome:
        return "Diluc"
    elif "Kaeya" in nome:
        return "Kaeya"
    elif "Amber" in nome:
        return "Amber"
    elif "Noelle" in nome:
        return "Noelle"
    elif "Lisa" in nome:
        return "Lisa"
    elif "barbara" in nome:
        return "Barbara"

# Nivel
def lv_ficha(nome):
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

# Raridade
def raridade_ficha(nome):
    if "Aether" in nome:
        return "⭐⭐⭐⭐⭐"
    elif "Lumine" in nome:
        return "⭐⭐⭐⭐⭐"
    elif "Xiao" in nome:
        return "⭐⭐⭐⭐⭐"
    elif "Razor" in nome:
        return "⭐⭐⭐⭐"
    elif "bennett" in nome:
        return "⭐⭐⭐⭐"
    elif "Xiangling" in nome:
        return "⭐⭐⭐⭐"
    elif "Hu Tao" in nome:
        return "⭐⭐⭐⭐⭐"
    elif "Fischl" in nome:
        return "⭐⭐⭐⭐"
    elif "Diluc" in nome:
        return "⭐⭐⭐⭐⭐"
    elif "Kaeya" in nome:
        return "⭐⭐⭐⭐"
    elif "Amber" in nome:
        return "⭐⭐⭐⭐"
    elif "Noelle" in nome:
        return "⭐⭐⭐⭐"
    elif "Lisa" in nome:
        return "⭐⭐⭐⭐"
    elif "barbara" in nome:
        return "⭐⭐⭐⭐"

# Ascensão da Personagem 
# )=0 !=1 @=2 #=3 $=4 %=5 &=6 
def ascensao_ficha(nome):
    if ")" in nome:
        return "0"
    elif "!" in nome:
        return "1"
    elif "@" in nome:
        return "2"
    elif "#" in nome:
        return "3"
    elif "$" in nome:
        return "4"
    elif "%" in nome:
        return "5"
    elif "&" in nome:
        return "6"

# Constelação da Personagem 
# {=0 }=1 [=2 ]=3 ;=4 <=5 >=6 
def constelacao_ficha(nome):
    if "{" in nome:
        return "Lv. 0"
    elif "}" in nome:
        return "Lv. 1"
    elif "[" in nome:
        return "Lv. 2"
    elif "]" in nome:
        return "Lv. 3"
    elif ";" in nome:
        return "Lv. 4"
    elif "<" in nome:
        return "Lv. 5"
    elif ">" in nome:
        return "Lv. 6"

# Elemento da Personagem
def elemento_ficha(nome):
    if "Aether" in nome:
        return "Anemo"
    elif "Lumine" in nome:
        return "Anemo"
    elif "Xiao" in nome:
        return "Anemo"
    elif "Razor" in nome:
        return "Electro"
    elif "bennett" in nome:
        return "Pyro"
    elif "Xiangling" in nome:
        return "Pyro"
    elif "Hu Tao" in nome:
        return "Pyro"
    elif "Fischl" in nome:
        return "Electro"
    elif "Diluc" in nome:
        return "Pyro"
    elif "Kaeya" in nome:
        return "Cryo"
    elif "Amber" in nome:
        return "Pyro"
    elif "Noelle" in nome:
        return "Geo"
    elif "Lisa" in nome:
        return "Electro"
    elif "barbara" in nome:
        return "Hydro"

# Tipo de arma
def arma_ficha(nome):
    if "Aether" in nome:
        return "Sword"
    elif "Lumine" in nome:
        return "Sword"
    elif "Xiao" in nome:
        return "Polearm"
    elif "Razor" in nome:
        return "Claymore"
    elif "bennett" in nome:
        return "Sword"
    elif "Xiangling" in nome:
        return "Polearm"
    elif "Hu Tao" in nome:
        return "Polearm"
    elif "Fischl" in nome:
        return "Bow"
    elif "Diluc" in nome:
        return "Claymore"
    elif "Kaeya" in nome:
        return "Sword"
    elif "Amber" in nome:
        return "Bow"
    elif "Noelle" in nome:
        return "Claymore"
    elif "Lisa" in nome:
        return "Electro"
    elif "barbara" in nome:
        return "Catalyst"

# Imagem URL
def url_ficha(nome):
    if "Aether" in nome:
        return "https://static.wikia.nocookie.net/gensin-impact/images/1/1c/Traveler_Male_Card.jpg/revision/latest?cb=20201024043323"
    elif "Lumine" in nome:
        return "https://static.wikia.nocookie.net/genshin-impact/images/0/02/Personagem_Viajante_Feminino_Cart%C3%A3o.jpg/revision/latest?cb=20210320120732&path-prefix=pt-br"
    elif "Xiao" in nome:
        return "https://static.wikia.nocookie.net/genshin-impact/images/0/0f/Personagem_Xiao_Cart%C3%A3o.jpg/revision/latest?cb=20210228053135&path-prefix=pt-br"
    elif "Razor" in nome:
        return "https://static.wikia.nocookie.net/genshin-impact/images/f/f3/Personagem_Razor_Cart%C3%A3o.jpg/revision/latest?cb=20210404003515&path-prefix=pt-br"
    elif "bennett" in nome:
        return "https://static.wikia.nocookie.net/genshin-impact/images/d/d7/Personagem_Bennett_Cart%C3%A3o.jpg/revision/latest?cb=20210319185532&path-prefix=pt-br"
    elif "Xiangling" in nome:
        return "https://static.wikia.nocookie.net/genshin-impact/images/4/44/Personagem_Xiangling_Cart%C3%A3o.jpg/revision/latest?cb=20210404172551&path-prefix=pt-br"
    elif "Hu Tao" in nome:
        return "https://static.wikia.nocookie.net/genshin-impact/images/d/d0/Personagem_Hutao_Card.jpg/revision/latest?cb=20210302180450&path-prefix=pt-br"
    elif "Fischl" in nome:
        return "https://static.wikia.nocookie.net/genshin-impact/images/4/48/Character_Fischl_Card.jpg/revision/latest?cb=20210109151504&path-prefix=pt-br"
    elif "Diluc" in nome:
        return "https://static.wikia.nocookie.net/genshin-impact/images/b/b1/Personagem_Diluc_Cart%C3%A3o.jpg/revision/latest?cb=20210319195352&path-prefix=pt-br"
    elif "Kaeya" in nome:
        return "https://static.wikia.nocookie.net/genshin-impact/images/6/65/Personagem_Kaeya_Cart%C3%A3o.jpg/revision/latest?cb=20210319204634&path-prefix=pt-br"
    elif "Amber" in nome:
        return "https://static.wikia.nocookie.net/genshin-impact/images/7/73/Personagem_Amber_Cart%C3%A3o.jpg/revision/latest?cb=20210319175153&path-prefix=pt-br"
    elif "Noelle" in nome:
        return "https://static.wikia.nocookie.net/gensin-impact/images/9/92/Character_Noelle_Card.jpg/revision/latest?cb=20200403111008"
    elif "Lisa" in nome:
        return "https://static.wikia.nocookie.net/genshin-impact/images/2/23/Personagem_Lisa_Cart%C3%A3o.jpg/revision/latest?cb=20210319212036&path-prefix=pt-br"
    elif "barbara" in nome:
        return "https://static.wikia.nocookie.net/genshin-impact/images/7/75/Personagem_Barbara_Cart%C3%A3o.jpg/revision/latest?cb=20210319184846&path-prefix=pt-br"

