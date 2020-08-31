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

# funcoes

def telaOpcoes():
    print("\n\n\n\n")
    print("- 1: X-Salada (R$ 3.50)")
    print("- 2: X-Bacon (R$ 4.50)")
    print("- 3: X-Tudo (R$ 6.00)")
    print("- 4: Mostrar Pedido")
    print("- 5: Sair")
    

def adicionaLanche(pedido,lista):

    lanche = {'1' : ("X-Salada",3.50),
              '2' : ("X-Bacon",4.50),
              '3' : ("X-Tudo",6.00)}
    
    if pedido in lanche.keys():
        lista.append(lanche[pedido])

def mostrarPedido(pedido,lista):
    lista.sort()
    total = 0
    for item in lista:
        print(f"     -{item[0]}   ---- R$ {item[1]:.2f}")
        total = total + item[1]
    print(f"\n\nTotal a pagar: R$ {total:.2f}")

def sair(*args):
    exit()




    


# Funcao Principal

def main():
    
    opcoes = {'1' : adicionaLanche,
              '2' : adicionaLanche,
              '3' : adicionaLanche,
              '4' : mostrarPedido,
              '5' : sair}
    

    lista = []

    while True:
        telaOpcoes()
        pedido = input("\n\n\nopção: ")

        if pedido in opcoes.keys():
            opcoes[pedido](pedido,lista)
        else:
            print("Opção inválida")






if __name__ == '__main__':
    main()
