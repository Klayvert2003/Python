frase = 'O python é uma linguagem de programação'\
    'multiparadigma'\
    'Python foi criado por Guido Van Rossum'.lower()

i = 0
qtd_aparece = 0
letra_mais_aparece = ''

while i < len(frase):
    letra_atual = frase[i]
    x = frase.count(letra_atual)

    if letra_atual == ' ':
        i += 1
        continue

    if qtd_aparece < x:
        qtd_aparece = x
        letra_mais_aparece = letra_atual
    i += 1

print('A letra que apareceu mais vezes foi: "' 
      f'{letra_mais_aparece}", e apareceu {qtd_aparece}x')