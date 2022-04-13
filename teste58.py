import random
tentativas = 0
jogador = 0
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
z = random.choice(x)
while z != jogador:
    jogador = int(input('Digite um valor: '))
    if z != jogador:
        tentativas += 1
    else:
        print('Você acertou na {}ª tentativa'.format(tentativas + 1))