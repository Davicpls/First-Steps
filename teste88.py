from random import randint
count = 0
palp = list()
palpog = list()
print('\033[1mPALPITES DA MEGA SENA')
print('-' * 25)
print('Quantos jogos você deseja jogar?')
r = int(input(': '))
for j in range(1, r + 1):
    for p in range(0, 6):
        palp.append(randint(1, 60))
    palpog.append(palp[:])
    palp.clear()
for x in range(0, len(palpog)):
    print(f'O {x + 1}º jogo: {palpog[x]}')
