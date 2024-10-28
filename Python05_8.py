import json

# Nome do arquivo onde os dados serão salvos
nome_arquivo = "favoritos.json"

# Função para carregar dados do arquivo JSON
def carregar_favoritos():
    try:
        with open(nome_arquivo, "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        # Se o arquivo não existir, retorna o dicionário padrão
        return {
            "livro": "Assassin's Creed Renascença",
            "som": "Wicked Game Song by Chris Isaak",
            "árvore": "Ipê",
            "Organismo": "Cavalo"
        }

# Função para salvar dados no arquivo JSON
def salvar_favoritos(favoritos):
    with open(nome_arquivo, "w") as arquivo:
        json.dump(favoritos, arquivo, indent=4)

# Carregar favoritos do arquivo
favoritos = carregar_favoritos()

# Exibir as opções de chave para o usuário
print("Escolha uma das seguintes opções para visualizar ou atualizar:")
for chave in favoritos.keys():
    print(f"- {chave}")

# Obter a escolha do usuário
fav_thing = input("Digite sua escolha: ")

# Verificar se a escolha é válida e atualizar o valor, se necessário
if fav_thing in favoritos:
    print(f"Seu item favorito em '{fav_thing}' é: {favoritos[fav_thing]}")
    
    # Perguntar se o usuário quer alterar o valor
    novo_valor = input(f"Digite o novo valor para '{fav_thing}': ")
    
    # Atualizar o valor no dicionário
    favoritos[fav_thing] = novo_valor
    salvar_favoritos(favoritos)  # Salvar o dicionário atualizado no arquivo
    print(f"Valor atualizado! Agora, seu item favorito em '{fav_thing}' é: {favoritos[fav_thing]}")
else:
    print("Opção inválida. Tente novamente com uma das opções listadas.")

