def Operations(opcao, num1, num2):
    if opcao == 'soma' or opcao == 1:
        total = num1 + num2
        print(f'O valor da sua operação é {total}')
    elif opcao == 'subtracao' or opcao == 'subtração' or opcao == 2:
        total = num1 - num2
        print(f'O valor da sua operação é {total}')
    elif opcao == 'multiplicacao' or opcao == 'multiplicação' or opcao == 3:
        total = num1 * num2
        print(f'O valor da sua operação é {total}')
    elif opcao == 'divisao' or opcao == 'divisão' or opcao == 4:
        total = num1 / num2
        print(f'O valor da sua operação é {total}')