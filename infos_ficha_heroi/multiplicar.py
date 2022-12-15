from infos_ficha_heroi.fichagenshin import nome_ficha, lv_ficha

# Multiplicador ATQ
def atq_multiplica(nome):
    lv = ''
    for i in lv_ficha(nome):
        if i.isnumeric(): 
            lv = lv + i
    if "Aether" in nome:
        return str(2 * int(lv))
    elif "Lumine" in nome:
        return str(2 * int(lv))
    elif "Xiao" in nome:
        return str(4 * int(lv))
    elif "Razor" in nome:
        return str(3 * int(lv))
    elif "bennett" in nome:
        return str(2 * int(lv))
    elif "Xiangling" in nome:
        return str(3 * int(lv))
    elif "Hu Tao" in nome:
        return str(1 * int(lv))
    elif "Fischl" in nome:
        return str(3 * int(lv))
    elif "Diluc" in nome:
        return str(3 * int(lv))
    elif "Kaeya" in nome:
        return str(2 * int(lv))
    elif "Amber" in nome:
        return str(2 * int(lv))
    elif "Noelle" in nome:
        return str(2 * int(lv))
    elif "Lisa" in nome:
        return str(2 * int(lv))
    elif "barbara" in nome:
        return str(2 * int(lv))

# Multiplicar DEF
def def_multiplica(nome):
    lv = ''
    for i in lv_ficha(nome):
        if i.isnumeric(): 
            lv = lv + i
    if "Aether" in nome:
        return str(7 * int(lv))
    elif "Lumine" in nome:
        return str(7 * int(lv))
    elif "Xiao" in nome:
        return str(8 * int(lv))
    elif "Razor" in nome:
        return str(8 * int(lv))
    elif "bennett" in nome:
        return str(8 * int(lv))
    elif "Xiangling" in nome:
        return str(7 * int(lv))
    elif "Hu Tao" in nome:
        return str(9 * int(lv))
    elif "Fischl" in nome:
        return str(6 * int(lv))
    elif "Diluc" in nome:
        return str(8 * int(lv))
    elif "Kaeya" in nome:
        return str(8 * int(lv))
    elif "Amber" in nome:
        return str(6 * int(lv))
    elif "Noelle" in nome:
        return str(8 * int(lv))
    elif "Lisa" in nome:
        return str(6 * int(lv))
    elif "barbara" in nome:
        return str(7 * int(lv))

# Multiplicador HP
def hp_multiplica(nome):
    lv = ''
    for i in lv_ficha(nome):
        if i.isnumeric(): 
            lv = lv + i
    if "Aether" in nome:
        return str(111 * int(lv))
    elif "Lumine" in nome:
        return str(111 * int(lv))
    elif "Xiao" in nome:
        return str(131 * int(lv))
    elif "Razor" in nome:
        return str(122 * int(lv))
    elif "bennett" in nome:
        return str(126 * int(lv))
    elif "Xiangling" in nome:
        return str(111 * int(lv))
    elif "Hu Tao" in nome:
        return str(160 * int(lv))
    elif "Fischl" in nome:
        return str(94 * int(lv))
    elif "Diluc" in nome:
        return str(133 * int(lv))
    elif "Kaeya" in nome:
        return str(119 * int(lv))
    elif "Amber" in nome:
        return str(96 * int(lv))
    elif "Noelle" in nome:
        return str(122 * int(lv))
    elif "Lisa" in nome:
        return str(97 * int(lv))
    elif "barbara" in nome:
        return str(100 * int(lv))