from artefatos_genshin.hp_artefato import hp_artefato, hpPorcento_artefato
from artefatos_genshin.atq_artefato import atq_artefato, atqPorcento_artefato, em_artefato, critDMG_artefato, critRate_artefato
from artefatos_genshin.def_artefato import defe_artefato, defePorcento_artefato


# Status dos Artefatos
def stats_artefatos(nome):
    status = ''
    if 'P' in nome:
        status = f'**HP**: {hp_artefato(nome)}'
    if 'K' in nome:
        status = status + f'\n**ATK**: {atq_artefato(nome)}'
    if 'F' in nome:
        status = status + f'\n**DEF**: {defe_artefato(nome)}'
    if 'H' in nome: 
        status = status + f'\n**HP%**: {hpPorcento_artefato(nome)}'
    if 'T' in nome:
        status = status + f'\n**ATK%**: {atqPorcento_artefato(nome)}'
    if 'D' in nome:
        status = status + f'\n**DEF%**: {defePorcento_artefato(nome)}'
    if 'M' in nome:
        status = status + f'\n**EM**: {em_artefato(nome)}'
    if 'C' in nome:
        status = status + f'\n**CRIT Rate%**: {critRate_artefato(nome)}'
    if 'R' in nome:
        status = status + f'\n**CRIT DMG%**: {critDMG_artefato(nome)}'
    return status