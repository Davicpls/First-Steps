primeiro = (int(input('Digite o primeiro termo da PA: ')))
razão = (int(input('Digite a razão da PA: ')))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razão
    cont += 1
print('FIM')