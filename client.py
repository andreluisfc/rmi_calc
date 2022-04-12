import Pyro4
from past.builtins import raw_input
from sys import exit

try:
    calculadora = Pyro4.Proxy("PYRONAME:calculadora")
    operacoes = [
                    [1, 'soma', calculadora.somar],
                    [2, 'subtracao', calculadora.subtrair],
                    [3, 'divisao', calculadora.dividir],
                    [4, 'multiplicacao', calculadora.multiplicar],
                    [0, 'sair', exit]
                 ]

    while True:
        num_a = int(raw_input('Informe o primeiro numero: '))
        num_b = int(raw_input('Informe o segundo numero: '))
        print('Informe a operacao a realizar')
        for op in operacoes:
            print(f'{str(op[0])} - {op[1]}')

        escolha = raw_input('escolha: ')

        if int(escolha) == 0:
            exit(0)

        for op in operacoes:
            if int(escolha) == op[0]:
                print(f'O resultado da sua {op[1]} foi {op[2](num_a, num_b)}')

        print('')

except ConnectionRefusedError as e:
    raise f'Erro ao obter classe de servidor RMI. ({e})'
except Exception as e:
    raise e


