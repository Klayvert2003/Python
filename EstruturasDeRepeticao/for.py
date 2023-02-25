"""
Loop For

loop -> estrutura de repetição
For -> uma dessas estruturas

Python for item in interavel:
    //execução do loop

utilizamos loops para iterar sobre sequências ou sobre valores iteráveis
- String
    nome = 'Klayvert Alves'
- Lista 
    lista = [1, 3, 5, 7, 9]
-Range
    numeros = range[1,10]
"""
"""
nome = 'Klayvert Alves'
lista = [1, 3, 5, 7, 9]
numeros = range(1,10) # Temos que transformar em uma lista

#Exemplo de for 1)
for letra in nome:
    print(letra)

#Exemplo de for 2(iterando sobre uma lista)
for numero in lista:
    print(numero)

#Exemplo de for 3 (iterando sobre um range)

range(valor_inicial, valor_final)

OBS: o valor_final não é incluso.
1
2
3
4
5
6
7
8
9
10 - Não

nome = 'Klayvert Alves'
lista = [1, 3, 5, 7, 9]
numeros = range(1,10) # Temos que transformar em uma lista

for numero in range(1, 10):
    print(numero)


Enumerate:
((0, 'G'), (1, 'e'), (2, 'e'), (3, 'k'), (4, ' ')

#Quando não precisamos de um valor, podemos descartá-lo usando o underline '_'
for _, letra in enumerate(nome):
    print(letra)


#Ao usar desta forma, o programa imprime os indices e a qual valor eles pertencem
for valor in enumerate(nome):
    print(valor)

#Ao usar desta forma, o programa imprime apenas os indices(posição de cada valor(no caso as letras))
for valor in enumerate(nome):
    print(valor[0])

#Ao usar desta forma, o programa imprime apenas os valores(no caso as letras)
for valor in enumerate(nome):
    print(valor[1])


qtde = int(input("Quantas vezes o programa deve dizer oi? "))
soma = 0

# for n in range(1, qtde + 1):
#     print(f"Imprimindo {n}º Olá!")

#Deixamos qtde + 1 pra pegar o valor correto que o usuário deseja pegar
for n in range(1, qtde + 1): #pois por conta do indice é sempre um número a menos do inserido
    num = int(input(f'Informe o {n}/{qtde} valor: '))
    soma = soma + num
print(f"A soma é: {soma}")

nome = 'Klayvert Alves'

for letra in nome:
    print(letra, end='') #Desta forma ele printa as letras uma na frente da outra, não pulando linha.
"""
#Unicode original: U+1F605
#Modificado: \U0001F605 (necessário adicionar três zeros no lugar do '+' e uma barra '\' antes de tudo)

emoji = '\U0001F605' #Sempre guardar o emoji unicode com uma barra antes para ser reconhecido

for _ in range(3): #Fazendo ele repetir três vezes apenas, sem uso de uma variável específica
    for num in range(1, 11): #Enquanto estiver dentro do range do indice um ele irá imprimir 10 vezes(11 -1)
        print(emoji * num)