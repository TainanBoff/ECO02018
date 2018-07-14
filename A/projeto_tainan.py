'''
projeto_tainan.py
Descricao: projeto para recuperacao de conceito da disciplina ECO02018
Nome: Tainan de Bacco Freitas Boff
Data: 05 jul 2018
'''

# Importacao de pacotes

import pandas as pd
from functools import reduce
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf
import statsmodels.tsa as smt
import numpy as np

# Declaracao de variaveis

# Entrada de dados - download de dados da internet via API

## Faturamento medio da industria de transformacao
faturamento = pd.read_csv('http://api.bcb.gov.br/dados/serie/bcdata.sgs.24346/dados?formato=csv', sep = ';', encoding = 'utf-8', decimal = ',', index_col = 'data', parse_dates = ['data'])
faturamento = faturamento.loc['2006-01-01':'2016-01-01']

## Utilizacao da capacidade instalada
utilizacao = pd.read_csv('http://api.bcb.gov.br/dados/serie/bcdata.sgs.24351/dados?formato=csv', sep = ';', encoding = 'utf-8', decimal = ',', index_col = 'data', parse_dates = ['data'])
utilizacao = utilizacao.loc['2006-01-01':'2016-01-01']

## Produtividade: calculada como a diferenca entre variacoes da producao fisica e variacoes do numero de horas trabalhadas
producao = pd.read_csv('http://api.bcb.gov.br/dados/serie/bcdata.sgs.21862/dados?formato=csv', sep = ';', encoding = 'utf-8', decimal = ',', index_col = 'data', parse_dates = ['data'])
producao = producao.loc['2006-01-01':'2016-01-01']
dlogproducao = np.log(producao).diff()

horas = pd.read_csv('http://api.bcb.gov.br/dados/serie/bcdata.sgs.24348/dados?formato=csv', sep = ';', encoding = 'utf-8', decimal = ',', index_col = 'data', parse_dates = ['data'])
horas = horas.loc['2006-01-01':'2016-01-01']
dloghoras = np.log(horas).diff()

produtividade = dlogproducao - dloghoras

## Custo do trabalho: calculado como a razao entre o indice de massa salarial real e o indice de horas trabalhadas na industria de transformacao (ambos com base em 2006)
salarios = pd.read_csv('http://api.bcb.gov.br/dados/serie/bcdata.sgs.24349/dados?formato=csv', sep = ';', encoding = 'utf-8', decimal = ',', index_col = 'data', parse_dates = ['data'])
salarios = salarios.loc['2006-01-01':'2016-01-01']

custo = salarios/horas

# Processamento e saida de dados

## Analise descritiva dos dados

### Faturamento
faturamento.head()
plt_faturamento = plt.plot(faturamento)
plt.savefig("imagens/faturamento.png")
plt.show()

### Utilizacao
utilizacao.head()
plt_utlizacao = plt.plot(utilizacao)
plt.savefig("imagens/utilizacao.png")
plt.show()

### Produtividade
produtividade.head()
plt_produtividade = plt.plot(produtividade)
plt.savefig("imagens/produtividade.png")
plt.show()

### Custo
custo.head()
plt_custo = plt.plot(custo)
plt.savefig("imagens/custo.png")
plt.show()

## Estatisticas descritivas

### Unifica os dados
dados = reduce(lambda left,right: pd.merge(left,right, on = 'data'), [faturamento, utilizacao, produtividade, custo])
dados.columns = ['faturamento', 'utilizacao', 'produtividade', 'custo']

### Gera e imprime as statisticas descritivas
est_desc_dados = dados.describe()
print(est_desc_dados)

### Salva a tabela de estatisticas descritivas em arquivo .csv
est_desc_dados.to_csv('tabelas/est_desc_dados.csv')

## Testes de raiz unitaria

### Faturamento
adf_faturamento = sm.tsa.stattools.adfuller(faturamento.valor)
print("Estatistica do teste ADF para o faturamento:", adf_faturamento[0])
print("Valores criticos para a estatistica de teste:", adf_faturamento[4])
print("P-valor:", adf_faturamento[1])

### Utilizacao
adf_utilizacao = sm.tsa.stattools.adfuller(utilizacao.valor)
print("Estatistica de teste:", adf_utilizacao[0])
print("Valores criticos para a estatistica de teste:", adf_utilizacao[4])
print("P-valor:", adf_utilizacao[1])

### Produtividade do trabalho
adf_produtividade = sm.tsa.stattools.adfuller(produtividade.valor.dropna())
print("Estatistica de teste:", adf_produtividade[0])
print("Valores criticos para a estatistica de teste:", adf_produtividade[4])
print("P-valor:", adf_produtividade[1])

### Custo do trabalho
adf_custo = sm.tsa.stattools.adfuller(custo.valor)
print("Estatistica de teste:", adf_custo[0])
print("Valores criticos para a estatistica de teste:", adf_custo[4])
print("P-valor:", adf_custo[1])

## Calculo das diferencas logaritmicas

### Faturamento
dlogfaturamento = np.log(faturamento).diff()
dlogfaturamento.head()
plt_dlogfaturamento = plt.plot(dlogfaturamento)
plt.savefig("imagens/dlogfaturamento.png")
plt.show()

### Utilizacao 
dlogutilizacao = np.log(utilizacao).diff()
dlogutilizacao.head()
plt_dlogutilizacao = plt.plot(dlogutilizacao)
plt.savefig("imagens/dlogutilizacao.png")
plt.show()

### Custo do trabalho
dlogcusto = np.log(custo).diff()
dlogcusto.head()
plt_custo = plt.plot(custo)
plt.savefig("imagens/custo.png")
plt.show()

## Unificacao dos dados diferenciados e impressao de estatisticas descritivas

### Unificacao das series diferenciadas
dlogdados = reduce(lambda left,right: pd.merge(left,right, on = 'data'), [dlogfaturamento, dlogutilizacao, produtividade, dlogcusto])
dlogdados.columns = ['dlogfaturamento', 'dlogutilizacao', 'dlogprodutividade', 'dlogcusto']

### Estatisticas descritivas
est_desc_dlogdados = dlogdados.describe()
print(est_desc_dlogdados)

### Salva a tabela em .csv
est_desc_dlogdados.to_csv('tabelas/est_desc_dlogdados.csv')

## Regressao linear
regressao = smf.ols(formula = 'dlogfaturamento ~ dlogutilizacao + dlogprodutividade + dlogcusto - 1', data = dlogdados,  missing = 'drop').fit()
resultado = regressao.summary()
print(resultado)

## Diagnostico

### Grafico dos residuos contra os valores ajustados
plt_res_fitt = plt.scatter(regressao.fittedvalues,regressao.resid)
plt.savefig("imagens/res_fitt.png")
plt.show()

### Teste de heterocedasticidade de Breusch-Pagan
bpteste = sm.stats.diagnostic.het_breuschpagan(regressao.resid, regressao.model.exog)
print('Estatistica de teste:', bpteste[0]) 
print('P-valor:', bpteste[1])  
print('Estatistica F:', bpteste[2])  
print('P-valor da estatistica F:', bpteste[3])

### Grafico dos residuos quadrados contra os valores ajustados
plt_res_fitt = plt.scatter(regressao.fittedvalues, regressao.resid**2)
plt.show()

### Grafico dos residuos quadrados contra utilizacao
plt_res_util = plt.scatter(dlogutilizacao.dropna(), regressao.resid**2)
plt.show()

### Grafico dos residuos quadrados contra produtividade
plt_res_prod = plt.scatter(produtividade.dropna(), regressao.resid**2)
plt.show()

### Grafico dos residuos quadrados contra custo
plt_res_custo = plt.scatter(dlogcusto.dropna(), regressao.resid**2)
plt.show()

## Teste de autocorrelacao de Durbin-Watson
dwteste = sm.stats.stattools.durbin_watson(regressao.resid)
print('A estatistica do teste e:', dwteste)

## Teste de normalidade de Jarque-Bera
jbteste = sm.stats.stattools.jarque_bera(regressao.resid)
print('A estatistica de teste e:',jbteste[0])
print('O p-valor e:',jbteste[1])
print('Assimetria:',jbteste[2])
print('Curtose:',jbteste[3])

## Teste de cointegracao de Johansen 
cointeste = smt.vector_ar.vecm.coint_johansen(dlogdados.dropna(),1,1)
print('As estatisticas de traco sao:',cointeste.lr1)
print('Os valores criticos para as estatisticas de traco, aos niveis de significancia de 1%, 5% e 10%, sao:')
print(cointeste.cvt)
print('As estatisticas de maximo autovalor sao:',cointeste.lr2)
print('Os valores criticos para as estatisticas de maximo autovalor, aos niveis de significancia de 1%, 5% e 10%, sao:')
print(cointeste.cvm)

# Saida: modelo final
print(resultado)

