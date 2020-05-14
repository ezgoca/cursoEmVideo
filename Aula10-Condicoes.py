# carro.siga()
# if carro.esquerda():
#   carro.siga()
#   carro.direita()
#   carro.siga()
#   carro.esquerda()
#   carro.siga()
#   carro.direita()
#   carro.siga()
# else:
#   carro.siga()
#   carro.esquerda()
#   carro.siga()
#   carro.esquerda()
#   carro.siga()
# carro.pare()

# tempo = int( input('Quantos anos tem seu carro?'))
# if tempo <=3:
#     print('Carro novo')
# else:
#     print('Carro velho')
# print('Carro novo'if tempo<=3 else 'Carro velho')
# print('--FIM--')

# nome = str(input('Qual é o seu Nome?')).strip().upper()
# n = nome.split()
# if n[0] == 'EZEQUIEL':
#     print('Este nome é lindo!')
# else:
#     print('Seu nome é tão normal')
# print('Bom dia, {}!'.format(nome))

n1=float(input('Digite a primeira nota\n' ))
n2=float(input('digite a segunda nota\n' ))
m=(n1+n2)/2
print('A sua media foi {:.1f}'.format(m))
if m>=6.0:
    print('Sua media foi boa! PARABÉNS!')
else:
    print('Sua media foi ruim! ESTUDE MAIS!')
# print('PARABéNS!'if m>=6 else 'Estude um pouco MAIS!')
