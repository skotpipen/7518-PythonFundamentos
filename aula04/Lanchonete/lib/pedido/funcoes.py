
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

    lanche = {"1" : ("X-Salada",3.50),
              "2" : ("X-Bacon",4.50),
              "3" : ("X-Tudo",6.00)}
    
    if pedido in lanche.keys():
        lista.append(lanche[pedido])


def mostrarPedido(pedido,lista):
    lista.sort()
    total = 0
    for item in lista:
        print(f"     -{item[0]}   ---- R$ {item[1]:.2f}")
        total = total + item[1]
    print(f"\n\nTotal a pagar: R$ {total:.2f}")



