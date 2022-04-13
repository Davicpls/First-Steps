import random

x = [0, 1, 2, 3, 4, 5]
z = random.choice(x)
escolha = int(input('Digite um número de 0 a 5: '))
if escolha == z:
    print('Você venceu!')
else:
    print('Você perdeu!')
print('O número escolhido pelo computador foi {}'.format(z))


