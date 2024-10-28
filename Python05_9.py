favoritos = {
    "livro": "Assassin's Creed Renascença",
    "som": "Wicked Game Song by Chris Isaak",
    "árvore": "Ipê"
}

# Exibindo somente o livro favorito
fav_thing = 'livro'
print("Meu livro favorito:")
print(favoritos[fav_thing])

# Usando um loop for para exibir cada chave e valor do dicionário
print("\nTodas as coisas favoritas:")
for chave, valor in favoritos.items():
    print(f"{chave.capitalize()}: {valor}")

