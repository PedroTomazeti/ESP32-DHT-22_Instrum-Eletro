import paho.mqtt.client as mqtt
import json
import csv
import os

# Nome do arquivo CSV
nome_arquivo = "dados_temperatura_umidade.csv"

# Verificar se o arquivo já existe, caso contrário criar e adicionar cabeçalho
if not os.path.exists(nome_arquivo):
    with open(nome_arquivo, mode='w', newline='') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)
        escritor_csv.writerow(["Temperatura", "Umidade"])

# Função para processar mensagens recebidas
def processar_mensagem(client, userdata, msg):
    try:
        print(f"Mensagem recebida no tópico {msg.topic}")
        mensagem = msg.payload.decode()
        print(f"Mensagem recebida: {mensagem}")
        dados = json.loads(mensagem)
        # Modifique os nomes utilizados para salvar
        # Por exemplo utilizo "umidade" e "temp"
        umidade = dados.get("umidade") # Atualize aqui
        temperatura = dados.get("temp") # E aqui

        with open(nome_arquivo, mode='a', newline='') as arquivo_csv:
            escritor_csv = csv.writer(arquivo_csv)
            escritor_csv.writerow([temperatura, umidade])

        print(f"Salvo no CSV: Temperatura: {temperatura}°C, Umidade: {umidade}%")
    except Exception as e:
        print(f"Erro ao processar mensagem: {e}")

# Função para tratar a conexão
def tratar_conexao(client, userdata, flags, rc):
    if rc == 0:
        print("Conectado com sucesso ao broker MQTT!")
        client.subscribe("tópico desejado") # Insira o tópico do seu broker
        print("Inscrito no tópico 'tópico desejado'") # Atualize aqui também
    else:
        print(f"Falha na conexão com o código {rc}")

# Criar uma instância do cliente MQTT
client = mqtt.Client()

# Configurar os callbacks usando decoradores
client.on_connect = tratar_conexao
client.on_message = processar_mensagem

# Conectar ao broker MQTT
client.connect("atualize.aqui", 1883, 60) # Mude para o broker que você está utilizando

# Manter o loop para processar callbacks
client.loop_forever()
