valores = []
for d in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {d}: ')))
    max_value = max(valores)
    max_index = valores.index(max_value)
    min_value = min(valores)
    min_index = valores.index(min_value)
print('-' * 32)
print(f'O maior valor digitado foi {max(valores)} e está nas posições ', end='')
for i, v in enumerate(valores):
    if v == max(valores):
        print(f'{i}...', end='')
print(f'\nO menor valor digitado foi {min(valores)} e está na posição ', end='')
for i, v in enumerate(valores):
    if v == min(valores):
        print(f'{i}...', end='')