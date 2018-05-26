"""

Nome: ex7.py
Descricao: Este programa solicita a idade do carro, decide e informa se ele e velho ou novo.
Autores: Bruno e Tainan
data: 25/05/2018
Versao: 0.0.1

"""
## Entrada de dados

# Inicializacao de variaveis

idadedocarro = 0.0
x = '' 

# Leitura do teclado
idadedocarro = float(input("Insira a idade do carro: "))

# Processamento de dados

if idadedocarro > 3:
    x = 'O carro e velho'
else:
    x = 'O carro e novo'

# Saida de dados

print(x)
