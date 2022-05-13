print('\033[1mSIMULADOR DE CAIXA ELETRÔNICO')
print('Cédulas disponíveis: RS1,00 / R$10,00 / R$20,00 / R$50,00')
print('-' * 32)
print('Qual valor você deseja sacar? (R$)')
n = int(input('R$ '))
c50 = c20 = c10 = c1 = 0
ci = 50
r = int
a = '1 real'
b = '10 reais'
c = '20 reais'
d = '50 reais'
while True:
    if n < 10:
        print(f'A quantidade de cédulas de {a} que serão entregues será de {n}.')
        break
    elif n == 10:
        c10 += 1
        print(f'A quantidade de cédulas de {b} que será entregue será de {c10}.')
        break
    elif n == 20:
        c20 += 1
        print(f'A quantidade de cédulas de {c} que será entregue é de {c20}.')
        break
    elif n == 50:
        c50 += 1
        print(f'A quantidade de cédulas de {d} que será entregue será de {c50}.')
        break
    elif n == 30:
        c20 += 1
        c10 += 1
        print(f'A quantidade de cédulas de {b} será de {c10}\nA quantidade de cédulas de {c} será de {c20}.')
    elif n == 40:
        c20 += 2
        print(f'A quantidade de cédulas de {c} que serão entregues será de {c20}.')
        break
    elif 10 < n < 20:
        c10 += 1
        c1 += (n - 10)
        print(f'A quantidade de cédulas de {a} será de {c1}\nA quantidade de cédulas de {b} será de {c10}.')
        break
    elif 20 < n < 30:
        c20 += 1
        c1 += (n - 20)
        print(f'A quantidade de cédulas de {a} será de {c1}\nA quantidade de cédulas de {c} será de {c20}.')
        break
    elif 30 < n < 40:
        c20 += 1
        c10 += 1
        c1 += (n - 30)
        print(f'A quantidade de cédulas de {a} será de {c1}\nA quantidade de cédulas de {b} será de {c10}'
              f'\nA quantidade de cédulas de {c} será de {c20}.')
        break
    elif 40 < n < 50:
        c20 += 2
        c1 += (n - 40)
        print(f'A quantidade de cédulas de {a} será de {c1}\nA quantidade de cédulas de {c} será de {c20}.')
        break
    if n > 50 and n % 2 == 0:
        c50 = n // ci
        r = n % ci
        if r == 0:
            print(f'A quantidade de cédulas de {d} será de {c50}.')
            break
        elif 10 < r < 20:
            c10 += 1
            c1 += (r - 10)
            print(f'A quantidade de cédulas de {d} será de {c50}\nA quantidade de cédulas de {b} será de {c10}'
                  f'\nA quantidade de cédulas de {a} será de {c1}.')
            break
        elif 20 < r < 30:
            c20 += 1
            c1 += (r - 20)
            print(f'A quantidade de cédulas de {d} será de {c50}\nA quantidade de cédulas de {c} será de {c20}'
                  f'\nA quantidade de cédulas de {a} será de {c1}.')
            break
        elif 30 < r < 40:
            c20 += 1
            c10 += 1
            c1 += (r - 30)
            print(f'A quantidade de cédulas de {d} será de {c50}.\nA quantidade de cédulas de {b} será de {c10}.'
                  f'\nA quantidade de cédulas de {c} será de {c20}.\nA quantidade de cédulas de {a} será de'
                  f' {c1}.')
            break
        elif 40 < r < 50:
            c20 += 2
            c1 += (r - 40)
            print(f'A quantidade de cédulas de {d} será de {c50}\nA quantidade de cédulas de {c} será de {c20}.'
                  f'\nA quantidade de cédulas de {a} será de {c1}.')
            break
        elif r == 10:
            c10 += 1
            print(f'A quantidade de cédulas de {d} será de {c50}.\nA quantidade de cédulas de {b} será de {c10}.')
            break
        elif r == 20:
            c20 += 1
            print(f'A quantidade de cédulas de {d} será de {c50}.\nA quantidade de cédulas de {c} será de {c20}.')
            break
        elif r == 30:
            c20 += 1
            c10 += 1
            print(f'A quantidade de cédulas de {d} será de {c50}.\nA quantidade de cédulas de {b} será de {c10}.'
                  f'\n A quantidade de cédulas de {c} será de {c20}.')
            break
        elif r == 40:
            c20 += 2
            print(f'\n A quantidade de cédulas de {d} será de {c50}.\nA quantidade de cédulas de {c} será de {c20}.')
            break
    if n > 50 and n % 2 == 1:
        c50 = n // ci
        r = n % ci
        if r < 10:
            print(f'A quantidade de cédulas de {d} será de {c50}.\nA quantidade de cédulas de {a} será {r}.')
            break
        elif 10 < r < 20:
            c10 += 1
            c1 += (r - 10)
            print(f'A quantidade de cédulas de {d} será de {c50}.\nA quantidade de cédulas de {b} será de {c10}.'
                  f'\nA quantidade de cédulas de {a} será de {c1}.')
            break
        elif 20 < r < 30:
            c20 += 1
            c1 += (r - 20)
            print(f'A quantidade de cédulas de {d} será de {c50}.\nA quantidade de cédulas de {c} será de {c20}.'
                  f'\nA quantidade de cédulas de {a} será de {c1}.')
            break
        elif 30 < r < 40:
            c20 += 1
            c10 += 1
            c1 += (r - 30)
            print(f'A quantidade de cédulas de {d} será de {c50}.\nA quantidade de cédulas de {b} será de {c10}.'
                  f'\nA quantidade de cédulas de {c} será de {c20}.\nA quantidade de cédulas de {a} será de'
                  f' {c1}.')
            break
        elif 40 < r < 50:
            c20 += 2
            c1 += (r - 40)
            print(f'A quantidade de cédulas de {d} será de {c50}.\nA quantidade de cédulas de {c} será de {c20}.'
                  f'\nA quantidade de cédulas de {a} será de {c1}.')
            break

