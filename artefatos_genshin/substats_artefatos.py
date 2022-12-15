import random

# Substats Artefatos
# P - HP, K - ATK, F - DEF, H - HP%, T - ATK%, D - DEF%, M - EM, C - CritRate, R - CRITDMG
# 3 estrelas 
def substats_artefatoTresEstrelas(nome):
    List = [
        'P', 'K', 'F', 'H', 'T', 'D', 'M', 'C', 'R'
        ]
    if 'P' in nome:
        List.remove('P')
    elif 'K' in nome:
        List.remove('K')
    elif 'F' in nome:
        List.remove('F')
    elif 'H' in nome:
        List.remove('H')
    elif 'T' in nome:
        List.remove('T')
    elif 'D' in nome:
        List.remove('D')
    elif 'M' in nome:
        List.remove('M')
    elif 'C' in nome:
        List.remove('C')
    elif 'R' in nome:
        List.remove('R')
    substatus = random.choice(List)
    if substatus == 'P':
        return 'P' +str(random.randrange(101, 144))
    elif substatus == 'K':
        return 'K'+str(random.randrange(7, 10))
    elif substatus == 'F':
        return 'F'+str(random.randrange(8, 12))
    elif substatus == 'H':
        numero = str(random.uniform(1.0245, 1.035))
        return 'H'+ numero[0:6]
    elif substatus == 'T':
        numero = str(random.uniform(1.0245, 1.035))
        return 'T'+ numero[0:6]
    elif substatus == 'D':
        numero = str(random.uniform(1.0306, 1.044))
        return 'D'+ numero[0:6]
    elif substatus == 'M':
        return 'M'+str(random.randrange(10, 14))
    elif substatus == 'C':
        numero = str(random.uniform(1.0163, 1.0233))
        return 'C'+ numero[0:6]
    elif substatus == 'R':
        numero = str(random.uniform(1.0306, 1.0466))
        return 'R'+numero[0:6]

# P - HP, K - ATK, F - DEF, H - HP%, T - ATK%, D - DEF%, M - EM, C - CritRate, R - CRITDMG
# 4 estrelas 
def substats_artefatoQuatroEstrelas(nome):
    List = [
        'P', 'K', 'F', 'H', 'T', 'D', 'M', 'C', 'R'
        ]
    if 'P' in nome:
        List.remove('P')
    elif 'K' in nome:
        List.remove('K')
    elif 'F' in nome:
        List.remove('F')
    elif 'H' in nome:
        List.remove('H')
    elif 'T' in nome:
        List.remove('T')
    elif 'D' in nome:
        List.remove('D')
    elif 'M' in nome:
        List.remove('M')
    elif 'C' in nome:
        List.remove('C')
    elif 'R' in nome:
        List.remove('R')
    substatus = random.choice(List)
    if substatus == 'P':
        return 'P' +str(random.randrange(168, 240))
    elif substatus == 'K':
        return 'K'+str(random.randrange(11, 16))
    elif substatus == 'F':
        return 'F'+str(random.randrange(13, 19))
    elif substatus == 'H':
        numero = str(random.uniform(1.0326, 1.0466))
        return 'H'+ numero[0:6]
    elif substatus == 'T':
        numero = str(random.uniform(1.0326, 1.0466))
        return 'T'+numero[0:6]
    elif substatus == 'D':
        numero = str(random.uniform(1.0408, 1.0583))
        return 'D'+numero[0:6]
    elif substatus == 'M':
        return 'M'+str(random.randrange(13, 19))
    elif substatus == 'C':
        numero = str(random.uniform(1.0218, 1.0311))
        return 'C'+numero[0:6]
    elif substatus == 'R':
        numero = str(random.uniform(1.0435, 1.0622))
        return 'R'+numero[0:6]

# P - HP, K - ATK, F - DEF, H - HP%, T - ATK%, D - DEF%, M - EM, C - CritRate, R - CRITDMG
# 5 estrelas 
def substats_artefatoCincoEstrelas(nome):   
    List = [
        'P', 'K', 'F', 'H', 'T', 'D', 'M', 'C', 'R'
        ]
    if 'P' in nome:
        List.remove('P')
    elif 'K' in nome:
        List.remove('K')
    elif 'F' in nome:
        List.remove('F')
    elif 'H' in nome:
        List.remove('H')
    elif 'T' in nome:
        List.remove('T')
    elif 'D' in nome:
        List.remove('D')
    elif 'M' in nome:
        List.remove('M')
    elif 'C' in nome:
        List.remove('C')
    elif 'R' in nome:
        List.remove('R')
    substatus = random.choice(List)# P - HP, K - ATK, F - DEF, H - HP%, T - ATK%, D - DEF%, M - EM, C - CritRate, R - CRITDMG
    if substatus == 'P':
        return 'P' +str(random.randrange(210, 301))
    elif substatus == 'K':
        return 'K'+str(random.randrange(14, 21))
    elif substatus == 'F':
        return 'F'+str(random.randrange(16, 24))
    elif substatus == 'H':
        numero = str(random.uniform(1.0408, 1.0583))
        return 'H'+numero[0:6]
    elif substatus == 'T':
        numero = str(random.uniform(1.0408, 1.0583))
        return 'T'+numero[0:6]
    elif substatus == 'D':
        numero = str(random.uniform(1.051, 1.0729))
        return 'D'+numero[0:6]
    elif substatus == 'M':
        return 'M'+str(random.randrange(16, 24))
    elif substatus == 'C':
        numero = str(random.uniform(1.0272, 1.0389))
        return 'C'+numero[0:6]
    elif substatus == 'R':
        numero = str(random.uniform(1.0544, 1.0777))
        return 'R'+numero[0:6]