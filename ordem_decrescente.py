numero_1 = float(input('Digite o número 1: '))
numero_2 = float(input('Digite o número 2: '))
numero_3 = float(input('Digite o número 3: '))

if numero_1 >= numero_2 and numero_1>= numero_3:
  maior = numero_1
  if numero_2 >= numero_3:
    meio = numero_2
    menor = numero_3
  else:
    meio = numero_3
    menor = numero_2


elif numero_2 >= numero_1 and numero_2 >= numero_3:
  maior = numero_2

  if numero_1 >= numero_3:
    meio = numero_1
    menor = numero_3

  else:
    meio = numero_3
    menor = numero_1

  
else:
  maior = numero_3
  if numero_1 >= numero_2:
    meio = numero_1
    menor = numero_2
  else:
    meio = numero_2
    menor = numero_1

  print(f' A ordem decrescente é: {maior}, {meio}, {menor} ')
