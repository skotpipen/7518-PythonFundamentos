#!/usr/bin/python3


def buscarRegistro(nomeArquivo):
    """
    Busca registro em um arquivo .csv e devolve a linha encontrada.
    buscarRegistro(nome do arquivo.csv)

    """
    cpf = input('Informe o cpf: ')
    
    with open(nomeArquivo) as arquivo:
        conteudo = arquivo.readlines() # como uma lista de strings
        for indice in range(len(conteudo)):
            if cpf in conteudo[indice].split(';'):
                registro = [indice, conteudo[indice].split(';')] 
                return registro
                break
        else:
            return [-2,'']


def exibirRegistro(registro):
    """
    Exibe o registro encontrado
    """

    if registro[0] >= -1:
        print('Código',registro[0])
        print('CPF:', registro[1][0])
        print('Nome:', registro[1][1])
        print('Idade:', registro[1][2])
        print('Sexo:', registro[1][3])
        print('UF:', registro[1][4],'\n')
    else:
        print("Registro não encontrado")


def removerRegistro(nomeArquivo, registro):
    """
    Remove um registro, informando o arquivo e o registro

    """
  
    if registro[0] >= 0:
        with open(nomeArquivo, 'r') as arquivo:
            conteudo = arquivo.readlines() # como uma lista de strings
                   
        del conteudo[registro[0]]          
        novoConteudo = ''.join(conteudo)
           
        with open(nomeArquivo, 'w') as arquivo:
            arquivo.write(novoConteudo)
            return True
    else:
        return False


def inserirRegistro(nomeArquivo, registro):
    """
    Insere Registro no Arquivo

    """

    if registro[0] == -1:
        with open(nomeArquivo, 'r') as arquivo:
            conteudo = arquivo.readlines() # como uma lista de strings

        conteudo.append(';'.join(registro[1]))

        novoConteudo = ''.join(conteudo)
           
        with open(nomeArquivo, 'w') as arquivo:
            arquivo.write(novoConteudo)
            return True
    else:
        return False


def capturarDados():
    """
    Captura os dados para inserir ou alterar registro

    """
    registro = []

    dados = []

    dados.append(input("Digite o CPF: "))
    dados.append(input("Digite o Nome: "))
    dados.append(input("Digite o Idade: "))
    dados.append(input("Digite o Sexo: "))
    dados.append(input("Digite o UF: "))
    dados.append("\n")

    registro.append(-1)
   
    registro.append(dados)

    return registro


def alterarRegistro(nomeArquivo):
    """
    Altera o registros, caso o campo fique fazio, é considerado que não há alterção

    """
    registro = buscarRegistro(nomeArquivo)
    if registro[0] >= 0:
        exibirRegistro(registro)
        dados = []

        if input("Desaja alterar este registro? S - Sim : ") == "S":
            dados.append (input(f"CPF: -{registro[1][0]}- :"))
            dados.append (input(f"NOME: -{registro[1][1]}- :"))
            dados.append (input(f"IDADE: -{registro[1][2]}- :"))
            dados.append (input(f"SEXO: -{registro[1][3]}- :"))
            dados.append (input(f"UF: -{registro[1][4]}- :"))

            for index in range(5):
                if dados[index] != "":
                    registro[1][index] = dados[index]

            if removerRegistro(nomeArquivo,registro):
                registro[0] = -1
                if inserirRegistro(nomeArquivo, registro):
                    print ("Alteração Realizada com sucesso")
                else:
                    print("Falha ao salvar alterações")
            else:
                print("Falha ao salvar alterações")

        else:
            print("Alteração cancelada")
    else:
        print("Registro não encotrado")


def exibirTodos(nomeArquivo):
    """
    Exibe todos os registros no arquivo

    """

    with open(nomeArquivo) as arquivo:
        conteudo = arquivo.readlines() # como uma lista de strings
        for indice in range(1,len(conteudo)):
            registro = [indice, conteudo[indice].split(';')] 
            exibirRegistro(registro)



