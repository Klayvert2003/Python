"""
Faça um programa que solicite ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um valor
inteiro, informe que não é um número inteiro.
"""

num = input('Digite um número inteiro: ') # Entrada do usuário


try:
    int(num) # Tratando exceção para output que não seja inteiro
except:
    print('Este número não é inteiro')

if int(num) %2:
    print('Número ímpar!')
else:
    print('Número par!')