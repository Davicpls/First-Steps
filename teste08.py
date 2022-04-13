m = float(input('Diga um valor em metros: '))
cm = m * 100
mm = m * 1000
km = m / 1000
dcm = m * 10
dam = m / 10
hm = m / 100
print('O valor {} em Metros pode ser convertido para {} cm e {} mm'.format(m, cm, mm))
print('O valor em Km vai ser {} \nEm Decímetros {}\nEm Decâmetros {} e \nEm Hectômetros {}'.format(km, dcm, dam, hm))
