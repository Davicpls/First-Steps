print('\033[1mLEITOR DE NÚMERO POR EXTENSO\033[m')
zv = ('ZERO', 'UM', 'DOIS', 'TRÊS', 'QUATRO', 'CINCO', 'SEIS', 'SETE', 'OITO',
      'NOVE', 'DEZ', 'ONZE', 'DOZE', 'TREZE', 'QUATORZE', 'QUINZE', 'DEZESSEIS', 'DEZESSETE',
      'DEZOITO', 'DEZENOVE', 'VINTE')
while True:
    print('Digite um número de 0 a 20')
    n = int(input(': '))
    if n <= 20:
        print(zv[n])
        break
    elif n > 20:
        print('Você digitou um valor maior que vinte!')

