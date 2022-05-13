lista = [[], []]
for v in range(1, 8):
    n = int(input(f'Digite o {v}º número: '))
    if n % 2 == 0:
        lista[0].append(n)
    if n % 2 == 1:
        lista[1].append(n)
lista[0].sort()
lista[1].sort()
print(f'Os números pares estão na ordem crescente na lista: {lista[0]}')
print(f'Os números ímpares estão na ordem crescente na lista: {lista[1]}')
