import pandas as pd
import numpy as np

# Criando DataFrame
df = pd.DataFrame({'user_id': [1,2,3,4,5,6,7,8,9,10,11], 
                    'acessos_app': [9, 34, None, None, 727, None, 1, 22, None, None, None],
                    'acessos_web': [None, 9899, 1, 19, 99, 102, None, None, 21, 87, None]})
# print(df)

# Adicionando coluna 'tem_app' junto de uma condição com numpy where onde se os valores da coluna escolhida forem
# maiores que zero ele retorna True, se não for, retorna False

df['tem_app'] = np.where(df.acessos_app > 0, True, False)

# print(df)
"""
    user_id  acessos_app  acessos_web  tem_app
0         1          9.0          NaN     True
1         2         34.0       9899.0     True
2         3          NaN          1.0    False
3         4          NaN         19.0    False
4         5        727.0         99.0     True
5         6          NaN        102.0    False
6         7          1.0          NaN     True
7         8         22.0          NaN     True
8         9          NaN         21.0    False
9        10          NaN         87.0    False
10       11          NaN          NaN    False
"""

# Adicionando coluna 'tem_web' junto de uma condição com numpy where onde se os valores da coluna escolhida forem
# maiores que zero ele retorna True, se não for, retorna False
df['tem_web'] = np.where(df.acessos_web > 0, True, False)
# print(df)
"""
    user_id  acessos_app  acessos_web  tem_app  tem_web
0         1          9.0          NaN     True    False
1         2         34.0       9899.0     True     True
2         3          NaN          1.0    False     True
3         4          NaN         19.0    False     True
4         5        727.0         99.0     True     True
5         6          NaN        102.0    False     True
6         7          1.0          NaN     True    False
7         8         22.0          NaN     True    False
8         9          NaN         21.0    False     True
9        10          NaN         87.0    False     True
10       11          NaN          NaN    False    False
"""

# Adicionando coluna 'app_e_web' junto de duas condições usando numpy where onde se os dois valores das colunas 
# escolhidas forem True é retornado True, se não, é retornado False

df['app_e_web'] = np.where((df.tem_app == True) & (df.tem_web == True), True, False)
# print(df)
"""
    user_id  acessos_app  acessos_web  tem_app  tem_web  app_e_web
0         1          9.0          NaN     True    False      False
1         2         34.0       9899.0     True     True       True
2         3          NaN          1.0    False     True      False
3         4          NaN         19.0    False     True      False
4         5        727.0         99.0     True     True       True
5         6          NaN        102.0    False     True      False
6         7          1.0          NaN     True    False      False
7         8         22.0          NaN     True    False      False
8         9          NaN         21.0    False     True      False
9        10          NaN         87.0    False     True      False
10       11          NaN          NaN    False    False      False
"""

# Adicionando coluna 'app_ou_web' junto de duas condições usando numpy where onde um dos dois valores das colunas 
# escolhidas forem True é retornado True, se não, é retornado False

df['app_ou_web'] = np.where((df.tem_app == True) | (df.tem_web == True), True, False)
# print(df)
"""
    user_id  acessos_app  acessos_web  tem_app  tem_web  app_e_web  app_ou_web
0         1          9.0          NaN     True    False      False        True
1         2         34.0       9899.0     True     True       True        True
2         3          NaN          1.0    False     True      False        True
3         4          NaN         19.0    False     True      False        True
4         5        727.0         99.0     True     True       True        True
5         6          NaN        102.0    False     True      False        True
6         7          1.0          NaN     True    False      False        True
7         8         22.0          NaN     True    False      False        True
8         9          NaN         21.0    False     True      False        True
9        10          NaN         87.0    False     True      False        True
10       11          NaN          NaN    False    False      False       False
"""