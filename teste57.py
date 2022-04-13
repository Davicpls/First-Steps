sexo = str
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite seu sexo (M/F): ').upper())
    if sexo != 'M' and sexo != 'F':
        print('Digite o sexo novamente com M ou F')
    if sexo == 'M':
        print('Seu sexo é Masculino')
    if sexo == 'F':
        print('Seu sexo é feminino')
print('Fim')
