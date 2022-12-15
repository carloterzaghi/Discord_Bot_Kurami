from infos_ficha_heroi.fichagenshin import nome_ficha, lv_ficha,raridade_ficha

def heroes_list(List):
    numero = 0
    retornar = ''
    for i in List:
        numero = numero + 1
        retornar = retornar + f'{str(numero)}. **{nome_ficha(i)}** • {lv_ficha(i)} • {raridade_ficha(i)} \n'
    return retornar
