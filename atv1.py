preco = float(input('Digite o preço do produto:  '))
desconto = float(input('Digite a porcentagem do desconto: '))

valor_desconto = (desconto / 100) * preco
preco_final = preco - valor_desconto

print(f'O valor do desconto é: {valor_desconto:2}')
print(f'O preco final do produto é: {preco_final:2} ')
