a = float(input('Digite um número: '))
b = float(input('Digite outro: '))
c = float(input('Digite outro: '))
maior = a
if a>b and a>c:
    maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('O maior número é {}'.format(maior))
menor = a
if a<b and a<c:
    menor = a
if b<c and b<a:
    menor = b
if c<a and c<b:
    menor = c
print('O menor número é {}'.format(menor))


