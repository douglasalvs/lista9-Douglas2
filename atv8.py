nomes = []


for i in range(5):
    nome = input(f"Digite o {i+1}º nome: ")
    nomes.append(nome)


contagem_a = sum(1 for nome in nomes if nome.lower().startswith('a'))


print(f"Quantidade de nomes que começam com a letra 'A': {contagem_a}")