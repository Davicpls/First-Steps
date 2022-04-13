n = 999
count = 0
media = 0
soma = 0
maior = 0
menor = 0
list = []
while count != n:
    x = int(input('Digite um número inteiro: '))
    count += 1
    soma += x
    media = soma / count
    list.append(x)
    print('Você deseja continuar adicionando elementos? (S/N)')
    não = input(': ').upper()
    if não == 'N':
        print('A média dos números digitados foi {:.1f}'.format(media))
        print('O maior termo foi {} e o menor termo foi {}'.format(max(list), min(list)))
        count = 999
    if não == 'S':
        pass
    else:
        count = 999



