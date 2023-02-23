# Definição de DataFrame: é um objeto bidimensional que contém dados em forma tabular. 
# Ou seja, como uma tabela do excel.
# é possível também adicionar linhas e colunas

import pandas as pd

# Criando DataFrame
df1 = pd.DataFrame()

#dict1 = {'identificacao': [1, 2, 3, 4, 5], 'nome': ['Caio', 'Rodrigo', 'Klayvert', 'José', 'Gabriel']}
dict1 = {'identificacao': [1, 2, 3, 4, 5], 'nome': ['Caio', 'Rodrigo', 'Klayvert', 'José', 'Gabriel']}

df2 = pd.DataFrame(data = dict1)
# print(df2)

df3 = pd.DataFrame(data = dict1, index = [29, 1, 0, 2222, 88]) #Adicionando o campo index no dataframe
# print(df3)

serie1 = pd.Series([1, 2, 3]) # Criando tabela simples de inteiros com pd.Series
# print(serie1)
serie2 = pd.Series(['a', 'b', 'c']) # Criando tabela simples de strings com pd.Series

df4 = pd.DataFrame({'coluna1': serie1, 'coluna2': serie2})
# print(df4)

import numpy as np

# Criando array utilizando biblioteca numpy
array1 = np.array([[1, 2, 3], ['São Paulo', 'Rio de Janeiro', 'Campinas'], ['SP', 'RJ', 'SP']])
#print(array1)

np.ndarray

# df5 = pd.DataFrame(data = array1.transpose() , index = ['linha1', 'linha2', 'linha3'], columns = ['identificacao', 'cidade', 'estado'])
df5 = pd.DataFrame(data = array1.transpose() , index = ['linha1', 'linha2', 'linha3'], columns = ['identificacao', 'cidade', 'estado'])
#print(df5)

matriz1 = np.matrix([[1, 2, 3], ['São Paulo', 'Rio de Janeiro', 'Campinas'], ['SP', 'RJ', 'SP']])

np.matrix
df6 = pd.DataFrame(data = matriz1.transpose() , index = ['linha1', 'linha2', 'linha3'], columns = ['identificacao', 'cidade', 'estado'])
# print(df6)

"""
Selecionando DataFrames
"""

# Criando nova coluna
df3['identificacao_mais_5'] = df3['identificacao'] + 5
# print(df3)

df3['index'] = 0

df3.index = [29, 0, 1, 2222, 88]
# print(df3)
# print(df3['nome'])
# print(df3.nome)

# print(df3.index)
# print(df3['index']) # Utilizar desta forma pra selecionar é mais útil!

# print(df3[df3.identificacao % 2 == 0])# Selecionando linhas conforme a lógica

#print(df3[df3.nome.str.contains('y') | (df3.identificacao == 5)])# Selecionando linhas conforme a lógica

"""
loc: localizar pelo NOME dos index ou columns
iloc: localizar pela POSIÇÃO dos index ou columns
"""
# print(df3)
# print(df3.loc[0])
# print(df3.iloc[0])

# print(df3.loc[0:1])
# print(df3.iloc[0:2])

# print(df3.loc[88:1:-1])
# print(df3.loc[:, 'nome'])

# print(df3.iloc[:, 1]) Buscando a coluna do dataframe pelo index de campo 1 (no caso o campo 'nome')

# print(df3.loc[1, 'nome']) 

# print(df3.iloc[2, 1])

# df3.loc[1, 'nome'] = 'Klayvert2' # Mudando valor do campo nome
# print(df3)

# print(df3.iloc[-1, -2])
# print(df3.loc[[88, 1]]) # criando lista dentro do dataframe e colocando o valor dos index que queremos selecionar
# print(df3.iloc[[1, 3]]) # criando lista dentro do dataframe e colocando os index que queremos selecionar

"""
Atributos do DataFrame
"""

# print(df3.dtypes) # Mostrando os tipos de dados do DataFrame(int, string, float, etc)
# df3.identificacao = df3.identificacao.astype(str) # Convertendo dados do DataFrame
# print(df3.dtypes)

# Valores nulos no DataFrame aparecem como NaN, logo, sua coluna é do tipo float
df3['teste1'] = [None, 2, 4, None, 10]

# Usando df3.columns para alterar nome da coluna index
# Colunas antigas eram ['identificacao', 'nome', 'identificacao_mais_5', 'index', 'teste1']
df3.columns = ['identificacao', 'nome', 'identificacao_mais_5', 'index_MODIFIED', 'teste1']
# print(df3)

# Usando df3.index para alterar valor do index
# Index antigos eram [29, 0, 1, 2222, 88]
# df3.index = [29, 0, 1, 40028922, 88]
# print(df3)

# print(df3.shape) # Mostra a quantidade de linhas e colunas respectivamente do DataFrame
# Saída = (5, 5) Significa que tem 5 linhas e 5 colunas no caso

# print(df3.values) # df3.values traz os valores das linhas(listas) do DataFrame em forma de np array

"""
Métodos:
Combine_first
"""

# print(df3)
"""
      identificacao      nome  identificacao_mais_5  index  teste1
29                1      Caio                     6      0     NaN
0                 2   Rodrigo                     7      0     2.0
1                 3  Klayvert                     8      0     4.0
2222              4      José                     9      0     NaN
88                5   Gabriel                    10      0    10.0"""

# Retornando valores de teste1 pra quando forem nulos traga os valores na coluna identificacao_mais_5
# print(df3.teste1.combine_first(df3['identificacao_mais_5']))
""" Output
29       6.0
0        2.0
1        4.0
2222     9.0
88      10.0
Name: teste1, dtype: float64
"""

# Método copy: Copia um DataFrame

df1000 = df3.copy()
# print(df1000)

# # Método count

# print(df1000.count())
""" Traz a quantidade de registros não nulos das colunas
identificacao           5
nome                    5
identificacao_mais_5    5
index                   5
teste1                  3
dtype: int64
"""

# Usando drop para remover uma coluna: 1º Forma
# print(df3)
"""
      identificacao      nome  identificacao_mais_5  index_MODIFIED  teste1
29                1      Caio                     6               0     NaN
0                 2   Rodrigo                     7               0     2.0
1                 3  Klayvert                     8               0     4.0
2222              4      José                     9               0     NaN
88                5   Gabriel                    10               0    10.0
"""
# df3 = df3.drop(columns = ['index_MODIFIED'])
# print(df3)
"""      identificacao      nome  identificacao_mais_5  teste1
29                1      Caio                     6     NaN
0                 2   Rodrigo                     7     2.0
1                 3  Klayvert                     8     4.0
2222              4      José                     9     NaN
88                5   Gabriel                    10    10.0"""

# Usando drop para remover uma coluna: 2º Forma
# df3.drop(columns = ['index_MODIFIED'], inplace=True)
# print(df3)
"""      identificacao      nome  identificacao_mais_5  teste1
29                1      Caio                     6     NaN
0                 2   Rodrigo                     7     2.0
1                 3  Klayvert                     8     4.0
2222              4      José                     9     NaN
88                5   Gabriel                    10    10.0"""

# df3.drop(index = [88], inplace=True) # Usando drop para remover um index:
# print(df3)

# Usando método drop_duplicates

df7 = pd.concat([df1000, df1000])
# print(df7)
"""   identificacao      nome  identificacao_mais_5  index_MODIFIED  teste1
29                1      Caio                     6               0     NaN
0                 2   Rodrigo                     7               0     2.0
1                 3  Klayvert                     8               0     4.0
2222              4      José                     9               0     NaN
88                5   Gabriel                    10               0    10.0
29                1      Caio                     6               0     NaN
0                 2   Rodrigo                     7               0     2.0
1                 3  Klayvert                     8               0     4.0
2222              4      José                     9               0     NaN
88                5   Gabriel                    10               0    10.0
"""

df7.drop_duplicates(inplace=True)
# print(df7)
"""
      identificacao      nome  identificacao_mais_5  index_MODIFIED  teste1
29                1      Caio                     6               0     NaN
0                 2   Rodrigo                     7               0     2.0
1                 3  Klayvert                     8               0     4.0
2222              4      José                     9               0     NaN
88                5   Gabriel                    10               0    10.0
"""

# Método dropna

df8 = df7.copy()
# print(df8)
"""
      identificacao      nome  identificacao_mais_5  index_MODIFIED  teste1
29                1      Caio                     6               0     NaN
0                 2   Rodrigo                     7               0     2.0
1                 3  Klayvert                     8               0     4.0
2222              4      José                     9               0     NaN
88                5   Gabriel                    10               0    10.0
29                1      Caio                     6               0     NaN
0                 2   Rodrigo                     7               0     2.0
1                 3  Klayvert                     8               0     4.0
2222              4      José                     9               0     NaN
88                5   Gabriel                    10               0    10.0
"""

# df8.dropna(inplace=True)
# print(df8)
"""
    identificacao      nome  identificacao_mais_5  index_MODIFIED  teste1
0               2   Rodrigo                     7               0     2.0
1               3  Klayvert                     8               0     4.0
88              5   Gabriel                    10               0    10.0
"""

# Método fillna

# print(df7)
""" Como estava antes do fillna
      identificacao      nome  identificacao_mais_5  index_MODIFIED  teste1
29                1      Caio                     6               0     NaN
0                 2   Rodrigo                     7               0     2.0
1                 3  Klayvert                     8               0     4.0
2222              4      José                     9               0     NaN
88                5   Gabriel                    10               0    10.0
"""

# df7.identificacao.fillna('NULL', inplace=True) # Substituindo valores nulos de apenas uma coluna
# df7.fillna('NULL', inplace=True) # Substituir valores nulos do DataFrame todo
# print(df7)
""" output
      identificacao      nome  identificacao_mais_5  index_MODIFIED teste1
29                1      Caio                     6               0   NULL
0                 2   Rodrigo                     7               0    2.0
1                 3  Klayvert                     8               0    4.0
2222              4      José                     9               0   NULL
88                5   Gabriel                    10               0   10.0
"""

# Método Head: é utilizado pra retornar as primeiras linhas (passando por parâmetro) 

# print(df7.head(2))

# # Método Tail: é utilizado pra retornar as ultimas linhas (passando por parâmetro) 
# print(df7.tail(2))

# df10 = pd.concat([df7, df7]) 
# Traz as linhas de forma agrupada(que nem em SQL) e utilizando 
# sum() para somar o valor da coluna identificacao_mais_5 onde há registros iguais 
# print(df10.groupby(['nome']).identificacao_mais_5.sum())
"""output
nome
Caio        12
Gabriel     20
José        18
Klayvert    16
Rodrigo     14
Name: identificacao_mais_5, dtype: int64
"""
#df3   =  identificacao      nome  identificacao_mais_5  index_MODIFIED  teste1
"""29                 1      Caio                     6               0     NaN
    0                 2   Rodrigo                     7               0     2.0
    1                 3  Klayvert                     8               0     4.0
    2222              4      José                     9               0     NaN
    88                5   Gabriel                    10               0    10.0"""

# Utilizando isin (utilizado também para slice)

# print(df3.isin([2, 4])) # Traz como True se caso o que coloquei como parâmetro existir
"""
      identificacao   nome  identificacao_mais_5  index_MODIFIED  teste1
29            False  False                 False           False   False
0              True  False                 False           False    True
1             False  False                 False           False    True
2222           True  False                 False           False   False
88            False  False                 False           False   False
"""

# Traz como True se caso o que coloquei como parâmetro existir
# print(df3[df3.nome.isin(['Caio', 'Klayvert'])] == True)

# Operações:

# Valor mínimo das colunas
# print(df3.identificacao_mais_5.min())


# Valor máximo das colunas
# print(df3.identificacao_mais_5.max())

# Valor da média das colunas
# print(df3.identificacao_mais_5.mean())

# Valor mediano das colunas
# print(df3.identificacao_mais_5.median())

# Valor da soma das colunas
# print(df3.identificacao_mais_5.sum()) # para numeros soma

# Concatenando strings com sum()
# print(df3.nome.sum())

# Traz o valor ddo desvio padrão das colunas
# print(df3.identificacao_mais_5.std())

# Método notnull

# Verificando quais valores da coluna teste1 são nulos
# print(df3.teste1.notnull())
"""
29      False Null
0        True
1        True
2222    False Null
88       True
Name: teste1, dtype: bool
"""

# Trazendo apenas os valores não nulos
# print(df3[df3.teste1.notnull() == True])

# Método rename (renomear colunas, campos etc)

# Alterando nome da coluna 'nome' para 'Nome'
# ATENÇÃO: deve ser passado a coluna ou index como dicionário ao usar o replace

# df3.rename(columns={'nome': 'Nome'}, inplace=True)
# print(df3)

# df3.rename(index={2222: 40028922}, inplace=True)
# print(df3)

# Alterando string usando replace no nome 'Klayvert' para 'Klayvert2'
# print(df3.nome.replace('Klayvert', 'Klayvert2'))

#Método round

# df3['teste2'] = [1.222, 4.5, 6.70100, 11.9000, 21321.221312]
# print(df3)

# Mudando casas decimais depois da vírgula com round()
# print(df3.teste2.round(0))
# print(df3.teste2.round(1))

# Método to_clipboard() para copiar para a área de transferência(não funciona no linux)
# print(df3.to_clipboard())

