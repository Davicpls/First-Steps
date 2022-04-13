h = float(input('Qual altura da parede em metros?: '))
l = float(input('Qual a largura da parede em metros?: '))
a = (h * l)
ti= (h * l)/2
print('Para uma altura de {}m e uma largura de {}m a parede terá {:.2f}m² e precisará de {:.2f} litros de tinta'.format(h, l, a, ti))
