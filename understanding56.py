i = 0
mulherv = ''
idade = 0
idademaior = 0
nome = str
for prog in range(1, 5):
    idade = int(input('Número: '))
    nome = input('Nome: ')
    sexo = input('Sexo: ')
    if prog == 1 and sexo in 'Ff':
        idademaior = idade
        mulherv = nome
    if sexo in 'Ff' and idade > idademaior:
        idademaior = idade
        mulherv = nome
print('A mulher mais velha tem {} anos e se chama {} '.format(idademaior, mulherv))