km = (float(input('Quantos KM o carro percorreu?: ')))
d = (int(input('Quantos dias o carro esteve alugado?: ')))
preço = (km * 0.15) + (d * 60)
print('O custo do aluguel deste carro será de R${:.2f}'.format(preço))
