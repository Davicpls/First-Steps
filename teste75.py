n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite outro número: '))
n4 = int(input('Digite outro número: '))
tp = (n1, n2, n3, n4)
print(f'Sua tupla ficou : {tp}', end='\n')
print(f'A quantidade de números 9 foram: {tp.count(9)}')
if tp.count(3) > 0:
    tres = tp.index(3)
    print(f'O número 3 apareceu a primeira vez na posição: {tres}')
elif tp.count(3) <= 0:
    print('Não tiveram números 3 na tupla')
if n1 % 2 == 0:
    print(f'O número {n1} que está na tupla é par')
if n2 % 2 == 0:
    print(f'O número {n2} que está na tupla é par')
if n3 % 2 == 0:
    print(f'O número {n3} que está na tupla é par')
if n4 % 2 == 0:
    print(f'O número {n4} que está na tupla é par')
if n1 % 2 == 1 and n2 % 2 == 1 and n3 % 2 == 1 and n4 % 2 == 1:
    print('Não há números pares nessa tupla')
