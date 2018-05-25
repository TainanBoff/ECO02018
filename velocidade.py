"""
Nome: velocidade
Descricao: Este programa solicita que seja informada a velocidade do carro do usuario. Caso ultrapasse 80 km/h, exibe uma mensagem dizendo que o usuario foi multado e informa o valor da multa, que equivale a R$5,00 por km acima dos 80 km/h.
Autora: Tainan Boff
Data: 25/05/2018
Versao: 0.0.1

"""

a = float(input("Qual a velocidade do carro? "))

if a > 80:
    print("Voce foi multado!")
    multa = (a-80)*5
    print("O valor da multa e R$", multa)

