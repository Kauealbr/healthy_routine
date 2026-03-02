from database import inserir_usuarios, listar_usuarios

def test_inserir_e_listar_usuario(): 
    inserir_usuarios("Teste Pytest")
    usuarios = listar_usuarios()
    nomes = [u[1] for u in usuarios] 

    assert "Teste Pytest" in nomes