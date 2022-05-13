tp = ('caneta', 'azul', 'pato', 'lilas', 'corno', 'kkkkmefudi',
      'dynatristonho', 'verde', 'saudade', 'beijin')
for p in tp:
    print(f'\nNa palavra {p} há as vogais: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
