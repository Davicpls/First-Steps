import random
print('\033[1mJOGO DO PAR OU ÍMPAR (SÓ PARA QUANDO VOCÊ PERDE)')
print('-' * 30)
r = random.randint(0, 10)
ÍMPAR = 'ÍMPAR'
PAR = 'PAR'
comp = ÍMPAR
comp = PAR
count = 0
while True:
    e = str(input('Escolha Par ou Ímpar: ').upper().strip())
    n = int(input('Digite um número de 0 a 10: '))
    r = random.randint(0, 10)
    print(r)
    if e == 'PAR':
        comp = ÍMPAR
    elif e == 'ÍMPAR':
        comp = PAR
    if (n + r) % 2 == 0 and e == PAR:
        count += 1
        print('Você ganhou!')
    if (n + r) % 2 == 0 and comp == PAR:
        print('Você perdeu!')
        break
    if (n + r) % 2 == 1 and comp == ÍMPAR:
        print('Você perdeu!')
        break
    if (n + r) % 2 == 1 and e == ÍMPAR:
        count += 1
        print('Você ganhou!')
print('Seu total de vitórias consecutivas foram {}'.format(count))