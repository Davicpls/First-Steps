import random
eu = str(input('Escolha pedra, papel ou tesoura \n: '))
comp = ['pedra', 'papel', 'tesoura']
x = random.choice(comp)
print('O Computador escolheu', x)
if x == 'tesoura' and eu == 'pedra':
    print('Você ganhou!')
elif x == 'pedra' and eu == 'papel':
    print('Você ganhou!')
elif x == 'papel' and eu == 'tesoura':
    print('Você ganhou!')
elif x == 'papel' and eu == x:
    print('Houve um empate!')
elif x == 'tesoura' and eu == x:
    print('Houve um empate!')
elif x == 'pedra' and eu == x:
    print('Houve um empate!')
else:
    print('Você perdeu!')