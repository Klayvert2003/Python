"""
Loop While

Forma geral

while expressão_booleana:
    //execução do loop

o bloco while será repetido enquanto a expressão booleana do loop while for True.

Expressão booleana é toda expressão onde o resultado é True or False.

#Exemplo 1:

num = 1

while num < 10:
    print(num)
    num += 1
"""

#Exemplo 2:

resposta = ' '

while resposta != 'sim' or 'SIM' or 'Sim' or 'S' or 's':
    resposta = input("Tu é gay? ")