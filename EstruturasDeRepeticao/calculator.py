from operations import Operations

while True:
    opcao = input('Digite qual operação deseja fazer: ([1]Soma, [2]Subtração, [3]Multiplicação ou [4]Divisão): ').lower()
    operacoes = [1, 2, 3, 4, 'soma', 'subtracao', 'subtração', 'multiplicacao', 'multiplicação', 'divisão', 'divisao']
    if opcao not in operacoes:
        print('Digite uma operação válida!!!')
        continue
    try:
        num1 = float(input('Digite o primeiro número da operação: \n'))
        num2 = float(input('Digite o segundo número da operação: \n'))
        Operations(opcao=opcao, num1=num1, num2=num2)
    except ValueError:
        print('Digite apenas números!!!')
        continue

    sair = input('Deseja sair do programa? [S]im ou [N]ão ').lower().startswith('s')
    if sair:
        break