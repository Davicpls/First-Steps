vel = int(input('A velocidade do carro em Km/h é: '))
limite = 80
multa = (vel - limite) * 7
if vel > 80:
    print('Você foi multado!')
    print('----------------')
    print('Sua multa custará R${}'.format(multa))
else:
    print('Você está dentro do limite da velocidade.')


