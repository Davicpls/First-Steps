print('\033[1;34mCalculadora de IMC\033[m')
print('-' * 22)
peso = float(input('Digite o seu peso em KG: '))
altura = float(input('Digite sua altura em metros: '))
imc = peso / (altura ** 2)
print('Seu IMC é {:.1f}! '.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso!')
elif 18.5 <= imc < 25:
    print('Você está no peso ideal!')
elif 25 <= imc < 30:
    print('Você está com sobrepeso!')
elif 30 <= imc < 40:
    print('Você está obeso!')
elif imc >= 40:
    print('Você tem obesidade mórbida!')

