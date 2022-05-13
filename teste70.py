cont = menor = maior = prod1000 = tot = 0
barato = ''
while True:
    produto = str(input('Digite o nome do produto: '))
    preço = float(input('Digite o preço do produto em R$:'))
    cont += 1
    r = ' '
    while r not in 'SN':
        print('Você deseja adicionar mais produtos? (S/N): ')
        r = input(': ').upper().strip()
    if r == 'S':
        tot += preço
        if preço > 1000:
            prod1000 += 1
        if cont == 1:
            menor = preço
            barato = produto
        else:
            if preço < menor:
                menor = preço
                barato = produto
    if r == 'N':
        tot += preço
        if preço > 1000:
            prod1000 += 1
            break
print('O total gasto na compra foi de R${}'.format(tot))
print('A quantidade de produtos que custam mais de R$1000 é igual a {}'.format(prod1000))
print('O nome do produto mais barato é {}'.format(barato))


