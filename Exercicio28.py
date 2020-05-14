import random
lista = [1,2,3,4,5]
num_user = int(input('Em que numero estou pensando entre 0 a 5?\n'))
num_programa = random.choice(lista)
if num_user == num_programa:
    print('Parabens, pensei neste numero {} mesmo!'.format(num_programa))
else:
    print('Você errou! o numero escolhido foi {}!'.format(num_programa))