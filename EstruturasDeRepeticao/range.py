"""
Ranges

- Precisamos conhecer o looping for para usar os ranges
- Precisamos conhecer o range para trabalhar melhor com um loop for

Ranges são utilizados para gerar sequências numéricas, não de forma aleatória.
mas sim de maneira especificada

Formas gerais:

# Forma 1

range(valor_de_parada)

OBS: valor_de_parada não incluso (inicio padrão 0 e passo de 1 em 1)

Exemplo Forma 1:
for num in range(11):
    print(num)


# Forma 2

range(valor_de_inicio, valor_de_parada)

OBS: valor_de_parada não incluso (inicio especificado pelo usuário, e passo de 1 em 1)

Exemplo Forma 2:
for num in range(4, 11):
    print(num)


# Forma 3

range(valor_de_inicio, valor_final, passo)

OBS: valor_de_parada não incluso (inicio especificado pelo usuário, e passo especificado pelo usuário)

Exemplo Forma 3:
#Primeira casa do range (valor inicial{indice}). Segunda casa (até onde vai{máximo}).
for num in range(5, 55, 5): #Terceira casa (de quanto em quanto vai{passo})
    print(num)


# Forma 4 (inversa)

range(valor_de_inicio, valor_final, passo)

OBS: valor_final não incluso (inicio especificado pelo usuário, e passo especificado pelo usuário)

Exemplo Forma 4:
#Primeira casa do range (valor inicial{indice}). Segunda casa (até onde vai{máximo}).
for num in range(10, 0, -1): #Terceira casa (de quanto em quanto vai{passo})
    print(num)
"""



