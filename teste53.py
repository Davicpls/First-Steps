nome = str(input('Digite uma frase qualquer: ')).strip().upper()
palavra = nome.split()
junto = ''.join(palavra)
print(junto[0:], junto[::-1])
if junto[0:] == junto[::-1]:
    print('Sua frase é um palíndromo!')
else:
    print('Sua frase não é um palíndromo!')