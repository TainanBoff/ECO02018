"""

Nome: ex8.py
Descricao: Calculo do custo de energia eletrica.
Autores: Bruno e Tainan
data: 25/05/2018
Versao: 0.0.1

"""
## Entrada de dados

# Inicializacao de variaveis
consumo = 0.0
instalacao = ''
x = 0.0

# Leitura do teclado
consumo = float(input("Informe a quantidade de kW/h consumida: "))
instalacao = input("Informe o tipo de instalacao: r para residencial, i para industria e c para comercio: ")

# Processamento de dados
if instalacao == 'r':
    if consumo <= 500:
        x = consumo*0.4
    else:
        x = consumo*0.65
elif instalacao == 'c':
    if consumo <= 1000:
        x = consumo*0.55
    else:
        x = consumo*0.6
else:
    if consumo <= 5000:
        x = consumo*0.55
    else:
        x = consumo*0.6

# Saida de dados

print("A conta de energia eletrica foi de R$",x)

