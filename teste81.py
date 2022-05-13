lista = []
count = 0
while True:
    count += 1
    n = int(input('Digite um valor: '))
    lista.append(n)
    r = input('Deseja continuar? S/N ').upper()
    if r == 'N':
        break
print(f'A quantidade de números digitados foram {count}')
lista.sort(reverse=True)
print(f'A ordem decrescente da lista é {lista} ')
if 5 in lista:
    print(f'O valor 5 foi digitado e está na lista - > {lista}')
else:
    print('O valor 5 não foi digitado e não está na lista')
