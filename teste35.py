l1 = float(input('Digite o valor da primeira reta em cm: '))
l2 = float(input('Digite o valor da segunda reta em cm: '))
l3 = float(input('Digite o valor da terceira reta em cm: '))

print('Para que um triângulo exista, a soma de dois lados tem que ser menor que o terceiro lado.')
print('--------------------------------------------------------------------------')
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l2 + l1:
    print('As 3 retas podem formar um triângulo')
else:
    print('Não é possível formar um triângulo')
