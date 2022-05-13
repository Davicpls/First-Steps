print('\033[1m       BOLETIM')
print('-' * 28)
lista = list()
listaf = list()
media = list()
while True:
    nome = str(input('Nome do aluno: ')).capitalize()
    lista.append(nome)
    nota1 = float(input('1ª Nota: '))
    lista.append(nota1)
    nota2 = float(input('2ª Nota: '))
    lista.append(nota2)
    listaf.append(lista[:])
    lista.clear()
    r = ' '
    while r not in 'SN':
        r = input('Deseja continuar? (S/N): ').upper().strip()
    if 'S' in r:
        pass
    if 'N' in r:
        break
for x in range(0, len(listaf)):
    print(f'\nAluno: {listaf[x][0]}; Notas --> {listaf[x][1]}/{listaf[x][2]}'
          f'\nMédia: {(listaf[x][1] + listaf[x][2]) / 2}')
