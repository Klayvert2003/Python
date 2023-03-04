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
"""
resposta = ' '

while resposta != 'sim' or 'SIM' or 'Sim' or 'S' or 's':
    resposta = input("você gosta de futebol? ")
"""

#Exemplo 3:

# condicao = True

# while condicao:
#     nome = input('Digite seu nome: ')
#     print(f'Seu nome é {nome}')
#     if nome == 'Klayvert':
#         condicao = False
#         break

# contador = 0

# while contador < 100:
#     contador += 1

#     # Não executa os blocos de código abaixo do if e volta no loop novamente se contador == 6
#     if contador == 6:
#         continue

#     # Pulando laço do while do número 10 ao número 20
#     if contador >= 10 and contador <= 20: 
#         continue

#     print(f'O laço repetiu {contador} vez(es)')

#     # Quebrando o laço While se o contador chegar ao 30
#     if contador == 30:
#         print(contador)
#         break

qtd_linhas = 5
qtd_colunas = 5

linha = 1

# Cria laço while normal para adicionar linhas
while linha <= qtd_linhas: 
    coluna = 1
    #Cria laço normal do while dentro de outro while que irá executar até que  
    #a expressão seja falsa e somente após isso voltará para o primeiro while(o que ele está dentro)
    while coluna <= qtd_colunas:
        print(f'{linha=}, {coluna=}')
        coluna += 1 
    linha += 1
    

print("Acabou")