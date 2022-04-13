cidade = str(input('Digite o nome da sua cidade: '))
cidade = cidade.upper().split()
cidade0 = cidade[0]
print('O primeiro nome da sua cidade é: {}'.format(cidade[0]))
print('O primeiro nome da sua cidade começa com o nome: SANTO? ')
print('SANTO' in cidade0)