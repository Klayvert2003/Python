"""
Tipo string
Em python um dado é considerado do tipo string quando:
Estiver na aspas simples -> 'Klayvert', '19 anos', 'alala', 'True', '4.3'
Estiver na aspas simples triplas -> '''Klayvert''', '''19 anos''', '''alala''', '''True''', '''4.3'''
Estiver na aspas duplas -> "Klayvert", "19 anos", "alala", "True", "4.3"
"""#Estiver na aspas duplas triplas -> """Klayvert""", """19 anos""", """alala""", """True"""", """4.3"""
"""
    local = "Gina's Bar"
    print(type(local), local)

    nome = 'Angelina \nJolie'
    print(nome)

    nome = 'Angelina Jolie'
    print('Maiúsculo:', nome.upper())
    print('Minúsculo:', nome.lower())
    print('Lista de Strings:', nome.split())

    print(nome[0:4])  #slice de string
    print(nome[5:15]) #slice de string

    print(nome.split()[0]) #Transforma em uma lista separada pelo espaço e seleciona o index da posição 0
    print(nome.split()[1]) #Transforma em uma lista separada pelo espaço e seleciona o index da posição 1
"""
#[ 0,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,  13,  14] 
#['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

nome = 'Geek University'

#Primeiro ':' comece do primeiro elemento. Segundo ':' va até o último. E o '-1' inverte a ordem.
print(nome[::-1])

#Faz a troca de todos os caracteres inseridos primeiro pelo segundo.
print(nome.replace('G', 'P'))

tomaluco = 'subino onibus'
print(tomaluco)
print(tomaluco[::-1])