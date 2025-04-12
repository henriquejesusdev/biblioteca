def adicionar_livro(biblioteca):
    titulo = input("Digite o título do livro: ").strip()
    autor = input("Digite o nome do autor: ").strip()
    while True:
        try:
            quantidade = int(input("Digite a quantidade de exemplares: "))
            if quantidade < 0:
                print("A quantidade não pode ser negativa.")
                continue
            break
        except ValueError:
            print("Digite um número válido.")
    
    biblioteca[titulo] = {"autor": autor, "quantidade": quantidade}
    print("Livro adicionado com sucesso!")

def listar_livros(biblioteca):
    if not biblioteca:
        print("Nenhum livro cadastrado.")
        return
    
    print("\nLista de livros:")
    for titulo in sorted(biblioteca.keys()):
        info = biblioteca[titulo]
        print(f"{titulo} - {info['autor']} - {info['quantidade']} disponível(is)")

def remover_livro(biblioteca):
    titulo = input("Digite o título do livro a ser removido: ").strip()
    if titulo in biblioteca:
        del biblioteca[titulo]
        print("Livro removido com sucesso!")
    else:
        print("Livro não encontrado.")

def atualizar_quantidade(biblioteca):
    titulo = input("Digite o título do livro: ").strip()
    if titulo in biblioteca:
        while True:
            try:
                nova_quantidade = int(input("Digite a nova quantidade: "))
                if nova_quantidade < 0:
                    print("A quantidade não pode ser negativa.")
                    continue
                biblioteca[titulo]["quantidade"] = nova_quantidade
                print("Quantidade atualizada com sucesso!")
                break
            except ValueError:
                print("Digite um número válido.")
    else:
        print("Livro não encontrado.")

def registrar_emprestimo(biblioteca, historico):
    titulo = input("Digite o título do livro: ").strip()
    if titulo in biblioteca:
        while True:
            try:
                quantidade = int(input("Digite a quantidade a ser emprestada: "))
                if quantidade <= 0:
                    print("A quantidade deve ser maior que zero.")
                    continue
                if quantidade <= biblioteca[titulo]["quantidade"]:
                    biblioteca[titulo]["quantidade"] -= quantidade
                    historico.append({"titulo": titulo, "quantidade": quantidade})
                    print("Empréstimo registrado com sucesso!")
                    break
                else:
                    print("Não há exemplares suficientes disponíveis.")
                    break
            except ValueError:
                print("Digite um número válido.")
    else:
        print("Livro não encontrado.")

def exibir_historico(historico):
    if not historico:
        print("Nenhum empréstimo registrado.")
        return
    
    print("\nHistórico de empréstimos:")
    for entrada in historico:
        print(f"{entrada['titulo']} - {entrada['quantidade']} exemplar(es) emprestado(s)")

def main():
    biblioteca = {}
    historico = []
    
    while True:
        print("\n=== Sistema de Gerenciamento de Biblioteca ===")
        print("1. Adicionar livro")
        print("2. Listar livros")
        print("3. Remover livro")
        print("4. Atualizar quantidade de livros")
        print("5. Registrar empréstimo")
        print("6. Exibir histórico de empréstimos")
        print("7. Sair")
        
        opcao = input("Escolha uma opção (1-7): ").strip()
        
        if opcao == "1":
            adicionar_livro(biblioteca)
        elif opcao == "2":
            listar_livros(biblioteca)
        elif opcao == "3":
            remover_livro(biblioteca)
        elif opcao == "4":
            atualizar_quantidade(biblioteca)
        elif opcao == "5":
            registrar_emprestimo(biblioteca, historico)
        elif opcao == "6":
            exibir_historico(historico)
        elif opcao == "7":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()