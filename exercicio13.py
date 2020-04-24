sal=float(input('Digite o salario do funcionario \nR$'))
aum=int(15)
aumento= sal+((sal*aum)/100)
print('O funcionario ganhava {:.2f} com aumento de {}% será {:.2f}'.format(sal,aum,aumento))