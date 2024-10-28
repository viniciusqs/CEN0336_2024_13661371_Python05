
# Dicionário das coisas favoritas
favoritos = {
    "livro": "Assassin's Creed Renascença",
    "som": "Wicked Game Song by Chris Isaak",
    "árvore": "Ipê",
    "Organismo": "Corpo humano"
}

# Exibindo as opções de chave para o usuário
print("Escolha uma das seguintes opções para visualizar:")
for chave in favoritos.keys():
    print(f"- {chave}")

# Obtendo a escolha do usuário
fav_thing = input("Digite sua escolha: ")

# Exibindo o valor associado à chave escolhida, se existir
if fav_thing in favoritos:
    print(f"Seu item favorito em '{fav_thing}' é: {favoritos[fav_thing]}")
else:
    print("Opção inválida. Tente novamente com uma das opções listadas.")

