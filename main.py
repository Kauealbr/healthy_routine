from database import conectar, criar_tabelas, criar_tabela_habitos, criar_tabela_usuarios, inserir_usuarios, atualizar_habito, excluir_habito, excluir_usuario, listar_usuarios, atualizar_usuario,  buscar_habitos_usuario, inserir_habito, listar_habitos
criar_tabelas()
criar_tabela_usuarios()
criar_tabela_habitos()
from recommender import gerar_recomendacoes 
from reports import gerar_relatorio


def mostrar_menu():
    print("\n=== SISTEMA DE ROTINA SAUDÁVEL ===")
    print("1 - Cadastrar usuario")
    print("2 - Listar usuarios")
    print("3 - Registrar habitos do usuario")
    print("4 - Listar Habitos do usuario")
    print("5 - Ver recomendacoes")
    print("6 - Ver relatorio de progresso")
    print("7 - Atualizar usuario")
    print("8 - Excluir Usuario")
    print("9 - Atualizar habito")
    print("10 - Excluir habito do Usuario")
    print("11 - Sair")



def iniciar_sistema():
    conexao = conectar()
    criar_tabelas()

while True:
    mostrar_menu()

    opcao = input("Escolha uma opcao: ")
    if opcao == "1": 
        print("\n=== CADASTRO DE USUARIO ===")
        nome = input("Digite o nome do usuario: ") 
        inserir_usuarios(nome)
        print("Usuario cadastrado com sucesso")
         
    elif opcao == "2":
        print("\n=== USUARIOS CADASTRADOS ===")
        usuarios = listar_usuarios()

        if not usuarios:
            print("Nenhum usuario cadastrado.")
        else:
            for usuario in usuarios:
             print(f"ID: {usuario[0]} | Nome: {usuario[1]}")
 

    elif opcao == "3":
        print("\n=== REGISTRO DE HABITOS ===")
        usuario_id = int(input("Digite o ID do usuario: ")) 

        horas_sono = float(input("Horas de sono: "))
        if horas_sono < 0: 
            print("Horas de sono não podem ser negativas.")
            continue
        
        agua_litros = float(input("Litros de agua: ")) 
        if agua_litros < 0:
            print("Quantidade de gua não pode ser negativa") 
            continue

        exercicio = int(input("Fez exercio? (1-Sim / 0-Não): "))
        if exercicio not in [0,1]:
            print("Valor invalido para exercicio. Use 1 para Sim ou 0 para Nao.") 

        humor = input("Como esta o humor hoje? ") 
        if not humor: 
            print("Ohumor não pode estar vazio.")
            continue
        

        inserir_habito(usuario_id, horas_sono, agua_litros, exercicio, humor)
        print("Habitos registrados com sucesso!") 

    elif opcao == "4":
        usuario_id = int(input("Digite o ID do usuario: "))
        habitos = buscar_habitos_usuario(usuario_id)

        if not habitos:
            print("Nenhum habito registrado para este usuario")
        else:
            for h in habitos:
                horas_sono, agua, exercicio, humor = h
                exercicio_txt = "Sim" if exercicio == 1 else "Não"
                print(f"Sono: {horas_sono}h | Água: {agua}L | Exercício: {exercicio_txt} | Humor: {humor}")


    elif opcao == "5": 
        print("\n=== RECOMENDACOES PERSONALIZADAS ===")
        usuario_id = int(input("Digite o ID do usuario: "))
        habitos = listar_habitos(usuario_id)

        if habitos: 
            recomendacoes = gerar_recomendacoes(habitos) 
            print("\n=== RECOMENDACOES PERSONALIZADAS ===") 
            for r in recomendacoes:
                print("-", r)
        else: 
            print("Nenhum habito encitrado par gerar recomendacoes.") 

    elif opcao == "6":
        print("\n=== RELATORIO DE PROGRESSO ===")
        usuario_id = int(input("Digite o ID do usuario: "))
        habitos = listar_habitos(usuario_id)

        relatorio = gerar_relatorio(habitos) 

        if relatorio: 
            print("\n=== RELATORIO DE PROGRESSO ===")
            print(f"Media de sono: {relatorio['media_sono']:.1f} horas")
            print(f"Media de agua: {relatorio['media_agua']:.1f} litros")
            print(f"Dias com exercicios: {relatorio['dias_exercicios']}")
            print(f"Total de registros: {relatorio['total_registros']}") 
        else: 
            print("Nenhum habito registrado para gerar relatorio") 

    elif opcao == "7":
        print("\n=== ATUALIZAR USUARIO ===")
        usuario_id = int(input("Digite o ID do usuario: "))
        novo_nome = input("Digite o novo nome: ")
        atualizar_usuario(usuario_id, novo_nome) 

    
    elif opcao == "8":
        print("\n=== EXCLUIR USUARIO ===")
        usuario_id = int(input("Digite o ID do usuario: "))
        excluir_usuario(usuario_id)

    elif opcao == "9":
        print("\n=== ATUALIZAR HABITOS ===")
        usuario_id = int(input("Digite o ID do usuario: "))
        horas_sono = float(input("Horas de sono: "))
        agua_litros = float(input("Litros de agua: "))
        exercicio = int(input("Fez exercicio? (1-Sim / 0-Nao): "))
        humor = input("Como esta o humor hoje? ")

        atualizar_habito(usuario_id, horas_sono, agua_litros, exercicio, humor) 

    elif opcao == "10":
        print("\n=== EXCLUIR HABITOS ===")
        usuario_id = int(input("Digite o ID do usuario: "))
        excluir_habito(usuario_id)


    
    elif opcao == "11":
        print("Encerrando o sistema...") 
        break
    
    else:
        print("Opção invalida!")



     
   

if __name__ == "__main__":
    iniciar_sistema()