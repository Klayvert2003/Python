"""
Faça um programa que pergunte a hora ao usuário e baseando-se no horário
exiba a saudação correta. 
Exemplo: Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23
"""

hora = input('Informe um horário: ')

try:
    int(hora)
except:
    print('A hora deve ser passada como um valor inteiro!')

if int(hora) > 0 and int(hora) <= 11:
    print('Bom dia!')
elif int(hora) >= 12 and int(hora) <= 17:
    print('Boa tarde!')
elif int(hora) >= 18 and int(hora) <= 23:
    print('Boa noite!')
else:
    print('Meia noite eu te conto')