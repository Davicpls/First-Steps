lista = []
e = str(input('Digite uma expressão: '))
lista.append(e)
if e.count('(') == e.count(')'):
    print('A expressão é válida!')
else:
    print('A expressão está errada!')