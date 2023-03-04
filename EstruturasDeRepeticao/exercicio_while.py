nome = 'Klayvert Alves'
novo_nome = ''

posicao = 0

# for i in range(0, 14):
#     novo_nome += f'*{nome[i]}*'
#     print(novo_nome)

while posicao < len(nome):
    letra = nome[posicao]
    novo_nome += f'*{letra}'
    posicao += 1

print(novo_nome)