print('\033[1m       BOLETIM')
print('-' * 28)
lista = list()
listaf = list()
notas = list()
nota = int
while True:
    nome = str(input('Nome do aluno: ')).capitalize()
    lista.append(nome)
    nota1 = float(input('1ª Nota: '))
    notas.append(nota1)
    nota2 = float(input('2ª Nota: '))
    notas.append(nota2)
    lista.append(notas[:])
    notas.clear()
    lista.append((nota1 + nota2) / 2)
    listaf.append(lista[:])
    lista.clear()
    r = ' '
    while r not in 'SN':
        r = input('Deseja continuar? (S/N): ').upper().strip()
    if 'S' in r:
        pass
    if 'N' in r:
        break
print('-' * 28)
print('Nº. NOME       MÉDIA')
print('-' * 28)
for x in range(0, len(listaf)):
    print(f'{x}   {listaf[x][0]}        {listaf[x][2]:.2f}')
print('-' * 32)
while nota != 999:
    nota = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    for p in range(0, len(listaf)):
        if nota == p:
            print(f'As notas de {listaf[p][0]} são {listaf[p][1]}.')
    if nota == 999:
        break

