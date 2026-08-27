litros = float(input('Digite a quantidade de litros: '))
tipo = input('Digite o tipo de combustível (E para Etanol / D para Diesel): ')

# Se o combustível for Etanol
if tipo == 'E':
    preco = 1.70
    if litros <= 15:
        desconto = preco * litros * 0.02
    else:
        desconto = preco * litros * 0.04
        
    valor_a_pagar = (preco * litros) - desconto
    print(f'Valor a ser pago pelo Etanol: R$ {valor_a_pagar:.2f}')

# Se o combustível for Diesel
elif tipo == 'D':
    preco = 2.00
    if litros <= 15:
        desconto = preco * litros * 0.03
    else:
        desconto = preco * litros * 0.05
        
    valor_a_pagar = (preco * litros) - desconto
    print(f'Valor a ser pago pelo Diesel: R$ {valor_a_pagar:.2f}')

else:
    print('Opção inválida! Digite E para Etanol ou D para Diesel.')
