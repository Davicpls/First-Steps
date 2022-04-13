preço = float(input('Qual o preço normal do produto? R$:'))
met = str(input('Métodos de pagamento:'' \na = Cheque / Dinheiro \nb = À vista no cartão \nc = 2x no cartão\nd = 3x ou mais no cartão\n:'))
dez = preço - preço * 10 / 100
vc = preço - preço * 5 / 100
c3 = preço + preço * 20 / 100
if met == 'a':
    print('À vista no dinheiro/cheque -> 10% de desconto -> preço R${} '.format(dez))
elif met == 'b':
    print('À vista no cartão -> 5% de desconto -> preço R${}'.format(vc))
elif met == 'c':
    print('Em até 2x no cartão -> preço R${}'.format(preço))
elif met == 'd':
    print('3x ou mais no cartão -> 20% de juros -> preço R${}'.format(c3))
