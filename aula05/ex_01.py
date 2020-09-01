# Arquivos


## Abertura de arquivos com a função open()

arquivo = open('arquivo.txt','r') # Abre o arquivo no modo leitura

arquivo = open('arquivo.txt','w') # abre o arquivo no modo escrita, sobrescrevendo o arquivo (truncate)

arquivo = open('arquivo.txt','x') # Cria o arquivo no modo escrita, caso exista ele da erro

arquivo = open('arquivo.txt','a') # Abre o arquivo no modo escrita e adciona o conteudo no fim do arquivo


conteudo = arquivo.read() # Le o arquivo como um todo
conteudo = arquivo.readline(1000)  # Lê um arquivo como um todo (ou até o limite de 1000 linhas) e tranforma em uma string   

conteudo = arquivo.readlines() # Le o arquivo e coloca dentro de uma lista 


# 1 abertura do arquivo para leitura
# 2 carrega as informaçoes
# 3 manipulação dos dados -> preservar o conteúdo
# 4 realizar a escrita (persistência)


arquivo.close # fecha o arquivo


## Exercicios

arquivo = open('arquivo.txt','a')

frase = 'esta é a primeira linha\nesta é a segunda linha\nesta é a terceira linha\n'

arquivo.write(frase)

arquivo.close


######################################

## Utilizando contextos (with)

with open('arquivo.txt') as arquivo: # Abre o arquivo le o arquivo , print e fecha automatico
    conteudo = arquivo.readlines()
    for linha in conteudo:
        print(linha, end='')





