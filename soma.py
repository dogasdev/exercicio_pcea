import math

n1 = float(input('Insira o primeiro valor: '))
n2 = float(input('Insira o segundo valor: '))

print('''Escolha a operação desejada:
1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão
5 - Potência (n²)
6 - Raiz quadrada
''')

opcao = int(input('Insira a operação desejada: '))

match opcao:
    case 1:
        print('SOMA')  
        soma = n1 + n2
        print(f'{n1} + {n2} = {soma}')
    case 2:
        print('SUBTRAÇÃO')
        sub = n1 - n2
        print(f'{n1} - {n2} = {sub}')
    case 3:
        print('MULTIPLICAÇÃO')
        multi = n1 * n2
        print(f'{n1} x {n2} = {multi}')
    case 4:
        print('DIVISÃO')
        if n2 != 0:
            div = n1 / n2
            print(f'{n1} ÷ {n2} = {div}')
        else:
            print('Erro: divisão por zero!')
    case 5:
        print('POTÊNCIA (ao quadrado)')
        potencia_n1 = math.pow(n1, 2)
        potencia_n2 = math.pow(n2, 2)
        print(f'{n1}² = {potencia_n1}')
        print(f'{n2}² = {potencia_n2}')
    case 6:
        print('RAIZ QUADRADA')
        if n1 >= 0:
            raiz_n1 = math.sqrt(n1)
            print(f'√{n1} = {raiz_n1}')
        else:
            print(f'Não é possível tirar a raiz quadrada de {n1}')
        if n2 >= 0:
            raiz_n2 = math.sqrt(n2)
            print(f'√{n2} = {raiz_n2}')
        else:
            print(f'Não é possível tirar a raiz quadrada de {n2}')
    case _:
        print('Opção inválida!')
