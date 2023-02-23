"""
Definição de dicionário: é um objeto que representa a coleção de um ou mais objetos. 
Cada objeto tem sua chave e seu valor. 
Assim, para acessar um valor de um determinado objeto, basta chamarmos sua chave.
Os dicionários são iniciados e terminados por chaves {}

Criando dicionários
"""

dict1 = {'chave1': 'valor1', 'chave2': 'valor2'}

# print(dict1)

dict2 = dict(a = 1, b = 2, c = 'c', d = 'd')

# print(dict2)

dict3 = dict([('a', 1), ('b', 2), ('c', 3)])
# print(dict3)

dict4 = {'chave1': ['valor1', 2, 3], 'chave2': [2, 'idade', 'nome']}
# print(dict4)

dict5 = {'id': [1, 2, 3], 'user': {'nome': ['Klayvert', 'José', 'Fernando'], 'idade': [29, 30, 50]}}
# print(dict5)

dict6 = dict(zip(['chave1', 'chave2', 'chave3'], ['valor1', 'valor2', 'valor3']))
# print(dict6)

dict7 = dict({'nomes': ('Caio', 'João'), 'idade': (29, 30)})
# print(dict7)

"""
Adicionando valores do dicionários
"""

# print(dict1['chave1'])

# print(dict1.get('chave2'))

# print(dict1.get('chave3', 'NÃO EXISTE ESSA CHAVE!!!!!!!'))

# print(list(dict1)[0])
# print(dict1.get(list(dict1)[0]))

# for chave in dict1.keys():
#     print(chave, dict1[chave])

# for chave, valor in dict1.items():
#     print(chave, valor)

"""
Juntando dicionários
"""

# dict1.update(dict2)
# print(dict1)

# dict1['NOVA CHAVE'] = 1000
# print(dict1)

# dict1.update({'OUTRA CHAVE': 'OUTRO VALOR'})
# print(dict1)

# print({**dict2, **dict3})
# Quando os valores são iguais ele não duplica, apenas sobrepõe


# Verificando se um valor pertence a chave
# print(1 == dict3['a'])
# print(dict3)
# dict3.clear() #esvazia o dicionário
# print(dict3)


# Criando cópia de um dicionarío já existente
# dictcopy = dict3.copy()
# print(dictcopy)

# Removendo itens do dicionários
# print(dict4)
# print(dict4.pop('chave1'))
# print(dict4)

# print(dict6)
# print(dict6.popitem())
# print(dict6)