# Estrutura de decisão


peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))

imc = peso/altura ** 2


if imc < 18.5:
    print(f'Peso: {peso:.2f} - Altura: {altura} - IMC: {imc:.2f} - Classificação: Magreza')
elif imc < 24.9:
    print(f'Peso: {peso:.2f} - Altura: {altura} - IMC: {imc:.2f} - Classificação: Normal')
elif imc < 29.9:
    print(f'Peso: {peso:.2f} - Altura: {altura} - IMC: {imc:.2f} - Classificação: Sobrepeso')
elif imc < 39.9:
    print(f'Peso: {peso:.2f} - Altura: {altura} - IMC: {imc:.2f} - Classificação: Obsidade')
else:    
    print(f'Peso: {peso:,2f} - Altura: {altura} - IMC: {imc:.2f} - Classificação: Obsidade Grave')


