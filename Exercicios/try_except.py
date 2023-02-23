"""
Aula de try - except

Tratando exceção sem try except
# if numero_str.isdigit():
#     numero_str_float = float(numero_str)
#     print(f'O dobro de {numero_str} é {numero_str_float * 2:.2f}')
# else:
#     print('Digite um número inteiro')

"""


numero_str = input('Vou dobrar o número que você digitar! ')

try:
    print('String:', numero_str)
    numero_str_float = float(numero_str)
    print('Float', numero_str_float)
    print(f'O dobro de {numero_str} é {numero_str_float * 2:.2f}')
except:
    print('Não é um número')