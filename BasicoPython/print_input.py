"""
    Recebendo dados do usuário
"""
from datetime import datetime # IMportando biblioteca datetime para manipular data e hora

# print("Qual é o seu nome?")
nome = input('Qual seu nome? ') # criando variável nome e solicitando entrada do usuário ao mesmo tempo

#Usando {nome} dentro da aspas simples para o valor da variável ja aparecer direto no print
print(f'Seja bem-vindo(a) {nome} ')

idade = input('Qual sua idade? ') #Todo dado recebido via input é do tipo String

print(f'O(a) {nome}, tem {idade} anos')

ano = datetime.now().year # Colocando na variável ano o valor da data do ano atual, no caso 2022

#int(idade) => Cast
# Cast é a conversão de um tipo de dado para outro

print(f'O(a) {nome} nasceu em {ano - int(idade)}') 