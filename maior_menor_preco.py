valor_ano_1 = float(input('Digite o valor do carro no 1º ano:'))
valor_ano_2 = float(input('Digite o valor do carro no 2º ano:'))
valor_ano_3 = float(input('Digite o valor do carro no 3º ano:'))

maior_valor = max(valor_ano_1, valor_ano_2, valor_ano_3)
menor_valor = min(valor_ano_1, valor_ano_2, valor_ano_3)

print(f' o valor mais alto é:{maior_valor}')
print(f' o valor mais baixo é:{menor_valor}')
