from random import randint
from time import sleep
# lista = [1,2,3,4,5]
lista = randint(0,5)
num_user = int(input('Em que numero estou pensando entre 0 a 5?\n'))
# num_programa = random.choice(lista)
# if num_user == num_programa:
print('-=-'*20)
print("Processandor....")
sleep(3)
print('-=-'*20)
if num_user == lista:
    print('Parabens, pensei neste numero {} mesmo!'.format(lista))
else:
    print('Você errou! o numero escolhido foi {}!'.format(lista))