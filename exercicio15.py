dias=int(input('Quantos dias alugados? \n'))
km=float(input('Quantos Kilometros percorridos?\n'))
vDia=60.00
kmRod=0.15
valor= (vDia*dias)+(kmRod*km)
print('O valor do aluguel será {:.2f} '.format(valor))