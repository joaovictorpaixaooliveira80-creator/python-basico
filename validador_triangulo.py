lado_1 = float(input('Digite o valor do lado 1 do triângulo: '))
lado_2 = float(input('Digite o valor do lado 2 do triângulo: '))
lado_3 = float(input('Digite o valor do lado 3 do triângulo: '))

if (lado_1 + lado_2 > lado_3) and (lado_1 + lado_3 > lado_2) and (lado_2 + lado_3 > lado_1):
    print('Pode formar um triângulo!')
    
    if lado_1 == lado_2 and lado_2 == lado_3:
        resultado = 'Equilátero'
    elif lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3:
        resultado = 'Isósceles'
    else:
        resultado = 'Escaleno'
        
    print(f'Esse Triângulo é um {resultado}!')

else:
    print('Estes valores não formam um triângulo.')
