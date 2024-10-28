mySet = set('ATGTGGG')
mySet2 = {'ATGCCT'}

print(mySet)   # Saída: {'A', 'T', 'G'}
print(mySet2)  # Saída: {'ATGCCT'}

# Pergunta se a pessoa quer ver a explicação
resposta = input("Você gostaria de ver a explicação sobre as diferenças na criação de conjuntos? (sim/não): ")

if resposta.lower() == 'sim':
    print("")
    print("Sim, importa como você cria o conjunto, pois isso determina os elementos que ele conterá. A escolha da sintaxe deve ser feita de acordo com o que você deseja armazenar no conjunto. Se você quer um conjunto de caracteres únicos, deve usar set(). Se você deseja criar um conjunto com uma ou mais strings, você pode usar as chaves {}.")

