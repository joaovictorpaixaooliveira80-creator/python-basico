numero_1 = float(input('Digite o primeiro numero: '))
numero_2 = float(input('Digite o segundo numero: '))
operação = input('Qual operação deseja fazer: ')

if operação == '+':
    resultado = numero_1 + numero_2
          
elif operação == '-':
   resultado = numero_1 - numero_2
                 
elif operação == '*':
    resultado = numero_1 * numero_2

elif operação == '/':
    resultado = numero_1 / numero_2
                 
# Resultado deve mostrar se é par ou impar 

if resultado % 2 == 0:
    print(f'O número {resultado} é PAR!')
else:
    print(f'O número {resultado} é ÍMPAR!')


# Resultado deve mostrar se é positivo ou negativo

if resultado > 0:
  print(f' O numero {resultado} é positivo!')

elif resultado < 0:
  print(f'O numero {resultado} é negativo!')


# Resultado deve mostrar se é inteiro ou decimal                  

if resultado % 1 == 0 :
  print(f' O número {resultado} é Inteiro! ')

else:
  print(f' O número {resultado} é Decimal! ')
