a = list()
b = list()
c = list()
while True:
    n = int(input('Digite um número: '))
    a.append(n)
    if n % 2 == 0:
        b.append(n)
    if n % 2 == 1:
        c.append(n)
    r = str(input('Você deseja continuar? S/N ')).upper()
    if r == 'N':
        break
print(f'A lista completa foi: {a}')
print(f'A lista somente com os números pares foi {b}')
print(f'A lista somente com os números impares foi {c}')