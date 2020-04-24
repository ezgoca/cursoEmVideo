prod=float(input('Qual a valor do produto? \n'))
desc=int(5)
novoPreco= prod-((prod*desc)/100)
print('O produto de R${} com desconto corresponde a R${}'.format(prod,novoPreco))