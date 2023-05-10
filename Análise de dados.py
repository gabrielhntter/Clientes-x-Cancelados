import pandas as pd
import plotly.express as px

#1 - Importar a base de dados
tabela = pd.read_csv("C:\\Users\Gabri\Downloads\c\ClientesBanco.csv", encoding="latin1") #LOCAL ONDE SE ENCONTRA A PLANILHA EXCEL QUE SERÁ USADA PARA ANÁLISE DE DADOS

#2 - Visualizar e tratar essa base de dados
tabela = tabela.drop("CLIENTNUM", axis=1)      #EXCLUINDO UMA COLUNA DA BASE DE DADOS

#Excluindo linhas com valores vazios
tabela = tabela.dropna()

#3 - Dar uma olhada na base de dados
print(tabela.describe().round(1))#Comando para análisar como os valores e as informações estão distribuidas

#4 - Construir uma análise para identificar o motivo de cancelamento
#Identificar qual o motivo ou os principais motivos dos clientes estarem cancelando o cartão de crédito

qtde_categoria = tabela["Categoria"].value_counts() #Avaliando como está a divisão entre Clientes x Cancelados
print(qtde_categoria)

qtde_categoria_perc = tabela["Categoria"].value_counts(normalize=True) #Porcentagem de clientes x cancelados
print(qtde_categoria_perc)

#Gerando gráficos para todas as colunas da tabela comparando Cleintes x Cancelados, assim analisando o que os clientes cancelados tem em comum.
for coluna in tabela:
  grafico = px.histogram(tabela, x=coluna, color="Categoria")
  grafico.show()