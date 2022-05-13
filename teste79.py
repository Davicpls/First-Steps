listinha = list()
while True:
    n = (int(input(f'Digite um número: ')))
    if n not in listinha:
        listinha.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado, não adicionado!')
    c = str(input('Deseja continuar? [S/N] ').upper())
    if c in 'N':
        break
listinha.sort()
print(f'Você digitou os valores {listinha}')