import getpass
from sistema import Sistema


def main():
    sistema = Sistema()
    token = None

    while True:
        try:
            print("\n=== MENU ===")
            print("1 - Registrar novo usuário")
            print("2 - Login")
            print("3 - Criar categoria")
            print("4 - Cadastrar produto")
            print("5 - Listar meus produtos")
            print("6 - Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                nome = input("Nome: ")
                email = input("Email: ")
                senha = getpass.getpass("Senha (oculta): ")
                sistema.registrar_usuario(nome, email, senha)

            elif opcao == '2':
                email = input("Email: ")
                senha = getpass.getpass("Senha (oculta): ")
                token = sistema.login(email, senha)

            elif opcao == '3':
                if not token:
                    print("Você precisa estar logado.")
                else:
                    nome = input("Nome da categoria: ")
                    sistema.criar_categoria(nome)

            elif opcao == '4':
                if not token:
                    print("Você precisa estar logado.")
                else:
                    nome = input("Nome do produto: ")
                    descricao = input("Descrição: ")
                    try:
                        preco = float(input("Preço: "))
                    except ValueError:
                        print("Preço inválido! Use um número.")
                        continue
                    categoria = input("Categoria: ")
                    sistema.cadastrar_produto(token, nome, descricao, preco, categoria)

            elif opcao == '5':
                if not token:
                    print("Você precisa estar logado.")
                else:
                    sistema.listar_produtos_do_usuario(token)

            elif opcao == '6':
                print("Saindo...")
                break

            else:
                print("Opção inválida!")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")


if __name__ == "__main__":
    main()