s1 = float(input('Quanto você ganha?: R$'))
s2 = ((s1 / 100) * 15) + s1
print('Com 15% de aumento o seu salário será: R${:.2f} '.format(s2))
