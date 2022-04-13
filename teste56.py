homem_mvelho = ''
maior_idadeh = 0
idade = int(0)
nome = str
count_m = 0
s = int(0)
for prog in range(1, 5):
    print('------ {}ª PESSOA ------'.format(prog))
    nome = str(input('Digite o nome da {}ª pessoa: '.format(prog)))
    idade = int(input('Digite a idade da {}ª pessoa: '.format(prog)))
    sexo = str(input('Digite o sexo da {}ª pessoa (M/F): '.format(prog).strip()))
    s += idade
    if prog == 1 and sexo in 'Mm':
        maior_idadeh = idade
        homem_mvelho = nome
    if sexo in 'Mm' and idade > maior_idadeh:
        maior_idadeh = idade
        homem_mvelho = nome
    if sexo == 'F' and idade < 20:
        count_m += 1
media = s / 4
print('A média de idade do grupo é de {:.0f} anos.'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(maior_idadeh, homem_mvelho))
print('A quantidade de mulheres com menos de 20 anos é {}'.format(count_m))