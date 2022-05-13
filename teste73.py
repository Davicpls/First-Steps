cb = ('Santos', 'Atlético-MG', 'Corinthians', 'Cuiaba', 'Internacional', 'Avaí', 'Bragantino',
      'Palmeiras', 'Flamengo', 'Coritiba', 'São Paulo', 'Botafogo', 'Chapecoense', 'América-MG',
      'Ceará SC', 'Athletico-PR', 'Athletico-GO', 'Goiás', 'Juventude', 'Fortaleza')
chapeco = cb.index('Chapecoense')
print(f'Os 5 primeiros colocados são: \n{cb[0:5]}')
print(f'Os últimos 4 colocados são: \n{cb[16:21]}')
print(f'A lista dos times em ordem alfabética é: \n{sorted(cb)}')
print(f'O Chapecoense está na posição {chapeco} da lista')
