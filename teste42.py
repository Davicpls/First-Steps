l1 = float(input('Digite o valor da primeira reta em cm: '))
l2 = float(input('Digite o valor da segunda reta em cm: '))
l3 = float(input('Digite o valor da terceira reta em cm: '))
print('--------------------------------------------------------------------------')
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l2 + l1:
    print('As 3 retas podem formar um triângulo!')
    if l1 == l2 == l3:
        print('O seu triângulo é EQUILÁTERO')
    elif l1 != l2 != l3 != l1:
        print('O seu triângulo é ESCALENO')
    else:
        print('O seu triângulo é ISÓSCELES')
else:
    print('Não é possível formar um triângulo')

