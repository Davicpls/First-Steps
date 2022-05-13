idadem_menor = int(0)
count = int(0)
counth = int(0)
while True:
    idade = int(input('\033[1mQual a sua idade?: '))
    sexo = ' '
    r = ' '
    while sexo not in 'MF':
        sexo = str(input('\033[1mQual o seu sexo? (M/F): ').upper().strip())
    while r not in 'SN':
        print('Você deseja continuar o programa? (S/N): ')
        r = input(': ').upper().strip()
    if r == 'S':
        if idade > 18:
            count += 1
        if sexo == 'M':
            counth += 1
        if sexo == 'F' and idade < 20:
            idadem_menor += 1
    if r == 'N':
        if idade > 18:
            count += 1
        if sexo == 'M':
            counth += 1
        if sexo == 'F' and idade < 20:
            idadem_menor += 1
        break
print('A quantidade de pessoas com mais de 18 anos foram {}'.format(count))
print('A quantidade de homens cadastrados foram {}'.format(counth))
print('A quantidade de mulheres com menos de 20 anos cadastradas foram {}'.format(idadem_menor))

