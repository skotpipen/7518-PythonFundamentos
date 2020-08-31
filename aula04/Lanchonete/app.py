#!/usr/bin/python3

## Imports
from lib import pedido as fazpedido

## Constantes

# funcoes

def sair(*args):
    exit()


# Funcao Principal

def main():
    opcoes = {'1' : fazpedido.adicionaLanche,
              '2' : fazpedido.adicionaLanche,
              '3' : fazpedido.adicionaLanche,
              '4' : fazpedido.mostrarPedido,
              '5' : sair}
    

    lista = []
    while True:
        fazpedido.telaOpcoes()
        pedidos = input("\n\n\nopção: ")

        if pedidos in opcoes.keys():
            opcoes[pedidos](pedidos,lista)
        else:
            print("Opção inválida")


if __name__ == "__main__":
    main()
