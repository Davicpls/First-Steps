num = int(input('Digite um número inteiro qualquer: '))
escolha = str(input('Escolha a base de conversão, sendo: \nx = binário\ny = octal\nz = hexadecimal\n: '))
x = bin(num)[2:]
y = oct(num)[2:]
z = hex(num)[2:]
if escolha == 'x':
    print('O valor em binário é {}'.format(x))
elif escolha == 'y':
    print('O valor em octal é {}'.format(y))
elif escolha == 'z':
    print('O valor em hexadecimal é {}'.format(z))
