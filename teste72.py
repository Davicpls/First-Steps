print('\033[1mLEITOR DE NÚMERO POR EXTENSO\033[m')
zv = ('ZERO', 'UM', 'DOIS', 'TRÊS', 'QUATRO', 'CINCO', 'SEIS', 'SETE', 'OITO',
      'NOVE', 'DEZ', 'ONZE', 'DOZE', 'TREZE', 'QUATORZE', 'QUINZE', 'DEZESSEIS', 'DEZESSETE',
      'DEZOITO', 'DEZENOVE', 'VINTE')
print('Digite um número de 0 a 20')
n = int(input(': '))
while True:
    if n <= 20:
        print(zv[n])
        break
    elif n > 20:
        print('Você digitou um valor maior que vinte!')
        n = int(input('Digite novamente (0 à 20): '))
        if n <= 20:
            print('\n', zv[n])
            break
