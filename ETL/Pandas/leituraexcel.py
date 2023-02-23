import pandas as pd

acessos = pd.read_excel(r'~/workspace/Python/ETL/Pandas/compras_e_acessos.xlsx', sheet_name='acessos')
# print(acessos)

compras = pd.read_excel(r'~/workspace/Python/ETL/Pandas/compras_e_acessos.xlsx', sheet_name='compras')
# print(compras)

# EXEMPLO DE INNER JOIN COM INTERSECÇÃO

# inner_join = acessos.merge(compras, how='inner', on='user_id')
# print(inner_join)

# inner_join = acessos.merge(compras, how='right', on='user_id')
# print(inner_join)

# inner_join = acessos.merge(compras, how='left', on='user_id')
# print(inner_join)

# inner_join = acessos.merge(compras, how='outer', on='user_id')
# print(inner_join)


# EXEMPLO DE INNER JOIN SEM INTERSECÇÃO

# left_join = acessos.merge(compras, how='left', on='user_id', indicator=True)
# print(left_join)

# left_join = left_join[left_join._merge == 'left_only']
# print(left_join)

# right_join = acessos.merge(compras, how='right', on='user_id', indicator=True)
# print(left_join)

# right_join = right_join[right_join._merge == 'right_only']
# print(right_join)

# full_join = acessos.merge(compras, how='outer', on='user_id', indicator=True)
# print(left_join)

# full_join = full_join[full_join._merge != 'both']
# print(full_join)