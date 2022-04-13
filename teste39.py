ano = int(input('Digite seu ano de nascimento(4 dígitos): '))
idade = 2022 - ano
tempo1 = 18 - idade
tempo2 = idade - 18
if idade < 18:
    print('Você ainda irá se alistar ao serviço militar!')
    print('Ainda falta {} anos para você poder se alistar!'.format(tempo1))
if idade == 18:
    print('Está na hora de se alistar no serviço militar!')
if idade > 18:
    print('Já passou do tempo de se alistar!')
    print('Já se passaram {} anos que você deveria ter se alistado!'.format(tempo2))
