## Escrever um script em python que some dois números informado pelo usuário
## e apresente o resultado da seguinte forma:
## Números informados: 5 e 4
## resultado esperado: 5 + 4 = 9

### Realizar o Exercício do capítulo 1.

numero1 = int(input("\n\nDigite o Primeiro Numero: "))
numero2 = int(input("\nDigite o Segundo Numero: "))

print("\n\nNumeros informados: ", numero1, "e", numero2)

resultado = numero1 + numero2

print("\nResultado esperado: ", numero1, "+", numero2, "=", resultado, end="\n\n")
