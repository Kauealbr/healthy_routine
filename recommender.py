def gerar_recomendacoes(habitos): 
    recomendacoes = []

    for h in habitos: 
        horas_sono = h[0]
        agua = h[1]
        exercicio = h[2] 
        humor = h[3]

        if horas_sono < 6: 
            recomendacoes.append("Dormir mais cedo para melhorar o descanso.")

        if agua <2: 
            recomendacoes.append("Beber mais agua para manter  hidratação.")
        
        if exercicio == 0: 
            recomendacoes.append("Tente realizar pelo menos uma caminhada hoje")
        
        if humor.lower() in ["triste", "estressado", "cansado"]: 
            recomendacoes.append("Reserve um tempo para relaxar ou meditar") 

    return recomendacoes