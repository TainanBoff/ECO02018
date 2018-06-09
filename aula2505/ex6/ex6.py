"""

Nome: ex6.py
Descricao: O programa converte uma temperatura em graus Celsius para graus Fahrenheit.
Autores: Bruno e Tainan
data: 25/05/2018
Versao: 0.0.1

"""

## Entrada de dados

# Inicializacao de variaveis

celsius = 0.0
fahrenheit = 0.0

# Leitura do teclado

celsius = float(input("Insira a temperatura em graus celsius: "))

# Processamento de dados

fahrenheit = (celsius*9/5) + 32

# Saida de dados

print(celsius,"graus Celsius equivalem a" , fahrenheit, "graus Fahrenheit")
