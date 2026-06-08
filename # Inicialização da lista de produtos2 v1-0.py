# Inicialização da lista de produtos
produtos = []

# 1. CREATE (Adicionar)
def adicionar_produto(nome):
    produtos.append(nome)
    print(f" Produto '{nome}' adicionado com sucesso!")

# 2. READ (Listar)
def listar_produtos():
    if not produtos:
        print("\nA lista de produtos está vazia.")
        return

    print("\n--- LISTA DE PRODUTOS ---")
    for i, nome in enumerate(produtos, start=1):
        print(f"{i}. {nome}")
    print("-------------------------")

# 3. UPDATE (Atualizar)
def quantidade_produto(produto_antigo, produto_novo):
    if produto_antigo in produtos:
        indice = produtos.index(produto_antigo)
        produtos[indice] = produto_novo
        print(f" Produto '{produto_antigo}' atualizado para 'produto_novo'!")
    else:
        print(f" Erro: Produto '{produto_antigo}' não encontrado.")

# 4. DELETE (Deletar)
def deletar_produto(nome):
    if nome in produtos:
        produtos.remove(nome)
        print(f" Produto '{nome}' removido com sucesso!")
    else:
        print(f" Erro: Produto '{nome}' não encontrado.")


# --- MENU DE CONTROLE PRINCIPAL ---

while True:
    print("\n=== SISTEMA DE GERENCIAMENTO DE PRODUTOS ===")
    print("1. Adicionar Produto")
    print("2. Listar Produtos")
    print("3. Quantidade do Produto")
    print("4. Deletar Produto")
    print("5. Sair")
    print("============================================")
    
    opcao = input("Escolha uma opção (1-5): ")

    match opcao:
        case "1":
            nome = input("Digite o nome du produto a adicionar: ")
            if nome:
                adicionar_produto(nome)
            else:
                print("O nome do produto não pode ser vazio.")
                
        case "2":
            listar_produtos()
            
        case "3":
            antigo = input("Digite o nome e a quantidae  do  que deseja atualizar: ")
            novo = input("Digite a nova quantidade para do produto: ")
            if antigo and novo:
                quantidade_produto(antigo, novo)
            else:
                print("Os nomes não podem ser vazios.")
                
        case "4":
            nome = input("Digite o nome do produto a ser deletado: ")
            if nome:
                deletar_produto(nome)
            else:
                print("O nome do produto não pode ser vazio.")
                
        case "5":
            print("\nSaindo do sistema... Até logo!")
            break  # Encerra o loop while e finaliza o programa
            
        case _:
            print("\n Opção inválida! Por favor, escolha um número de 1 a 5.")