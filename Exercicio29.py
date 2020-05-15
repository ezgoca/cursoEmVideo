vel = float(input('Digite a velocidade do carro: \n'))
if vel >= 80:
    multa = (vel - 80) * 7
    print('Você foi multado com o valor total R${}'.format(multa))
else:
    print('Tenha um bom dia e uma otima viagem')
