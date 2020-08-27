###
### While
###

"""
Criem um menu interativo que contenha as seguintes opções:

   - 1: X-Salada (3.50)
   - 2: X-Bacon (4.50)
   - 3: X-Tudo (6.00)
   - 4: Mostrar Pedido
   - 5: Sair

A cada vez que a pessoa escolher algum lanche, ele deverá ser adicionado ao pedido;
Caso o usuário escolher a opção 4, deverá apresentar a lista de itens escolhidos

Ao digitar 5, o programa deve ser encerrado

"""


###
### for
###

"""
Aproveitando o exercício do menu, implemente:

    - A somatória do pedido

"""


lista = []
while True:
    
    print("\n\n\n\n")
    print("- 1: X-Salada (R$ 3.50)")
    print("- 2: X-Bacon (R$ 4.50)")
    print("- 3: X-Tudo (R$ 6.00)")
    print("- 4: Mostrar Pedido")
    print("- 5: Sair")
    
    pedido = int(input("\n\n\nopção: "))
    
    if pedido == 1:
        print(" X-Salada (R$ 3.50) adicionado a lista")
        lista.append(["X-Salada",3.50])
    elif pedido == 2:
        print(" X-Bacon (R$ 4.50) adicionado a lista")
        lista.append(["X-Bacon",4.50])
    elif pedido == 3:
        print(" X-Tudo (R$ 6.00) adicionado a lista")
        lista.append(["X-Tudo",6])
    elif pedido == 4:
        print(" Total em pedidos: ")
        lista.sort()
        total = 0
        for item in lista:
            print(f"    - {item[0]}  ---- R$ {item[1]:.2f}")
            total = total + item[1]
        print(f" Total a pagar: R$ {total:.2f}")
    elif pedido == 5:
        break
    






