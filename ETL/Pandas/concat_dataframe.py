import pandas as pd

df_1 = pd.DataFrame({"nome": ["Caio", "José", "Rodrigo", "Endriw"], 
                     "idade": [28, 45, 27, 16]})
# print(df_1)

df_2 = pd.DataFrame({"nome": ["Caio", "Mariane", "Maria"], 
                     "idade": [28, 29, 59]})
# print(df_2)

# Concatenando dois DataFrames e mostrando registros duplicados
df = pd.concat([df_1, df_2], ignore_index=True)
# print(df)

df.reset_index(drop=True, inplace=True)
# print(df)

# Concatenando dois DataFrames e mostrando só registros não duplicados
DF = pd.concat([df_1, df_2]).drop_duplicates().reset_index(drop=True)
# print(DF)