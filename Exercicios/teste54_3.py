"""
Faça um programa que leia o nome do usuário. Se o nome tiver:
4 letras ou menos escreva -> 'Seu nome é curto'
5 ou 6 letras escreva -> 'Seu nome é normal'
Mais que 6 letras escreva -> 'Seu nome é muito grande' 
"""

nome = input('Digite seu nome: ')

if len(nome) <= 4:
    print('Seu nome é curto!')
elif len(nome) >= 5 and len(nome) <= 6:
    print('Seu nome é normal!')
elif len(nome) > 6:
    print('Seu nome é muito grande!')