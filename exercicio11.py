largura=float(input('Digite a medida da largura em M: '))
altura=float(input('Digite a medida da altura em M: '))
area= largura*altura
print('A dimensão da parede  de {}alt. x {}lag. em metros quadrados é {}'.format(altura,largura,area))
print('A quantidade de tinta usada será {:.0f} litros'.format(area/2))
