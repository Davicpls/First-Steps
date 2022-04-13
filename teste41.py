ano = int(input('Ano de nascimento do atleta (4 dígitos): '))
idade = 2022 - ano
if ano <= 9:
    print(f'O atleta tem {idade} anos e está na categoria \033[1mMIRIM.')
if 9 < ano <= 14:
    print(f'O atleta de {idade} anos está na categoria \033[1mINFANTIL.')
if 14 < ano <= 19:
    print(f'O atleta de {idade} anos está na categoria \033[1mJUNIOR.')
if ano == 20:
    print(f'O atleta de {idade} anos está na categoria \033[1mSÊNIOR.')
if ano > 20:
    print(f'O atleta de {idade} anos está na categoria \033[1mMASTER.')