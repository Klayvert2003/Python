#Tipos numéricos Float trabalham com casa decimais
#separados por ponto(.) e não Vírgula(,)

#Forma Incorreta
valor = 1,44 # Isso é uma tupla (por conta da vírgula)
print(type(valor), valor)

#Forma Correta
valor = 1.44 # Isso é um float (por conta do ponto)
print(type(valor), valor)

#É possível passar dois valores sequenciais a duas variáveis diferentes(dupla atribuição)
valor1, valor2 = 1, 44
print(type(valor1), valor1)
print(type(valor2), valor2)

#Convertendo float pra int(aproxima o valor por conta de ser um inteiro e não mais um float)
res = int(valor)
print(res)
print(type(res))

#Trabalhando com números complexos
num_complexo = 5j
print(type(num_complexo), num_complexo)

#Elevando a dois
print(num_complexo ** 2) 

