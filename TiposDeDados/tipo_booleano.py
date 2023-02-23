#Tipo booleano.
#Duas constantes, Verdadeiro(True) e Falso(False).
#OBS: Sempre com a inicial maiúscula.
#Errado true, TRUE, false, FALSE.
#Certo True e False(serve pra None também).

ativo = True
print(ativo)

#Operações básicas.

#Negação (not).
#Observação: fazendo a negação, o valor booleano sempre será o contrário do que era antes.


print(not ativo)

logado = False

#Ou (or).
#É uma operação binária, ou seja, depende de dois valores. Ou um ou outro devem ser True.
#O retorno só é False quando ambas condições são False.
#True or True = True
#True or False = True
#False or True = True
#False or False = False

print(ativo or logado)

#E (and).
#É uma operação binária, ou seja, depende de dois valores.
#O retorno só é True quando ambas condições são True.
#True or True = True
#True or False = False
#False or True = False
#False or False = False

logado1 = True
logado2 = True

print(logado1 and logado2)