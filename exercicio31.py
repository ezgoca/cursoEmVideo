distancia = float(input('Digite a distancia pecorrida em KM:\n'))
if distancia<=200:
    preco = distancia*0.50
    print('Sua viagem é curta com o Valor de R$ {}'.format(preco))
else:
    preco = distancia*0.45
    print('Sua viagem é longa com o valor de R${}'.format(preco))
#preco =distacia*0.50 if distacia <= 200 else distancia*0.45
# print('Sua viagem de {} KM será com o preço de {}. '.format(distancia,preco))