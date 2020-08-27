
#### 
#### if, else, elif 
####
"""
1) Escreva um programa que receba o ano de nascimento, e que ele retorne à geração
a qual a pessoa pertence. Para definir a qual geração uma pessoa pertence temos a
seguinte tabela:
    
    Geração         Intervalo
    Baby Boomer     Até 1964
    Geração X       1965 - 1979
    Geração Y       1980 - 1994
    Geração Z       1995 - Atual
    

    Para testar se seu script está funcionando, considere os seguintes resultados esperados:
        • ano nascimento = 1988: Geração: Y
        • ano nascimento = 1958: Geração: Baby Boomer
        • ano nascimento = 1996: Geração: Z
"""

ano = int(input("Digite o ano de seu nascimento: "))

if ano <= 1964:
    print(f"Ano nascimento = {ano}: Geração: Baby Boomer")
elif ano <= 1979:
    print(f"Ano nascimento = {ano}: Geração: X")
elif ano <= 1994:
    print(f"Ano nascimento = {ano}: Geração: Y")
elif ano <= 2020:
    print(f"Ano nascimento = {ano}: Geração: Z")



