import pandas as pd

df = pd.DataFrame({'product_id': [1,2,3,4,5,6,7,8,9,10], 
                    'name': [ 'camiseta', 'geladeira', 'fogao', 'dicionario', 'perfume', 
                    'microondas', 'tv', 'calça', 'meia', 'chuteira']})
# print(df)

# Utilizando pandas apply para definir as categorias dos produtos conforme condições inseridas nele
df['categoria'] = df['name'].apply(lambda x: 'eletrodomestico' if x in ['geladeira', 'fogao', 'tv', 'microondas'] 
                                            else('vestuario' if x in ['camiseta', 'calça', 'meia', 'chuteira']
                                            else('livro' if x in ['biblia', 'dicionario'] 
                                            else 'outros')))
print(df)
""" é retornado:
   product_id        name        categoria
0           1    camiseta        vestuario
1           2   geladeira  eletrodomestico
2           3       fogao  eletrodomestico
3           4  dicionario            livro
4           5     perfume           outros
5           6  microondas  eletrodomestico
6           7          tv  eletrodomestico
7           8       calça        vestuario
8           9        meia        vestuario
9          10    chuteira        vestuario
"""