primeiro = int(input('Digite o primeiro termo da sua PA: '))
razão = int(input('Digite a razão da sua PA: '))
termo = primeiro
count = 1
n = 11
while count < n:
    print('{} -> '.format(termo), end='')
    termo += razão
    count += 1
    if count == n:
        print('\nVocê gostaria de adicionar mais termos? Se sim, quantos?')
        q = int(input(': '))
        n += q
        if q == 0:
            print('FIM')



