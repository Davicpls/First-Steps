cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m',
         'stop':'\033[m'}
dia = input('Qual dia do mês você nasceu? ')
mes = input('Qual mês você nasceu? ')
ano = input('Qual ano você nasceu? ')
print('Você nasceu no dia {}{}{} do mes de {}{}{} do ano de {}{}{}. {}Correto?'.format(cores['azul'], dia, cores['stop'], cores['amarelo'], mes, cores['stop'], cores['pretoebranco'], ano, cores['stop'], cores['limpa']))
