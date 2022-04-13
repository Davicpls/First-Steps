print('\033[1;35mAprovador de empréstimos.\033[m')
print('\033[1m----------------------\033[m')
imov = float(input('Valor do imóvel em R$:'))
sal = float(input('Seu salário mensal em R$:'))
anos = int(input('Em quantos anos você pretende pagar o imóvel?: '))
meses = anos * 12
prestm = imov / meses
sal30 = (30 * sal) / 100
if sal30 >= prestm:
    print('A prestação mensal será de \033[1;33mR${:.2f} e o \nempréstimo será ACEITO!'.format(prestm))
else:
    print('O seu empréstimo será NEGADO!')