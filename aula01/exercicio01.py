
## Em muitos programas, nos é solicitado o preenchimento de algumas informações como
## nome, CPF, idade e unidade federativa. Escreva um script em Python que solicite as
## informações cadastrais mencionadas e que em seguida as apresente da seguinte forma:


# Confirmação de cadastro:
# Nome: Guido Van Rossum
# CPF: 999.888.777/66
# Idade: 65



nome = input ("\n\n\nDigite o seu nome: ")
cpf = input("Digite o seu CPF: ")
idade = int(input ("Digite sua idade: "))

print("\n\n---------------------------")
print("Confirmação de Cadastro:")
print("Nome:",nome)
print("CPF:",cpf)
print("Idade:",idade, end='\n\n')
print("---------------------------\n\n\n")




