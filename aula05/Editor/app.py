#!/usr/bin/python3

import ioregistro as reg

"""
Crie um script em python que seja capaz de interagir com arquivos:

    - seja possível ler um arquivo CSV
    - inserir novos registros
    - remover registros
    - alterar registros
    - exibir registros
    - busca por cpf

"""
def buscar_registro(nomeArquivo):
    registro = reg.buscarRegistro(nomeArquivo)
    reg.exibirRegistro(registro)


def inserir_registro(nomeArquivo):
    registro = reg.capturarDados()
    reg.exibirRegistro(registro)
    
    if input("Deseja cadastrar este registro? S- Sim: ") == "S":
        if reg.inserirRegistro(nomeArquivo, registro):
            print (" Registro cadastrado com sucesso\n")
        else:
            print("Falha de cadastro\n")
    else:
        print("Cancelado\n")


def remover_registro(nomeArquivo):
    registro = reg.buscarRegistro(nomeArquivo)
    reg.exibirRegistro(registro)

    if input("Deseja apagar esse registro: S - Sim: ") == "S":

        if reg.removerRegistro(nomeArquivo,registro):
            print ("Registro apagado com sucesso\n")
        else:
            print("Falha ao apagar  arquivo\n")
    else:
        print("Cancelado\v")


def alterar_registro(nomeArquivo):
    reg.alterarRegistro(nomeArquivo)
   

def exibir_todos(nomeArquivo):
    reg.exibirTodos(nomeArquivo)


def sair():
    exit()


def main():

    nomeArquivo = "arquivo.csv"
    
    while True:
        
        opcoes = {
                '1':buscar_registro,
                '2':inserir_registro,
                '3':remover_registro,
                '4':alterar_registro,
                '5':exibir_todos,
                '6':sair
                }

        escolha = input(f'\nInforme a opção desejada:\n'
                      f'1- Buscar registro\n'
                      f'2- Inserir registo\n'
                      f'3- Remover registro\n'
                      f'4- alterar registro\n'
                      f'5- exibir todos os registros\n'
                      f'6- Sair\n'
                      f'Opção ==> ')

        if escolha in opcoes.keys():
            opcoes[escolha](nomeArquivo)




if __name__ == "__main__":
    main()


