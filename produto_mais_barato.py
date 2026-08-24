produto_1 = float(input("Digite o valor do produto 1: R$ "))
produto_2 = float(input("Digite o valor do produdo 2: R$ "))
produto_3 = float(input("Digite o valor do produto 3: R$ "))

menor_valor = min(produto_1, produto_2, produto_3)

print(f' O produto mais barato é: R$ {menor_valor}')
