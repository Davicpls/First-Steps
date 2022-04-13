dist = int(input('Qual a distância da sua viagem em Km?: '))
preço1 = dist * 0.50
preço2 = dist * 0.45
if dist <= 200:
    print(f'O preço da sua passagem será de R${preço1}')
else:
    print(f'O preço da sua passagem será de R${preço2}')

