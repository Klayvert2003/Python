"""
Listas

Listas em Python funcionam como vetores ou matrizes, ou seja, arrays em outras linguagens
com a diferença de serem DINÂMICOS e também de podermos colocar QUALQUER tipo de dados

-Dinâmicos:pois não possui tamanho fixo; Ou seja, basta criar a lista e adicionar elementos;
Qualquer tipo de dado: Não possuem tipo de dado fixo: ou seja, podemos inserir qualquer tipo de dado
As listas em python são representadas por colchetes: []

# Podemos facilmente checar se determinado valor está contido na lista
# num = 7

# if num in lista4:
#     print(f"Encontrei o número {num}")
# else:
#     print(f"tem {num} aqui não")

# Podemos facilmente ordenar uma lista

# lista1.sort() #Ordenando a lista de int em ordem crescente
# print(lista1)

# lista5.sort() #Ordenando a lista por ordem alfabética e por ordem de caracter maiúsculo
# print(lista5)

# Podemos facilmente contar o número de ocorrências de um valor em uma lista
print(lista1.count(1))
print(lista5.count('e'))

# Adicionar elementos em uma lista

#Para adicionar elementos em uma lista, utilizamos a função append

print(lista1)
#Adicionando elementos com o append
#Só é possível adicionar UM elemento por vez, e coloca a lista como elemento único(sublista)
lista1.append(19191) 
lista5.append([' ', 'Di', 'Pietro','Hildebrand'])
print(lista5)

if [' ', 'Di', 'Pietro','Hildebrand'] in lista5:
    print("Encontrei os novos itens adicionados")
else:
    print("Não encontrei novos itens")

# Adiciona cada elemento da lista como valor adicional (dentro da lista original)
lista5.extend([' ', 'Di', 'Pietro','Hildebrand']) 
print(lista5)


# Podemos inserir um novo elemento na lista informando a posição do index
# Ao fazer isso ele é adicionado no index do valor antigo que estava nele (no caso substituiu o 98)
# OBSERVAÇÃO: O INSERT NÃO SUBSTITUI, APENAS COLOCA O VALOR ANTIGO A SUA DIREITA     

lista1.insert(3,222) # nome_lista.insert(index, valor_que_sera_inserido)
print(lista1)


# Juntando duas listas criando uma nova
# lista6 = lista1 + lista2

# Juntando duas listas já existentes: duas formas
# Forma 1:
# lista1.extend(lista2)

#Forma 2:
# lista1 += lista2
# print(lista1)


# Revertendo uma lista

# Forma 1:

# lista1.reverse()
# lista2.reverse()

# Forma 2:

# print(lista1[::-1])
# print(lista2[::-1])


# Copiando uma lista
lista6 = lista2.copy()
print(lista6)


# Contando quantos elementos a lista possui
print(len(lista5))


# Removendo o último elemento de uma lista
# OBS: O pop não somente remove o último elemento mas também o retorna

print(lista5)
lista5.pop()
print(lista5)

# Podemos remover um elemento pelo index
# Os elementos a direita do index removido serão deslocados para a esquerda
# OBS: Se não houver elementos no index informado o erro "index error" será retornado

print(lista5)
lista5.pop()
print(lista5)


# Removendo todos os itens da lista
print(lista5)
lista5.clear()
print(lista5)


# Podemos repetir elementos em uma lista apenas usando:

nova = [1, 2, 3, 4, 5]
print(nova)
nova *= 3
print(nova)



"""

lista1 = [1, 2, 67, 98, 120, 3, 19191, 123, 9, 1231321, 11111]

lista2 = ['K', 'l', 'a', 'y', 'v', 'e', 'r', 't']

lista3 = []

lista4 = list(range(11))

lista5 = list('Klayvert Alves')


# Podemos converter uma str para uma lista

# Exepmlo 1:

curso = "Básico ao avançado de Python"
print(curso)

# Variável str recebe ela mesmo com a função split, logo, é convertida para uma lista
curso = curso.split() 
print(curso)