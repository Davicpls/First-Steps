nome = str(input('Digite uma frase qualquer: ')).strip().upper()
palavra = nome.split()
junto = ''.join(palavra)
inverso = ''
for letra in range(len(junto) - 1, - 1, - 1):
    inverso += junto[letra]
print(junto, inverso)
if junto == inverso:
    print('Sua frase é um palíndromo!')
else:
    print('Sua frase não é um palíndromo')

    #DIFÍCIL PRA KRL