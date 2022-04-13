real = float(input('Quantos reais você tem na carteira: ? R$'))
doll = real / 4.79
print('Se você tem R${} na carteira, você poderá comprar US${:.2f} dólares'.format(real, doll))
