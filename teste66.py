print('\033[1mQuantos números digitados e a soma (999 para parar) -->')
n = s = 0
count = 0
while True:
    n = int(input('Digite um número inteiro: '))
    if n == 999:
        break
    count += 1
    s += n
print(f'A quantidade de números digitados foi {count} e a soma deles é {s}')
