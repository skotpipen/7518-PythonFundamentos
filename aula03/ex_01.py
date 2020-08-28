
## Funções

#1 - Funçoes Nativa

# print()
# input()
#max()

print("isso é uma função nativa da linguagem")

#2 - Funções a partir da Bibliotecas

import random

random.randint(0,10)


#3 - Funçoes definidas pelo usuario
def funcao_soma(num1, num2):
    return num1 + num2

res = soma(1,15)

#Variaveis imutaveis, sao passagem por valor (copia)
#Variaveis mutaveis, passagem por referencia, altera na origem

# strings, inteiros, booleanos, floats, listas

def func(nome):
    print(f'Olá! Meu nome é {nome}')

valor padrao

def soma1(num1,num2=0)
    return num1 + num2  # num2 é igual a 0 caso nao seja informado


print(soma1(3))

def soma_multipla(*args): #aceita multiplos paramentros
    print(args)

def exemplo_kwargs(**kwargs): # cria uma lista de dicionarios
    print(kwargs)







# funçoes anonimas




anonima = lambda x,y: x+y


anonima(4,5)  # respostas 9


