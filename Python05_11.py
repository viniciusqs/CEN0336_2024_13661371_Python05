# Definindo os conjuntos A e B
set_a = {3, 14, 15, 9, 26, 5, 35}
set_b = {60, 22, 14, 0, 9}

# Encontrando a interseção
interseccao = set_a.intersection(set_b)

# Encontrando a diferença (A - B)
diferenca_a_b = set_a.difference(set_b)

# Encontrando a diferença (B - A)
diferenca_b_a = set_b.difference(set_a)

# Encontrando a união
uniao = set_a.union(set_b)

# Encontrando a diferença simétrica (A Δ B)
diferenca_simetrica = set_a.symmetric_difference(set_b)

# Imprimindo os resultados
print("Conjunto A:", set_a)
print("Conjunto B:", set_b)
print("")
print("Interseção (A ∩ B):", interseccao)
print("Diferença (A - B):", diferenca_a_b)
print("Diferença (B - A):", diferenca_b_a)
print("União (A ∪ B):", uniao)
print("Diferença Simétrica (A Δ B):", diferenca_simetrica)

