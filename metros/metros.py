"""
Nome: metros.py
Descricao: Este programa solicita que seja informado um valor em metros e o converte para milimetros.
Autora: Tainan Boff
Data: 25/05/2018
Versao: 0.0.1
"""

## Entrada de dados

# Inicializacao das variaveis

a = 0.0
milimetros = 0.0

# Leitura do teclado

a = float(input("Digite o valor em metros: "))

# Processamento de dados

milimetros = a*1000

# Saida de dados

print(a,"metros equivalem a", milimetros, "milimetros")
