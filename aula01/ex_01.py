#!/usr/bin/python3

## shebang! <- Shell bang

# isto é um comentário

jujuba = 10
taxa_juros = 3.10 # flutuantes
alfanumerico = "10" # string <> texto


# Operadores Aritimeticos
num1 = 5.50
num2 = 4.85

### Operações

## Soma
soma = num1 + num2

## subtração
sub = num1 - num2

## Multiplicacao
multi = num1 * num2

## Divisao
div = num1 / num2

## Chao (floor)
res = 5 // 2 # 2

## resto da divisão
resto = 5 % 2 # 1

## Exponenciação

exp = 2 ** 2 ** 3 # Ordem resolução da direita para esquerda


### Booleanos

estou_ao _vivo = True
aula_terminou - False

## Comparação

## > < == != <= >=

## 0 < x < 5

## peradores logicos

or -> "maleavel"

x = 5
print (x > 2 or x > 10)

print (x > 2 and x > 10)

print(not x > 2) # inverte a relação booleana - se é falso fica true)



### String

frases = "Ola, tudo bem"
mesma_coisa = "Ola, tudo bem"

frases.replace(' ','x') # substitui os espaçoes em branco com x

id(frases)

## Strings sao dados imutaveis-

frases[0] # resposta O
frases[2] # resposta a
frases[0:3] # resposta Ola - ele mostra de 0 ate 2 - a virgula é excluida

frases[-1] # resposta m
frases[:-1] # resposta Ola, tudo be


# no interpretador coloca help(print) mostra as opções do comando print

print (frases,'sim') # mostra Ola, tudo bem sim

print (frases,'sim', sep='-') 


#entrada de dados

nome = input ('Digite seu nome')
print (nome)

# toda entrada de inpuit é uma string e deve ser convertida para numero caso necessario

num = int(input('Digitte um numero'))













