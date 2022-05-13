matriz = [[], [], []], [[], [], []], [[], [], []]
somap = list()
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um número para a posição [{l}] [{c}]: '))
        if matriz[l][c] % 2 == 0:
            somap.append(matriz[l][c])
print('-' * 32)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
somat = matriz[0][2] + matriz[1][2] + matriz[2][2]
print(f'A soma dos números pares é igual a {sum(somap)}')
print(f'A soma dos números da terceira coluna é {somat}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')