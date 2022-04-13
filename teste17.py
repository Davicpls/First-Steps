import math
co = float(input('Diga em cm o tamanho do cateto oposto de um triângulo retângulo: '))
ca = float(input('Diga em cm o tamanho do cateto adjacente de um triângulo retângulo: '))
sc = math.pow(co, 2) + math.pow(ca, 2)
hp = math.pow(sc, 2)
print('O comprimento da hipotenusa em cm é igual a {:.2f}'.format(sc))
