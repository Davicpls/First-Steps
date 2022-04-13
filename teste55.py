list = []
for pess in range(1, 6):
    peso = int(input('Digite o peso da {}ª pessoa (KG): '.format(pess)))
    list.append(peso)
print('O maior peso foi {}KG e o menor peso foi {}KG'.format(max(list), min(list)))
