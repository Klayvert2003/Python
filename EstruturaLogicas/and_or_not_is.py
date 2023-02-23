"""
Estruturas Lógicas:
and(e), or(ou), not(n]ao, ou negação), is(é)
Operadores unários:
    - not, is

Operadores binários
    - and, or
"""

ativo = True
logado = True
"""
if ativo and logado: #Se ativo E logado for True
    print("Bem vindo usuário!")
else: 
    print("Você precisa ativar sua conta.")
if not ativo: #Se NÃO está ativo então:
    print("Você precisa ativar sua conta.")
else:
    print("Bem vindo usuário!")
if logado is False: #Se logado É falso, então:
    print("Você precisa ativar sua conta")
else:
    print("Bem vindo usuário")
"""

#Significado -> Ativo é verdadeiro?
print(ativo is True)