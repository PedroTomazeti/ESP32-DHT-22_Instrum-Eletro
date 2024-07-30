import pandas as pd
import numpy as np

# Carregar dados do arquivo CSV
file_path = 'caminho/do/csv'  # Altere este caminho para o local do seu arquivo CSV
data = pd.read_csv(file_path)

# Calcular a média
media_temperatura = data['Temperatura'].mean()
media_umidade = data['Umidade'].mean()

# Calcular o desvio padrão
desvio_padrao_temperatura = data['Temperatura'].std()
desvio_padrao_umidade = data['Umidade'].std()

# Calcular a incerteza padrão da média (incerteza tipo A)
n_medições = len(data)
incerteza_tipo_a_temperatura = desvio_padrao_temperatura / np.sqrt(n_medições)
incerteza_tipo_a_umidade = desvio_padrao_umidade / np.sqrt(n_medições)

# Exibir os resultados
print(f"Média da Temperatura: {media_temperatura}")
print(f"Desvio Padrão da Temperatura: {desvio_padrao_temperatura}")
print(f"Incerteza Tipo A da Temperatura: {incerteza_tipo_a_temperatura}")

print(f"Média da Umidade: {media_umidade}")
print(f"Desvio Padrão da Umidade: {desvio_padrao_umidade}")
print(f"Incerteza Tipo A da Umidade: {incerteza_tipo_a_umidade}")
