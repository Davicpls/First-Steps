lista = list()
lista2 = list()
menor = maior = 0
while True:
    lista.append(str(input('Nome: ')))
    lista.append(float(input('Peso(KG): ')))
    if len(lista2) == 0:
        maior = menor = lista[1]
    else:
        if lista[1] > maior:
            maior = lista[1]
        if lista[1] < menor:
            menor = lista[1]
    lista2.append(lista[:])
    lista.clear()
    r = ' '
    while r not in 'SN':
        print('Deseja continuar?(S/N) ')
        r = input(': ').upper().strip()
    if 'S' in r:
        pass
    if 'N' in r:
        break
print(f'A quantidade de pessoas cadastradas foram {len(lista2)}')
print(f'O maior peso dos cadastrados foi de {maior}KG. De ', end='')
for p in lista2:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso dos cadastrados foi de {menor}KG. De ', end='')
for p in lista2:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
