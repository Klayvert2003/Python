while True:
    sair = input('Deseja sair? [S/N] ')
    if sair.lower() == 's':
        break
    opcao = input('Digite qual operação deseja fazer: (soma, subtracao, multiplicacao ou divisao): ')
    if opcao.lower() != 'soma' and 'subtracao' and 'multiplicacao' and 'divisao':
        print('Digite uma opção válida!!!')
        continue
    
    num1 = float(input('Digite o primeiro número da operação: \n'))
    num2 = float(input('Digite o segundo número da operação: \n'))

    if opcao == 'soma':
        total = num1 + num2
        print(total)
    elif opcao == 'subtracao':
        total = num1 - num2
        print(total)
    elif opcao == 'multiplicacao':
        total = num1 * num2
        print(total)
    else:
        total = num1 / num2
        print(total)
