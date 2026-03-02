from recommender import gerar_recomendacoes

def test_recomendacao_sono(): 
    habitos = [(5, 2, 1, "feliz")]
    recomendacoes = gerar_recomendacoes(habitos)

    assert any("Dormir mais cedo" in r for r in recomendacoes)

def test_recomendacao_agua(): 
    habitos = [(8, 1, 1, "feliz")]
    recomendacoes = gerar_recomendacoes(habitos)

    assert any("Beber mais agua" in r for r in recomendacoes)


def test_recomendacao_exercicio(): 
    habitos = [(8, 2, 0, "feliz")]
    recomendacoes = gerar_recomendacoes(habitos)

    assert any("caminhada" in r.lower() for r in recomendacoes)