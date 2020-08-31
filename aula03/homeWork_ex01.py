#!/usr/bin/python3

"""
Crie um programa em python que peça ao usuário informar dois números, e depois
escolha as seguintes opções:

    1- Soma
    2- Subtração
    3- Divisao
    4- Multiplicação
    5- Sair
    

De acordo com a opção executar a operação com os números informados.

Cada operação deverá ser armazenada em uma função.

"""


"""
Transformar o exercício da lanchonete aplicando a modularização de acordo
com o modelo contido no padrao_script.py 

main: menu e direcionamentos

criar:
    uma função para funcionalidade:
        1- adicionar o lanche
        2- mostrar pedido
        3- consolidar total

"""

## Imports


## Constantes

## Funcoes

def soma(n1,n2):
    return n1 + n2

def subtracao(n1,n2):
    return n1 - n2

def multiplicacao(n1,n2):
    return n1 * n2

def divisao(n1,n2):
    if n2 != 0:
        return n1 / n2
    else:
        return "Não existe divisão por ZERO"

def sair(*args):
    exit()


# Funcao Principal

def main():
    operacoes = {'1': soma,
                 '2': subtracao,
                 '3': multiplicacao,
                 '4': divisao,
                 '5': sair}

    while True:
        print ("\n\nDigite 2 números: ")
        n1 = float(input("\nPrimeiro Número: "))
        n2 = float(input("\nSegundo Número: "))


        operacao = input(f"\n\nDigite a operação desejada:\n"
                         f"1 - Soma \n"
                         f"2 - Subtração \n"
                         f"3 - Multiplicação \n"          
                         f"4 - Divisão \n"
                         f"5 - Sair\n")

        if operacao in operacoes.keys():
            print(operacoes[operacao](n1,n2),"\n\n\n")
        else:
            print("Opção Invalida\n\n\n")

if __name__ == '__main__':
    main()









