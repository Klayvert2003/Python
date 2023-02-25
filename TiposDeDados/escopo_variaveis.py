"""
Escopo de variáveis

Dois casos de escopo:
1 - Variáveis globais: são reconhecidas, ou seja, seu escopo compreende todo o programa
2 - Variáveis locais:  são reconhecidas apenas no bloco onde foram declaradas
    ou seja, seu escopo está limitado ao bloco no qual foi declarada

Para declarar variáveis em Python, fazemos:
nome_variavel = valor_variavel

Python é uma linguagem de tipagem dinâmica, siginifica que, ao declarar uma variável não é 
necessário colocar o tipo do dado. Este tipo é inferido ao atribuirmos o valor a mesma.
(Se vira pra descobrir o tipo da variável e você pode inserir tipos de dados diferentes na mesma variável)

Exemplo em C:
int numero = 42;

Exemplo em Java
int numero = 42;
"""

NUMERO = 42 # Exemplo de variável global

if NUMERO > 10:
    novo = NUMERO + 10 # Variável 'novo' é local, pois se não entrar na condição a mesma não será criada
    print(novo)

#Caso a variável 'numero' não entre na condição acima, a variável 'novo' não é criada.
#logo, não podemos utilizá-la
print(novo)  