a1 = float(input('Digite a 1ª Reta em CM. \n'))
a2 = float(input('Digite a 2ª Reta em CM. \n'))
a3 = float(input('Digite a 3ª Reta em CM.\n'))
# if (a2 - a3) < a1 < (a2 + a3):
#     print('verdadeiro')
    # if (a1 - a3) < a2 < (a1 + a3):
    #     print('Verdadeiro')
        # if (a1 - a2) < a3 < (a1 + a2):
        #     print('As retas podem forma um TRIANGULO')
if (a2 - a3) < a1 <(a2 + a3) and (a1 - a3) < a2 < (a1 + a3) and (a1 - a2) < a3 < (a1 + a2):
    print('Condição verdadeira para forma triangulo')
else:
    print('Não podem forma um triangulo')
