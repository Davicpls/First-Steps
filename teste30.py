num = int(input('Digite um número inteiro: '))
u = num // 1 % 10
x = [0, 2, 4, 6, 8]
if u in x:
    print('O número é par')
else:
    print('O número é impar')