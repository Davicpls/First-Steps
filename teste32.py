ano = int(input('Digite um ano: '))
bis = ano % 4
if bis == 0:
    print('Esse ano é bissexto!')
else:
    print('Esse ano não é bissexto!')
