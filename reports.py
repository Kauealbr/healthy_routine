def gerar_relatorio(habitos):
    if not habitos:
        return None

    total_sono = 0
    total_agua = 0
    dias_exercicio = 0

    for h in habitos:
        sono, agua, exercicio, humor = h
        total_sono += sono
        total_agua += agua  # CORRETO
        if exercicio == 1:
            dias_exercicio += 1

    media_sono = total_sono / len(habitos)
    media_agua = total_agua / len(habitos)

    return {
        "media_sono": media_sono,
        "media_agua": media_agua,
        "dias_exercicios": dias_exercicio,
        "total_registros": len(habitos)
    }
