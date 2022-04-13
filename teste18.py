import math

n1 = (float(input('Digite um ângulo em graus: ')))
rad = n1 * math.pi / 180
sin = math.sin(rad)
cos = math.cos(rad)
tan = math.tan(rad)
print('O seno desse ângulo é {:.2f}'.format(sin))
print('O cosseno desse ângulo é {:.2f}'.format(cos))
print('A tangente desse ângulo é {:.2f}'.format(tan))
