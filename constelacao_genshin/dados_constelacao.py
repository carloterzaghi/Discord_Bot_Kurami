
# Dados das Constelações de cada Herói
def info_constelacao(nome):
    # Aether
    if "Aether" in nome:
        if "{" in nome:
            return ("🔒 *Vórtice Furioso*\n" + "🔒 *Turbilhão de Revolta*\n" + "🔒 *Rajada de Vento*\n" + "🔒 *Apreciando a Brisa*\n" + "🔒 *Vórtice Stellaris*\n" + "🔒 *Ventos Entrelaçados*")
        elif "}" in nome:
            return (
                "🔓 **Vórtice Furioso**\n ➤ A abilidade Vórtice de Palma da mais 10%" + " de dano." + 
                + "🔒 *Turbilhão de Revolta*\n" + "🔒 *Rajada de Vento*\n" + "🔒 *Apreciando a Brisa*\n" + "🔒 *Vórtice Stellaris*\n" + "🔒 *Ventos Entrelaçados*")
        elif "[" in nome:
            return ("🔓 **Vórtice Furioso**\n ➤ A abilidade Vórtice de Palma da mais 10%" + " de dano.\n" + 
            + "🔓 **Turbilhão de Revolta**\n " 
            + "🔒 *Rajada de Vento*\n" + "🔒 *Apreciando a Brisa*\n" + "🔒 *Vórtice Stellaris*\n" + "🔒 *Ventos Entrelaçados*" )
        elif "]" in nome:
            return ("🔓 **Vórtice Furioso**\n" + "🔓 **Turbilhão de Revolta**\n" + "🔓 **Rajada de Vento**\n" + "🔒 *Apreciando a Brisa*\n" + "🔒 *Vórtice Stellaris*\n" + "🔒 *Ventos Entrelaçados*")
        elif ";" in nome:
            return ("🔓 **Vórtice Furioso**\n" + "🔓 **Turbilhão de Revolta**\n" + "🔓 **Rajada de Vento**\n" + "🔓 **Apreciando a Brisa**\n" + "🔒 *Vórtice Stellaris*\n" + "🔒 *Ventos Entrelaçados*")
        elif "<" in nome:
            return ("🔓 **Vórtice Furioso**\n" + "🔓 **Turbilhão de Revolta**\n" + "🔓 **Rajada de Vento**\n" + "🔓 **Apreciando a Brisa**\n" + "🔓 **Vórtice Stellaris**\n" + "🔒 *Ventos Entrelaçados*")
        elif ">" in nome:
            return ("🔓 **Vórtice Furioso**\n" + "🔓 **Turbilhão de Revolta**\n" + "🔓 **Rajada de Vento**\n" + "🔓 **Apreciando a Brisa**\n" + "🔓 **Vórtice Stellaris**\n" + "🔓 **Ventos Entrelaçados**")
    # Lumine    
    elif "Lumine" in nome:
        if "{" in nome:
            return ("🔒 *Vórtice Furioso*\n" + "🔒 *Turbilhão de Revolta*\n" + "🔒 *Rajada de Vento*\n" + "🔒 *Apreciando a Brisa*\n" + "🔒 *Vórtice Stellaris*\n" + "🔒 *Ventos Entrelaçados*")
        elif "}" in nome:
            return (
                "🔓 **Vórtice Furioso**\n" + "🔒 *Turbilhão de Revolta*\n" + "🔒 *Rajada de Vento*\n" + "🔒 *Apreciando a Brisa*\n" + "🔒 *Vórtice Stellaris*\n" + "🔒 *Ventos Entrelaçados*")
        elif "[" in nome:
            return ("🔓 **Vórtice Furioso**\n" + "🔓 **Turbilhão de Revolta**\n" + "🔒 *Rajada de Vento*\n" + "🔒 *Apreciando a Brisa*\n" + "🔒 *Vórtice Stellaris*\n" + "🔒 *Ventos Entrelaçados*" )
        elif "]" in nome:
            return ("🔓 **Vórtice Furioso**\n" + "🔓 **Turbilhão de Revolta**\n" + "🔓 **Rajada de Vento**\n" + "🔒 *Apreciando a Brisa*\n" + "🔒 *Vórtice Stellaris*\n" + "🔒 *Ventos Entrelaçados*")
        elif ";" in nome:
            return ("🔓 **Vórtice Furioso**\n" + "🔓 **Turbilhão de Revolta**\n" + "🔓 **Rajada de Vento**\n" + "🔓 **Apreciando a Brisa**\n" + "🔒 *Vórtice Stellaris*\n" + "🔒 *Ventos Entrelaçados*")
        elif "<" in nome:
            return ("🔓 **Vórtice Furioso**\n" + "🔓 **Turbilhão de Revolta**\n" + "🔓 **Rajada de Vento**\n" + "🔓 **Apreciando a Brisa**\n" + "🔓 **Vórtice Stellaris**\n" + "🔒 *Ventos Entrelaçados*")
        elif ">" in nome:
            return ("🔓 **Vórtice Furioso**\n" + "🔓 **Turbilhão de Revolta**\n" + "🔓 **Rajada de Vento**\n" + "🔓 **Apreciando a Brisa**\n" + "🔓 **Vórtice Stellaris**\n" + "🔓 **Ventos Entrelaçados**")
    # Xiao
    elif "Xiao" in nome:
        if "{" in nome:
            return ("🔒 *Eon da Dissolução: Destruidor de Mundos*\n" + "🔒 *Aniquilação Eon: Flor de Caleidos*\n" + "🔒 *Conquistador do Mal: Diásidade da Ira*\n" + "🔒 *Transcensão: Extinção do Sofrimento*\n" + "🔒 *Evolution Eon: Origem da Ignorância*\n" + "🔒 *Conquistador do Mal: Guardião Yaksha*")
        elif "}" in nome:
            return ("🔓 **Eon da Dissolução: Destruidor de Mundos**\n" + "🔒 *Aniquilação Eon: Flor de Caleidos*\n" + "🔒 *Conquistador do Mal: Diásidade da Ira*\n" + "🔒 *Transcensão: Extinção do Sofrimento*\n" + "🔒 *Evolution Eon: Origem da Ignorância*\n" + "🔒 *Conquistador do Mal: Guardião Yaksha*")
        elif "[" in nome:
            return ("🔓 **Eon da Dissolução: Destruidor de Mundos**\n" + "🔓 **Aniquilação Eon: Flor de Caleidos**\n" + "🔒 *Conquistador do Mal: Diásidade da Ira*\n" + "🔒 *Transcensão: Extinção do Sofrimento*\n" + "🔒 *Evolution Eon: Origem da Ignorância*\n" + "🔒 *Conquistador do Mal: Guardião Yaksha*" )
        elif "]" in nome:
            return ("🔓 **Eon da Dissolução: Destruidor de Mundos**\n" + "🔓 **Aniquilação Eon: Flor de Caleidos**\n" + "🔓 **Conquistador do Mal: Diásidade da Ira**\n" + "🔒 *Transcensão: Extinção do Sofrimento*\n" + "🔒 *Evolution Eon: Origem da Ignorância*\n" + "🔒 *Conquistador do Mal: Guardião Yaksha*")
        elif ";" in nome:
            return ("🔓 **Eon da Dissolução: Destruidor de Mundos**\n" + "🔓 **Aniquilação Eon: Flor de Caleidos**\n" + "🔓 **Conquistador do Mal: Diásidade da Ira**\n" + "🔓 **Transcensão: Extinção do Sofrimento**\n" + "🔒 *Evolution Eon: Origem da Ignorância*\n" + "🔒 *Conquistador do Mal: Guardião Yaksha*")
        elif "<" in nome:
            return ("🔓 **Eon da Dissolução: Destruidor de Mundos**\n" + "🔓 **Aniquilação Eon: Flor de Caleidos**\n" + "🔓 **Conquistador do Mal: Diásidade da Ira**\n" + "🔓 **Transcensão: Extinção do Sofrimento**\n" + "🔓 **Evolution Eon: Origem da Ignorância**\n" + "🔒 *Conquistador do Mal: Guardião Yaksha*")
        elif ">" in nome:
            return ("🔓 **Eon da Dissolução: Destruidor de Mundos**\n" + "🔓 **Aniquilação Eon: Flor de Caleidos**\n" + "🔓 **Conquistador do Mal: Diásidade da Ira**\n" + "🔓 **Transcensão: Extinção do Sofrimento**\n" + "🔓 **Evolution Eon: Origem da Ignorância**\n" + "🔓 **Conquistador do Mal: Guardião Yaksha**")
    # Razor
    elif "Razor" in nome:
        if "{" in nome:
            return ("🔒 *Instinto de Lobo*\n" + "🔒 *Supressão*\n" + "🔒 *Companheiro da Alma*\n" + "🔒 *Morder*\n" + "🔒 *Garras afiadas*\n" + "🔒 *Lupus Fulguris*")
        elif "}" in nome:
            return (
                "🔓 **Instinto de Lobo**\n" + "🔒 *Supressão*\n" + "🔒 *Companheiro da Alma*\n" + "🔒 *Morder*\n" + "🔒 *Garras afiadas*\n" + "🔒 *Lupus Fulguris*")
        elif "[" in nome:
            return ("🔓 **Instinto de Lobo**\n" + "🔓 **Supressão**\n" + "🔒 *Companheiro da Alma*\n" + "🔒 *Morder*\n" + "🔒 *Garras afiadas*\n" + "🔒 *Lupus Fulguris*" )
        elif "]" in nome:
            return ("🔓 **Instinto de Lobo**\n" + "🔓 **Supressão**\n" + "🔓 **Companheiro da Alma**\n" + "🔒 *Morder*\n" + "🔒 *Garras afiadas*\n" + "🔒 *Lupus Fulguris*")
        elif ";" in nome:
            return ("🔓 **Instinto de Lobo**\n" + "🔓 **Supressão**\n" + "🔓 **Companheiro da Alma**\n" + "🔓 **Morder**\n" + "🔒 *Garras afiadas*\n" + "🔒 *Lupus Fulguris*")
        elif "<" in nome:
            return ("🔓 **Instinto de Lobo**\n" + "🔓 **Supressão**\n" + "🔓 **Companheiro da Alma**\n" + "🔓 **Morder**\n" + "🔓 **Garras afiadas**\n" + "🔒 *Lupus Fulguris*")
        elif ">" in nome:
            return ("🔓 **Instinto de Lobo**\n" + "🔓 **Supressão**\n" + "🔓 **Companheiro da Alma**\n" + "🔓 **Morder**\n" + "🔓 **Garras afiadas**\n" + "🔓 **Lupus Fulguris**")
    # Bennett
    elif "bennett" in nome:
        if "{" in nome:
            return ("🔒 *Grande Expectativa*\n" + "🔒 *Conquistador do Impasse*\n" + "🔒 *Fervor Imparável*\n" + "🔒 *Odisseia Inesperada*\n" + "🔒 *Verdadeiro Explorador*\n" + "🔒 *Fogo Arrisca Comigo*")
        elif "}" in nome:
            return (
                "🔓 **Grande Expectativa**\n" + "🔒 *Conquistador do Impasse*\n" + "🔒 *Fervor Imparável*\n" + "🔒 *Odisseia Inesperada*\n" + "🔒 *Verdadeiro Explorador*\n" + "🔒 *Fogo Arrisca Comigo*")
        elif "[" in nome:
            return ("🔓 **Grande Expectativa**\n" + "🔓 **Conquistador do Impasse**\n" + "🔒 *Fervor Imparável*\n" + "🔒 *Odisseia Inesperada*\n" + "🔒 *Verdadeiro Explorador*\n" + "🔒 *Fogo Arrisca Comigo*" )
        elif "]" in nome:
            return ("🔓 **Grande Expectativa**\n" + "🔓 **Conquistador do Impasse**\n" + "🔓 **Fervor Imparável**\n" + "🔒 *Odisseia Inesperada*\n" + "🔒 *Verdadeiro Explorador*\n" + "🔒 *Fogo Arrisca Comigo*")
        elif ";" in nome:
            return ("🔓 **Grande Expectativa**\n" + "🔓 **Conquistador do Impasse**\n" + "🔓 **Fervor Imparável**\n" + "🔓 **Odisseia Inesperada**\n" + "🔒 *Verdadeiro Explorador*\n" + "🔒 *Fogo Arrisca Comigo*")
        elif "<" in nome:
            return ("🔓 **Grande Expectativa**\n" + "🔓 **Conquistador do Impasse**\n" + "🔓 **Fervor Imparável**\n" + "🔓 **Odisseia Inesperada**\n" + "🔓 **Verdadeiro Explorador**\n" + "🔒 *Fogo Arrisca Comigo*")
        elif ">" in nome:
            return ("🔓 **Grande Expectativa**\n" + "🔓 **Conquistador do Impasse**\n" + "🔓 **Fervor Imparável**\n" + "🔓 **Odisseia Inesperada**\n" + "🔓 **Verdadeiro Explorador**\n" + "🔓 **Fogo Arrisca Comigo**")
    # Xiangling
    elif "Xiangling" in nome:
        if "{" in nome:
            return ("🔒 *Crocante por fora, macio por dentro*\n" + "🔒 *Óleo encontra fogo*\n" + "🔒 *Fritar*\n" + "🔒 *Ceia lenta*\n" + "🔒 *Guoba Mad*\n" + "🔒 *Pyronado condensado*")
        elif "}" in nome:
            return (
                "🔓 **Crocante por fora, macio por dentro**\n" + "🔒 *Óleo encontra fogo*\n" + "🔒 *Fritar*\n" + "🔒 *Ceia lenta*\n" + "🔒 *Guoba Mad*\n" + "🔒 *Pyronado condensado*")
        elif "[" in nome:
            return ("🔓 **Crocante por fora, macio por dentro**\n" + "🔓 **Óleo encontra fogo**\n" + "🔒 *Fritar*\n" + "🔒 *Ceia lenta*\n" + "🔒 *Guoba Mad*\n" + "🔒 *Pyronado condensado*" )
        elif "]" in nome:
            return ("🔓 **Crocante por fora, macio por dentro**\n" + "🔓 **Óleo encontra fogo**\n" + "🔓 **Fritar**\n" + "🔒 *Ceia lenta*\n" + "🔒 *Guoba Mad*\n" + "🔒 *Pyronado condensado*")
        elif ";" in nome:
            return ("🔓 **Crocante por fora, macio por dentro**\n" + "🔓 **Óleo encontra fogo**\n" + "🔓 **Fritar**\n" + "🔓 **Ceia lenta**\n" + "🔒 *Guoba Mad*\n" + "🔒 *Pyronado condensado*")
        elif "<" in nome:
            return ("🔓 **Crocante por fora, macio por dentro**\n" + "🔓 **Óleo encontra fogo**\n" + "🔓 **Fritar**\n" + "🔓 **Ceia lenta**\n" + "🔓 **Guoba Mad**\n" + "🔒 *Pyronado condensado*")
        elif ">" in nome:
            return ("🔓 **Crocante por fora, macio por dentro**\n" + "🔓 **Óleo encontra fogo**\n" + "🔓 **Fritar**\n" + "🔓 **Ceia lenta**\n" + "🔓 **Guoba Mad**\n" + "🔓 **Pyronado condensado**")
    # Hu Tao
    elif "Hu Tao" in nome:
        if "{" in nome:
            return ("🔒 *Buquê vermelho*\n" + "🔒 *Chuvas sinistras*\n" + "🔒 *Carmine persistente*\n" + "🔒 *Jardim do Descanso Eterno*\n" + "🔒 *Incenso Floral*\n" + "🔒 *Abraço da Borboleta*")
        elif "}" in nome:
            return (
                "🔓 **Buquê vermelho**\n" + "🔒 *Chuvas sinistras*\n" + "🔒 *Carmine persistente*\n" + "🔒 *Jardim do Descanso Eterno*\n" + "🔒 *Incenso Floral*\n" + "🔒 *Abraço da Borboleta*")
        elif "[" in nome:
            return ("🔓 **Buquê vermelho**\n" + "🔓 **Chuvas sinistras**\n" + "🔒 *Carmine persistente*\n" + "🔒 *Jardim do Descanso Eterno*\n" + "🔒 *Incenso Floral*\n" + "🔒 *Abraço da Borboleta*" )
        elif "]" in nome:
            return ("🔓 **Buquê vermelho**\n" + "🔓 **Chuvas sinistras**\n" + "🔓 **Carmine persistente**\n" + "🔒 *Jardim do Descanso Eterno*\n" + "🔒 *Incenso Floral*\n" + "🔒 *Abraço da Borboleta*")
        elif ";" in nome:
            return ("🔓 **Buquê vermelho**\n" + "🔓 **Chuvas sinistras**\n" + "🔓 **Carmine persistente**\n" + "🔓 **Jardim do Descanso Eterno**\n" + "🔒 *Incenso Floral*\n" + "🔒 *Abraço da Borboleta*")
        elif "<" in nome:
            return ("🔓 **Buquê vermelho**\n" + "🔓 **Chuvas sinistras**\n" + "🔓 **Carmine persistente**\n" + "🔓 **Jardim do Descanso Eterno**\n" + "🔓 **Incenso Floral**\n" + "🔒 *Abraço da Borboleta*")
        elif ">" in nome:
            return ("🔓 **Buquê vermelho**\n" + "🔓 **Chuvas sinistras**\n" + "🔓 **Carmine persistente**\n" + "🔓 **Jardim do Descanso Eterno**\n" + "🔓 **Incenso Floral**\n" + "🔓 **Abraço da Borboleta**")
    # Fischl
    elif "Fischl" in nome:
        if "{" in nome:
            return ("🔒 *Olhar das Profundezas*\n" + "🔒 *Devorador de Todos os Pecados*\n" + "🔒 *Asas do Pesadelo*\n" + "🔒 *Sua Peregrinação de Sombrio*\n" + "🔒 *Contra a Luz Em Fuga*\n" + "🔒 *Corvo Evernight*")
        elif "}" in nome:
            return (
                "🔓 **Olhar das Profundezas**\n" + "🔒 *Devorador de Todos os Pecados*\n" + "🔒 *Asas do Pesadelo*\n" + "🔒 *Sua Peregrinação de Sombrio*\n" + "🔒 *Contra a Luz Em Fuga*\n" + "🔒 *Corvo Evernight*")
        elif "[" in nome:
            return ("🔓 **Olhar das Profundezas**\n" + "🔓 **Devorador de Todos os Pecados**\n" + "🔒 *Asas do Pesadelo*\n" + "🔒 *Sua Peregrinação de Sombrio*\n" + "🔒 *Contra a Luz Em Fuga*\n" + "🔒 *Corvo Evernight*" )
        elif "]" in nome:
            return ("🔓 **Olhar das Profundezas**\n" + "🔓 **Devorador de Todos os Pecados**\n" + "🔓 **Asas do Pesadelo**\n" + "🔒 *Sua Peregrinação de Sombrio*\n" + "🔒 *Contra a Luz Em Fuga*\n" + "🔒 *Corvo Evernight*")
        elif ";" in nome:
            return ("🔓 **Olhar das Profundezas**\n" + "🔓 **Devorador de Todos os Pecados**\n" + "🔓 **Asas do Pesadelo**\n" + "🔓 **Sua Peregrinação de Sombrio**\n" + "🔒 *Contra a Luz Em Fuga*\n" + "🔒 *Corvo Evernight*")
        elif "<" in nome:
            return ("🔓 **Olhar das Profundezas**\n" + "🔓 **Devorador de Todos os Pecados**\n" + "🔓 **Asas do Pesadelo**\n" + "🔓 **Sua Peregrinação de Sombrio**\n" + "🔓 **Contra a Luz Em Fuga**\n" + "🔒 *Corvo Evernight*")
        elif ">" in nome:
            return ("🔓 **Olhar das Profundezas**\n" + "🔓 **Devorador de Todos os Pecados**\n" + "🔓 **Asas do Pesadelo**\n" + "🔓 **Sua Peregrinação de Sombrio**\n" + "🔓 **Contra a Luz Em Fuga**\n" + "🔓 **Corvo Evernight**")
    # Diluc
    elif "Diluc" in nome:
        if "{" in nome:
            return ("🔒 *Convicção*\n" + "🔒 *Brasa escaldante*\n" + "🔒 *Fogo e Aço*\n" + "🔒 *Chama fluindo*\n" + "🔒 *Phoenix*\n" + "🔒 *Espada Flamejante, Nêmesis da Escuridão*")
        elif "}" in nome:
            return (
                "🔓 **Convicção**\n" + "🔒 *Brasa escaldante*\n" + "🔒 *Fogo e Aço*\n" + "🔒 *Chama fluindo*\n" + "🔒 *Phoenix*\n" + "🔒 *Espada Flamejante, Nêmesis da Escuridão*")
        elif "[" in nome:
            return ("🔓 **Convicção**\n" + "🔓 **Brasa escaldante**\n" + "🔒 *Fogo e Aço*\n" + "🔒 *Chama fluindo*\n" + "🔒 *Phoenix*\n" + "🔒 *Espada Flamejante, Nêmesis da Escuridão*" )
        elif "]" in nome:
            return ("🔓 **Convicção**\n" + "🔓 **Brasa escaldante**\n" + "🔓 **Fogo e Aço**\n" + "🔒 *Chama fluindo*\n" + "🔒 *Phoenix*\n" + "🔒 *Espada Flamejante, Nêmesis da Escuridão*")
        elif ";" in nome:
            return ("🔓 **Convicção**\n" + "🔓 **Brasa escaldante**\n" + "🔓 **Fogo e Aço**\n" + "🔓 **Chama fluindo**\n" + "🔒 *Phoenix*\n" + "🔒 *Espada Flamejante, Nêmesis da Escuridão*")
        elif "<" in nome:
            return ("🔓 **Convicção**\n" + "🔓 **Brasa escaldante**\n" + "🔓 **Fogo e Aço**\n" + "🔓 **Chama fluindo**\n" + "🔓 **Phoenix**\n" + "🔒 *Espada Flamejante, Nêmesis da Escuridão*")
        elif ">" in nome:
            return ("🔓 **Convicção**\n" + "🔓 **Brasa escaldante**\n" + "🔓 **Fogo e Aço**\n" + "🔓 **Chama fluindo**\n" + "🔓 **Phoenix**\n" + "🔓 **Espada Flamejante, Nêmesis da Escuridão**")
    # Kaeya
    elif "Kaeya" in nome:
        if "{" in nome:
            return ("🔒 *Sangue Excelente*\n" + "🔒 *Desempenho interminável*\n" + "🔒 *Dança de Geada*\n" + "🔒 *Beijo Congelado*\n" + "🔒 *Abraço de frostbiting*\n" + "🔒 *Redemoinho Glacial*")
        elif "}" in nome:
            return (
                "🔓 **Sangue Excelente**\n" + "🔒 *Desempenho interminável*\n" + "🔒 *Dança de Geada*\n" + "🔒 *Beijo Congelado*\n" + "🔒 *Abraço de frostbiting*\n" + "🔒 *Redemoinho Glacial*")
        elif "[" in nome:
            return ("🔓 **Sangue Excelente**\n" + "🔓 **Desempenho interminável**\n" + "🔒 *Dança de Geada*\n" + "🔒 *Beijo Congelado*\n" + "🔒 *Abraço de frostbiting*\n" + "🔒 *Redemoinho Glacial*" )
        elif "]" in nome:
            return ("🔓 **Sangue Excelente**\n" + "🔓 **Desempenho interminável**\n" + "🔓 **Dança de Geada**\n" + "🔒 *Beijo Congelado*\n" + "🔒 *Abraço de frostbiting*\n" + "🔒 *Redemoinho Glacial*")
        elif ";" in nome:
            return ("🔓 **Sangue Excelente**\n" + "🔓 **Desempenho interminável**\n" + "🔓 **Dança de Geada**\n" + "🔓 **Beijo Congelado**\n" + "🔒 *Abraço de frostbiting*\n" + "🔒 *Redemoinho Glacial*")
        elif "<" in nome:
            return ("🔓 **Sangue Excelente**\n" + "🔓 **Desempenho interminável**\n" + "🔓 **Dança de Geada**\n" + "🔓 **Beijo Congelado**\n" + "🔓 **Abraço de frostbiting**\n" + "🔒 *Redemoinho Glacial*")
        elif ">" in nome:
            return ("🔓 **Sangue Excelente**\n" + "🔓 **Desempenho interminável**\n" + "🔓 **Dança de Geada**\n" + "🔓 **Beijo Congelado**\n" + "🔓 **Abraço de frostbiting**\n" + "🔓 **Redemoinho Glacial**")
    # Amber
    elif "Amber" in nome:
        if "{" in nome:
            return ("🔒 *Uma seta para governar todos eles*\n" + "🔒 *Coelho acionado*\n" + "🔒 *Queima!*\n" + "🔒 *Não é uma boneca qualquer...*\n" + "🔒 *É o Barão Bunny!*\n" + "🔒 *Incêndios*")
        elif "}" in nome:
            return (
                "🔓 **Uma seta para governar todos eles**\n" + "🔒 *Coelho acionado*\n" + "🔒 *Queima!*\n" + "🔒 *Não é uma boneca qualquer...*\n" + "🔒 *É o Barão Bunny!*\n" + "🔒 *Incêndios*")
        elif "[" in nome:
            return ("🔓 **Uma seta para governar todos eles**\n" + "🔓 **Coelho acionado**\n" + "🔒 *Queima!*\n" + "🔒 *Não é uma boneca qualquer...*\n" + "🔒 *É o Barão Bunny!*\n" + "🔒 *Incêndios*" )
        elif "]" in nome:
            return ("🔓 **Uma seta para governar todos eles**\n" + "🔓 **Coelho acionado**\n" + "🔓 **Queima!**\n" + "🔒 *Não é uma boneca qualquer...*\n" + "🔒 *É o Barão Bunny!*\n" + "🔒 *Incêndios*")
        elif ";" in nome:
            return ("🔓 **Uma seta para governar todos eles**\n" + "🔓 **Coelho acionado**\n" + "🔓 **Queima!**\n" + "🔓 **Não é uma boneca qualquer...**\n" + "🔒 *É o Barão Bunny!*\n" + "🔒 *Incêndios*")
        elif "<" in nome:
            return ("🔓 **Uma seta para governar todos eles**\n" + "🔓 **Coelho acionado**\n" + "🔓 **Queima!**\n" + "🔓 **Não é uma boneca qualquer...**\n" + "🔓 **É o Barão Bunny!**\n" + "🔒 *Incêndios*")
        elif ">" in nome:
            return ("🔓 **Uma seta para governar todos eles**\n" + "🔓 **Coelho acionado**\n" + "🔓 **Queima!**\n" + "🔓 **Não é uma boneca qualquer...**\n" + "🔓 **É o Barão Bunny!**\n" + "🔓 **Incêndios**")
    # Noelle
    elif "Noelle" in nome:
        if "{" in nome:
            return ("🔒 *Eu tenho você de volta*\n" + "🔒 *Empregada de combate*\n" + "🔒 *Empregada invulnerável*\n" + "🔒 *Para ser limpo*\n" + "🔒 *Mestre Favonius Sweeper*\n" + "🔒 *Deve ser impecável*")
        elif "}" in nome:
            return (
                "🔓 **Eu tenho você de volta**\n" + "🔒 *Empregada de combate*\n" + "🔒 *Empregada invulnerável*\n" + "🔒 *Para ser limpo*\n" + "🔒 *Mestre Favonius Sweeper*\n" + "🔒 *Deve ser impecável*")
        elif "[" in nome:
            return ("🔓 **Eu tenho você de volta**\n" + "🔓 **Empregada de combate**\n" + "🔒 *Empregada invulnerável*\n" + "🔒 *Para ser limpo*\n" + "🔒 *Mestre Favonius Sweeper*\n" + "🔒 *Deve ser impecável*" )
        elif "]" in nome:
            return ("🔓 **Eu tenho você de volta**\n" + "🔓 **Empregada de combate**\n" + "🔓 **Empregada invulnerável**\n" + "🔒 *Para ser limpo*\n" + "🔒 *Mestre Favonius Sweeper*\n" + "🔒 *Deve ser impecável*")
        elif ";" in nome:
            return ("🔓 **Eu tenho você de volta**\n" + "🔓 **Empregada de combate**\n" + "🔓 **Empregada invulnerável**\n" + "🔓 **Para ser limpo**\n" + "🔒 *Mestre Favonius Sweeper*\n" + "🔒 *Deve ser impecável*")
        elif "<" in nome:
            return ("🔓 **Eu tenho você de volta**\n" + "🔓 **Empregada de combate**\n" + "🔓 **Empregada invulnerável**\n" + "🔓 **Para ser limpo**\n" + "🔓 **Mestre Favonius Sweeper**\n" + "🔒 *Deve ser impecável*")
        elif ">" in nome:
            return ("🔓 **Eu tenho você de volta**\n" + "🔓 **Empregada de combate**\n" + "🔓 **Empregada invulnerável**\n" + "🔓 **Para ser limpo**\n" + "🔓 **Mestre Favonius Sweeper**\n" + "🔓 **Deve ser impecável**")
    # Lisa
    elif "Lisa" in nome:
        if "{" in nome:
            return ("🔒 *Circuito Infinito*\n" + "🔒 *Campo Eletromagnético*\n" + "🔒 *Trovão Ressonante*\n" + "🔒 *Erupção plasmática*\n" + "🔒 *Eletrocutar*\n" + "🔒 *Bruxa pulsante*")
        elif "}" in nome:
            return (
                "🔓 **Circuito Infinito**\n" + "🔒 *Campo Eletromagnético*\n" + "🔒 *Trovão Ressonante*\n" + "🔒 *Erupção plasmática*\n" + "🔒 *Eletrocutar*\n" + "🔒 *Bruxa pulsante*")
        elif "[" in nome:
            return ("🔓 **Circuito Infinito**\n" + "🔓 **Campo Eletromagnético**\n" + "🔒 *Trovão Ressonante*\n" + "🔒 *Erupção plasmática*\n" + "🔒 *Eletrocutar*\n" + "🔒 *Bruxa pulsante*" )
        elif "]" in nome:
            return ("🔓 **Circuito Infinito**\n" + "🔓 **Campo Eletromagnético**\n" + "🔓 **Trovão Ressonante**\n" + "🔒 *Erupção plasmática*\n" + "🔒 *Eletrocutar*\n" + "🔒 *Bruxa pulsante*")
        elif ";" in nome:
            return ("🔓 **Circuito Infinito**\n" + "🔓 **Campo Eletromagnético**\n" + "🔓 **Trovão Ressonante**\n" + "🔓 **Erupção plasmática**\n" + "🔒 *Eletrocutar*\n" + "🔒 *Bruxa pulsante*")
        elif "<" in nome:
            return ("🔓 **Circuito Infinito**\n" + "🔓 **Campo Eletromagnético**\n" + "🔓 **Trovão Ressonante**\n" + "🔓 **Erupção plasmática**\n" + "🔓 **Eletrocutar**\n" + "🔒 *Bruxa pulsante*")
        elif ">" in nome:
            return ("🔓 **Circuito Infinito**\n" + "🔓 **Campo Eletromagnético**\n" + "🔓 **Trovão Ressonante**\n" + "🔓 **Erupção plasmática**\n" + "🔓 **Eletrocutar**\n" + "🔓 **Bruxa pulsante**")
    # Barbara
    elif "barbara" in nome:
        if "{" in nome:
            return ("🔒 *Canções Alegres*\n" + "🔒 *Explosão de vitalidade*\n" + "🔒 *Estrela do Amanhã*\n" + "🔒 *Atenção seja Meu Poder*\n" + "🔒 *O Mais Puro Companheirismo*\n" + "🔒 *Dedicando tudo a você*")
        elif "}" in nome:
            return (
                "🔓 **Canções Alegres**\n" + "🔒 *Explosão de vitalidade*\n" + "🔒 *Estrela do Amanhã*\n" + "🔒 *Atenção seja Meu Poder*\n" + "🔒 *O Mais Puro Companheirismo*\n" + "🔒 *Dedicando tudo a você*")
        elif "[" in nome:
            return ("🔓 **Canções Alegres**\n" + "🔓 **Explosão de vitalidade**\n" + "🔒 *Estrela do Amanhã*\n" + "🔒 *Atenção seja Meu Poder*\n" + "🔒 *O Mais Puro Companheirismo*\n" + "🔒 *Dedicando tudo a você*" )
        elif "]" in nome:
            return ("🔓 **Canções Alegres**\n" + "🔓 **Explosão de vitalidade**\n" + "🔓 **Estrela do Amanhã**\n" + "🔒 *Atenção seja Meu Poder*\n" + "🔒 *O Mais Puro Companheirismo*\n" + "🔒 *Dedicando tudo a você*")
        elif ";" in nome:
            return ("🔓 **Canções Alegres**\n" + "🔓 **Explosão de vitalidade**\n" + "🔓 **Estrela do Amanhã**\n" + "🔓 **Atenção seja Meu Poder**\n" + "🔒 *O Mais Puro Companheirismo*\n" + "🔒 *Dedicando tudo a você*")
        elif "<" in nome:
            return ("🔓 **Canções Alegres**\n" + "🔓 **Explosão de vitalidade**\n" + "🔓 **Estrela do Amanhã**\n" + "🔓 **Atenção seja Meu Poder**\n" + "🔓 **O Mais Puro Companheirismo**\n" + "🔒 *Dedicando tudo a você*")
        elif ">" in nome:
            return ("🔓 **Canções Alegres**\n" + "🔓 **Explosão de vitalidade**\n" + "🔓 **Estrela do Amanhã**\n" + "🔓 **Atenção seja Meu Poder**\n" + "🔓 **O Mais Puro Companheirismo**\n" + "🔓 **Dedicando tudo a você**")
