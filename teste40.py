n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))
media = (n1 + n2) / 2
if media < 5.0:
    print('Sua média foi {:.2f} e você foi \033[1mREPROVADO!'.format(media))
if 5.0 <= media <= 6.9:
    print('Sua média foi {:.2f} e você está na \033[1mRECUPERAÇÃO!'.format(media))
if media >= 7.0:
    print('Sua média foi {:.2f} e você está \033[1mAPROVADO!'.format(media))
