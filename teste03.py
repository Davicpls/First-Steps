cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m',
         'stop':'\033[m'}
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro: '))
s = (n1 + n2)
print('A soma entre {}{}{} e {}{}{} é igual a {}{}{}.'.format(cores['azul'], n1, cores['stop'],
                                                             cores['amarelo'], n2, cores['stop'],
                                                             cores['pretoebranco'], s, cores['stop']))
