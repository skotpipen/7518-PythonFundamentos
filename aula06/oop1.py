#### Orientação à Objetos

## Abstração
## Encapsulamento 
#   antes dos atributos/metodo colocar _ , ocuta/protege o atribut/metodo 
#  antes dos atributos/metodo __ siginifica que é de uso interno do python, a classe herança nao tem acesso ao atributo
  

## Herança




## Polimorfismo
# reescrever um metodo na classe herançaI


### Organização
### Representação de contextos reais
### Generalização

# Pessoa:
#  - cpf
#  - nome
#  - data nasc
#  - celular

class Pessoa:
    def __init__(self, # Construtor
                 _cpf='1111111-09',
                 _nome='teste'):

        self._cpf = ''    # Atributos
        self._nome = ''
        self._data_nasc = ''
        self._cel = ''
        self._idade = 0

    def seApresentar(self): # comportamentos
        return f'Olá, meu nome é {self._nome}, e tenho {self._idade} anos'

    def retornaAnoQueNasceu(self):
        return self._data_nasc

    def adicionaCPF(self, cpf): 
        self._cpf = cpf

    def veirCPF(self):
        print(self.__cpf)

    def adicionaNome(self, nome):
        self._nome = nome

    def adicionaDataNasc(self, data_nasc):
        self._data_nasc = data_nasc

    def adicionaCel(self, cel):
        self._cel = cel
   
    def adicionaIdade(self, idade):
        self._idade = int(idade)





## Criando Herança da Classe a cima
## chamada pessoa 2

class Pessoa2(Pessoa):
    
    def __init__(self):

        super().__init__()
        self._uf = ''

    def adicionaUf(self,uf):
        self._uf = uf

    def getDados(self):
#        print(self._nome)
        print(self._cpf)

        







