sal=float(input('Qual o valor do seu salario em R$: \n'))
if sal>1250:
    aumento=sal+((sal/100)*10)
    print('O valor com aumento de 10% será {}'.format(aumento))
else:
    aumento=sal+((sal/100)*15)
    print('O valor com aumento de 15% será {}'.format(aumento))