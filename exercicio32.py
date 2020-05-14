ano = int(input('Digite o ano atual com 4 digitos: \n'))
# if ano%4==0 and ano%100!=0 or ano%400==0:
if ano%4==0:
    if ano%100!=0 or ano%400==0:
            print('O ano {} digitado é bisexto'.format(ano))
else:
    print('O ano {} digitado NÃO é bisexto'.format(ano))